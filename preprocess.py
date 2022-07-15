import string
import os
from pathlib import Path
import json
import operator
from tqdm import tqdm
from functools import reduce
import pickle
import config


def clean_data(list):
    """

    :param list: list of captions
    :return: list with clean data
    """
    null_punct = str.maketrans('', '', string.punctuation)
    for desc in list:
        desc = [word.lower() for word in desc.split()]
        desc = [w.translate(null_punct) for w in desc]
        desc = [word for word in desc if word.isalpha()]
        desc = [word for word in desc if len(word) > 1]
        yield ' '.join(desc)


def print_iterator(it):
    for x in it:
        print(x, end='\n')
    print('')  # for new line


def load_memes(start=0, end=100):
    """

    :param start: start number to load memes
    :param end: end number to load memes
    :return: dictionary like { token:[meme list], }
    """
    isascii_word = lambda w: len(w) == len(w.encode())
    isascii_list = lambda l: reduce(lambda rez, word: rez & True if isascii_word(word) else False & rez, l, True)
    dirname = config.meme_dir
    lookup = dict()
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
    return lookup


def reduce_data(lookup):
    # returns only top 20 most used memes from dataset
    train_descriptions = {k: v for k, v in lookup.items()}
    b = {}
    a = []
    # checks if memes have more than two blocks
    for key in train_descriptions.keys():
        if train_descriptions[key][0].count('|') == 1:
            a.append(key)
    # checks for the most used 20 memes
    for key in a:
        b[key] = len(train_descriptions[key])
    d = sorted(b.items(), key=operator.itemgetter(1), reverse=True)
    keyList = []
    for val in d:
        keyList.append(val[0])
    for key in list(train_descriptions.keys()):
        if key not in keyList:
            del train_descriptions[key]
    with open(config.train_path, "wb") as fp:
        pickle.dump(train_descriptions, fp)
    return train_descriptions


def run():
    lookup = load_memes()
    print(f'Memes loaded: {len(lookup)}')  # 99 memes, in the latest dataset 100
    print(f'Meme example: {lookup[list(lookup)[0]][0]}')  # when you off the dope | and you think you a bird
    return reduce_data(lookup)
