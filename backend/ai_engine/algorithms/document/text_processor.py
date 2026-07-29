import re


class TextProcessor:
    """
    ASEO Text Processing Algorithm v4

    Multilingual NLP Processor

    Supports:

    - English
    - Arabic
    - Mixed Documents

    Responsible for:

    - Keeping original text
    - Cleaning
    - Normalization
    - Sentence splitting
    - Tokenization
    - Keyword extraction

    """



    def __init__(self):


        self.stop_words = {


            # English

            "the",
            "a",
            "an",
            "and",
            "to",
            "of",
            "in",
            "is",
            "are",
            "can",
            "must",
            "should",
            "allow",
            "provide",


            # Arabic

            "من",
            "في",
            "على",
            "الى",
            "إلى",
            "و",
            "عن",
            "أن",
            "إن",
            "يمكن",
            "يجب"

        }





    # =====================================
    # Main Pipeline
    # =====================================

    def process(
        self,
        text: str
    ):


        original_text = text



        cleaned_text = self.clean_text(
            text
        )



        sentences = self.split_sentences(
            original_text
        )



        tokens = self.tokenize(
            cleaned_text
        )



        keywords = self.extract_keywords(
            tokens
        )



        return {


            "original_text":
                original_text,


            "clean_text":
                cleaned_text,


            "sentences":
                sentences,


            "tokens":
                tokens,


            "keywords":
                keywords

        }





    # =====================================
    # Cleaning
    # =====================================

    def clean_text(
        self,
        text
    ):


        text = text.lower()



        # Keep Arabic + English + numbers

        text = re.sub(
            r"[^a-zA-Z0-9\u0600-\u06FF\s.]",
            "",
            text
        )



        text = re.sub(
            r"\s+",
            " ",
            text
        )


        return text.strip()





    # =====================================
    # Sentence Splitting
    # =====================================

    def split_sentences(
        self,
        text
    ):


        sentences = re.split(
            r"[.!؟?]",
            text
        )


        return [

            sentence.strip()

            for sentence in sentences

            if sentence.strip()

        ]





    # =====================================
    # Tokenization
    # =====================================

    def tokenize(
        self,
        text
    ):


        words = text.split()


        tokens = []



        for word in words:


            word = word.strip(
                ".,!?;:"
            )



            if word and word not in self.stop_words:


                tokens.append(
                    word
                )



        return tokens





    # =====================================
    # Keyword Extraction
    # =====================================

    def extract_keywords(
        self,
        tokens
    ):


        frequency = {}



        for token in tokens:


            frequency[token] = (
                frequency.get(token, 0) + 1
            )



        return list(
            frequency.keys()
        )