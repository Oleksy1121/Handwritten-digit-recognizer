# ✍️ Hand-Digit Recognizer App

The "Hand-Digit Recognizer App" is a full-stack web application designed to allow users to draw a digit, which is then sent to a backend service for prediction using a trained deep learning model. This project combines a modern frontend with a robust FastAPI backend and an advanced PyTorch training module.

## ✨ Features

- **Interactive Drawing:** Users can draw digits directly in their web browser using an intuitive canvas interface.
- **Real-time Prediction:** The drawn image is sent to the backend, where a trained machine learning model performs the digit prediction.
- **Result Display:** Prediction results are clearly presented to the user, including the model's confidence for each possible digit.
- **Modular Codebase:** Both the backend and the training module are designed with modularity in mind, facilitating easy extension and maintenance.

## 📦 Project Structure

The project is structured into three main components:

1. **`training/` (ML Training Module):** Contains the PyTorch code for training the digit classification model.
2. **`backend/` (API):** A FastAPI server that handles prediction requests by interacting with the trained model.
3. **`frontend/` (Web Application):** The user interface built with React, enabling interaction with the model.

## 🛠️ Technologies Used

### ML Training Module

- **PyTorch:** The primary framework for building and training the deep learning model.
- **NumPy, Pandas, Matplotlib, Matplotlib,  Seaborn, PIL, Scikit-learn, :** Libraries for data manipulation, analysis, and visualization of training results.
- **[`training-notebook.ipynb`](training/training-notebook.ipynb):** A Jupyter Notebook detailing the data exploration, model training, and evaluation process.

### Backend

- **FastAPI:** A fast and modern Python web framework used for building the REST API.
- **Python:** The programming language for the backend logic.

### Frontend

- **React:** A JavaScript library for building user interfaces.
- **Styled-components:** A library for writing CSS in JavaScript, used for styling UI components.
- **Axios:** An HTTP client for making API requests.

## 📊 Data and Model

### Data

The digit images used for training the model were sourced from Kaggle: **[Handwritten Digits Dataset (Not in MNIST)](https://www.kaggle.com/datasets/jcprogjava/handwritten-digits-dataset-not-in-mnist)**

### Model

The deep learning model was trained using PyTorch. The architecture employed is a **TinyVGG** replica, based on the model described on **[CNNExplainer.com](https://poloclub.github.io/cnn-explainer/)**. This choice provided an efficient and concise Convolutional Neural Network (CNN) suitable for digit classification.

A set of modular Python scripts (`engine.py`, `model_builder.py`, `data_setup.py`, `utils.py`, `image_transforms.py`, `paths.py`, `plots.py`, `predictions.py`, `train.py`) was developed to manage the training process, allowing for easy experimentation and expansion.


## 🎯 Further Steps & Future Improvements

This project serves as a robust foundation for a hand-digit recognition application. Here are some potential areas for future development and improvements:

- **Dockerization:**
    
    - Containerize the backend and frontend components using Docker. This would streamline the deployment process, ensure consistent environments, and facilitate easier scaling and management.
- **Model Performance Enhancement:**
    
    - While the model exhibits excellent test results during training, its performance in the live application environment (with user-drawn digits) could be improved. This discrepancy suggests potential issues with data augmentation during inference, preprocessing of user input, or domain shift.