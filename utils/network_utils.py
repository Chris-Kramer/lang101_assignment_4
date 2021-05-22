#!/usr/bin/env python
"""
---------------------------------- Import libraries-------------------------------------------
"""
import re #regex
import os
from pathlib import Path
import csv 
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm
import spacy
nlp = spacy.load("en_core_web_sm")
            
"""
------------- Make a df from a txt file--------------
"""
        
def txt_to_df(txt_file):
    
    df = pd.DataFrame(columns = ["title", "text"])    
    # Open txt file
    with open(txt_file, "r", encoding = "utf-8") as file:
        #Read file
        text = file.read()
        #Get title
        title = re.findall(r"(?!.*/).*txt", txt_file)
        #create row and append it
        df_row = {"title": title, "text": text}
        df = df.append(df_row, ignore_index = True)
        
    return df

"""
------------- Create csv_file with edgelist from a df--------------
"""
            
def create_edgelist(data, output_dest, entity_label, batch = 500): 
    #filter data
    data = data["text"]
    
    #List of text_entities
    print("Getting Named entities ...")
    text_entities = []
    for text in tqdm(data): #Plus one since range doesn't indluce last value
        #skip entries that aren't a string
        if isinstance(text, str) == False:
            print(f"{text} is not a string... skipping it...")
            continue
        # create temporary list 
        tmp_entities = []
        # create doc object
        nlp.max_length = len(text)
        doc = nlp(text)
        # for every named entity
        for entity in doc.ents:
            # if that entity is "label"
            if entity.label_ == entity_label:
                # append to temp list
                tmp_entities.append(entity.text)
        # append temp list to main list
        text_entities.append(tmp_entities)

    edgelist = []
    print("creating edgelist ...")
    # iterate over every document
    for text in tqdm(text_entities):
        # use itertools.combinations() to create edgelist
        edges = list(combinations(text, 2))
        # for each combination - i.e. each pair of 'nodes'
        for edge in edges:
            # append this to final edgelist
            edgelist.append(tuple(sorted(edge)))
        
    # Count edges
    print("Counting edges ...")
    counted_edges = []
    for key, value in tqdm(Counter(edgelist).items()):
        source = key[0]
        target = key[1]
        weight = value
        counted_edges.append((source, target, weight))
    # Create df with edges (i.e. the edgelist)
    edges_df = pd.DataFrame(counted_edges, columns=["nodeA", "nodeB", "weight"])
    # Make df to csv file
    edges_df.to_csv(output_dest, index=False)

#Define behaviour when called from command line
if __name__=="__main__":
    pass