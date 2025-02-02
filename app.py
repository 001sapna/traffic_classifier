import streamlit as st
import numpy as np
import tensorflow
from PIL import Image
from tensorflow.keras.models import load_model

# Load the Keras model
model = load_model('traffic_classifier.keras')

# Dictionary to label all traffic signs classes
classes = { 0:'Speed limit (20km/h)', 1:'Speed limit (30km/h)', 2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)', 4:'Speed limit (70km/h)', 5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)', 7:'Speed limit (100km/h)', 8:'Speed limit (120km/h)',
            9:'No passing', 10:'No passing veh over 3.5 tons', 11:'Right-of-way at intersection',
            12:'Priority road', 13:'Yield', 14:'Stop', 15:'No vehicles', 16:'Veh > 3.5 tons prohibited',
            17:'No entry', 18:'General caution', 19:'Dangerous curve left', 20:'Dangerous curve right',
            21:'Double curve', 22:'Bumpy road', 23:'Slippery road', 24:'Road narrows on the right',
            25:'Road work', 26:'Traffic signals', 27:'Pedestrians', 28:'Children crossing',
            29:'Bicycles crossing', 30:'Beware of ice/snow', 31:'Wild animals crossing',
            32:'End speed + passing limits', 33:'Turn right ahead', 34:'Turn left ahead',
            35:'Ahead only', 36:'Go straight or right', 37:'Go straight or left', 38:'Keep right',
            39:'Keep left', 40:'Roundabout mandatory', 41:'End of no passing', 42:'End no passing veh > 3.5 tons' }

# Streamlit App
st.title('Traffic Sign Classification')
st.write('Upload a traffic sign image to classify it.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the image
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image) / 255.0  # Normalize the image

    # Make prediction
    pred = model.predict(image)
    pred_class = np.argmax(pred)
    sign = classes[pred_class]
    st.write(f'Predicted Class: {sign}')
