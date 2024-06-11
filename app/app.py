import tensorflow as tf
from flask import Flask, request, jsonify
from utils import preprocess_image

app = Flask(__name__)
model = tf.keras.models.load_model('model/weld_defect_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = preprocess_image(file)
    prediction = model.predict(image)
    predicted_class = tf.argmax(prediction[0])
    return jsonify({'defect': int(predicted_class)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
