import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
You will be given text. This will be enclosed in triple backticks.
You are a compliance checker for the registration of a medical device under the MDR regulation. 
Check whether the given text by the user fulfills the requirements. If the Requirement is fulfilled, return TRUE. Jump a line and then congratulate the user on getting their MDR certification.
Otherwise return FALSE, jump a line, explain what is wrong, and rewrite the text according to correct standards.

'''{description}'''

Result:
"""


prompt = PromptTemplate(
    input_variables=["description"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="MedRegPro", page_icon=":robot:")
st.header("MedRegPro checker")

st.markdown("Requirement: Provide a general description of the device, including its intended purpose, intended users (e.g., healthcare professionals, patients), and the medical conditions, diseases, or medical states it's meant to diagnose, treat, monitor, prevent, or alleviate. It should also cover the device's mode of action and the principle of operation")

def get_api_key():
    return "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"

openai_api_key = get_api_key()

def get_text():
    input_text = st.text_area(label="Device Description", label_visibility='collapsed', placeholder="Your description...", key="input")
    return input_text

input = get_text()


def get_feedback():
    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_description = prompt.format(description=input)

    formatted_description = llm(prompt_with_description)

    st.write("## Your Feedback")

    st.write(formatted_description)

if st.button("*Check*", type='primary', help="Just click bro come on."):
       
    with st.spinner("Checking MDR Regulations... please wait..."):
       

       
        get_feedback()


