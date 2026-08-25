from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import JSON
from sqlalchemy import DateTime

import uuid

from sqlalchemy.sql import func

from .base import Base



# ==================================================
# Organization Intelligence
# ==================================================


class OrganizationModel(Base):

    __tablename__ = "organizations"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(255),
        nullable=False
    )


    plan = Column(
        String(100),
        default="Free"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )



# ==================================================
# Workspace Intelligence
# ==================================================

class WorkspaceModel(Base):

    __tablename__ = "workspaces"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    organization_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    name = Column(
        String(255),
        nullable=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

# ==================================================
# Customers
# ==================================================


class CustomerModel(Base):

    __tablename__ = "customers"


    id = Column(
        String,
        primary_key=True
    )


    name = Column(
        String,
        nullable=False
    )


    plan = Column(
        String,
        default="Free"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )





# ==================================================
# Projects
# ==================================================


class ProjectModel(Base):

    __tablename__ = "projects"


    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    organization_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    workspace_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    owner_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    name = Column(
        String(255),
        nullable=False
    )


    description = Column(
        String,
        nullable=True
    )


    status = Column(
        String,
        default="created"
    )


    quality = Column(
        Integer,
        default=0
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )





# ==================================================
# Agent Memory
# ==================================================


class AgentMemoryModel(Base):

    __tablename__ = "agent_memories"


    id = Column(

        Integer,

        primary_key=True,

        autoincrement=True,

        index=True
    )


    agent_name = Column(
        String(100),
        nullable=False,
        index=True
    )


    memory_type = Column(
        String(50),
        nullable=False,
        index=True
    )


    content = Column(
        JSON,
        nullable=True
    )


    project_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    organization_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )





# ==================================================
# Knowledge Patterns
# ==================================================


class KnowledgePatternModel(Base):

    __tablename__ = "knowledge_patterns"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    category = Column(
        String(100),
        nullable=False,
        index=True
    )


    name = Column(
        String(255),
        nullable=False,
        index=True
    )


    pattern_family = Column(
        String(255),
        nullable=True,
        index=True
    )


    variant = Column(
        String(500),
        nullable=True
    )


    confidence_score = Column(
        Float,
        nullable=False,
        default=0
    )


    context = Column(
        JSON,
        nullable=True
    )


    priority_score = Column(
        Float,
        nullable=False,
        default=0.5
    )


    usage_count = Column(
        Integer,
        nullable=False,
        default=0
    )


    success_rate = Column(
        Float,
        nullable=False,
        default=0
    )


    last_success_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    extra_data = Column(
        JSON,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )





# ==================================================
# Knowledge Relations
# ==================================================


class KnowledgeRelationModel(Base):

    __tablename__ = "knowledge_relations"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    source_id = Column(
        Integer,
        nullable=False,
        index=True
    )


    target_id = Column(
        Integer,
        nullable=False,
        index=True
    )


    relation_type = Column(
        String(100),
        nullable=False
    )


    confidence = Column(
        Float,
        default=0
    )


    usage_count = Column(
        Integer,
        default=0
    )


    extra_data = Column(
        JSON,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )





# ==================================================
# Decision Memory
# ==================================================


class DecisionMemoryModel(Base):

    __tablename__ = "decision_memory"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    decision_history_id = Column(
        Integer,
        nullable=True
    )


    agent_name = Column(
        String,
        nullable=False
    )


    architecture = Column(
        JSON,
        nullable=False
    )


    similarity_score = Column(
        Float,
        default=0
    )


    success_score = Column(
        Float,
        default=0
    )


    memory_score = Column(
        Float,
        default=0
    )


    usage_count = Column(
        Integer,
        default=0
    )


    extra_data = Column(
        JSON,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )




# ==================================================
# Evolution Memory Intelligence
# ==================================================

class EvolutionMemoryModel(Base):

    __tablename__ = "evolution_memory"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    architecture = Column(
        String(255),
        nullable=True,
        index=True
    )


    recommendation = Column(
        String(255),
        nullable=False,
        index=True
    )


    success_rate = Column(
        Float,
        nullable=False,
        default=0
    )


    confidence = Column(
        Float,
        nullable=False,
        default=0
    )


    success_score = Column(
        Float,
        nullable=False,
        default=0
    )


    successful_count = Column(
        Integer,
        nullable=False,
        default=0
    )


    usage_count = Column(
        Integer,
        nullable=False,
        default=0
    )


    context = Column(
        JSON,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


# ==================================================
# Execution Records
# ==================================================

class ExecutionRecordModel(Base):

    __tablename__ = "execution_records"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    project_id = Column(
        String,
        nullable=True
    )


    request = Column(
        String,
        nullable=False
    )


    team = Column(
        JSON,
        nullable=True
    )


    software = Column(
        JSON,
        nullable=True
    )


    deployment = Column(
        JSON,
        nullable=True
    )


    operations = Column(
        JSON,
        nullable=True
    )


    status = Column(
        String,
        default="PENDING"
    )


    started_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    finished_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==================================================
# Execution Tasks
# ==================================================

class TaskModel(Base):

    __tablename__ = "tasks"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    execution_id = Column(
        Integer,
        nullable=True,
        index=True
    )


    name = Column(
        String(255),
        nullable=False
    )


    description = Column(
        String,
        nullable=True
    )


    agent_name = Column(
        String(255),
        nullable=True
    )


    status = Column(
        String(50),
        default="PENDING"
    )


    input_data = Column(
        JSON,
        nullable=True
    )

    output_data = Column(
        JSON,
        nullable=True
    )


    started_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )