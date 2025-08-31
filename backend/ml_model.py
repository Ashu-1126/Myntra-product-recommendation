import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Define file paths for the saved model and data
model_file_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

def train_and_save_model():
    """
    Loads data, trains the model, and saves the trained model and data to disk.
    This function should be run once locally to generate the necessary files.
    """
    products_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "cleaned_myntra_dataset_backend.csv"))

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix_content = tfidf_vectorizer.fit_transform(products_df["tags"])
    cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

    indices = pd.Series(products_df.index, index=products_df["p_id"]).drop_duplicates()
    
    # Save the model and data to a pickle file
    with open(model_file_path, 'wb') as model_file:
        pickle.dump({
            'tfidf_vectorizer': tfidf_vectorizer,
            'cosine_similarities_content': cosine_similarities_content,
            'indices': indices,
            'product_ids': products_df["p_id"]
        }, model_file)
    print("Machine learning model and data saved successfully.")

def load_model_and_data():
    """
    Loads the pre-saved model and data from disk.
    This function is designed for lazy loading.
    """
    if not os.path.exists(model_file_path):
        raise FileNotFoundError(f"Model file not found at {model_file_path}. Please run ml_model.py locally to train and save the model.")
        
    with open(model_file_path, 'rb') as model_file:
        model_data = pickle.load(model_file)
    return model_data

def give_recommendation(p_id, model_data):
    """
    Generates product recommendations based on a given product ID.
    """
    indices = model_data['indices']
    cosine_similarities_content = model_data['cosine_similarities_content']
    products_ids = model_data['product_ids']

    idx = indices.get(p_id)
    if idx is None:
        return []

    cosine_scores = list(enumerate(cosine_similarities_content[idx]))
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
    cosine_scores = cosine_scores[1:11]
    products_indices = [i[0] for i in cosine_scores]
    product_ids = products_ids.iloc[products_indices].tolist()
    return product_ids

if __name__ == "__main__":
    train_and_save_model()
