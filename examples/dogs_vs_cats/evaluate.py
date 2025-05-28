import pathlib
try:
    import tensorflow.keras as keras
    from tensorflow.keras.utils import image_dataset_from_directory
except ModuleNotFoundError:
    import keras
    from keras.utils import image_dataset_from_directory
from example_package_hammingweight import EvaluationExporter

base_dir = pathlib.Path("cats_vs_dogs")

model = keras.models.load_model("convnet_from_scratch.keras")

callbacks = [EvaluationExporter(job="vision")]
test_dataset = image_dataset_from_directory(
    base_dir / "test",
    image_size=(180, 180),
    batch_size=32)

model.evaluate(
    test_dataset,
    callbacks=callbacks)

print("Done!")
