from ai_engine.event_bus import (
    Event,
    EventBus,
    EventTypes
)

from ai_engine.registry import (
    AgentRegistry,
    AgentInfo
)





class ASEOOrchestratorV13:
    """
    ASEO Orchestrator v13

    Event Driven Autonomous Agent Manager.
    """



    def __init__(self):

        self.registry = AgentRegistry()

        self.event_bus = EventBus()





    def register_agent(
        self,
        name,
        agent,
        version="1.0"
    ):


        info = AgentInfo(

            name,

            agent,

            version

        )


        self.registry.register(

            info

        )


        self.event_bus.publish(

            Event(

                EventTypes.AGENT_STARTED,

                name,

                {
                    "status":
                    "registered"
                }

            )

        )





    def run_agent(
        self,
        name,
        task
    ):


        agent_info = self.registry.get(

            name

        )



        if not agent_info:


            raise Exception(

                "Agent not found"

            )




        result = agent_info.agent.execute(

            task

        )



        self.event_bus.publish(

            Event(

                EventTypes.AGENT_COMPLETED,

                name,

                result

            )

        )



        return result





    def agents(self):


        return self.registry.list_agents()





    def events(self):


        return self.event_bus.get_history()