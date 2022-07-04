from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf

VOCAB_SIZE: int = 50280


def get_tokenizer():
    return GPT2Tokenizer.from_pretrained("tokenizer/")


def get_model(vocab_size: int = VOCAB_SIZE, model_weights_path='model/final_weights'):
    model = TFGPT2LMHeadModel.from_pretrained("distilgpt2")
    model.resize_token_embeddings(vocab_size)
    latest = tf.train.latest_checkpoint(model_weights_path)
    model.load_weights(latest)
    return model
