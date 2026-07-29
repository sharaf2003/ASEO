from .role_manager import RoleManager

from .permission_engine import PermissionEngine

from .audit_logger import AuditLogger

from .security_policy import SecurityPolicy




class GovernanceManager:
    """
    ASEO Governance Manager v22.4
    """

    def __init__(self):

        self.roles = RoleManager()

        self.permissions = PermissionEngine()

        self.audit = AuditLogger()

        self.policy = SecurityPolicy()



    def evaluate(
        self,
        user,
        role,
        action
    ):


        role_result = self.roles.create_role(

            user,

            role

        )


        permission = self.permissions.check(

            role,

            action

        )


        audit = self.audit.log(

            user,

            action

        )


        policy = self.policy.validate(

            action

        )


        return {

            "role":
                role_result,

            "permission":
                permission,

            "audit":
                audit,

            "policy":
                policy,

            "status":
                "secure"

        }