from ai_engine.event_bus import (
    Event,
    EventBus
)



bus = EventBus()



bus.publish(

    Event(
        "test.event",
        "system",
        {
            "status":"ok"
        }
    )

)



print(
    bus.get_history()
)