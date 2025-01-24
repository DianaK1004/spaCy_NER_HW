# Named Entity Recognition (NER) Mini-assignment using spaCy

## Overview
This is a simple NER assignment using [spaCy](https://spacy.io/), a popular library for Natural Language Processing (NLP) in Python. The project demonstrates how to use spaCy to identify and extract named entities like persons, organizations, dates, and more from a given text.

## Features
- Extracts named entities such as `PERSON`, `ORG`, `DATE`, and `GPE` from text.
- Customizable to train on specific datasets if needed.
- Easy-to-follow implementation for beginners in NLP.

## Requirements
- Python 3.8 or higher
- [spaCy](https://spacy.io/) (v3.x)
- Additional libraries specified in `requirements.txt`

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Example
Sample input text:
```plaintext
Apple is looking at buying U.K. startup for $1 billion on January 15, 2025.
```

Extracted entities:
```
- ORG: Apple
- GPE: U.K.
- MONEY: $1 billion
- DATE: January 15, 2025
```

## Resources
- [spaCy Documentation](https://spacy.io/docs)
- [Named Entity Recognition (NER) Guide](https://spacy.io/usage/linguistic-features#named-entities)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
