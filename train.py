import pickle
import tensorflow as tf
from utils import get_model
from datetime import datetime
import os
import config


def training():
    with open(config.captions_path, "rb") as f:
        captions = pickle.load(f)
        captions = tf.convert_to_tensor(captions)

    with open(config.labels_path, "rb") as f:
        labels = pickle.load(f)
        labels = tf.convert_to_tensor(labels)

    start_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    checkpoint_path_base = os.path.join(config.checkpoint_dir,
                                        f"training_{start_time}")
    trial_checkpoint_path = f"{checkpoint_path_base}/cp.ckpt"

    model = get_model(model_weights_path=None)
    optimizer = tf.keras.optimizers.Adam(learning_rate=config.learning_rate)
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    model.compile(optimizer=optimizer,
                  loss=[loss],
                  metrics=["sparse_categorical_accuracy"])

    trial_checkpoint_path = f"cp.ckpt"
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        trial_checkpoint_path,
        save_weights_only=True,
        verbose=1
    )

    # Train the model
    model.fit(x=captions, y=labels, epochs=config.epochs, batch_size=config.batch_size,
              callbacks=[cp_callback],
              validation_split=config.validation_split)

    model.save(f"{checkpoint_path_base}/final_model")
    model.save_weights(f"{checkpoint_path_base}/final_weights")

    model.save_pretrained(f"{checkpoint_path_base}/transformer_pretrained")
