---
title: Question Generation from Hindi Stories
subtitle: Computational Linguistics - 1 | Project 2
author:
- Abhinav S Menon
- Pratyaksh Gautam
- Shashwat Singh
---

This project implements the system of question generation proposed in the paper
[__"Hindi Question Generation Using Dependency Structures"__](https://arxiv.org/pdf/1906.08570.pdf).

## Data Source
For our corpus, we chose the short stories of Premchand, scraped from
[__this website__](http://premchand.co.in/stories/).

## Methodology
### Overview
The data is first sentence tokenized, and questions are removed from the corpus.
This is in line with the limitations of the method described in the paper.

Then the data is put through a dependency parser and a list of questions
is generated from each sentence, by replacing constituents with appropriate
question words.

This list of questions is then printed to an output file.

### Important Functions

- `tree.py`
  - `maketree()`: Converts dependency parser output to tree representation.
  - `makesent()`: Converts tree representation to list of words.
- `trav.py`
  - `traverse()`: Generates a list of questions for the whole tree.
- `rules.py`: Contains functions to replace specific constituents with appropriate question words.
- `scraping.py`:
  - `scrape_page()`: Scrapes the page and prints the cleaned data to file.
  - `sentence_tokenize()`: Simply tokenize using regex.

## Analysis and Observations
## Possible Future Versions
