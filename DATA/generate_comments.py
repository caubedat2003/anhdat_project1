import random
import os

# Define file path
file_path = r"C:\DATA\comment_book3.txt"

# Sample data
user_ids = [f"user_{i}" for i in range(1, 1001)]
id_book = [
    "67c41911fe178ddab2bb6480", "67c436a7d91ea203c5769945", "67c58c90b0ac7c96530b4ba8",
    "67c58cf0b0ac7c96530b4ba9", "67c58db5b0ac7c96530b4baa", "67e956f08a6d3c3af4da582b",
    "67e957958a6d3c3af4da582c", "67e958118a6d3c3af4da582d", "67e959188a6d3c3af4da582e",
    "67e959528a6d3c3af4da582f"
]
comments = [
    "Amazing book, a must-read!", "Not what I expected, quite disappointing.", "Absolutely fantastic!", 
    "A bit slow in the middle, but worth finishing.", "Loved the storyline and characters.", 
    "Didn't like the writing style.", "Inspirational and thought-provoking.", "Too complicated for me.",
    "Best book I've read this year!", "A total waste of time.", "Highly recommend to everyone!",
    "Overrated and boring.", "Emotional and beautifully written.", "Had potential but failed.", 
    "Couldn't put it down!", "Lacked depth and originality.", "A classic that everyone should read.",
    "Disjointed plot, not engaging.", "One of the best books in its genre.", "Good for a light read.",
    "Great book, I loved it!", "Not bad, but could be better.", "Amazing read, highly recommended!",
    "Too slow for my taste.", "A masterpiece, will read again!", "Boring and not engaging.",
    "Loved the characters!", "Interesting but overhyped.", "Worth every penny!", "Would not recommend.",
    "Good", "Bad", "Average", "Excellent", "Poor", "Fantastic", "Mediocre",
    "Incredible", "Disappointing", "Satisfactory", "Unsatisfactory", "Remarkable", "Unremarkable",
    "Outstanding", "Subpar", "Exceptional", "Inferior", "Superb", "Lousy",
    "Brilliant", "Dreadful", "Wonderful", "Terrible", "Marvelous", "Awful",
]

# Generate dataset
with open(file_path, "w", encoding="utf-8") as f:
    f.write("user_id,book_id,comment\n")  # CSV header
    for user in user_ids:
        for _ in range(50):  # 50 comments per user
            book = random.choice(id_book)
            comment = random.choice(comments)
            f.write(f"{user},{book},{comment}\n")

print(f"Dataset saved to {file_path}")
