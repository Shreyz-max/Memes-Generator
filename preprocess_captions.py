import os.path
import pickle
import string
import unicodedata
from typing import List
from special_tokens import END_OF_TEXT_TOKEN, END_OF_BOX_TOKEN
from utils import get_tokenizer
from preprocess import run
import config


def _category_name_to_token(category_name: str) -> str:
    return f"<|{category_name}|>"


def _char_to_ascii(char: str) -> str:
    """
    Makes sure that a character is included in the allowed ASCII alphabet.
    """
    normalized = unicodedata.normalize("NFD", char)
    if normalized in string.printable + " ":
        return normalized
    else:
        return ""


def _process_single_caption(category_token: str, caption: str) -> str:
    caption = "".join(map(_char_to_ascii, caption))
    caption = caption.replace("|", END_OF_BOX_TOKEN)
    caption_with_tokens = [
        category_token,
        caption,
        END_OF_TEXT_TOKEN
    ]
    return " ".join(caption_with_tokens)


def _create_caption_labels(tokenized_text: List[int], block_size=256):
    examples = []
    for i in range(0, len(tokenized_text) - block_size + 1, block_size):
        examples.append(tokenized_text[i:i + block_size])

    inputs, labels = [], []
    for ex in examples:
        inputs.append(ex[:-1])
        labels.append(ex[1:])

    return inputs, labels


def preprocessed_captions():
    tokenizer = get_tokenizer(None)
    tokenized_captions = []
    if os.path.exists(config.train_path):
        with open(config.train_path, "rb") as f:
            train_descriptions = pickle.load(f)
    else:
        train_descriptions = run()
    for category_name, memes in train_descriptions.items():
        # Create a special token for category name
        category_token = _category_name_to_token(category_name)
        # Normalize each captions and add category token
        category_captions = list(map(
            lambda caption: _process_single_caption(category_token, caption),
            memes
        ))
        category_captions_merged = "\n".join(category_captions)
        tokenized_category = tokenizer.encode(category_captions_merged)
        tokenized_captions.extend(tokenized_category)

    inputs, labels = _create_caption_labels(tokenized_captions)
    with open(config.captions_path, "wb") as f:
        pickle.dump(inputs, f)

    with open(config.labels_path, "wb") as f:
        pickle.dump(labels, f)