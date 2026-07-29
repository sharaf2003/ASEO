from ai_engine.debugging_engine import (
    SelfDebuggingEngine
)



engine = SelfDebuggingEngine()



result = engine.debug(

    "Database connection failed"

)



print(result)