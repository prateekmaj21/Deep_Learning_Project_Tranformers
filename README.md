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


## News Summarization and News Topic ( Part 2): 

The project performs two main tasks:

1. **Zero-Shot Topic Classification:**
    - Uses the `facebook/bart-large-mnli` model to classify input text into predefined categories.
    -  No prior training data for specific topics is needed.
    - The model relies on its general language understanding to infer the most probable topic.
    - Demonstrates the concept of zero-shot learning.
    - Example input text is analyzed for categories: "Politics", "Sport", "Technology", "Entertainment", and "Business".
    - Outputs the probability score for each category.

2. **Text Summarization:**
    - Leverages the `facebook/bart-large-xsum` model for extractive summarization.
    - Generates concise summaries of input text, preserving key information.
    - Sets `do_sample=False` for deterministic output (reproducible summaries).


## How to Run

1.  **Install Dependencies:** Execute the installation commands mentioned above.

2.  **Run the Code:**  Execute the Python script.  It will output the topic classifications and generated summary.


## Example Usage and Output

The code provides an example sequence about the Samsung Galaxy S25 Ultra and its relation to Galaxy AI.


**Zero-Shot Classification Output:**

The code will print the probability score for each candidate label (e.g., Technology, Politics, etc).  The label with the highest probability represents the model's prediction for the input text. Given the example text, "Technology" is expected to have the highest probability.


**Text Summarization Output:**

The code will generate a concise summary of the provided text, constrained by the specified minimum and maximum length parameters.


## Further Development

- **Explore other models:** Experiment with different transformer models for zero-shot classification and summarization to find those that are better suited for your particular needs.

- **Customizable Candidate Labels:** Adapt the `candidate_labels` list to classify text into your custom topics.

- **Fine-tuning:** While this project focuses on zero-shot learning, you could fine-tune these or other models on a custom dataset to achieve even better performance.

- **Evaluation Metrics:** Implement evaluation metrics (precision, recall, F1-score) to assess the accuracy of the classification and summarization tasks.


## Conclusion

This project offers a straightforward example of how to use transformer models for effective text analysis. By employing pre-trained models, the process becomes accessible and efficient.   This serves as a good starting point for building more sophisticated natural language processing applications.

