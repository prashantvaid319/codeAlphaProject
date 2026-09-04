# PROJECT REPORT
## FAQ Chatbot Using NLP and Cosine Similarity

### Abstract
The FAQ Chatbot is an NLP-based application designed to automatically answer frequently asked questions. Instead of manually searching an FAQ page, users can type questions in natural language. The system preprocesses the text, converts questions into TF-IDF vectors, calculates cosine similarity, and returns the answer associated with the most similar FAQ.

### 1. Introduction
Frequently Asked Questions are useful for customer support, but users may have difficulty finding the exact question they need. A chatbot can provide a more natural interface by accepting a question and automatically retrieving the closest known answer.

### 2. Objectives
- Build an FAQ dataset.
- Apply NLP preprocessing.
- Convert text into numerical representations.
- Match questions using cosine similarity.
- Return the best answer.
- Provide an optional web-based chat interface.

### 3. Methodology
The chatbot follows these stages:

1. FAQ Collection
2. Text Cleaning
3. Tokenization
4. Stop-word Removal
5. Lemmatization
6. TF-IDF Vectorization
7. Cosine Similarity
8. Threshold-based Response
9. Chat UI

### 4. TF-IDF
TF-IDF stands for Term Frequency-Inverse Document Frequency. It gives higher importance to terms that are useful for distinguishing documents while reducing the importance of very common words.

### 5. Cosine Similarity
Cosine similarity measures the angle between two vectors. A score closer to 1 indicates stronger similarity, while a score closer to 0 indicates weaker similarity.

### 6. Dataset
The project contains 30 example FAQs covering accounts, passwords, payments, orders, delivery, refunds, returns, coupons, and customer support.

### 7. Software Requirements
- Python 3.x
- NLTK
- scikit-learn
- Streamlit
- NumPy

### 8. Hardware Requirements
A standard laptop or desktop computer is sufficient. No dedicated GPU is required.

### 9. Results
The chatbot successfully matches user questions with semantically or lexically similar FAQ questions when important words overlap. A confidence threshold prevents low-similarity questions from receiving potentially incorrect FAQ answers.

### 10. Limitations
TF-IDF is mainly based on word/phrase overlap. It may fail when two questions have the same meaning but use very different vocabulary.

### 11. Future Scope
The system can be improved using:
- Sentence Transformers
- BERT-based semantic embeddings
- Intent classification
- Multilingual NLP
- Speech recognition
- Database integration
- Authentication and admin management
- Cloud deployment

### 12. Conclusion
The project demonstrates how classical NLP techniques can be combined to create a lightweight and explainable FAQ chatbot. TF-IDF and cosine similarity provide a simple baseline that is fast, easy to understand, and suitable for small FAQ datasets.
