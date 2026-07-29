from datetime import datetime
from pathlib import Path
import json



class Trainer:
    """
    ASEO Generic AI Training Engine.

    Responsible for:

    - Training execution
    - Epoch management
    - Metrics tracking
    - Checkpoint saving
    - Training history

    """


    def __init__(
        self,
        model,
        dataset,
        epochs=10
    ):

        self.model = model

        self.dataset = dataset

        self.epochs = epochs

        self.history = []

        self.start_time = None

        self.end_time = None



    # =====================================
    # Training Process
    # =====================================

    def train(self):

        """
        Execute training pipeline.
        """


        self.start_time = datetime.now()


        print(
            f"Starting training: {self.model.name}"
        )


        for epoch in range(
            1,
            self.epochs + 1
        ):


            print(
                f"Epoch {epoch}/{self.epochs}"
            )


            result = self.model.train(
                self.dataset.train_data
            )


            self.history.append({

                "epoch":
                    epoch,

                "result":
                    result

            })


        self.end_time = datetime.now()


        self.model.is_trained = True


        return self.history



    # =====================================
    # Evaluation
    # =====================================

    def evaluate(self):

        """
        Evaluate trained model.
        """


        metrics = self.model.evaluate(
            self.dataset.test_data
        )


        self.model.metrics = metrics


        return metrics



    # =====================================
    # Save Checkpoint
    # =====================================

    def save_checkpoint(
        self,
        path
    ):

        """
        Save training checkpoint.
        """


        checkpoint = {

            "model":
                self.model.name,

            "version":
                self.model.version,

            "trained":
                self.model.is_trained,


            "history":
                self.history,


            "metrics":
                self.model.metrics,


            "created":
                str(datetime.now())

        }



        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                checkpoint,
                file,
                indent=4
            )



    # =====================================
    # Training Report
    # =====================================

    def report(self):

        return {

            "model":
                self.model.name,


            "epochs":
                self.epochs,


            "history":
                self.history,


            "metrics":
                self.model.metrics,


            "started":
                str(self.start_time),


            "finished":
                str(self.end_time)

        }