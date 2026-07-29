from ai_engine.memory.knowledge_store import KnowledgeStore



memory = KnowledgeStore()



print("===================")
print("SEARCH")
print("===================")


print(
    memory.search(
        "customer"
    )
)



print("===================")
print("SUMMARY")
print("===================")


print(
    memory.get_summary()
)