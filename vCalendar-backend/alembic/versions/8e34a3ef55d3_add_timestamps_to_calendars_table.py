"""Add timestamps to calendars table

Revision ID: 8e34a3ef55d3
Revises: ee6eb113eb9a
Create Date: 2023-06-02 19:54:28.974257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e34a3ef55d3'
down_revision = 'ee6eb113eb9a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendars', sa.Column('modified_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(now())'), nullable=False))
    op.add_column('calendars', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(now())'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('calendars', 'created_at')
    op.drop_column('calendars', 'modified_at')
    # ### end Alembic commands ###
