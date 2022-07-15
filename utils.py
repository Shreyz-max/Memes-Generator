from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf
import config


def get_tokenizer():
    """

    :return: Pretrained tokeniser
    """
    return GPT2Tokenizer.from_pretrained(config.tokenizer_dir)


def get_model(vocab_size: int = config.VOCAB_SIZE, model_weights_path=config.model_weights_path):
    """

    :param vocab_size: default 50280 (has been calculated based on data)
    :param model_weights_path: pretrained weights if any
    :return: returns the pretrained model
    """
    model = TFGPT2LMHeadModel.from_pretrained("distilgpt2")
    model.resize_token_embeddings(vocab_size)
    latest = tf.train.latest_checkpoint(model_weights_path)
    model.load_weights(latest)
    return model
