import gensim
import nltk
import string
import re
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

# Ensure necessary NLTK resources are downloaded
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words("english"))

# Load dataset
def load_comments(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = f.readlines()
    return [comment.strip() for comment in comments]

# Preprocess text
def preprocess_text(text):
    text = text.lower()  # Lowercasing
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenization
    tokens = [word for word in tokens if word not in STOPWORDS]  # Remove stopwords
    return tokens

# Load and preprocess comments
comments = load_comments("C:/DATA/comment_book.txt")
comments2 = load_comments("C:/DATA/comment_book2.txt")
comments.extend(comments2)  # Combine both datasets
comments3 = load_comments("C:/DATA/comment_book3.txt")
comments.extend(comments3)  # Combine all datasets
processed_comments = [preprocess_text(comment) for comment in comments]

# Train Word2Vec model
word2vec_model = Word2Vec(sentences=processed_comments, vector_size=100, window=5, min_count=2, workers=4)

# Save the trained model
word2vec_model.save("C:/DATA/word2vec_model.model")

print("✅ Word2Vec model trained and saved successfully!")
