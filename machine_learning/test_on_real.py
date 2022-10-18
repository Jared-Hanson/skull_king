import os
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
data_dir = pathlib.Path("dataset")



batch_size = 32
img_height = 300
img_width = 200

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
class_names = train_ds.class_names
print(class_names)

for image_file in os.scandir("test_imgs"):
    if ".DS_Store" not in image_file.path:
        print(image_file.path)
        img = tf.keras.utils.load_img(
            image_file.path, target_size=(300, 200)
        )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

    interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
    print(interpreter.get_signature_list())
    classify_lite = interpreter.get_signature_runner('serving_default')

    predictions_lite = classify_lite(sequential_input=img_array)['outputs']
    score_lite = tf.nn.softmax(predictions_lite)


    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
    )