"""Change columns to be nullable

Revision ID: eb5866d51fd2
Revises: 67cc006d50bf
Create Date: 2023-10-04 10:18:25.640458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "eb5866d51fd2"
down_revision: Union[str, None] = "67cc006d50bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.drop_table("flowstyle")
        with op.batch_alter_table("component", schema=None) as batch_op:
            batch_op.drop_index("ix_component_frontend_node_id")
            batch_op.drop_index("ix_component_name")
    except Exception:
        pass

    try:
        op.drop_table("component")
    except Exception:
        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table(
            "component",
            sa.Column("id", sa.CHAR(length=32), nullable=False),
            sa.Column("frontend_node_id", sa.CHAR(length=32), nullable=False),
            sa.Column("name", sa.VARCHAR(), nullable=False),
            sa.Column("description", sa.VARCHAR(), nullable=True),
            sa.Column("python_code", sa.VARCHAR(), nullable=True),
            sa.Column("return_type", sa.VARCHAR(), nullable=True),
            sa.Column("is_disabled", sa.BOOLEAN(), nullable=False),
            sa.Column("is_read_only", sa.BOOLEAN(), nullable=False),
            sa.Column("create_at", sa.DATETIME(), nullable=False),
            sa.Column("update_at", sa.DATETIME(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
        )
        with op.batch_alter_table("component", schema=None) as batch_op:
            batch_op.create_index("ix_component_name", ["name"], unique=False)
            batch_op.create_index(
                "ix_component_frontend_node_id", ["frontend_node_id"], unique=False
            )
    except Exception:
        pass

    try:
        op.create_table(
            "flowstyle",
            sa.Column("color", sa.VARCHAR(), nullable=False),
            sa.Column("emoji", sa.VARCHAR(), nullable=False),
            sa.Column("flow_id", sa.CHAR(length=32), nullable=True),
            sa.Column("id", sa.CHAR(length=32), nullable=False),
            sa.ForeignKeyConstraint(
                ["flow_id"],
                ["flow.id"],
            ),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("id"),
        )
    except Exception:
        pass
    # ### end Alembic commands ###
