
from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("../data/alpaca_bfsi_dataset.json") as f:
    dataset = json.load(f)

stored_questions = [item["instruction"] + " " + item["input"] for item in dataset]
stored_embeddings = model.encode(stored_questions, convert_to_tensor=True)

def check_similarity(user_query, threshold=0.85):
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, stored_embeddings)
    max_score = scores.max().item()
    if max_score > threshold:
        index = scores.argmax().item()
        return dataset[index]["output"]
    return None
