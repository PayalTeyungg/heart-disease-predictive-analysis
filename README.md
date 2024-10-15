
# Heart Disease Predictive Streamlit app using Linear Regression

This repository contains Python code for predicting heart disease using a dataset of patient information. It leverages exploratory data analysis (EDA), correlation analysis, and logistic regression to analyze the dataset and predict the likelihood of heart disease.





## Workflow
    1.Data Loading: The dataset is loaded using pandas, and initial exploration (head, tail, shape, etc.) is performed to understand the structure.
    
    2.Handling Duplicates: Duplicate rows in the dataset are dropped.
    
    3.Categorical Feature Analysis: Plots are created using Seaborn to analyze categorical features with respect to the target variable.
    
    4.Numerical Feature Analysis: Numerical features are analyzed using pair plots to understand relationships between variables.
    
    5.Correlation Matrix: A correlation matrix is generated to examine the strength of relationships between features.
    
    6.Modeling: Logistic regression is used for predicting the target variable (heart disease likelihood).

    7.Load Model: The pre-trained model is loaded using pickle.

    8.Input Data: The app allows users to input various health metrics.

    9.Prediction: Upon clicking the "Heart Disease Test Result" button, the model predicts the likelihood of heart disease based on the provided inputs.


## Dependencies

    Python 3.x
    Pandas
    NumPy
    Matplotlib
    Seaborn
    Plotly
    Scikit-learn
    Streamlit
    Pickle (built-in)
    
## Installation of necessary dependencies

    pip install -r requirements.txt

    pip install streamlit numpy scikit-learn
    
## Running the Code

Clone the project

```bash
  git clone https://github.com/yourusername/heart-disease-prediction.git

```

Go to the project directory

```bash
  cd heart-disease-prediction

```

Run the code using  Python environment (e.g., Jupyter Notebook, VSCode):

```bash
  python heart_disease_prediction.py

```


Run the Streamlit app:

```bash
  streamlit run app.py

```

Open your web browser and go to http://localhost:8501 to access the app.

## License

[MIT](https://choosealicense.com/licenses/mit/)

