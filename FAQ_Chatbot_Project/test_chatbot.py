from chatbot import get_response

tests = [
    "I forgot my password",
    "How can I track my package?",
    "Can I pay using UPI?",
    "I want to return a damaged item",
]

for question in tests:
    answer, score, matched = get_response(question)
    print("\nQuestion:", question)
    print("Answer:", answer)
    print("Score:", round(score, 3))
    print("Matched FAQ:", matched)
