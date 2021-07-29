from scraping import *
from config import *
from trav import *
import os
import sys

data_dir_path = input("Enter data dir path: ")
corpus_file_path = ""
corpus_file = None

corpus_given = input("Will you provide corpus? y/n ")
corpus_file_name = ""
corpus_file_path = ""
text = ""

if corpus_given == "y" or corpus_given == "Y":
    corpus_file_path = input("corpus file name? ")
    # create_relevant_data_files(data_dir_path)
    file = open(corpus_file_path, "r")
    text = file.read()

elif corpus_given == "n" or corpus_given == "N":

    corpus_file_path = create_relevant_data_files(data_dir_path)

    corpus_file = open(corpus_file_path, "w")

    choice = input("Get url from file? y/n? ")

    url_file_content = ""
    url_list = []
    text = ""

    if choice == "y" or choice == "Y":
        # read the url file
        url_file_path = os.path.join(data_dir_path, "url_file.txt")
        url_file = open(url_file_path, "r")
        url_file_content = url_file.read()
        url_list = url_file_content.split("\n")
        for url in url_list:
            if url == "":
                continue
            try:
                text += scrape_page(url, corpus_file)
            except ValueError:
                print(f"Invalid url in url file: {url}")
                sys.exit()


    elif choice == "n" or choice == "N":
        story_name = input("Enter story name: ")
        print("Scraping", story_name+'...')
        try:
            text = scrape_page(urllib.parse.urljoin(SEED_URL,story_name), corpus_file)
            print(story_name, "scraped.")
        except ValueError:
            print("The story name isn't on the website.")
            sys.exit()

        corpus_file.close()



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
    question_file.write('\n'.join([' '.join(q)+'?' if q != "" else "" for q in questions ]))
