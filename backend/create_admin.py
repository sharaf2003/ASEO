from app.database.session import SessionLocal

from app.models.organization import Organization
from app.models.workspace import Workspace
from app.models.user import User

from app.security.password import hash_password



db = SessionLocal()



organization = Organization(
    name="ASEO Organization",
    plan="PRO"
)

db.add(organization)
db.commit()
db.refresh(organization)



workspace = Workspace(
    organization_id=organization.id,
    name="Main Workspace"
)

db.add(workspace)
db.commit()
db.refresh(workspace)



user = User(
    organization_id=organization.id,
    workspace_id=workspace.id,
    email="admin@aseo.ai",
    name="ASEO Admin",
    password_hash=hash_password("123456"),
    role="OWNER"
)

db.add(user)
db.commit()


print("Admin created successfully")
print("Email: admin@aseo.ai")
print("Password: 123456")