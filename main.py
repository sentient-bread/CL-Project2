from scraping import *
from config import *
from trav import *

story_name = input("Enter story name: ")
SEED_URL += story_name

data_dir_path = input("Enter data dir path: ")
corpus_file_path = create_relevant_data_files(data_dir_path)
corpus_file = open(corpus_file_path,"w")

print("Scraping", story_name+'...')

text = scrape_page(SEED_URL, corpus_file)
corpus_file.close()

print(story_name, "scraped.")

sentences = sentence_tokenize(text)

print("Data tokenised.\nGenerating questions...")

questions = []
for sentence in sentences:
    try:
        parse = parser.parse(sentence.split())
        tree = maketree(parse)
        ql = traverse(tree)
        qs = list(map(makesent, ql))
        questions += qs + [""]
    except:
        print("Error found in sentence", sentence)
        pass

print("Questions generated.")

with open("questions.txt","w") as question_file:
    question_file.write('\n'.join([' '.join(q) for q in questions]))
