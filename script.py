import pandas as pd
import string
import matplotlib.pyplot as plt

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

movies = pd.read_csv('train.txt', sep='\t', names=["title", "from", "genre", "director", "plot"])

plot = movies['plot'].apply(preprocess_text)

print(plot.head())

rows, cols = movies.shape
print(f"Number of rows: {rows}, number of columns: {cols}")

# histogram of genres



