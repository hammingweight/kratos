import pathlib
import tensorflow.keras as keras
from tensorflow.keras.utils import load_img, img_to_array

test_model = keras.models.load_model("convnet_from_scratch.keras")

for i in range(1,12501):
    image = load_img(f"test1/{i}.jpg", target_size=(180, 180))
    image_tensor = img_to_array(image)
    image_tensor = image_tensor.reshape(1, 180, 180, 3)
    prediction = (test_model.predict(image_tensor, verbose=0) >= 0.5).astype(int).item()
    print(f"{i},{prediction}")