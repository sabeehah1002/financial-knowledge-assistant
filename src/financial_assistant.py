import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENT_FOLDER = os.path.join(BASE_DIR, "documents")

STOP_WORDS = {
    "what", "should", "we", "do", "for", "the", "is", "are", "a", "an",
    "to", "and", "or", "of", "in", "on", "with", "by", "be", "can",
    "how", "who", "when", "where", "why", "it", "this", "that"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text

def get_keywords(text):
    words = clean_text(text).split()
    return [word for word in words if word not in STOP_WORDS and len(word) > 2]

def load_documents():
    documents = {}

    for file_name in os.listdir(DOCUMENT_FOLDER):
        if file_name.endswith(".txt"):
            file_path = os.path.join(DOCUMENT_FOLDER, file_name)

            with open(file_path, "r", encoding="utf-8") as file:
                documents[file_name] = file.read()

    return documents

def calculate_score(question, document_text):
    question_keywords = get_keywords(question)
    document_words = get_keywords(document_text)

    score = 0

    for keyword in question_keywords:
        if keyword in document_words:
            score += document_words.count(keyword)

    return score

def find_best_document(question, documents):
    best_document_name = None
    best_document_text = ""
    best_score = 0

    for document_name, document_text in documents.items():
        score = calculate_score(question, document_text)

        if score > best_score:
            best_score = score
            best_document_name = document_name
            best_document_text = document_text

    return best_document_name, best_document_text, best_score

def find_best_sentences(question, document_text):
    question_keywords = get_keywords(question)
    sentences = re.split(r"(?<=[.!?])\s+", document_text)

    sentence_scores = []

    for sentence in sentences:
        sentence_words = get_keywords(sentence)
        score = 0

        for keyword in question_keywords:
            if keyword in sentence_words:
                score += 1

        if score > 0:
            sentence_scores.append((score, sentence.strip()))

    sentence_scores.sort(reverse=True)

    top_sentences = [sentence for score, sentence in sentence_scores[:2]]
    return top_sentences
def search_policy(question):
    documents = load_documents()
    document_name, document_text, score = find_best_document(question, documents)

    if score == 0:
        return "No matching policy found. Please ask a different question."

    best_sentences = find_best_sentences(question, document_text)

    answer = " ".join(best_sentences)
    return f"{answer}\n\nSource: {document_name}"

def main():
    documents = load_documents()

    print("Financial Knowledge Assistant")
    print("=============================")
    print("This assistant searches banking policy documents.")
    print("You can ask about fraud, wire transfers, customer data, compliance, or access control.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Enter your question: ")

        if question.lower() == "exit":
            print("Thank you. Exiting the assistant.")
            break

        document_name, document_text, score = find_best_document(question, documents)

        if score == 0:
            print("\nNo matching policy found. Please ask a different question.\n")
        else:
            best_sentences = find_best_sentences(question, document_text)

            print("\nMost Relevant Document:", document_name)
            print("Match Score:", score)

            print("\nAnswer:")
            for sentence in best_sentences:
                print("-", sentence)

            print("\nSource:")
            print("This answer was retrieved from:", document_name)
            print("-" * 60)

if __name__ == "__main__":
    main()