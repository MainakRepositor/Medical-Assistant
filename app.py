import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Create a DataFrame from the sample data
df = pd.read_csv('asthma.csv',encoding='unicode_escape')
df = df.reset_index(drop=True)

# Streamlit app
st.title('Integrated Medicine Information')

# Sidebar for user input
medicine_name = st.sidebar.text_input('Enter Medicine Name', '')

if medicine_name == '':
    st.warning('Please enter a valid medicine name')



else:
    # Filter the DataFrame based on the entered medicine name
    filtered_df = df[df['Brand'].str.lower().str.contains(medicine_name.lower())]
   

    # Display the results in a table
    st.write('**Medicine Information**')
    st.write(filtered_df)
    

# Display additional information about asthma and medication
st.write('**Medication Information**')
st.write("Please consult a healthcare professional for detailed information on asthma treatment and medication. The 'Time to Cure' column provides general information and may vary based on individual cases.")

