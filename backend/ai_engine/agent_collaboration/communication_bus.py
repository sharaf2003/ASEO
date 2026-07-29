class CommunicationBus:
    """
    ASEO Agent Communication Bus v22.8
    """

    def send(
        self,
        sender,
        receiver,
        message
    ):

        return {

            "from":
                sender,

            "to":
                receiver,

            "message":
                message,

            "status":
                "delivered"

        }