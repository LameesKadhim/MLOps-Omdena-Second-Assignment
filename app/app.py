from calculateBMI import calculate_bmi
from flask import Flask, jsonify, request


# instantiate flask object
app = Flask("__name__")

@app.route('/', methods=['GET','POST'])

def get_input():
    ''' a function to get REQUEST USING FLASK, EVALUATE AND RETURN RESULT'''
    packet = request.get_json(force=True)
    height = packet["height"]
    weight = packet["weight"]

  
    body_mass = calculate_bmi(height, weight)
    return jsonify(packet, body_mass)

#driver function
if __name__ == "__main__":
    app.run()
