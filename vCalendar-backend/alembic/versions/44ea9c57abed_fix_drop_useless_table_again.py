"""fix: drop useless table (again)

Revision ID: 44ea9c57abed
Revises: 1ddb4cc256d8
Create Date: 2023-06-02 19:53:21.577628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44ea9c57abed'
down_revision = '1ddb4cc256d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("_database_generator_table")


def downgrade() -> None:
    pass
