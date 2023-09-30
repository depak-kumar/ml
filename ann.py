# Import necessary libraries
import streamlit as st
from faker import Faker

# Create a Faker instance
fake = Faker()

# Streamlit app title and description
st.title("Anonymous Text Generator")
st.write("This app generates random anonymous text.")

# Sidebar options
with st.sidebar:
    st.write("Options:")
    num_paragraphs = st.slider("Number of Paragraphs", 1, 10, 1)
    num_sentences = st.slider("Sentences per Paragraph", 1, 10, 3)

# Generate and display anonymous text
st.header("Generated Text:")
for _ in range(num_paragraphs):
    paragraph = fake.paragraphs(nb=num_sentences)
    st.write(paragraph)

# Footer
st.write("Powered by Streamlit and Faker.")
