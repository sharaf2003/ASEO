import re



class LanguageDetector:
    """
    ASEO Language Detection Algorithm v1

    Supports:

    - Arabic
    - English

    """



    def __init__(self):

        self.languages = [

            "arabic",

            "english"

        ]



    def detect(
        self,
        text: str
    ):


        arabic_chars = re.findall(
            r"[\u0600-\u06FF]",
            text
        )


        english_chars = re.findall(
            r"[A-Za-z]",
            text
        )



        arabic_count = len(
            arabic_chars
        )


        english_count = len(
            english_chars
        )



        total = arabic_count + english_count



        if total == 0:

            return {

                "language":"unknown",

                "confidence":0

            }



        if arabic_count > english_count:


            return {

                "language":
                    "arabic",

                "confidence":
                    round(
                        arabic_count / total,
                        2
                    )

            }



        else:


            return {

                "language":
                    "english",

                "confidence":
                    round(
                        english_count / total,
                        2
                    )

            }