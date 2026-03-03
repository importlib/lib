from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def word_similarity(word1, word2):
 words = [word1, word2]
 
 vectorizer = TfidfVectorizer()
 tfidf_matrix = vectorizer.fit_transform(words)
 
 similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
 similarity_percentage = similarity[0][0] * 100
    
 return similarity_percentage

 
similarity_score = word_similarity('apple', 'apple')

print(f"Similarity Score: {similarity_score}")
