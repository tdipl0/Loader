import streamlit as st
import pandas as pd

st.title("Data Loader")
st.write("Your file must contain column headers Name,Salary and Bonus")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Original data:")
    st.dataframe(df)


    df['Total Compensation'] = df['Salary'] + df['Bonus']

    st.write("With Total Compensation column:")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')


    st.download_button(
        label="Download processed CSV",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )
