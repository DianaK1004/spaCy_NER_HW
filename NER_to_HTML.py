import spacy  
from spacy import displacy 
from os import listdir  
import os

import spacy.cli
spacy.cli.download("en_core_web_sm") 

nlp = spacy.load('en_core_web_sm')
corpus_directory = './corpus_texts_eng'  

files = [f for f in listdir(corpus_directory) if f.endswith('.txt')]

# HTML-file for the displacy visualisation
html_output_path = 'ner_visualization.html'

# Opening the file in "write"
with open(html_output_path, 'w', encoding='utf-8') as html_file:
    
    html_file.write("<html><head><title>NER Displacy</title></head><body>\n")
    
    # Going through files to perform NER
    for file_name in files:
        file_path = os.path.join(corpus_directory, file_name)

        with open(file_path, 'rb') as file:
            text = file.read().decode('utf-8')
        
        doc = nlp(text)
        
        # Using displacy for visualisation
        html_visualization = displacy.render(doc, style='ent', page=True, jupyter=False)
        html_file.write(f"<h2>Named Entities in {file_name}</h2>\n")
        html_file.write(html_visualization + "\n")
    
    html_file.write("</body></html>\n")

print(f"Die NER-Visualisierung wurde in '{html_output_path}' gespeichert.")
