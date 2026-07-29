from datetime import datetime



class CommitManager:
    """
    ASEO Commit Manager v15
    """



    def create_commit(
        self,
        message
    ):

        return {

            "commit":

                message,


            "timestamp":

                datetime.now().isoformat()

        }