"""
Module Name: c_impoart.py 
Purpose: Commom module to import packages/libraries 
Created data: Sep, 2019
Author: Sophia Yue

"""
"""
Code Starts here
Packages/Libraries relatyed to surprise
"""
from surprise import Reader
from surprise import Dataset

from surprise import KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline
from surprise.model_selection import LeaveOneOut

from surprise.accuracy import rmse
from surprise import accuracy
from surprise.model_selection import train_test_split

"""
Packages/Libraries relatyed to panda
"""

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import Timestamp

from collections import Counter
from collections import defaultdict
import heapq  
from operator import itemgetter
import itertools

import datetime
from datetime import datetime, timedelta, date
import time 

import teradata
import sqlalchemy
from sqlalchemy import create_engine

"""
 inspect is to  get function name                
"""

import inspect  
import re
"""
  - need tio import math, otherwise will get nan not defined  
  x = float('nan')
  math.isnan(x)
""" 
import math 

"""
 Import related to geopy/map 
"""

from geopy.geocoders import Nominatim
from geopy.distance import geodesic 
from geopy.extra.rate_limiter import RateLimiter
from geopy.point import Point  
from geopy import distance

import matplotlib.pyplot as plt
import seaborn as sns

#import plotly.plotly as py
import plotly.offline as pyoff

import plotly.graph_objs as go


import folium
from folium.plugins import FastMarkerCluster

from sklearn.cluster import KMeans
import xgboost as xgb
from sklearn.model_selection import KFold, cross_val_score, train_test_split



pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

import warnings
warnings.filterwarnings("ignore")

import pickle
from sklearn.metrics import accuracy_score