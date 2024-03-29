
import pickle
from recommender import AprioriRecommentor
import json
import pandas as pd
# with open("./recommender_model.pkl", "rb") as model_object:
#     model = pickle.load(model_object)
    
#     model_object.close()

model = pd.read_pickle("final_model.pkl")
    
res = model.show_products_recommended_to_user(20712)

print(json.dumps(res, indent = 4) )