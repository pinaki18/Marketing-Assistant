import os 
# from apikey import apikey 

import streamlit as st
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain, SimpleSequentialChain
# from langchain.prompts import PromptTemplate



st.title("Your Marketing Assistant")
main_option = st.selectbox(
    "What would you like to generate?",
    ("LinkedIn post","Newsletter","Twitter thread","Ad Copy", "Blog Post", "Other"),
    placeholder="Select an option...",
)


if main_option:
    st.write(f"Great! Now briefly describe the product/service for which you want {main_option}.")
    st.write("Note: If you are describing your product highlight its main features or benefits")
    description = st.text_input("Enter the description here")


target_audience = st.text_input("Do you have a target audience?")
objective = main_option = st.selectbox(
    "Do you have a specific objective?",
    ("Increase awareness","Drive traffic to website","Boost Sales","Engage with audience", "Other"),
    placeholder="Select an option...",
)

# final_template = PromptTemplate(
#     input_variables=['main_option', 'description', 'objective', 'target_audience'],
#     template = f"""Write me a {main_option} based on the following description: Description: {description} Objective: {objective} , Target Audience: {target_audience}"""
# )


# llm = OpenAI(temperature=0.9)
# final_chain = LLMChain(llm=llm, prompt = final_template, verbose=True)