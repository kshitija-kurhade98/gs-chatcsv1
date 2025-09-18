#import streamlit as st

#st.title('🎈 App Name')

#st.write('Hello world!')

import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI

load_dotenv()


openai_api_key = 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


def chat_with_csv(df,prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(result)
    return result

st.set_page_config(layout='wide')

st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv)
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            if input_text is not None:
                if st.button("Chat with CSV"):
                    st.info("Your Query: "+input_text)
                    result = chat_with_csv(data, input_text)
                    st.success(result)

