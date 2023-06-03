"""Alter timestamp columns SQL schema

Revision ID: dce330416022
Revises: 9e145e2f3557
Create Date: 2023-06-04 01:09:08.042945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dce330416022'
down_revision = '9e145e2f3557'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('calendars', 'created_at')
    op.drop_column('calendars', 'modified_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'modified_at')
    op.add_column('calendars',
                  sa.Column('modified_at', sa.DATETIME(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'),
                            nullable=False))
    op.add_column('calendars',
                  sa.Column('created_at', sa.DATETIME(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'),
                            nullable=False))
    op.add_column('users',
                  sa.Column('modified_at', sa.DATETIME(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'),
                            nullable=False))
    op.add_column('users',
                  sa.Column('created_at', sa.DATETIME(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'),
                            nullable=False))


def downgrade() -> None:
    op.drop_column('calendars', 'created_at')
    op.drop_column('calendars', 'modified_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'modified_at')
    op.add_column('calendars',
                  sa.Column('modified_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'),
                            nullable=False))
    op.add_column('calendars',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'),
                            nullable=False))
    op.add_column('users',
                  sa.Column('modified_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'),
                            nullable=False))
    op.add_column('users',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'),
                            nullable=False))


