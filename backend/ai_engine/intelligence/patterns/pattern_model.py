class EngineeringPattern:
    """
    Represents an evolving engineering pattern.
    """


    def __init__(
        self,
        name,
        architecture,
        confidence,
        category="general",
        usage_count=0,
        success_count=0,
        failure_count=0
    ):

        self.name = name

        self.architecture = architecture

        self.confidence = confidence

        self.category = category


        # Learning metrics

        self.usage_count = usage_count

        self.success_count = success_count

        self.failure_count = failure_count



    def success_rate(self):

        if self.usage_count == 0:

            return 0


        return (
            self.success_count /
            self.usage_count
        )



    def failure_rate(self):

        if self.usage_count == 0:

            return 0


        return (
            self.failure_count /
            self.usage_count
        )



    def to_dict(self):

        return {

            "name":
                self.name,


            "architecture":
                self.architecture,


            "confidence":
                self.confidence,


            "category":
                self.category,


            "usage_count":
                self.usage_count,


            "success_count":
                self.success_count,


            "failure_count":
                self.failure_count,


            "success_rate":
                round(
                    self.success_rate(),
                    3
                ),


            "failure_rate":
                round(
                    self.failure_rate(),
                    3
                )
        }