import db_fetch as db_fetch
import importlib
importlib.reload(db_fetch)
import sqlite3
import pandas as pd
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main():
    pass

def create_similarity_matrix():
    ing_parts = joblib.load('../database/ing_parts.z')
    doc = ing_parts.map(lambda x: ' '.join([i for i in x]))
    X = vectorizer.fit_transform(doc)
    cos_sim = cosine_similarity(X)
    joblib.dump(cos_sim, '../database/recipe_cosine_similarity.z')

if __name__ == '__main__':
    main()
