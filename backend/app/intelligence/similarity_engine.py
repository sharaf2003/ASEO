from collections import Counter

import re



class SimilarityEngine:

    """
    ASEO Internal Similarity Engine v1

    Responsible for comparing:

    - User requests
    - Previous projects
    - Agent experiences
    - Knowledge patterns

    This is the first layer before
    advanced learning models.
    """



    def __init__(self):

        self.stop_words = {

            "the",
            "a",
            "an",
            "with",
            "for",
            "and",
            "to",
            "create",
            "build",
            "make"

        }



    # =============================================
    # Text Processing
    # =============================================


    def normalize(

        self,

        text: str

    ) -> list[str]:


        text = text.lower()


        words = re.findall(

            r"\b[a-zA-Z0-9_]+\b",

            text

        )


        return [

            word

            for word in words

            if word not in self.stop_words

        ]



    # =============================================
    # Word Similarity
    # =============================================


    def calculate_similarity(

        self,

        text_a: str,

        text_b: str

    ) -> float:


        words_a = self.normalize(

            text_a

        )


        words_b = self.normalize(

            text_b

        )



        if not words_a or not words_b:

            return 0.0



        counter_a = Counter(

            words_a

        )


        counter_b = Counter(

            words_b

        )



        common = (

            set(counter_a.keys())

            &

            set(counter_b.keys())

        )



        score = (

            len(common)

            /

            max(

                len(set(words_a)),

                len(set(words_b))

            )

        )



        return round(

            score * 100,

            2

        )



    # =============================================
    # Compare Knowledge Items
    # =============================================


    def compare(

        self,

        current_request: str,

        previous_experience: str

    ) -> dict:


        score = self.calculate_similarity(

            current_request,

            previous_experience

        )


        return {

            "similarity_score": score,

            "related": score >= 50

        }