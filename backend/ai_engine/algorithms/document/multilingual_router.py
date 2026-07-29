from ai_engine.algorithms.document.language_detector import LanguageDetector

from ai_engine.algorithms.document.requirement_extractor import RequirementExtractor

from ai_engine.algorithms.document.arabic_requirement_extractor import ArabicRequirementExtractor



class MultilingualRouter:
    """
    ASEO Multilingual Requirement Router v1

    Responsible for:

    - Detect document language
    - Select correct NLP extractor
    - Return unified requirements format

    Supported Languages:

    - Arabic
    - English

    """



    def __init__(self):


        # Language Detection Algorithm

        self.language_detector = LanguageDetector()



        # English NLP Engine

        self.english_extractor = RequirementExtractor()



        # Arabic NLP Engine

        self.arabic_extractor = ArabicRequirementExtractor()





    # =====================================
    # Main Routing Function
    # =====================================

    def extract(
        self,
        text
    ):


        language = self.language_detector.detect(
            text
        )



        if language["language"] == "arabic":


            requirements = self.arabic_extractor.extract(
                text
            )


        else:


            requirements = self.english_extractor.extract(
                text
            )



        return {


            "language":
                language,


            "requirements":
                requirements


        }