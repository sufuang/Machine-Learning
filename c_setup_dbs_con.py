# -*- coding: utf-8 -*-
"""
Module Name: c_setup_dbs_con.py 
Purpose: Commom module to import packages/libraries 
Created data: Sep, 2019
Author: Sophia Yue

"""

def cf_setup_dbs_con(userName, passWord):
    """
     module name  : c_setup_dbs_con
     purpose      : Setup database connection
     parameter    : 
       userName: User name to access Teradata 
       passWord: Password to access Teradata 
     Return       :  
       session    : udaExec  connection
       td_enginex : Teradata engine 
    Notes:
     - Need to import the following packages/libraries 
       import sqlalchemy
       from sqlalchemy import create_engine
       import teradata     
    """
    udaExec = teradata.UdaExec (appName="Teradata_Test", version="1.0", logConsole=False)
    session = udaExec.connect(method="odbc", system="tqdpr02",
            username = userName, password= passWord )
    t_engine   = 'teradata://{0}:{1}@tqdpr02/temp_tables'.format(userName, passWord)
    print ("t_engine", t_engine)
    td_enginex = create_engine(t_engine) 
    return session,  td_enginex 