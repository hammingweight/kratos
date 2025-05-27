# coding: utf-8
import tensorflow.keras as keras
class EvaluationExporter(keras.callbacks.Callback):
    def on_test_end(self, logs=None):
        keys = list(logs.keys())
        print("\nStop testing; got log keys: {}".format(keys))
        for (k, v) in logs.items():
            print(f"{k}:{v} ({type(v)})")
        print(self.model.loss)
        print(self.model.metrics)
        #print(dir(self.model))
        print(type(self.model.trainable_weights[10]))

