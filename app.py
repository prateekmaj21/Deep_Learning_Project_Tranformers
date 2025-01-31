import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer, SimilarityFunction
import nltk
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import torch
from transformers import pipeline

# Download stopwords if not already done
nltk.download('stopwords', quiet=True)

st.title("Text Classification and Summarization")

# Text input area
sequence_to_classify = st.text_area("Enter text here:", height=200, value="""The Samsung Galaxy S25 Ultra will be the flagship handset for the company's Galaxy AI software. Following the launch at the upcoming Galaxy Unpacked event, the S25 family, including the powerful Galaxy S25 Ultra, will be the basis for the development and growth of Galaxy AI through 2025 and beyond.
It’s an opportunity for Samsung to take the initiative and determine the future of mobile artificial intelligence.
Although Google used the launch of the Pixel 8 and Pixel 8 Pro in October 2023 as the signal to start the AI-powered smartphone revolution, Samsung’s simultaneous launch of the Galaxy S24 family and the introduction of Galaxy AI brought AI to the mainstream consumer. Kantar Research cited AI as a driving force behind sales in 2024, with nearly 1 in 4 consumers purchasing a Galaxy S24 handset on the strength of AI.
""")


if st.button("Classify and Summarize"):
    try:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        candidate_labels = ["Politics", "Sport", "Technology", "Entertainment", "Business"]
        result = classifier(sequence_to_classify, candidate_labels, multi_label=False)

        st.subheader("Classification Results:")
        for label, score in zip(result['labels'], result['scores']):
            st.write(f"{label}: {score:.2f}")
        
        summarizer = pipeline("summarization", model="facebook/bart-large-xsum")
        summary = summarizer(sequence_to_classify, max_length=80, min_length=70, do_sample=False)
        res = summary[0]['summary_text']

        st.subheader("Summary:")
        st.write(res)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
