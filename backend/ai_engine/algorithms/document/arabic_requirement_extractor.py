import re


class ArabicRequirementExtractor:
    """
    ASEO Arabic Requirement Extraction Algorithm v1.5

    Extracts:

    - Actor
    - Action
    - Object
    - Requirement Type

    Arabic Rule Based NLP Engine
    """



    def __init__(self):


        # ===============================
        # Actors
        # ===============================

        self.actors = {


            "المستخدم":
                "user",


            "العميل":
                "customer",


            "المدير":
                "admin",


            "المريض":
                "patient",


            "الطبيب":
                "doctor",


            "الموظف":
                "employee"

        }





        # ===============================
        # Actions
        # ===============================

        self.actions = {


            "يحجز":
                "book",


            "حجز":
                "book",


            "يسجل":
                "register",


            "تسجيل":
                "register",


            "يدخل":
                "login",


            "دخول":
                "login",


            "ينشئ":
                "create",


            "إنشاء":
                "create",


            "يعدل":
                "update",


            "تعديل":
                "update",


            "يحذف":
                "delete",


            "حذف":
                "delete",


            "يدير":
                "manage",


            "إدارة":
                "manage",


            "يعرض":
                "view",


            "عرض":
                "view"

        }





        # ===============================
        # Objects
        # ===============================

        self.objects = {


            "المواعيد":
                "appointments",


            "موعد":
                "appointment",


            "المستخدمين":
                "users",


            "المستخدمون":
                "users",


            "المستخدم":
                "user",


            "النظام":
                "system",


            "الحساب":
                "account",


            "الملف":
                "file"

        }







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
    # Analyze Sentence
    # =====================================

    def analyze_sentence(
        self,
        sentence
    ):


        sentence = self.normalize_text(
            sentence
        )


        actor = self.find_actor(
            sentence
        )


        action = self.find_action(
            sentence
        )



        if actor and action:


            obj = self.extract_object(
                sentence
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
    # Arabic Normalization
    # =====================================

    def normalize_text(
        self,
        text
    ):


        replacements = {


            "يمكن للعميل":
                "العميل",


            "للعميل":
                "العميل",


            "يقوم المدير بإدارة":
                "المدير إدارة",


            "يقوم المدير بادارة":
                "المدير إدارة",


            "بإدارة":
                "إدارة",


            "بالإدارة":
                "إدارة",


            "للمستخدمين":
                "المستخدمين",


            "للمستخدم":
                "المستخدم",


            "بحجز":
                "حجز"

        }



        for old, new in replacements.items():


            text = text.replace(
                old,
                new
            )



        text = re.sub(
            r"\s+",
            " ",
            text
        )


        return text.strip()







    # =====================================
    # Actor Detection
    # =====================================

    def find_actor(
        self,
        sentence
    ):


        actors_sorted = sorted(

            self.actors.items(),

            key=lambda x: len(x[0]),

            reverse=True

        )


        words = sentence.split()



        for arabic, english in actors_sorted:


            if arabic in words:


                return english



        return None







    # =====================================
    # Action Detection
    # =====================================

    def find_action(
        self,
        sentence
    ):


        actions_sorted = sorted(

            self.actions.items(),

            key=lambda x: len(x[0]),

            reverse=True

        )



        for arabic, english in actions_sorted:


            if arabic in sentence:


                return english



        return None







    # =====================================
    # Object Extraction
    # =====================================

    def extract_object(
        self,
        sentence
    ):


        objects_sorted = sorted(

            self.objects.items(),

            key=lambda x: len(x[0]),

            reverse=True

        )



        for arabic, english in objects_sorted:


            if arabic in sentence:


                return english



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

                r"[.!؟]",

                text

            )


            if sentence.strip()

        ]