# ai_engine/agents/self_healing_agent/file_repairer.py


import ast





class FileRepairer:
    """
    ASEO File Repairer v2

    Applies automatic code repairs.

    """



    def repair(
        self,
        file_path,
        fix
    ):


        try:


            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()






            fix_type = fix.get(
                "type"
            )





            # =====================
            # Syntax Repair
            # =====================

            if fix_type == "syntax":


                content = self.fix_syntax(
                    content
                )






            # =====================
            # Validate After Repair
            # =====================

            validation = self.validate_syntax(
                content
            )



            if not validation["valid"]:


                return {


                    "status":

                        "failed",


                    "file":

                        file_path,


                    "error":

                        validation["error"]

                }







            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:


                file.write(
                    content
                )







            return {


                "status":

                    "fixed",



                "file":

                    file_path,


                "validation":

                    "passed"

            }







        except Exception as error:


            return {


                "status":

                    "failed",


                "error":

                    str(error)

            }









    # =================================
    # Syntax Fix Engine
    # =================================


    def fix_syntax(
        self,
        content
    ):


        # Remove tabs

        content = content.replace(
            "\t",
            "    "
        )



        # Remove trailing spaces

        lines = content.splitlines()



        cleaned_lines = []



        for line in lines:


            cleaned_lines.append(

                line.rstrip()

            )



        content = "\n".join(
            cleaned_lines
        )



        return content







    # =================================
    # Syntax Validation
    # =================================


    def validate_syntax(
        self,
        content
    ):


        try:


            ast.parse(
                content
            )



            return {


                "valid":

                    True,


                "error":

                    None

            }






        except Exception as error:


            return {


                "valid":

                    False,


                "error":

                    str(error)

            }