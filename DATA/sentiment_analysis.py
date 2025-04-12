import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, LSTM, SimpleRNN
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
import random
import pickle

# Load comments dataset
DATA_PATH = "C:/DATA/comment_book.txt"
DATA_PATH2 = "C:/DATA/comment_book2.txt"
DATA_PATH3 = "C:/DATA/comment_book3.txt"
def load_comments(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        comments = f.readlines()
    return [comment.strip() for comment in comments]

comments = load_comments(DATA_PATH)
comments2 = load_comments(DATA_PATH2)
comments.extend(comments2)  # Combine both datasets
comments3 = load_comments(DATA_PATH3)
comments.extend(comments3)  # Combine all datasets

# Generate random labels (0: Negative, 1: Neutral, 2: Positive) for demonstration
labels = [random.randint(0, 2) for _ in range(len(comments))]

# Tokenization and sequence conversion
tokenizer = Tokenizer()
tokenizer.fit_on_texts(comments)
sequences = tokenizer.texts_to_sequences(comments)
word_index = tokenizer.word_index

# Padding sequences
max_length = 100
X = pad_sequences(sequences, maxlen=max_length)
y = np.array(labels)

# Load pre-trained Word2Vec model
word2vec_model = Word2Vec.load("C:/DATA/word2vec_model.model")
embedding_dim = 100

# Create embedding matrix
embedding_matrix = np.zeros((len(word_index) + 1, embedding_dim))
for word, i in word_index.items():
    if word in word2vec_model.wv:
        embedding_matrix[i] = word2vec_model.wv[word]

# Define model creation functions
def create_cnn_model():
    model = Sequential([
        Embedding(input_dim=len(word_index) + 1, output_dim=embedding_dim, weights=[embedding_matrix], 
                  input_length=max_length, trainable=False),
        Conv1D(filters=128, kernel_size=5, activation='relu'),
        GlobalMaxPooling1D(),
        Dense(3, activation='softmax')
    ])
    return model

def create_rnn_model():
    model = Sequential([
        Embedding(input_dim=len(word_index) + 1, output_dim=embedding_dim, weights=[embedding_matrix], 
                  input_length=max_length, trainable=False),
        SimpleRNN(128, return_sequences=False),
        Dense(3, activation='softmax')
    ])
    return model

def create_lstm_model():
    model = Sequential([
        Embedding(input_dim=len(word_index) + 1, output_dim=embedding_dim, weights=[embedding_matrix], 
                  input_length=max_length, trainable=False),
        LSTM(128, return_sequences=False),
        Dense(3, activation='softmax')
    ])
    return model

# Compile and train models
def train_model(model, X_train, y_train, X_test, y_test, model_name):
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))
    model.save(f"C:/DATA/{model_name}.h5")
    print(f"✅ {model_name} trained and saved!")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create, train, and save models
cnn_model = create_cnn_model()
train_model(cnn_model, X_train, y_train, X_test, y_test, "cnn_sentiment")

rnn_model = create_rnn_model()
train_model(rnn_model, X_train, y_train, X_test, y_test, "rnn_sentiment")

lstm_model = create_lstm_model()
train_model(lstm_model, X_train, y_train, X_test, y_test, "lstm_sentiment")

# Save test data
np.save("C:/DATA/X_test.npy", X_test)
np.save("C:/DATA/y_test.npy", y_test)

TOKENIZER_PATH = "C:/DATA/tokenizer.pkl"

# Save the tokenizer
with open(TOKENIZER_PATH, "wb") as handle:
    pickle.dump(tokenizer, handle)


print("✅ All models trained successfully!")