"""drop useless table again (again)

Revision ID: 9e145e2f3557
Revises: 8e34a3ef55d3
Create Date: 2023-06-04 01:07:42.426864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e145e2f3557'
down_revision = '8e34a3ef55d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("_database_generator_table")


def downgrade() -> None:
    pass
