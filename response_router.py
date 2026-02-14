
from similarity_engine import check_similarity

def get_final_response(user_query):
    dataset_response = check_similarity(user_query)
    if dataset_response:
        return dataset_response
    return "Your request will be processed as per bank policy guidelines."
