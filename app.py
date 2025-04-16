import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Define the input size expected by your model
input_size = (224, 224)  # Adjust this based on your model's input size

# Define the class labels and names corresponding to the output classes of your model
class_names = [
    (0, "Bijapur Jowar"),
    (1, "Masoor Dal"),
    (2, "Moong Dal"),
    (3, "Moth Bean"),
    (4, "Peanut"),
    (5, "Putani"),
    (6, "Rice"),
    (7, "Toor Dal"),
    (8, "Urad Dal"),
    (9, "Wheat"),
    (10, "Whole Moong")
    # Add more tuples for additional classes
]

# Function to preprocess the image
def preprocess_image(frame):
    resized_frame = cv2.resize(frame, input_size)
    normalized_frame = resized_frame / 255.0
    preprocessed_frame = np.expand_dims(normalized_frame, axis=0)
    return preprocessed_frame

# Load your pre-trained model from the .h5 file
model = load_model('MN.h5', compile=False)
  # Replace with your model file path

# Access the camera
camera = cv2.VideoCapture(0)  # 0 represents the default camera
cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Unable to capture frame from the camera.")
        break

    # Preprocess the frame
    preprocessed_frame = preprocess_image(frame)

    # Make predictions using your loaded model
    predictions = model.predict(preprocessed_frame)

    # Get the class index with the highest probability
    predicted_class_index = np.argmax(predictions)

    # Get the class label and name corresponding to the predicted class index
    predicted_class_label, predicted_class_name = class_names[predicted_class_index]

    # Display the image with the predicted class label and name
    text = f'Predicted: {predicted_class_label} - {predicted_class_name}'
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Camera Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()
cv2.destroyAllWindows()