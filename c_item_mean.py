# -*- coding: utf-8 -*-
"""
Module Name: c_get_unit_qty_mean.py 
Purpose: Module of common functions to get item mean
Created data: Sep, 2019
Author: Sophia Yue
"""
def c_get_unit_qty_mean(s_dataset):
   """
     module name: c_get_unit_qty_mean
     Purpose    : Common function to reate a dictionay with key as iprod_sk and value as mean of unit_qty                    
     Parameter
       s_dataset : Surprise  dataset with columns of ihh_sk, iprod_sk, unit_qty 
     
    return:
       d_mean : a dictionary with key as iprod_sk and value as mean of unit_qty  
       df_mean: a dataframe with columns of iprod_sk, prod_sk, and unit_qty_mean 
   
    Steps:
        1: Create a dataframe from a list of iprod_sk, prod_sk, unit_qty mean
        2: Craete a dataframe to get mean of unit_qty for iprod_sk 
        3: Build a dictionary with key as iprod_sk and value as mean of unit_qty
        4: Build a dataframe as iprod_sk, prod_sk, qty_unit_mean
   """      
   iprod_sk_unit = []
   for ihh_sk in range(s_dataset.n_users):
       _unit_qty = s_dataset.ur[ihh_sk]
       for iprod_sk, unit_qty in _unit_qty:
           iprod_sk_unit.append([iprod_sk, s_dataset.to_raw_iid(iprod_sk).astype(np.int64),unit_qty])
   df = pd.DataFrame(iprod_sk_unit)
   df.columns = ['iprod_sk', 'prod_sk', 'unit_qty']
   print("c_get_qty_mean - df.head", df.head() )
   
   """
    step2: Craete a dataframe to get mean of unit_qty group by iprod_sk and prod_sk   
           -  df_qty_mean_x with index as iprod_sk and prod_sk with column of mean of unit_qty
   """
   df_qty_mean_x = df.groupby (by = ['iprod_sk', 'prod_sk']).agg({'unit_qty':['mean']}) 
   
   """
    step3: Build and return a dictionary with key as iprod_sk and value as mean 
   """
   mean_ary= []
   l_iprod_sk = []
   l_mean = []
   for index, row in df_qty_mean_x.iterrows():
       l_index = list(index)   # nw: 'tuple' object has no attribute 'apply'
       iprod_sk = l_index[0]
       prod_sk  = l_index[1]
       u_mean =  round(list(row)[0],4) 
       mean_ary.append([iprod_sk, prod_sk, u_mean])
       l_iprod_sk.append(iprod_sk)
       l_mean.append(u_mean)
    
   #3: Build a dictionary with key as iprod_sk and value as mean of unit_qty 
   d_mean = dict(zip(l_iprod_sk, l_mean))
    
   # Step4: Build a dataframe as iprod_sk, prod_sk, qty_unit_mean
   df_mean = pd.DataFrame(l_iprod_sk)
   df_mean.columns = ['iprod_sk', 'prod_sk', 'unit_qty_mean']
   return d_mean, df_mean
  
    
def c_build_trainset(tnx_tbl, userName, passWord, N, M, maxScale)
    """
     module name: c_build_trainset
     Purpose    : build trainset
     Parameter
       tnx_tbl : Transaction table with schema 
       N       : No of most popular user
       M       : No of most popular product 
       userName: User name to access Teradata 
       passWord: Password to access Teradata 
       maxScale: Maximum unit_qty  
    return:
       d_mean: a dictionary with key as iprod_sk and value as mean of unit_qty  
    Steps:       
     1. Connect to Teradata 
     2. Run a query to read data from Teradata table and create a dataframe
     3. Get most popular hh_sk  and prod_sk
     4: Build surprise dataset 
     5: Build trainSet and testSet
    """
    #Step1: Connect to Teradata 
    udaExec = teradata.UdaExec (appName="Teradata_Test", version="1.0", logConsole=False)
    session = udaExec.connect(method="odbc", system="tqdpr02",
            username = userName, password= passWord
    
    #Step2: Run a query to read data from Teradata table and create a dataframe
    query = """
    select HH_SK, PROD_SK, UNIT_QTY   
    from {0}""".format()
    df_sum_qty = pd.read_sql(query,session) 
    
    # Step3: Get most popular hh_sk  and prod_sk
    user_ids_count = Counter(df_sum_qty.HH_SK)   # type: collections.Counter
    prod_ids_count = Counter(df_sum_qty.PROD_SK)
   
    user_ids = [u for u, c in user_ids_count.most_common(N)]
    prod_ids = [m for m, c in prod_ids_count.most_common(M)]
    df_sum_qty_final = df_sum_qty[df_sum_qty.HH_SK.isin(user_ids) & df_sum_qty.PROD_SK.isin(prod_ids)]  
    
    # Step4: Build surprise dataset                         
    reader = Reader(rating_scale=(1, maxScale))  # Reader object; rating_scale is required 
    data = Dataset.load_from_df(df_sum_qty_final[['HH_SK', 'PROD_SK', 'UNIT_QTY']], reader) # type:  surprise.dataset.DatasetAutoFolds
    ft = data.build_full_trainset()
    print("The total no of users in ft = data.build_full_trainset():", ft.n_users,  "The total no of items in ft:", ft.n_items )
    
    """
     Step5: Build trainSet and testSet
     - Set aside one purchase per user for testing
       - Randomly remove one row from data to create the testSet and the rest would be trainSet
         - If the user only has one row, it'll not in trainSet 
    """
    LOOCV = LeaveOneOut(n_splits=1, random_state=1)
    for train, test in LOOCV.split(data):
        trainSet = train
        testSet  =  test
    print("The total number of users in trainSet:", trainSet.n_users,  "The total number of items in trainSet:", trainSet.n_items ) 
    print("The total length of testSet:", len(testSet),"\nExample of testSet:", testSet[0:2])     
    return trainSet, testSet