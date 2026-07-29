from .event import Event




class EventBus:
    """
    ASEO Event Bus v13

    Central communication system
    between autonomous agents.
    """



    def __init__(self):

        self.listeners = []

        self.history = []




    def subscribe(
        self,
        callback
    ):


        self.listeners.append(
            callback
        )





    def publish(
        self,
        event: Event
    ):


        self.history.append(

            event.to_dict()

        )



        for listener in self.listeners:


            listener(event)





    def get_history(self):


        return self.history