import streamlit as st
import openai
from googletrans import Translator

# Set your API key
api_key = "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"
openai.api_key = api_key

# Initialize the translator
translator = Translator()

# Streamlit app title
st.title("Marathi Text Generation with OpenAI")

# Sidebar for user input
prompt = st.text_area("Enter your prompt in Marathi")

# Generate text when the user clicks the button
if st.button("Generate"):
    # Request completion from the API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    # Translate the generated text to Marathi
    generated_text = response.choices[0].text.strip()
    translated_text = translator.translate(generated_text, src='en', dest='mr').text

    # Display animated text and box with the translated response
    st.write("## Generating text...")
    with st.spinner('In progress...'):
        st.success(translated_text)
