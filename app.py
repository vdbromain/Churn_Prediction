# Library to make the app
import streamlit as st

# To add the link of the dashboard with the embeded code from Tableau
import streamlit.components.v1 as components

# To load the model
import pickle

# To import the image (favicon)
from PIL import Image

import pandas as pd

# Personnal function
from modeling.modeling import modeling

#Function who create and collect the data on streamlit app
def collecting_data(df):
    gender = st.radio("What's the customer's gender ?", ("Male", "Female"))
    if gender == "Male":
        df.loc['Gender'] = 'M'
    else :
        df.loc['Gender'] = 'F'

    df['Customer_Age'] = st.slider('How old is the customer ?',18 ,100, key="Customer_Age")

    df['Dependent_count'] = st.slider("How many dependent relatives does the customer have ?", 0, 6, key="Dependent_count")

    df['Months_on_book'] = st.slider("How long is the customer client in your bank ? (in months)", 13, 60, key="months_on_book'")

    df['Total_Relationship_Count'] = st.slider("How many products does the customer have in your bank ?", 0, 6, key="total_relationship_count")

    df['Months_Inactive_12_mon'] = st.slider("How many months was the customer inactive during last year ? (months)", 0, 6, key="months_inactive_12_mon")

    df['Contacts_Count_12_mon'] = st.slider("How many contacts do you have with the customer last year ?", 0, 6, key="contacts_count_12_mon")

    df['Credit_Limit'] = st.slider("What's the customer's credit's limit ? ($)", 1400, 40000, key="credit_limit")

    df['Total_Revolving_Bal'] = st.slider("What is the total revolving balance on the customer's credit card ? ($)", 0, 3000, key="total_revolving_bal")

    df['Total_Amt_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount change in the last quarter compared to the previous quarter?", 0, 5, key="total_amt_chng_Q4_Q1")

    df['Total_Trans_Amt'] = st.slider("How much was the customer's total amount transaction for last 12 months ? ($)", 0, 20000, key="total_trans_amt")

    df['Total_Trans_Ct'] = st.slider("How many transactions did the customer make during last 12 months ?", 0, 200, key="total_trans_ct")

    df['Total_Ct_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount changed in the last quarter compared to the previous one ?", 0.00, 5.00, key="total_ct_chng_Q4_Q1'")

    df['Avg_Utilization_Ratio'] = st.slider("What's the ratio for the customer's average card's utilization ?", 0.00, 1.00, key="avg_utilization_ratio")

    return df

# Loading the plk file with the dataframe shape the model will need
features_path = "modeling/model/classification/X_form.pkl"
# Loading the pkl file containing a df with the columns used by the ML engineer in his model
df = pickle.load(open(features_path, "rb"))

# Open the favicon image
img = Image.open(".streamlit/img/save-money.png")
# To take the page on the whole width for the dashboard to be displayed on its entirety
st.set_page_config(page_title="Churn Prediction", layout="wide", page_icon=img)
# To delete the settings' hamburger on the top-right and the "made with streamlit in the bottom"
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# App's header
st.image(".streamlit/img/header.png", width=1580)

# Sentence before the form
st.header("Can you enter below your customer's datas please ?")

# Radio button Female / Male beside each other
st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>",
    unsafe_allow_html=True,
)

df = collecting_data(df)


# st.write('<style>.stButton>button{display:block;margin:0 auto;}</style>', unsafe_allow_html=True)
st.write(
    "<style>.stButton>button{display:block;margin:0 auto;font-size:24px;width:200px;height:80px;}</style>",
    unsafe_allow_html=True,
)

# Create the button and when you click on it, it'll run the code in the condition
if st.button("Predict"):

    predict_churn = modeling(df)
    if predict_churn[0] == "Attrited Customer":
        st.markdown(
            "<h1 style='text-align: center; color: red;'>With the data you gave us, it seems the customer should churn your bank !</h1>",
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            "<h1 style='text-align: center; color: green;'>With the data you gave us, it seems the customer should stay in your bank !</h1>",
            unsafe_allow_html=True,
        )

# Dashboard part
st.header("Dashboard Explanations :")
st.write(
    """This Dashboard has analyzes to see and understand customers' profiles in more detail. 
    It is a visualization made to understand the characteristics of customers and the attrited customers 
    features according to these characteristics parameters. The KPIs of the data above appear in numerical form. 
    Below are 6 different dynamic analysis. By clicking on the analyzes, you can see that the data in the table changes dynamically"""
)

# Link of the Tableau's dashboard
tableau_dashboard = """<div class='tableauPlaceholder' id='viz1677667958870' style='position: relative'><noscript><a href='#'>
                    <img alt='Dashboard Analytics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GY&#47;GYZ6GWSPJ&#47;1_rss.png' style='border: none' />
                    </a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                    <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;GYZ6GWSPJ' /> <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GY&#47;GYZ6GWSPJ&#47;1.png' /> 
                    <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' />
                    <param name='language' value='en-US' /></object></div>                
                    <script type='text/javascript'>                    var divElement = document.getElementById('viz1677667958870');                    
                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) 
                    { vizElement.style.width='1580px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) 
                    { vizElement.style.width='1580px';vizElement.style.height='927px';} else 
                    { vizElement.style.width='100%';vizElement.style.height='2677px';}                     
                    var scriptElement = document.createElement('script');                    
                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""

# To show the dashboard on the app
components.html(tableau_dashboard, width=1580, height=927)

# Dashboard explanations
st.header("Dashboard contains dynamic parameters :")
st.write(
    """1. Attition by Card Color: It shows the reliability and general distribution of customers
according to the card type as a cake slice graph.
2. Number of Clients by Age: It shows the age distribution of customers.
3. Client's INCOME Category: It shows the income distribution of customers.
4. Client's Education Level: Gives customers' education level in 7 different areas.
5. Client's Marital Status: It shows whether customers are married or not in 3
different status.
6. Attrusion Rate by Age: Gives the proportions and number of attrited clients
according to certain age tranches."""
)

# Display the footer
st.image(".streamlit/img/footer.png", width=1580)
