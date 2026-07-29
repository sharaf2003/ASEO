from ai_engine.database import (
    Base,
    engine,
    SessionLocal,
    CustomerModel,
    ProjectModel
)



from uuid import uuid4



Base.metadata.create_all(

    bind=engine

)



db = SessionLocal()



customer = CustomerModel(

    id=str(uuid4()),

    name="Startup Company",

    plan="Professional"

)



db.add(customer)

db.commit()



project = ProjectModel(

    id=str(uuid4()),

    name="Ecommerce Platform",

    status="production",

    quality=100

)



db.add(project)

db.commit()



print({

    "customer":

        customer.name,


    "plan":

        customer.plan,


    "project":

        project.name,


    "quality":

        project.quality

})



db.close()