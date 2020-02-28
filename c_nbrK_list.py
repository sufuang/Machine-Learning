# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:47:22 2019
Module Name: c_nbrK_list.py 
Purpose: Commom module to import packages/libraries 
Created data: Sep, 2019
Author: Sophia Yue
"""


def cf_cr_nbrK_list(iuid, kNeighbors, raw_uid= True):
       """
         module name: cf_cr_nbrK_list
         Purpose    : Create a list of raw iuid, raw uid/iid and score in kNeighbors
                      - The list will create an array and will be used to merge with topN items  
         Parameter:
           iuid: Internal user id
           kNeighbors: A list of  tuple with uid/iid and score for k Neighbors for iuid  
           raw_uid   : An indicator to use to_raw_uid or to_raw_iid to convert the internal id in kNeighbors to raw id
            True  (Default)
             - The id in kNeighbors is internal user id
               - Will use use to_raw_uid  to convert the internal id to raw id
           False
             - The id in kNeighbors is internal item id
               - Will use use to_raw_uid  to convert the internal id to raw id
           
        return:
           A list with raw iuid, raw uid/iid and score in kNeighbors 
        Notes: 
         - The score referred to unit_qty
         - The item id  refered to prod_hhsk 
       """ 
    
       """
         bnbr_x is by converting/flatening the list of tuple in kNeighbors to a flat list, e.g.
         [(iuid0, score0), (iuid1, score1) .... (iuid9, score9)] -> [iuid0, score0, iuid1, score1 .... iuid9, score9] 
       """
       knbr_x =  list (itertools.chain(*kNeighbors)) 
        
       """
        knbr_y is a list of tuple of raw id  and score, e.g 
        [iuid0, score0, iuid1, score1 .... iuid9, score9]  -> [('rid0', score0), ('rid1', score1) .... ('rid9', score9)] 
       """
       knbr_id     =  knbr_x[::2]      # Get internal user id from knbr_x (:2 would skip the score)
       knbr_rnkscr = knbr_x[1::2]      # get rank for itembase or score for userbase from knbr_x 
       if raw_uid:
          knbr_rawid  = [trainSet.to_raw_uid(x) for x in knbr_id]  # Convert internal user id to raw user id  
       else:
          knbr_rawid  = [trainSet.to_raw_iid(x) for x in knbr_id]  # Convert internal item id to raw id  
          
       knbr_y = list(zip(knbr_rawid, knbr_rnkscr) )   
    
       """
       knbr is a list of target user raw id, and raw id and score of user which  is close to the target user, e.g, 
       ['rid', 'rid0', score0,  .... 'rid9', score9]
       """
       return  [trainSet.to_raw_uid(iuid)] + list (itertools.chain(*knbr_y)) # convert list of tuple to a list