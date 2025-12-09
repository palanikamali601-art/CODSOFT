import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = {
    "title": ["Inception", "Interstellar", "The Dark Knight", "Titanic", "Avatar"],
    "genre": ["Sci-Fi", "Sci-Fi", "Action", "Romance", "Sci-Fi"]
}

df = pd.DataFrame(movies)

vectorizer = TfidfVectorizer()
genre_vectors = vectorizer.fit_transform(df["genre"])


similarity_matrix = cosine_similarity(genre_vectors)


def recommend(movie_name):
    if movie_name not in df["title"].values:
        print("Movie not found!")
        return

    index = df[df["title"] == movie_name].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended movies similar to:", movie_name)
    for i, score in sorted_scores[1:4]: 
        print("-", df["title"][i], f"({df['genre'][i]})")


recommend("Inception")
