import streamlit as st
import pandas as pd
import pickle
import joblib

# Load the trained model
model = joblib.load('Model.pkl')

# Load dataset
df = pd.read_csv('cleaned_data.csv')



# Create the web app
def main():
    # Set the title and description
    st.title('Sales Prediction')
    st.write('Enter the details to predict its Sales.')


    # Get user inputs
    Year = st.number_input('Year', min_value=2010, step=1)
    Country = st.selectbox('Country', sorted(df['Country'].unique()))

    # Filter regions based on selected country
    regions = df[df['Country'] == Country]['Region'].unique()
    Region = st.selectbox('Region', sorted(regions))


    # Filter states based on selected country and region
    states = df[(df['Country'] == Country) & (df['Region'] == Region)]['State'].unique()
    State = st.selectbox('State', sorted(states))

    # Filter cities based on selected country, region, and state
    cities = df[(df['Country'] == Country) & (df['Region'] == Region) & (df['State'] == State)]['City'].unique()
    City = st.selectbox('City', sorted(cities))

    Category = st.selectbox('Category', sorted(df['Category'].unique()))

    # Filter sub-categories based on selected category
    sub_categories = df[df['Category'] == Category]['Sub-Category'].unique()
    Sub_Category = st.selectbox('Sub-Category', sorted(sub_categories))

    Segment = st.selectbox('Segment', sorted(df['Segment'].unique()))

    Ship_Mode = st.selectbox('Ship Mode', sorted(df['Ship Mode'].unique()))
    Product_Name = st.selectbox('Product Name', sorted(df['Product Name'].unique()))
    Days_to_Ship = st.number_input('Days to Ship', min_value=0, step=1)
    Discount = st.number_input('Discount', min_value=0.0, step=0.1)
    Actual_Discount = st.number_input('Actual Discount', min_value=0.0, step=0.1)
    Profit = st.number_input('Profit', min_value=0.0, step=0.1)
    Quantity = st.number_input('Quantity', min_value=0, step=1)
    
    
    
    data = pd.DataFrame({       
                            'City': City,
                            'Country': Country,
                            'Region': Region,
                            'Segment': Segment,
                            'Ship Mode': Ship_Mode,
                            'State': State,
                            'Days to Ship': Days_to_Ship,
                            'Product Name': Product_Name,
                            'Discount': Discount,
                            'Actual Discount': Actual_Discount,
                            'Profit': Profit,
                            'Quantity': Quantity,
                            'Category': Category,
                            'Sub-Category': Sub_Category,
                            'Year': Year}, index=[0])
    

    if st.button('Predict Sales'):
        # Make predictions
        predictions = model.predict(data)
        predicted_Sales = "{:.2f}".format(predictions[0])
        st.success(f'Predicted sales is {predicted_Sales}')



# Run the web app
if __name__ == '__main__':
    main()

