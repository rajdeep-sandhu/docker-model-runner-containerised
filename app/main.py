import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialise OpenAI client
# Use a dummy API key for the client, even though a local LLM does not need one.
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

# Streamlit UI
st.title("LLM Chat")
prompt = st.text_area(
    label="Enter your prompt:", value="Write 500 words about Spitz breeds."
)

if st.button("Send"):
    with st.spinner("Getting response..."):
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        try:
            response = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages=messages
            )

            st.success("Response:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")
