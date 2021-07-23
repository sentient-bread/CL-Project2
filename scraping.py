from config import *
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import re

def clean_text(text):
    # takes text and gets rid of the english stuff from it
    return_text = re.sub(r'[A-Z]|[0-9]|[a-z]', "", text)
    return_text = re.sub('\n', '', return_text)
    return return_text

def scrape_page(url, corpus_file):
    # takes corpus_file object
    # takes url
    # scrapes url and writes to corpus_file
    # corpus_file is either in write mode or readmode
    # that is an assumption

    response = requests.get(url)
    soup_for_page = BeautifulSoup(response.content, 'html.parser')

    all_paragraphs = soup_for_page.find_all('p')
    # parsed_url = urllib.parse.urlparse(url)
    output_text = ""

    for para in all_paragraphs:
        for content in para.contents:
            # each content has a string attribute
            # which represents the text

            string = content.string
            if string is not None:
                output_text += string
    
    output_text_cleaned = clean_text(output_text)
    corpus_file.write(output_text_cleaned)
    return output_text_cleaned

def create_relevant_data_files(data_dir_path):

    try:
        os.mkdir(data_dir_path)
    except FileExistsError:
        # in case the data directory already exists
        pass
    

    file_path = os.path.join(data_dir_path, "corpus.txt")

    try:
        os.mknod(file_path)
    except FileExistsError:
        # file was already made
        pass

