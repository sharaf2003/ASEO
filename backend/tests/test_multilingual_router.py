from ai_engine.algorithms.document.multilingual_router import MultilingualRouter



router = MultilingualRouter()



arabic_text = """
يمكن للعميل حجز المواعيد.
يقوم المدير بإدارة المستخدمين.
"""



english_text = """
The customer can book appointments.
The admin manages users.
"""



print("===================")
print("ARABIC TEST")
print("===================")

print(
    router.extract(
        arabic_text
    )
)



print("===================")
print("ENGLISH TEST")
print("===================")

print(
    router.extract(
        english_text
    )
)