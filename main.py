from ctypes import *                            # in nixshell only
import ctypes.util                              # in nixshell only
cdll.LoadLibrary(ctypes.util.find_library('z')) # in nixshell only

 
# import numpy as np 
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import img_to_array
# from PIL import Image
# import schedule
import pyscreenshot as ImageGrab
import time
import subprocess
import os
import json


# class NSFWClassifier:
#     IMAGE_DIM = 224  # Model input image dimensions (224x224)
#     CATEGORIES = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']

#     def __init__(self, model_path):
#         self.model = self.load_model(model_path)

#     def load_model(self, model_path):
#         """
#         Load the pre-trained model from the given path.
#         """
#         return tf.keras.models.load_model(model_path, compile=False)

#     def preprocess_image(self, image):
#         """
#         Load and preprocess an image for prediction.
#         """
#         image = image.resize((self.IMAGE_DIM, self.IMAGE_DIM))
#         image = img_to_array(image)
#         image = image / 255.0  # Normalize to [0, 1] range
#         return np.expand_dims(image, axis=0)

#     def classify_image(self, image):
#         """
#         Classify a single image using the loaded model.
#         """
#         image = self.preprocess_image(image)
#         predictions = self.model.predict(image)[0]
#         prediction_dict = {self.CATEGORIES[i]: float(predictions[i]) for i in range(len(self.CATEGORIES))}
        
#         # Get the most likely result
#         most_likely_category = max(prediction_dict, key=prediction_dict.get)
#         most_likely_probability = prediction_dict[most_likely_category]
        
#         return most_likely_category, most_likely_probability


def takescreenshot():
    # Take a screenshot
    im = ImageGrab.grab(backend="grim")
    # Convert image to PIL format for processing
    im = im.convert("RGB")
    return im


def classify_image(image):
        image = takescreenshot()
        predictions = self.model.predict(image)[0]
        prediction_dict = {self.CATEGORIES[i]: float(predictions[i]) for i in range(len(self.CATEGORIES))}
        
        # Get the most likely result
        most_likely_category = max(prediction_dict, key=prediction_dict.get)
        most_likely_probability = prediction_dict[most_likely_category]
        
        return most_likely_category, most_likely_probability

def block_and_warning():
    print()
    # schedule.every(2).seconds.do(takescreenshot)

    # end_time = time.time() + 1 * 60  # 1 minutes from now
    # results = []

    # while time.time() < end_time:
    #     logging.info(f"Bad content detected right now {time.time} .... taking more screeshots to make sure!!") #Log
    #     category, probability = takescreenshot()
    #     results.append((category, probability))
    #     time.sleep(3)  # Wait 5 seconds before taking another screenshot

    # # Calculate the average results
    # category_counts = {category: 0 for category in classifier.CATEGORIES}
    
    # for result in results:
    #     category_counts[result[0]] += 1
    
    # most_common_category = max(category_counts, key=category_counts.get)
    # logging.info(f"Most common catogry in the last period , Is : {most_common_category}")

    # if most_common_category in ["hentai", "porn", "sexy"]:
        
    #     subprocess.run(['sudo', '-u', 'mwalid', 'notify-send', "🚫|Haram Detected|🚫", "System will shutdown in 10 seconds."])
    #     logging.info("The notifcation should now be sent!")

    #     time.sleep(10)
        
    #     logging.info("Taking action right now :/ !!!")

    #     subprocess.run(['systemctl', 'poweroff'])

        

def main_loop():
    while True:
        category, probability = takescreenshot()
        if category in ["hentai", "porn", "sexy"] and probability > 0.7:  # Adjust the threshold as needed
            block_and_warning()
        else:
            time.sleep(np.random.randint(1, 8))  # Random interval between 1 to 10 seconds

if __name__ == "__main__":
    model_path = r'/home/mwalid/Security/PornBlocker/nsfw_mobilenet2.224x224.h5'  # Update this to your model's path
    classifier = NSFWClassifier(model_path)
    
    main_loop()
