
from special_tokens import END_OF_TEXT_TOKEN, END_OF_BOX_TOKEN, CATEGORY_TOKENS
import json
import requests
from utils import get_model, get_tokenizer

# using API to create memes
IMGFLIP_API = "https://api.imgflip.com/caption_image"
# loading model and tokeniser
model = get_model()
tokenizer = get_tokenizer()


def clean_caption(decoded_caption, category_id):
    # cleans the generated caption
    caption = decoded_caption.replace(CATEGORY_TOKENS[category_id], "") \
        .replace(END_OF_TEXT_TOKEN, "") \
        .strip()
    caption = caption.split(END_OF_BOX_TOKEN)
    return caption


def generate_caption(category_id):
    # generates the caption for a particular category id
    model_input = tokenizer.encode(CATEGORY_TOKENS[category_id], return_tensors="tf")
    model_output = model.generate(
        model_input,
        do_sample=True,
        max_length=30,
        top_p=0.96,
        top_k=0,
        temperature=0.5,
        pad_token_id=50256
    )
    caption = tokenizer.decode(model_output[0], skip_special_tokens=False)
    caption = clean_caption(caption, category_id)
    upper = caption[0]
    lower = caption[1]
    return upper, lower


def get_api_credentials(cred="credentials.json"):
    # gets credentials to use api
    with open(cred) as f:
        credentials = json.load(f)
    return credentials


def get_meme(category_id, upper, lower):
    # given text and category id it returns the meme
    cred = get_api_credentials()
    username = cred['username']
    password = cred['password']
    params = {
        'username': username,
        'password': password,
        'template_id': category_id,
        'text0': upper,
        'text1': lower}
    imgflip_response = requests.request("POST", IMGFLIP_API,
                                        params=params).json()
    return imgflip_response


def main(category_id):
    # accumulating all the tasks into one
    credentials = get_api_credentials()
    upper, lower = generate_caption(category_id)
    imgflip_response = get_meme(category_id, upper, lower)
    try:
        return imgflip_response["data"]["url"]
    except KeyError:
        imgflip_response = get_meme(category_id, 'AI could not generate meme', 'try again')
        return imgflip_response["data"]["url"]
