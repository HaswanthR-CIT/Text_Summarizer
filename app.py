from flask import Flask, render_template, request
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import re

app = Flask(__name__)

# Initialize the summarizer model
print("Loading the summarization model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Model loaded successfully!")

# Initialize NLTK resources
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def trim_to_last_sentence(text, max_sentences):
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Limit to max_sentences, ensuring complete sentences
    sentences = sentences[:max_sentences]
    if sentences and sentences[-1] and not sentences[-1].endswith(('.', '!', '?')):
        sentences = sentences[:-1]
    return ' '.join(sentences) if sentences else text

def extract_topics(text, top_n=5):
    # Tokenize and filter
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalnum() and word not in stop_words]
    # Count frequencies
    word_counts = Counter(words)
    # Grab top N words
    return [word for word, _ in word_counts.most_common(top_n)]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        text = request.form.get("text")
        length_choice = request.form.get("length")

        # Debug log
        print(f"Received length choice: {length_choice}")

        # Validate input
        if not text or len(text.split()) < 30:
            error = "Please enter at least 30 words for a better summary."
            return render_template("index.html", error=error)

        # Set length parameters
        if length_choice == "short":
            max_length = 30
            min_length = 10
            max_sentences = 2
        elif length_choice == "medium":
            max_length = 50
            min_length = 20
            max_sentences = 3
        elif length_choice == "long":
            max_length = 80
            min_length = 30
            max_sentences = 4
        else:
            max_length = 50
            min_length = 20
            max_sentences = 3  # Default medium

        # Generate summary and topics
        try:
            summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            summary_text = summary[0]["summary_text"]
            # Trim to complete sentences
            summary_text = trim_to_last_sentence(summary_text, max_sentences)
            # Get topics
            topics = extract_topics(text)
            print(f"Generated summary: {summary_text}")
            print(f"Extracted topics: {topics}")
            return render_template("index.html", summary=summary_text, original_text=text, topics=topics)
        except Exception as e:
            error = f"Something went wrong: {str(e)}"
            return render_template("index.html", error=error)

    # GET: Show form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)