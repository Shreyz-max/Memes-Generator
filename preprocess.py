import string

null_punct = str.maketrans('', '', string.punctuation)


def clean_data(list):
    for desc in list:
        desc = [word.lower() for word in desc.split()]
        desc = [w.translate(null_punct) for w in desc]
        desc = [word for word in desc if word.isalpha()]
        desc = [word for word in desc if len(word) > 1]
        yield ' '.join(desc)


import os
from pathlib import Path
import json
from tqdm import tqdm
from functools import reduce
from random import random

isascii_word = lambda w: len(w) == len(w.encode())
isascii_list = lambda l: reduce(lambda rez, word: rez & True if isascii_word(word) else False & rez, l, True)
dirname = os.path.join('ImgFlip575K_Dataset', 'dataset', 'memes')
lookup = dict()


def print_iterator(it):
    for x in it:
        print(x, end='\n')
    print('')  # for new line


def load_memes(start=0, end=100):
    i = 0
    for filename in tqdm(os.listdir(dirname)):  # foreach json file in memes
        i += 1
        if i < start or i > end:
            continue
        meme_name = Path(filename).stem  # remove file extension
        with open(os.path.join(dirname, filename)) as json_file:
            memes = json.load(json_file)
            # lookup[meme_name] = list(map(lambda meme: ' | '.join(meme['boxes']), memes))
            lookup[meme_name] = []
            for meme in memes:
                words = ' | '.join(clean_data(meme['boxes']))
                if isascii_list(words):
                    lookup[meme_name].append(words)


load_memes()
print(f'Memes loaded: {len(lookup)}')  # 99 memes, in the latest dataset 100
print(f'Meme example: {lookup[list(lookup)[0]][0]}')  # when you off the dope | and you think you a bird
