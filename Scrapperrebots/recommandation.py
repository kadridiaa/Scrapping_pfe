import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Constants
ALLOWED_USER_TYPES = ['doctor', 'nurse', 'worker', 'blind', 'handicap', 'deaf', 'non-verbal', 'old people']
ALLOWED_OFFER_TYPES = ['doctor', 'nurse', 'worker']  # Adjusted for doctors, nurses, and workers

# Sample User and Offer Data
users = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'full_name': ['User1', 'User2', 'User3', 'User4'],
    'type': ['doctor', 'nurse', 'worker', 'blind'],
})

offers = pd.DataFrame({
    'id': [101, 102, 103, 104],
    'title': ['Offer1', 'Offer2', 'Offer3', 'Offer4'],
    'description': ['Description1', 'Description2', 'Description3', 'Description4'],
    'type_needed': ['doctor', 'nurse', 'other', 'worker'],
})

# Collaborative Filtering
def user_user_collaborative_filtering(user_id, users, nb_neighbors=2):
    """
    Perform user-user collaborative filtering to recommend offers.

    Parameters:
    - user_id (int): The ID of the user for whom recommendations are needed.
    - users (pd.DataFrame): DataFrame containing user data.
    - nb_neighbors (int): Number of neighbors to consider. Default is 2.

    Returns:
    - List of recommended offer IDs.
    """
    user_data = users[users['id'] == user_id][['id', 'type']]
    users_subset = users[users['type'] == user_data['type'].values[0]]

    if len(users_subset) == 0:
        return []

    # Calculate cosine similarity between users
    user_similarity = cosine_similarity(users_subset[['id']].values.reshape(1, -1),
                                        users_subset[['id']].values)

    # Get the most similar users
    similar_users = pd.Series(user_similarity[0]).sort_values(ascending=False)[1:nb_neighbors + 1]

    return users_subset[users_subset['id'].isin(similar_users.index)]['id'].tolist()

# Content-Based Filtering
def content_based_filtering(user_type, offers):
    """
    Perform content-based filtering to recommend offers based on user type.

    Parameters:
    - user_type (str): The type of the user.
    - offers (pd.DataFrame): DataFrame containing offer data.

    Returns:
    - List of recommended offer IDs.
    """
    # Check if the user type is allowed
    if user_type not in ALLOWED_USER_TYPES:
        return []

    # Filter offers based on user type
    relevant_offers = offers[offers['type_needed'].isin(ALLOWED_OFFER_TYPES)]

    # TF-IDF Vectorization of offer descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(relevant_offers['description'])

    # Use Nearest Neighbors to find similar offers
    nn_model = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')
    nn_model.fit(tfidf_matrix)
    _, indices = nn_model.kneighbors(tfidf_matrix)

    return relevant_offers.iloc[indices.flatten()]['id'].tolist()

# Hybrid Recommendation System
def recommend_offers(user_id, users, offers):
    """
    Recommend offers for a given user using a hybrid recommendation system.

    Parameters:
    - user_id (int): The ID of the user for whom recommendations are needed.
    - users (pd.DataFrame): DataFrame containing user data.
    - offers (pd.DataFrame): DataFrame containing offer data.

    Returns:
    - List of recommended offer IDs.
    """
    # Collaborative Filtering
    similar_users = user_user_collaborative_filtering(user_id, users)

    # Content-Based Filtering
    user_type = users[users['id'] == user_id]['type'].values[0]
    content_based_offers = content_based_filtering(user_type, offers)

    # Combine recommendations
    combined_recommendations = list(set(similar_users + content_based_offers))

    return combined_recommendations

# Example: Get recommendations for all users
for user_id_to_recommend in users['id']:
    recommendations = recommend_offers(user_id_to_recommend, users, offers)
    print(f"Recommended Offers for User{user_id_to_recommend}: {recommendations}")
