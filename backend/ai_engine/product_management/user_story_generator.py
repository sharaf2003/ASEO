class UserStoryGenerator:
    """
    ASEO User Story Generator v21.9
    """

    def generate(
        self,
        features
    ):

        stories = []


        for feature in features:

            stories.append(

                f"As a user I can use {feature}"

            )


        return stories