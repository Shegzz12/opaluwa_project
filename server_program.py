from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize values to be used if no data is received
heart_rate = 0
blood_oxygen = 0
temperature = 0

@app.route('/input_data', methods=['POST'])
def receive_data():
    global heart_rate, blood_oxygen, temperature
    received_data = request.get_json()
    if 'heart_rate' in received_data and 'blood_oxygen' in received_data and 'temperature' in received_data:
        heart_rate = received_data['heart_rate']
        blood_oxygen = received_data['blood_oxygen']
        temperature = received_data['temperature']
        print(f"Received result1: {heart_rate}, result2: {blood_oxygen}, result3: {temperature}")
        return "Data received successfully", 200
    else:
        return "Invalid data format", 400

@app.route('/data_to_app', methods=['GET'])
def predict_user_input():
    try:
        global heart_rate, blood_oxygen, temperature
        # Use the received values or default values if not received
        # input1 = val1
        # input2 = val2
        # input3 = val3

        # Call the utility function to make predictions
        # result = util.predict_user_input(input1, input2, input3)
        # Construct the response
        response = jsonify({
            'heart_rate': heart_rate,
            'blood_oxygen': blood_oxygen,
            'temperature': temperature
        })

        return response

    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
