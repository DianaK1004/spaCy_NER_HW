import spacy 
from spacy import displacy 
import os 
from os import listdir 
import spacy.cli

spacy.cli.download("en_core_web_sm")  # Downloaded the spaCy model for English from here https://spacy.io/models/en 

nlp = spacy.load('en_core_web_sm')
corpus_directory = './corpus_texts_eng' 
files = [f for f in listdir(corpus_directory) if f.endswith('.txt')]

# Open a file in write to save the NER output
with open('ner_output.txt', 'w', encoding='utf-8') as output_file:
    
    # Iterate over each file in the folder and process the text
    for file_name in files:
        file_path = os.path.join(corpus_directory, file_name)
        
        with open(file_path, 'rb') as file:
            text = file.read().decode('utf-8')
        
        # Process the text with spaCy
        doc = nlp(text)
        output_file.write(f"Named Entities in {file_name}:\n")
        for ent in doc.ents:
            output_file.write(f'{ent.text}\t : {ent.label_}\n')
        
        output_file.write("\n")
    
    print("Named Entity Recognition results have been saved to 'ner_output.txt'")

