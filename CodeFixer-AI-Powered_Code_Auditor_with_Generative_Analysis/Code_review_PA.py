import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
key = os.getenv('GEMINI_API_KEY')

try:
    # Setting up the API key
    genai.configure(api_key=key)
except Exception as e:
    st.error("Failed to configure the Generative AI API. Please check your API key.")
    st.stop()

# Setting up the headers
st.title("🤖 CodeFixer: Your AI Reviewer")
st.subheader('Struggling with Python code? Let CodeFixer help!')

# Taking user input
user_prompt = st.text_area("Paste your Python code here:")

# If the button is clicked, generate responses
if st.button("Analyze Code"):
    try:
        model = genai.GenerativeModel(model_name='models/gemini-2.5-flash',
                                  system_instruction="""You are a friendly AI assistant.
                                                        Given a python code to review, analyze the submitted code and identify bugs, errors or areas of improvement.
                                                        Provide the fixed code snippets.
                                                        Explain the reasoning behind code corrections or suggestions. 
                                                        If the code is not in python politely 
                                                        remind the user that you are a python code review assistant.
                                                       """)
        # If the prompt is provided
        if user_prompt:
            response = model.generate_content(user_prompt)
            
            # Displaying the response on the webpage
            st.write("### Review Results:")
            st.write(response.text)
        else:
            st.warning("Please enter some Python code to analyze.")
    except Exception as e:
        st.error(f"An error occurred while processing your request: {e}")