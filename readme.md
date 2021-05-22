# Assignment 4 - Network analysis
**Christoffer Kramer**  
**14-03-2021**  

**Creating reusable network analysis pipeline**  
This exercise is building directly on the work we did in class. I want you to take the code we developed together and in your groups and turn it into a reusable command-line tool. You can see the code from class here:  
https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/session6.ipynb  
This command-line tool will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, as we did in class.  
- Your script should be able to be run from the command line  
- It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"  
- For any given weighted edgelist given as an input, your script should be used to create a network visualization, which will be saved in a folder called viz.  
- It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.  

## Methods
This repository, is a full network analysis pipeline, which can be used to create edgelists, calculate centrality measures, and visualize networks. The script “create_edgelist.py” can create edgelists from either a CSV file (with a column called “text”), a txt-file, and a directory of txt-files. It uses SpaCy’s named entity recognition to find nodes. The nodes can be any of SpaCy’s named entity recognition labels. It then counts edges between nodes and outputs an edgelist.
The script “assignment4-cmk.py” uses networkx to create a Graph and then draws it. This graph is then used for calculating centrality measures (eigenvector, betweenness, and degree), which is saved in a CSV file. 

## Calculating centrality measures and visualization
NOTE: If using a custom edgelist it might take a while to run!  
This should work on Linux and Mac.  

**Step 1: Clone repo**
- open terminal
- Navigate to destination for repo
- type the following command
 ```console
 git clone https://github.com/Chris-Kramer/lang101_assignment_4.git
 ```
**step 2: Navigate to folder**
- Navigate to "lang101_assignment_4".
```console
cd lang101_assignment_4
```  
- Use the bash script _run-script_assignment4-cmk.sh_ to set up environment and run the script for visualization and centrality calculations:  
```console
bash run-script_assignment4-cmk.sh
```

### Running on windows  
I have not been able to make this script work on windows. The problem is Pygraphviz, which is, to put it mildly, a pain in the … neck to install on windows. If you wish to run it from windows, you should create a virtual environment, install dependencies (requirements.txt and SpaCy’s en_core_web_sm NLP model), and then run the script manually from the src folder. However, installing pygraphviz can be a hassle, and you might need to install that library (and its dependencies) manually, and then remove it from the requirements file. 

### Output
The output is a visualization of the network, which can be found in the viz folder, and a CSV file with centrality measures, which can be found in the output folder.   

### Parameters  
This script takes the following parameters, it has already been supplied with default values. But you are welcome to try and change them. I have added some edgelists under "data/edgelists", you can use. 

- `--edgelist` The filename of the edgelist. The edgelist must be located in the folder "data/edgelists"  
    - Default = real_news_edgelist.csv  
- `--filter` Specify how large a weight an edge should have in order to be included in the centrality measures.  
    - Default = 500  
- `--csv_output` The filename for the csv-file with centrality measures. The file will be located in the folder "output".  
    - Default = edgelist_centrality.csv  
- `--viz_output` The filename for the network visualisation. The file will be located in the folder "viz".  
    - Default = edgelist_graph.png    
    
### Example:  
_With bash script:_  
```console
bash run-script_assignment4-cmk.sh --edgelist fake_news_edgelist.csv --filter 800 --csv_output fake_news_centrality.csv --viz_output fake_news_viz.png
```  
_Without bash script:_  
```console
python assignment4-cmk.py --edgelist fake_news_edgelist.csv --filter 800 --csv_output fake_news_centrality.csv --viz_output fake_news_viz.png
```

## Creating edgelists
NOTE: If creating your own custom edgelist it might take a while to run!  
This should work on Linux and Mac.  
- Use the bash script "run-script_create_edgelist.sh" to create edgelists.  
```console
bash run-script_create_edgelist.sh --input_file input.txt --output_edgelist name_of_edgelist.csv
```  
The scrip can create an edgelist from either a directory of txt-files, a txt-file or a csv-file with a column called "text". The input must be located in the folder "data/raw_data".  

### Running on windows
If you want to run this script on windows, you must remove the last two lines in the requirements.txt (unless you have managed to install pygraphviz and graphviz). Then create a virtual environment, activate it, install dependencies (requirements.txt and SpaCy’s en_core_web_sm NLP model), then run the script create_edgelist.py from the src folder.  

### Output  
The output is an edgelist, which can be found in the folder data/edgelists.  

### Parameters
The bash scrip _run-script_create_edgelist.sh_ takes the following parameters:  
- `--input_file` This is the path to the txt-file, the csv-file or the directory of txt-files. It must be located in the folder "data/raw_data". So, if you wish to use a file from the corpus, you must move it to the correct directory (in this case the parent directory) first.  
    - Default = NO DEFAULT    
- `--label` The Entity label you wish to use as nodes. These labels come from SpaCy's library and can be found here https://spacy.io/models/en.  
    - Default = PERSON  
- `--output_edgelist` The name of the edgelist. The edgelist will be saved in the folder "data/edgelists".  
    - Default = edgelist.csv  
    
### Example:  
_With bash script:_  
```console
bash run-script_create_edgelist.sh --input_file Barclay_Postern_1911.txt --label ORG --output_edgelist Barclay_Postern_edgelist.csv
```  
_Without bash script:_  
```console
python create_edgelist.py --input_file Barclay_Postern_1911.txt --label ORG --output_edgelist Barclay_Postern_edgelist.csv
```
