#!/usr/bin/env python
"""
----------- Import libs ------------
"""
#System tools
import os
import sys
from pathlib import Path
sys.path.append(os.path.join(".."))

#Arparse
from argparse import RawTextHelpFormatter # Formatting
import argparse

#Homebrewed functions
import utils.network_utils as nu

#data processeing
import pandas as pd

#Regex
import re
"""
---------- Main function ----------
"""
def main():
    """
    ---------- Parameters -----------
    """
    ap = argparse.ArgumentParser(description=
                                 "[INFO] Create an edgelist \n"
                                 "[INFO] Can take a txt file as input \n"
                                 "[INFO] Can take a directory of txt files as input \n"
                                 "[INFO] Can take a csv file with a column called 'text' as input \n"
                                 "[INFO] Uses SpaCy's NER model for entity recognition \n"
                                 "[INFO] The script will create an edgelist in the folder 'data/edgelists' \n",
                                formatter_class=RawTextHelpFormatter) 
    
    #input 
    ap.add_argument("-i_f", "--input_file",
                    required = True,
                    type = str,
                    help = 
                    "[INFO] Must be a txt file, a directory with txt files or a csv_file with a text column called 'text' \n"
                    "[INFO] It must be located in the folder 'data/raw_data' \n"
                    "[TYPE] str \n"
                    "[DEFAULT] No Default! \n"
                    "[EXAMPLE] --input_file Barclay_Postern_1911.txt")
    
    #Entity label
    ap.add_argument("-l", "--label",
                     required = False,
                     default = "PERSON",
                     type = str,
                     help =
                     "[INFO] The entity label for named entity recognition (SpaCy's labels) \n"
                     "[INFO] See 'https://spacy.io/models/en' for more labels \n"
                     "[TYPE] str \n"
                     "[DEFAULT] PERSON \n"
                     "[EXAMPLE] --label ORG")
    #Output edgelist
    ap.add_argument("-o_e", "--output_edgelist",
                     required = False,
                     default = "edgelist.csv",
                     type = str,
                     help =
                     "[INFO] The name of the output the edgelist \n"
                     "[INFO] The output file will be located in 'data/edgelists' \n"
                     "[TYPE] str \n"
                     "[DEFAULT] edgelist.csv \n"
                     "[EXAMPLE] --output_edgelist barclay_p_edgelist.csv")
    
    #return arguments
    args = vars(ap.parse_args())
    
    #Save arguments in variables for readability
    input_file = os.path.join("..", "data", "raw_data", args["input_file"])
    output_edgelist = os.path.join("..", "data", "edgelists", args["output_edgelist"])
    label = args["label"]
    """
    ---------- Test input type and create csv -----------
    """
    #Get name for output csv file
    output_csv = os.path.join("..", "data", "raw_data", str(re.findall("[^\.]+", args["input_file"])[0]) + ".csv")
    #If input is a txt file
    if input_file.endswith(".txt"):
        print("Creating edgelist from txt-file ...")
        df = nu.txt_to_df(input_file)
        nu.create_edgelist(df, output_edgelist, label)
        
    #Else if input is a directory    
    elif os.path.isdir(input_file):
        print("Creating edgelist from directory ...")
        
        df = pd.DataFrame(columns = ["title", "text"])
        for file_name in Path(input_file).glob("*.txt"):
            df_txt = nu.txt_to_df(str(file_name)) 
            df = df.append(df_txt, ignore_index = True)
        
        nu.create_edgelist(df, output_edgelist, label)
            
    #Else if input file is a csv file
    elif input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
        print("Creating edgelist from csv...")
        nu.create_edgelist(df, output_edgelist, label)
        sys.exit()
        
    #If input is neither a txt, csv or dir
    else:
        print("The input must be a txt file, a csv file or a directory of txt files")
        sys.exit()
    
#Define behaviour when called from commandline
if __name__=="__main__":
    main()