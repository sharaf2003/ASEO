from pathlib import Path
import json
import random



class DatasetManager:
    """
    Base Dataset Manager for ASEO AI Models.

    Responsible for:

    - Loading data
    - Managing datasets
    - Train/Validation/Test split
    - Dataset validation

    """


    def __init__(
        self,
        name: str,
        dataset_path: str
    ):

        self.name = name

        self.dataset_path = Path(dataset_path)

        self.data = []

        self.train_data = []

        self.validation_data = []

        self.test_data = []



    # =====================================
    # Load Dataset
    # =====================================

    def load(self):

        """
        Load dataset files.
        """

        if not self.dataset_path.exists():

            raise FileNotFoundError(
                "Dataset path not found"
            )


        for file in self.dataset_path.iterdir():

            if file.is_file():

                self.data.append(
                    str(file)
                )


        return self.data



    # =====================================
    # Dataset Split
    # =====================================

    def split(
        self,
        train_ratio=0.7,
        validation_ratio=0.15
    ):

        """
        Split dataset into:

        Training
        Validation
        Testing

        """


        random.shuffle(
            self.data
        )


        total = len(
            self.data
        )


        train_end = int(
            total * train_ratio
        )


        validation_end = int(
            total *
            (
                train_ratio +
                validation_ratio
            )
        )


        self.train_data = (
            self.data[:train_end]
        )


        self.validation_data = (
            self.data[
                train_end:
                validation_end
            ]
        )


        self.test_data = (
            self.data[
                validation_end:
            ]
        )


        return {

            "train":
                len(self.train_data),

            "validation":
                len(self.validation_data),

            "test":
                len(self.test_data)

        }



    # =====================================
    # Dataset Information
    # =====================================

    def info(self):

        return {

            "name":
                self.name,

            "total_samples":
                len(self.data),

            "train":
                len(self.train_data),

            "validation":
                len(self.validation_data),

            "test":
                len(self.test_data)

        }



    # =====================================
    # Save Dataset Metadata
    # =====================================

    def save_metadata(
        self,
        path
    ):


        metadata = {

            "name":
                self.name,

            "samples":
                len(self.data),

            "train":
                len(self.train_data),

            "validation":
                len(self.validation_data),

            "test":
                len(self.test_data)

        }


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4
            )