# ✍️ Hand-Digit Recognizer App

The "Hand-Digit Recognizer App" is a full-stack web application designed to allow users to draw a digit, which is then sent to a backend service for prediction using a trained deep learning model. This project combines a modern frontend with a robust FastAPI backend and an advanced PyTorch training module.

## ✨ Features

- **Interactive Drawing:** Users can draw digits directly in their web browser using an intuitive canvas interface.
- **Real-time Prediction:** The drawn image is sent to the backend, where a trained machine learning model performs the digit prediction.
- **Result Display:** Prediction results are clearly presented to the user, including the model's confidence for each possible digit.
- **Modular Codebase:** Both the backend and the training module are designed with modularity in mind, facilitating easy extension and maintenance.

## 🚀 App Preview

[Hand-Digit Recognizer Demo](attachments\app_demo.gif)

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

## 🚀 How to Run the Application

To run the application locally, you will need [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or a Docker engine) installed, and [Miniconda/Anaconda](https://docs.conda.io/en/latest/miniconda.html) for the `training` module.

Navigate to the root directory of the project (where `docker-compose.yml` is located).

### 1. Running Backend and Frontend (Docker)

The backend and frontend services are containerized, ensuring consistent environments and easy deployment.

```bash
docker compose up -d --build
```

* `docker compose up`: Starts the services defined in `docker-compose.yml`.
* `-d`: Runs the containers in detached mode (in the background).
* `--build`: Forces a rebuild of the Docker images for the services (`backend`, `frontend`) before starting them. This is crucial for the initial run or after any changes to the code or Docker configuration.

**Important note on image size**: The Docker image for the backend service is sizable, weighing around 3 GB, mainly due to the PyTorch library. Ensure you have sufficient free disk space.

Once the containers are running:

* The Backend API will be accessible at: http://localhost:8000
* The Frontend Application will be accessible at: http://localhost:3000


### 2. Stopping the Application
To stop the running Docker containers execute:

```Bash
docker compose down
```
This command will stop and remove the containers created by `docker compose up`.


### 3. Setting up and Running the Training Module (training/)
The `training/` module requires a separate Conda environment to manage its PyTorch and other ML dependencies.

1. Install Conda: If you haven't already, download and install Miniconda.
2. Navigate to the `training` directory:

``` bash
conda env create -f environment.yml
conda activate hand-digit-training
```

## 🎯 Further Steps & Future Improvements

This project serves as a robust foundation for a hand-digit recognition application. Here are some potential areas for future development and improvements:

- **Model Performance Enhancement:**
    
    - While the model exhibits excellent test results during training, its performance in the live application environment (with user-drawn digits) could be improved. This discrepancy suggests potential issues with data augmentation during inference, preprocessing of user input, or domain shift.