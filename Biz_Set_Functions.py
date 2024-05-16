#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# these are the functions used to clean our data set

def made_df(file_name):
    try:
        content = pd.read_csv(file_name)
        return content
    
    except FileNotFoundError:
        print("File not found")
        
def lower_columns(data_frame):
    data_frame.columns = data_frame.columns.str.lower()
    return data_frame.columns

def add_year(df,year):
    df['year'] = year
    return df['year']


def replace_naics(naics_code):
    # Dictionary mapping NAICS codes to industry names
    naics_dict = {
    "11": "11","21": "21","22": "22","23": "23","31": "31","32": "32","33": "33","42": "42","44": "44","45": "45",
    "48": "48","49": "49","51": "51","52": "52","53": "53","54": "54","55": "55","56": "56","61": "61","62": "62","71":"71",
    "72": "72","81": "81","92": "92"
}
    
    
    industry_code = naics_code[:2]  # Extract first two digits of NAICS code
    return naics_dict.get(industry_code, "UI")


def replace_town_with_region(town):
    
    puerto_rico_regions = {
    "1": "Mountain","3": "Western","5": "Western","7": "Metro Area","9": "Mountain","11": "Western","13": "Northern",
    "15": "Southern","17": "Northern","19": "Mountain","21": "Metro Area","23": "Western","25": "Metro Area","27": "Northern","29": "Eastern",
    "31": "Metro Area","33": "Metro Area","35": "Mountain","37": "Eastern","39": "Mountain","41": "Mountain","43": "Southern",
    "45": "Mountain","47": "Mountain","49": "Eastern","51": "Northern","53": "Eastern","54":"Northern","55": "Western","57": "Southern",
    "59": "Southern","61": "Metro Area","63": "Metro Area","65": "Northern","67": "Western","69": "Eastern","71": "Western",
    "73": "Mountain","75": "Southern","77": "Eastern","79": "Western","81": "Western","83": "Eastern","85": "Eastern",
    "87": "Eastern","89": "Eastern","91": "Northern","93": "Western","95": "Eastern","97": "Western","99": "Western",
    "101": "Mountain","103": "Eastern","105": "Mountain","107": "Mountain","109": "Southern","111": "Southern","113": "Southern",
    "115": "Western","117": "Western","119": "Eastern","121": "Western","123": "Southern","125": "Western","127": "Metro Area",
    "129": "Eastern","131": "Western","133": "Southern","135": "Northern","137": "Northern","139": "Metro Area","141": "Mountain",
    "143": "Northern","145": "Northern","147": "Eastern","149": "Southern","151": "Eastern","153": "Western",
}

    # Check if the town exists in the dictionary
    if town in puerto_rico_regions:
        # Replace the town with its corresponding region
        return puerto_rico_regions[town]
    else:
        # Return the original town name if it doesn't exist in the dictionary
        return town

