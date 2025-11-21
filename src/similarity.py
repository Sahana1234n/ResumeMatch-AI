from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ats_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def calculate_similarity_bert(text1, text2):
    """
    Calculate cosine similarity between two texts using SBERT embeddings.
    
    Args:
        text1 (str): First text (resume)
        text2 (str): Second text (job description)
    
    Returns:
        float: Cosine similarity score between 0 and 1
    """
    # Encode the texts to embeddings
    embeddings1 = ats_model.encode(text1, convert_to_numpy=True)
    embeddings2 = ats_model.encode(text2, convert_to_numpy=True)
    
    # Normalize embeddings (optional but recommended)
    embeddings1 = embeddings1 / np.linalg.norm(embeddings1)
    embeddings2 = embeddings2 / np.linalg.norm(embeddings2)
    
    # Compute cosine similarity
    similarity = float(np.dot(embeddings1, embeddings2))
    return similarity