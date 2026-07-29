import re



class RequirementExtractor:
    """
    ASEO Requirement Extraction Algorithm v2

    Responsible for extracting:

    - Requirement type
    - Actor
    - Action
    - Object

    Hybrid approach:

    Rule Engine
    +
    NLP Pattern Matching

    """



    def __init__(self):


        # Supported actors

        self.actors = [

            "user",
            "customer",
            "admin",
            "patient",
            "doctor",
            "employee"

        ]



        # Action normalization

        self.action_mapping = {


            "login":
                "login",

            "register":
                "register",

            "create":
                "create",

            "update":
                "update",

            "delete":
                "delete",

            "manage":
                "manage",

            "manages":
                "manage",

            "managed":
                "manage",

            "booking":
                "book",

            "book":
                "book",

            "books":
                "book",

            "search":
                "search",

            "view":
                "view",

            "add":
                "add"

        }



        self.stop_words = [

            "the",
            "a",
            "an",
            "can",
            "must",
            "should",
            "allow",
            "to"

        ]



    # =====================================
    # Main Extraction
    # =====================================

    def extract(
        self,
        text
    ):


        sentences = self.split_sentences(
            text
        )


        requirements = []


        for sentence in sentences:


            result = self.analyze_sentence(
                sentence
            )


            if result:

                requirements.append(
                    result
                )


        return requirements



    # =====================================
    # Sentence Analysis
    # =====================================

    def analyze_sentence(
        self,
        sentence
    ):


        words = self.clean_sentence(
            sentence
        )


        actor = self.find_actor(
            words
        )


        action_index, action = self.find_action(
            words
        )



        if actor and action:


            obj = self.extract_object(
                words,
                action_index
            )


            return {

                "type":
                    "functional",


                "actor":
                    actor,


                "action":
                    action,


                "object":
                    obj

            }


        return None



    # =====================================
    # Clean Sentence
    # =====================================

    def clean_sentence(
        self,
        sentence
    ):


        sentence = sentence.lower()


        sentence = re.sub(
            r"[^a-z0-9\s]",
            "",
            sentence
        )


        words = sentence.split()



        return [

            word

            for word in words

            if word not in self.stop_words

        ]



    # =====================================
    # Actor Detection
    # =====================================

    def find_actor(
        self,
        words
    ):


        for word in words:

            if word in self.actors:

                return word


        return None



    # =====================================
    # Action Detection
    # =====================================

    def find_action(
        self,
        words
    ):


        for index, word in enumerate(words):


            if word in self.action_mapping:


                return (

                    index,

                    self.action_mapping[word]

                )


        return (

            None,

            None

        )



    # =====================================
    # Object Extraction
    # =====================================

    def extract_object(
        self,
        words,
        action_index
    ):


        if action_index is None:

            return None



        if action_index + 1 < len(words):


            return words[action_index + 1]



        return None



    # =====================================
    # Sentence Split
    # =====================================

    def split_sentences(
        self,
        text
    ):


        return [

            sentence.strip()

            for sentence in re.split(
                r"[.!?]",
                text
            )

            if sentence.strip()

        ]