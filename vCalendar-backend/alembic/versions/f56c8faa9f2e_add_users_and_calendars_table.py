"""Add users and calendars table

Revision ID: f56c8faa9f2e
Revises: 
Create Date: 2023-05-27 18:08:26.230540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f56c8faa9f2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    # op.create_table('users',
    #                 sa.Column('id', sa.Integer(), nullable=False),
    #                 sa.Column('email', sa.String(), unique=True, nullable=False),
    #                 sa.Column('hashed_password'))


def downgrade() -> None:
    pass
