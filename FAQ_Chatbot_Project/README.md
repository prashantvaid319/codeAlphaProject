# FAQ Chatbot using NLP and Cosine Similarity

## 1. Project Overview
This project implements a simple FAQ chatbot that matches a user's question with the most similar question in a predefined FAQ dataset.

## 2. Technologies
- Python
- NLTK
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit

## 3. Architecture
User Question
-> Text Preprocessing
-> TF-IDF Vectorization
-> Cosine Similarity
-> Best FAQ
-> Answer

## 4. NLP Preprocessing
The chatbot:
1. Converts text to lowercase.
2. Removes non-alphabetic characters.
3. Tokenizes the text using NLTK.
4. Removes English stop words.
5. Lemmatizes tokens.

## 5. Matching
TF-IDF converts FAQ questions and the user's question into numerical vectors. Cosine similarity compares the vectors. The FAQ with the highest score is selected.

A threshold of 0.20 is used to avoid returning unrelated answers.

## 6. Installation

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install packages:
```bash
pip install -r requirements.txt
```

## 7. Run in Terminal

```bash
python chatbot.py
```

## 8. Run Web UI

```bash
streamlit run app.py
```

## 9. Example
User:
"I forgot my login password"

Bot:
"Click 'Forgot Password' on the login page and follow the instructions sent to your registered email."

## 10. Future Improvements
- Sentence-BERT embeddings for semantic similarity
- Intent classification
- Voice input/output
- Database-backed FAQs
- Admin panel for adding FAQs
- Multilingual support
- Conversation history
- Deployment on Streamlit Cloud

## 11. Viva Questions
1. What is NLP?
2. Why is preprocessing needed?
3. What is tokenization?
4. What are stop words?
5. What is lemmatization?
6. What is TF-IDF?
7. What is cosine similarity?
8. Why is cosine similarity useful for text?
9. What is the purpose of the similarity threshold?
10. What are the limitations of TF-IDF?
11. How could BERT improve this chatbot?
12. What is the time complexity of matching against N FAQs?

## 12. Short Project Description
An NLP-based FAQ chatbot was developed using NLTK and scikit-learn. The system preprocesses FAQ questions and user queries, represents them using TF-IDF vectors, calculates cosine similarity, and returns the answer associated with the most similar FAQ. A Streamlit interface provides a simple interactive chat experience.
