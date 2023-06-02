"""Create database and drop useless column

Revision ID: 39d4a035a110
Revises: 
Create Date: 2023-06-02 19:49:52.799946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39d4a035a110'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("_database_generator_table")


def downgrade() -> None:
    pass
