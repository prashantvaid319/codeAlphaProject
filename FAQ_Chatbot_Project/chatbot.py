import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess

BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "data" / "faqs.json"

with open(FAQ_FILE, "r", encoding="utf-8") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
faq_vectors = vectorizer.fit_transform(processed_questions)

def get_response(user_question: str, threshold: float = 0.20):
    if not user_question.strip():
        return "Please enter a question.", 0.0, None

    processed_query = preprocess(user_question)
    query_vector = vectorizer.transform([processed_query])

    scores = cosine_similarity(query_vector, faq_vectors)[0]
    best_index = scores.argmax()
    best_score = float(scores[best_index])

    if best_score < threshold:
        return (
            "Sorry, I couldn't find a relevant answer. "
            "Please rephrase your question or contact customer support.",
            best_score,
            None,
        )

    return faqs[best_index]["answer"], best_score, faqs[best_index]["question"]

def chat():
    print("=" * 55)
    print("        FAQ CHATBOT - TF-IDF + COSINE SIMILARITY")
    print("=" * 55)
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Goodbye!")
            break

        answer, score, matched_question = get_response(user_input)
        print(f"Bot: {answer}")
        if matched_question:
            print(f"[Matched FAQ: {matched_question} | Score: {score:.2f}]")
        print()

if __name__ == "__main__":
    chat()
