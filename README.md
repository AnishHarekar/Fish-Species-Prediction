Fish Species Prediction
This repository contains code for a machine learning model to predict fish species based on various features. The model is built using Python and Flask, and it can be deployed to Heroku for online inference.

Problem Statement
The goal of this project is to develop a machine learning model that can accurately predict the species of a fish based on its various attributes such as weight, length, height, and width. This can be useful for fishery management, market analysis, and ecological studies.

Model Overview
We have trained a logistic regression model on the Fish Market dataset available on Kaggle. The model takes in features such as length1, length2, length3, weight, height, and width of the fish as input and predicts the species of the fish.

File Structure
fish_species_prediction.py: Python script containing the Flask application for serving predictions.
templates/: Directory containing HTML templates for the web interface.
randomforestclassifier.pkl: Pickle file containing the trained logistic regression model.
requirements.txt: File listing all Python dependencies required to run the application.
