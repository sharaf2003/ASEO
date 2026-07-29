class ProjectHistory:
    """
    ASEO Project History v22.9.2
    """

    def __init__(
        self,
        store
    ):

        self.store = store



    def history(
        self
    ):

        return {

            "projects":

                self.store.get_all(),

            "count":

                len(
                    self.store.get_all()
                )

        }