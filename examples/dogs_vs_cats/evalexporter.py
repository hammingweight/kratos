# coding: utf-8
import tensorflow.keras as keras
from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway

class EvaluationExporter(keras.callbacks.Callback):
    def __init__(self, pgw_addr="localhost:9091", job="gangplank"):
        super().__init__()
        self.pgw_addr = pgw_addr
        self.job = job
        self.registry = CollectorRegistry()
        self.gauge_loss = Gauge("gangplank_loss", "Evaluation loss", registry=self.registry)
        self.gauge_accuracy = Gauge("gangplank_accuracy", "Evaluation accuracy", registry=self.registry)
        
    def on_test_end(self, logs=None):
        keys = list(logs.keys())
        print("\nStop testing; got log keys: {}".format(keys))
        for (k, v) in logs.items():
            print(f"{k}:{v} ({type(v)})")
        #print(self.model.loss)
        #print(self.model.metrics)
        #print(type(self.model.trainable_weights[10]))
        self.gauge_accuracy.set(logs["accuracy"])
        self.gauge_loss.set(logs["accuracy"])
        pushadd_to_gateway(self.pgw_addr, self.job, self.registry)
        

