# Deep_Learning_Project_Tranformers

## Automatic Text Summarization Evaluation (Part 1): 

This project evaluates the performance of various text summarization models using ROUGE and BERTScore metrics.  Different summarization models from the Hugging Face Transformers library are used, and their outputs are compared against a reference summary.

## Project Setup

1. **Install Dependencies:**  The project relies on several libraries, including `transformers`, `rouge-score`, `bert-score`, and `nltk`.  Ensure these are installed before running.


2. **Reference Summary:** A reference summary is provided as a baseline for comparison.


3. **Evaluation Metrics:**
    * **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**  ROUGE measures the overlap of n-grams between the generated summary and the reference summary.  ROUGE-1, ROUGE-2, and ROUGE-L scores are calculated.
    * **BERTScore:** BERTScore leverages contextual embeddings from BERT to compare the semantic similarity between generated and reference summaries.

## Evaluation Process

The project evaluates several models including: Google's T5 (with two different prompts), DistilBERT, T5 Small, PEGASUS, LED (Longformer Encoder-Decoder), and two versions of Facebook's BART (BART X-SUM and BART CNN Data).

For each model:

1. **Text Input:**  A sample text is used as input to the model.
2. **Summary Generation:** Each model generates a summary of the input text using pre-defined parameters for length and sampling.
3. **Metric Calculation:** ROUGE and BERTScore are calculated, comparing the generated summary to the reference summary.
4. **Results:** The precision, recall, and F1-score for each metric are displayed for each model.


## Results Interpretation

The results section (output of the script) provides the evaluation scores for each model. A higher score indicates better performance.  Comparison of the scores across models allows determining which model provides the most accurate and relevant summary.

The specific scores will vary depending on the text input and the models' capabilities but serve as a comparative assessment of their summarization skills.
