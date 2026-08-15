from sqlalchemy.orm import Session


from app.models.artifact import Artifact



class ArtifactRepository:

    """
    Repository for execution artifacts.
    """



    # =====================================================
    # Create Artifact
    # =====================================================

    def create(

        self,

        db: Session,

        artifact: Artifact

    ) -> Artifact:


        db.add(artifact)

        db.flush()


        return artifact



    # =====================================================
    # Get Artifact By ID
    # =====================================================

    def get_by_id(

        self,

        db: Session,

        artifact_id: int

    ) -> Artifact | None:


        return (

            db.query(Artifact)

            .filter(

                Artifact.id == artifact_id

            )

            .first()

        )



    # =====================================================
    # Get Execution Artifacts
    # =====================================================

    def get_by_execution(

        self,

        db: Session,

        execution_id: int

    ) -> list[Artifact]:


        return (

            db.query(Artifact)

            .filter(

                Artifact.execution_id == execution_id

            )

            .order_by(

                Artifact.created_at.asc()

            )

            .all()

        )