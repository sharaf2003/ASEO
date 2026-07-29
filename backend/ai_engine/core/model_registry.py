from pathlib import Path
import json
from datetime import datetime



class ModelRegistry:
    """
    ASEO AI Model Registry.

    Responsible for:

    - Registering AI models
    - Managing versions
    - Loading model information
    - Tracking active models

    """


    def __init__(
        self,
        registry_path="ai_engine/models/registry.json"
    ):

        self.registry_path = Path(
            registry_path
        )

        self.models = {}

        self.load_registry()



    # =====================================
    # Load Registry
    # =====================================

    def load_registry(self):

        if self.registry_path.exists():

            with open(
                self.registry_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.models = json.load(file)



    # =====================================
    # Save Registry
    # =====================================

    def save_registry(self):

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with open(
            self.registry_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.models,
                file,
                indent=4
            )



    # =====================================
    # Register Model
    # =====================================

    def register(
        self,
        name,
        version,
        model_type,
        path,
        metrics=None
    ):

        model_id = f"{name}_{version}"


        self.models[model_id] = {


            "name":
                name,


            "version":
                version,


            "type":
                model_type,


            "path":
                path,


            "metrics":
                metrics or {},


            "created_at":
                str(datetime.now()),


            "active":
                False

        }


        self.save_registry()


        return model_id



    # =====================================
    # Activate Model
    # =====================================

    def activate(
        self,
        model_id
    ):


        if model_id not in self.models:

            raise Exception(
                "Model not found"
            )


        for model in self.models.values():

            model["active"] = False



        self.models[model_id]["active"] = True


        self.save_registry()



    # =====================================
    # Get Active Model
    # =====================================

    def get_active_model(
        self
    ):


        for model in self.models.values():

            if model["active"]:

                return model


        return None



    # =====================================
    # List Models
    # =====================================

    def list_models(
        self
    ):

        return self.models