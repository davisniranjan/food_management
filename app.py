from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In a real application, the data would be stored in a database
# For this example, we'll use a simple list to store the food donations
food_donations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate_food():
    data = request.get_json()
    hotel_name = data['hotel_name']
    food_items = data['food_items']

    # Store the donation in the food_donations list
    food_donations.append({'hotel_name': hotel_name, 'food_items': food_items})

    return jsonify({'message': 'Food donation successful'})

@app.route('/get_food_donations', methods=['GET'])
def get_food_donations():
    return jsonify(food_donations)

if __name__ == '__main__':
    app.run(debug=True)
