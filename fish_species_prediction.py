
from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Load your trained model
with open('logisticregression.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template( 'fish_species_prediction.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    weight = float(request.form['weight'])
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])

    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[length1, length2, length3, weight, width, height]])

    # Make prediction
    prediction = model.predict(input_data)

    # Return the predicted species
    return render_template('prediction.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)