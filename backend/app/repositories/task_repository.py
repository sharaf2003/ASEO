from sqlalchemy.orm import Session


from app.models.task import Task



class TaskRepository:

    """
    Repository for execution tasks.
    """



    # =====================================================
    # Create Task
    # =====================================================

    def create(

        self,

        db: Session,

        task: Task

    ) -> Task:


        db.add(task)

        db.flush()


        return task



    # =====================================================
    # Get Task By ID
    # =====================================================

    def get_by_id(

        self,

        db: Session,

        task_id: int

    ) -> Task | None:


        return (

            db.query(Task)

            .filter(

                Task.id == task_id

            )

            .first()

        )



    # =====================================================
    # Get Execution Tasks
    # =====================================================

    def get_by_execution(

        self,

        db: Session,

        execution_id: int

    ) -> list[Task]:


        return (

            db.query(Task)

            .filter(

                Task.execution_id == execution_id

            )

            .order_by(

                Task.created_at.asc()

            )

            .all()

        )



    # =====================================================
    # Update Task Status
    # =====================================================

    def update_status(

        self,

        db: Session,

        task: Task,

        status: str

    ) -> Task:


        task.status = status


        db.flush()


        return task