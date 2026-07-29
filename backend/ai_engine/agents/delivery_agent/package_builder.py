import os
import shutil





class PackageBuilder:
    """
    ASEO Package Builder v1
    """



    def build_zip(
        self,
        project_path,
        project_name
    ):


        os.makedirs(

            "deliveries",

            exist_ok=True

        )



        output_path = os.path.join(

            "deliveries",

            project_name

        )



        zip_file = shutil.make_archive(

            output_path,

            "zip",

            project_path

        )



        return zip_file