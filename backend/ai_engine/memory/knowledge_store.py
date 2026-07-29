from ai_engine.memory.persistent_storage import PersistentStorage



class KnowledgeStore:
    """
    ASEO Knowledge Store v4

    Persistent AI Memory

    Features:

    - Store documents
    - Store requirements
    - Store knowledge graphs
    - Store project plans
    - Smart duplicate detection
    - Search memory
    - Knowledge summary

    """



    def __init__(self):


        self.storage = PersistentStorage()


        self.memory = self.storage.load()



        if not self.memory:


            self.memory = {


                "documents": [],


                "requirements": [],


                "knowledge_graphs": [],


                "plans": []

            }


            self.save()



        else:


            # Migration for old memory versions

            if "plans" not in self.memory:

                self.memory["plans"] = []

                self.save()






    # =====================================
    # Save Memory
    # =====================================

    def save(
        self
    ):


        self.storage.save(
            self.memory
        )






    # =====================================
    # Store Document
    # =====================================

    def store_document(
        self,
        document_data
    ):


        if document_data not in self.memory["documents"]:


            self.memory["documents"].append(
                document_data
            )


            self.save()







    # =====================================
    # Requirement Key
    # =====================================

    def requirement_key(
        self,
        requirement
    ):


        return (

            requirement.get("actor"),

            requirement.get("action"),

            requirement.get("object")

        )







    # =====================================
    # Store Requirements
    # =====================================

    def store_requirements(
        self,
        requirements
    ):


        for requirement in requirements:


            new_key = self.requirement_key(
                requirement
            )


            exists = False



            for index, existing in enumerate(
                self.memory["requirements"]
            ):


                old_key = self.requirement_key(
                    existing
                )


                if new_key == old_key:


                    exists = True



                    if (
                        "type" in requirement
                        and
                        "type" not in existing
                    ):


                        self.memory["requirements"][index] = requirement



                    break





            if not exists:


                self.memory["requirements"].append(
                    requirement
                )



        self.save()







    # =====================================
    # Store Knowledge Graph
    # =====================================

    def store_graph(
        self,
        graph
    ):


        if graph not in self.memory["knowledge_graphs"]:


            self.memory["knowledge_graphs"].append(
                graph
            )


            self.save()







    # =====================================
    # Store Project Plan
    # =====================================

    def store_plan(
        self,
        plan
    ):


        if plan not in self.memory["plans"]:


            self.memory["plans"].append(
                plan
            )


            self.save()







    # =====================================
    # Get Latest Plan
    # =====================================

    def get_latest_plan(
        self
    ):


        if self.memory["plans"]:


            return self.memory["plans"][-1]



        return None







    # =====================================
    # Retrieve Memory
    # =====================================

    def get_memory(
        self
    ):


        return self.memory







    # =====================================
    # Search Memory
    # =====================================

    def search(
        self,
        keyword
    ):


        keyword = keyword.lower()


        results = []



        for item in self.memory["requirements"]:


            content = str(item).lower()



            if keyword in content:


                results.append(
                    item
                )



        return results







    # =====================================
    # Knowledge Summary
    # =====================================

    def get_summary(
        self
    ):


        actors = set()

        entities = set()

        actions = set()



        for requirement in self.memory["requirements"]:


            actor = requirement.get(
                "actor"
            )


            action = requirement.get(
                "action"
            )


            obj = requirement.get(
                "object"
            )



            if actor:

                actors.add(actor)



            if action:

                actions.add(action)



            if obj:

                entities.add(obj)





        return {


            "actors":

                list(actors),



            "entities":

                list(entities),



            "actions":

                list(actions),



            "statistics":

            {

                "documents":

                    len(
                        self.memory["documents"]
                    ),


                "requirements":

                    len(
                        self.memory["requirements"]
                    ),


                "graphs":

                    len(
                        self.memory["knowledge_graphs"]
                    ),


                "plans":

                    len(
                        self.memory["plans"]
                    )

            }

        }






    # =====================================
    # Clear Memory
    # =====================================

    def clear(
        self
    ):


        self.memory = {


            "documents": [],


            "requirements": [],


            "knowledge_graphs": [],


            "plans": []

        }


        self.save()