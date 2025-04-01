from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bson import ObjectId
from .models import Comment
from book.models import Book
from book.serializers import BookSerializer
from .serializers import CommentSerializer
import numpy as np
import tensorflow as tf
from mongoengine.queryset.visitor import Q

class CommentListAPIView(APIView):
    def get(self, request, product_id):
        try:
            comments = Comment.objects(product=ObjectId(product_id))  # Ensure proper ID filtering
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AddCommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.create(serializer.validated_data)
            return Response({"message": "Comment added successfully!", "comment": CommentSerializer(comment).data}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Load tokenizer
import pickle

TOKENIZER_PATH = "C:/DATA/tokenizer.pkl"
MODEL_PATH = "C:/DATA/lstm_sentiment.h5"

with open(TOKENIZER_PATH, "rb") as handle:
    tokenizer = pickle.load(handle)

# Load sentiment analysis model
model = tf.keras.models.load_model(MODEL_PATH)

# Define max length (same as training)
MAX_LENGTH = 100

def preprocess_text(comments):
    """Tokenize and pad comments for prediction."""
    sequences = tokenizer.texts_to_sequences(comments)
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_LENGTH)
    return padded_sequences

def predict_sentiment_score(comment_text):
    """Predict sentiment score using the LSTM model."""
    processed_comment = preprocess_text([comment_text])  # Preprocess input
    prediction = model.predict(processed_comment)  # Get prediction probabilities

    # Extract positive sentiment probability (index 2 corresponds to 'positive')
    positive_score = float(prediction[0][2])  # Ensure it's a float
    return positive_score
class RecommendBooksAPIView(APIView):
    def get(self, request):
        # Get all books
        all_books = Book.objects.filter(_cls="Product.Book")

        book_scores = []

        for book in all_books:
            comments = Comment.objects.filter(product=book)
            if not comments:
                continue  # Skip books without comments
            
            sentiment_scores = []

            for comment in comments:
                sentiment_score = predict_sentiment_score(comment.content)
                sentiment_scores.append(sentiment_score)

            # Calculate average sentiment score
            avg_sentiment_score = np.mean(sentiment_scores) if sentiment_scores else 0.0

            # Debugging: Print sentiment scores to confirm sorting behavior
            print(f"Book: {book.title} | Avg Sentiment Score: {avg_sentiment_score}")

            # Store book with its AI-predicted average sentiment score
            book_scores.append((book, avg_sentiment_score))

        # Sort books by AI-predicted average sentiment score (highest first)
        sorted_books = sorted(book_scores, key=lambda x: x[1], reverse=True)

        # Select top books
        top_books = [book[0] for book in sorted_books]

        # Serialize books
        serializer = BookSerializer(top_books, many=True)

        return Response(serializer.data)