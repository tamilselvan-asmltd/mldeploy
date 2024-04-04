import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('/Users/smartfix/Downloads/price_prediction_tree.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print("Received data:", data)

    output = model.predict([data])
    print("Output:", output)

    return jsonify({'prediction_amount': output[0]})

if __name__ == "__main__":
    app.run(debug=True)
