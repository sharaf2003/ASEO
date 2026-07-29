from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
import json


class AIModel(ABC):
    """
    Base AI Model Interface for ASEO.

    Every AI algorithm/model in the system
    must inherit from this class.

    Examples:
    - DocumentUnderstandingModel
    - UMLVisionModel
    - RequirementAnalysisModel
    - CodeGenerationModel
    """

    def __init__(
        self,
        name: str,
        version: str
    ):

        self.name = name

        self.version = version

        self.created_at = datetime.now()

        self.is_trained = False

        self.metrics = {}



    # ==========================================
    # Training
    # ==========================================

    @abstractmethod
    def train(
        self,
        dataset
    ):
        """
        Train AI model using dataset.

        Example:
        PDF Dataset
        UML Images Dataset
        Code Dataset
        """

        pass



    # ==========================================
    # Prediction
    # ==========================================

    @abstractmethod
    def predict(
        self,
        input_data
    ):
        """
        Generate prediction/result.

        Example:

        Document Agent:
        PDF -> Requirements JSON

        UML Agent:
        Image -> Diagram Structure
        """

        pass



    # ==========================================
    # Evaluation
    # ==========================================

    @abstractmethod
    def evaluate(
        self,
        test_data
    ):
        """
        Evaluate model performance.

        Examples:

        Accuracy
        Precision
        Recall
        F1 Score
        BLEU
        Code Quality Score
        """

        pass



    # ==========================================
    # Save Model
    # ==========================================

    def save(
        self,
        path: str
    ):

        """
        Save model metadata.

        Real trained weights will be saved by
        PyTorch / TensorFlow later.
        """

        model_info = {

            "name": self.name,

            "version": self.version,

            "created_at": str(
                self.created_at
            ),

            "is_trained": self.is_trained,

            "metrics": self.metrics

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
                model_info,
                file,
                indent=4
            )



    # ==========================================
    # Load Model
    # ==========================================

    def load(
        self,
        path: str
    ):

        """
        Load model metadata.

        Model weights will later be loaded from:

        PyTorch (.pth)
        TensorFlow (.h5)
        ONNX
        """

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


        self.name = data["name"]

        self.version = data["version"]

        self.is_trained = data["is_trained"]

        self.metrics = data["metrics"]



    # ==========================================
    # Model Information
    # ==========================================

    def info(self):

        return {

            "name": self.name,

            "version": self.version,

            "trained": self.is_trained,

            "metrics": self.metrics

        }