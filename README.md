# Sales Prediction - Streamlit App

Welcome to the GitHub repository for the Sales Prediction Streamlit App! This project aims to provide an intuitive web application for predicting sales based on historical data. The app leverages the power of Streamlit, allowing users to interact with the prediction model through a user-friendly interface.

## Project Overview

This Streamlit app enables users to predict sales using machine learning techniques applied to a historical sales dataset. The app's key features include:

- Predicting the sales amount based on various features.
- Interactive exploration of the dataset and data visualization.
- Input relevant features (such as customer demographics, region, and product details) to obtain accurate sales predictions.
- The app employs a trained machine learning model to make predictions.

## Live Deployment

The Sales Prediction Streamlit app is live and can be accessed using the following link: [Sales Prediction Streamlit App](https://internship-project-testbook-by-06neel.streamlit.app/)

Feel free to explore the app and experiment with different input scenarios to observe how the model predicts sales based on the provided data.

## Usage

1. Access the Streamlit app using the provided link: [Sales Prediction Streamlit App](https://internship-project-testbook-by-06neel.streamlit.app/)
2. Interact with the user interface to input the relevant features for a sales prediction.
3. Observe the predicted sales amount based on the provided features.

## Installation and Local Setup

To run the Sales Prediction Streamlit App locally on your machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/06Neel/Internship_Project_TestBook.git
2. Navigate to the project directory:
   ```bash
    cd sales-prediction-app
3. Create a virtual environment (optional but recommended) and activate it:
    - **For Windows:**
         ``` bash
         venv\Scripts\activate
      
   - **For Unix or Linux:**
     ``` bash
     source venv/bin/activate
4. Install the required dependencies:
      ```bash
      pip install -r requirements.txt
5. Run the Streamlit app:
      ```bash
      streamlit run app.py
6. Open your web browser and go to
   ```bash
    http://localhost:8501
to access the Sales Prediction app.
## Dataset
The dataset used for this project is included in the data/ directory. Before running the app, ensure that the dataset file is available in this directory.

## Project Structure
    The repository structure is organized as follows:
            ```bash
               sales-prediction-app/
               ├── app.py              # Main Streamlit app script
               ├── data/               # Dataset files
               │   ├── sales_data.csv  # Historical sales data
               ├── models/             # Trained model files
               │   ├── sales_model.pkl # Serialized sales prediction model
               ├── README.md           # Project documentation (this file)
               └── requirements.txt    # Required Python packages

## Model Training
The machine learning model used in the app is trained separately and saved as a serialized file (sales_model.pkl) in the models/ directory. If you wish to train your own model, you can refer to the provided Jupyter Notebook.

## Contribution
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request. Let's collaborate and enhance this project together.

## License
This project is licensed under the MIT License.

## Acknowledgements
We extend our gratitude to the Streamlit team for providing an excellent platform to create interactive apps easily.


