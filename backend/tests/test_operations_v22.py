from ai_engine.operations import OperationsManager



manager = OperationsManager()



result = manager.monitor(

    "AI Customer Support SaaS",

    {

        "cpu":25,

        "memory":45

    }

)



print(result)