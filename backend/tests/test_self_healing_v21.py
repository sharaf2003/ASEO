from ai_engine.self_healing import HealingManager



healer = HealingManager()



result = healer.heal(

    "Database connection failed"

)



print(result)