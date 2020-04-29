import streamlit as st

def test_page_2_func():

    st.title('test page 2')

    userinput = st.slider("how cool is this app?", min_value=0, max_value=10)
    
    st.write('only '+str(userinput)+'? Harsh.')