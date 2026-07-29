from datetime import datetime


class AuditLogger:
    """
    ASEO Audit Logger v22.4
    """

    def log(
        self,
        user,
        action
    ):

        return {

            "user":
                user,

            "action":
                action,

            "timestamp":
                datetime.now().isoformat(),

            "recorded":
                True

        }