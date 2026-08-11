from sqlalchemy.orm import Session

from app.models.project import Project



class LifecycleService:

    """
    Manages ASEO project lifecycle states.
    """


    ALLOWED_TRANSITIONS = {


        "CREATED": {

            "ANALYZING",

            "FAILED"

        },


        "ANALYZING": {

            "BUILDING",

            "FAILED"

        },


        "BUILDING": {

            "DEPLOYING",

            "FAILED"

        },


        "DEPLOYING": {

            "OPERATIONAL",

            "FAILED"

        },


        "OPERATIONAL": set(),


        "FAILED": set(),

    }



    def update_status(

        self,

        db: Session,

        project: Project,

        status: str

    ):


        current_status = (

            str(project.status)

            .strip()

            .upper()

        )


        new_status = (

            str(status)

            .strip()

            .upper()

        )



        if current_status == new_status:

            return project



        allowed = self.ALLOWED_TRANSITIONS.get(

            current_status,

            set()

        )



        if new_status not in allowed:

            raise ValueError(

                f"Invalid lifecycle transition: "

                f"{current_status} -> {new_status}"

            )



        try:


            project.status = new_status.lower()


            db.flush()


            return project



        except Exception:


            db.rollback()

            raise