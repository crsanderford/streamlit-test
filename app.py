import streamlit as st

from test_module.test_page_1 import test_page_1_func
from test_module.test_page_2 import test_page_2_func


def main():
    st.sidebar.title("Streamlit Test")

    page_labels = ['test page 1', 'test page 2']
    page_funcs = [test_page_1_func, test_page_2_func]

    page_dict = dict(zip(page_labels,page_funcs))



    userinput = st.sidebar.selectbox(label='choose a page', options=page_labels)

    func_to_run = page_dict[userinput]
    func_to_run()


if __name__ == "__main__":
    main()