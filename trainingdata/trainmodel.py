import spacy
from spacy.training import Example
from spacy.util import minibatch
import random

# # Function to load data from a CSV file
# def load_data(filename, label):
#     with open(filename, 'r', encoding='utf-8') as file:
#         lines = [line.strip() for line in file]
#     return [(line, label) for line in lines]

# # Load data
# valid_data = load_data('trainingsetvalid.csv', {"cats": {"VALID": 1, "NOT_VALID": 0}})
# not_valid_data = load_data('trainingsetnotvalid.csv', {"cats": {"VALID": 0, "NOT_VALID": 1}})

# # Combine and shuffle data
# train_data = valid_data + not_valid_data
# random.shuffle(train_data)

# # Load a spaCy model
# nlp = spacy.load("fr_core_news_sm")

# # Add text classifier to the pipeline if it doesn't exist
# if 'textcat' not in nlp.pipe_names:
#     textcat = nlp.add_pipe('textcat', last=True)
# else:
#     textcat = nlp.get_pipe('textcat')

# # Add labels to text classifier
# textcat.add_label("VALID")
# textcat.add_label("NOT_VALID")

# # Convert training data to spaCy's Example objects
# examples = []
# for text, annotations in train_data:
#     doc = nlp.make_doc(text)
#     examples.append(Example.from_dict(doc, annotations))

# # Training the model
# random.seed(1)
# spacy.util.fix_random_seed(1)
# optimizer = nlp.begin_training()

# for i in range(5):  # Adjust the number of iterations as needed
#     random.shuffle(examples)
#     batches = minibatch(examples, size=8)
#     for batch in batches:
#         nlp.update(batch, sgd=optimizer)

# # Save the trained model


# # Save the trained model
# nlp.to_disk("title_classify_fr")

trained_model_fr = spacy.load("title_classify_fr")
trained_model_en = spacy.load("title_classify_en")
result_fr = (trained_model_fr("Obama va en europe pour sa fete").cats)
result_en = (trained_model_en("Obama va en europe pour sa fete").cats)

print(result_fr['VALID'])
print(result_fr['NOT_VALID'])
print(result_en['VALID'])
print(result_en['NOT_VALID'])

if (result_fr['VALID'] > result_fr['NOT_VALID']):
    print("True")