import streamlit as st
import requests

def test_page_1_func():
    st.title("test page 1")

    userinput = st.text_input("submit a review to score.")

    url = 'http://labs-yelp-api-dev.us-east-1.elasticbeanstalk.com/infer_sentiment/'


    query_string = {'review': userinput}
    r = requests.get(url=url, params=query_string)

    response = r.json()
    
    st.write(str(response['sentiment']))