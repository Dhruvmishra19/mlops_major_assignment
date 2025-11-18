MLOps Major Assignment

PGD - MLOps • End-to-End Automated Pipeline


Assignment Objectives

This project implements an end-to-end MLOps workflow that includes:

Model Training

Uses the Olivetti Faces Dataset from sklearn.

Trains a DecisionTreeClassifier model.

Saves the trained model as savedmodel.pth using joblib.

CI/CD with GitHub Actions

Automatically runs on every push to the dev branch.

Executes:

train.py to train the model.

test.py to evaluate the model accuracy.

Docker and Flask Application

Flask web application for image upload and prediction.

Packaged into a Docker container.

Image pushed to Docker Hub.

Kubernetes Deployment

Deploys the Dockerized Flask application.

Ensures 3 running replicas using a Kubernetes Deployment YAML file.
