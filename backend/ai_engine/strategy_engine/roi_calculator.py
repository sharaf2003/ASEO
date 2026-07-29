class ROICalculator:
    """
    ASEO ROI Calculator v21.8
    """

    def calculate(
        self,
        opportunity
    ):


        cost = 10000

        expected_return = 30000


        roi = (
            (expected_return - cost)
            /
            cost
        ) * 100


        return {

            "investment":
                cost,

            "expected_return":
                expected_return,

            "roi":
                roi

        }