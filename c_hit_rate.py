# -*- coding: utf-8 -*-
"""
Module Name: c_hit_rate.py 
Purpose: Module of common functions to get hit rate
Created data: Sep, 2019
Author: Sophia Yue
"""

def cf_HitRate(topNPredicted, leftOutPredictions):
    """
    Module name: cf_HitRate
    Purpose    : Function to get hit rate
                 ( Item in leftOutPredictions also been selected in top N recommended items)
    Parameters:
       topNPredicted      : top N predictions/items been recommended  
       leftOutPredictions : Predictions form test dataset 
       - leftOutPredictions is a "prediction" object containing:
         The (raw) user id uid.
         The (raw) item id iid.
         The true rating
         The estimated rating   
     Return
       Hit rate 
    """  
    hits = 0
    total = 0
    # For each left-out rating
    for leftOut in leftOutPredictions:
        userID = leftOut[0]
        leftOutProdID = leftOut[1]
        # Is it in the predicted top 10 for this user?
        hit = False
        for prodID, predictedRating in topNPredicted[int(userID)]:
            if (int(leftOutProdID) == int(prodID)):
                hit = True
                break
        if (hit) :
            hits += 1
        total += 1
    # Compute overall precision
    return hits/total