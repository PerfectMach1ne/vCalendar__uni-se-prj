"""Add trigger for modified_at columns #2

Revision ID: 2438d8ea7388
Revises: 4e591052ea23
Create Date: 2023-06-04 01:23:03.447462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2438d8ea7388'
down_revision = '4e591052ea23'
branch_labels = None
depends_on = None


create_trigger = """CREATE TRIGGER trig_users_modifiedat
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE calendars SET modified_at = CURRENT_TIMESTAMP WHERE id = old.id;
END"""

drop_trigger = """DROP TRIGGER trig_users_modifiedat"""


def upgrade() -> None:
    op.execute(create_trigger)


def downgrade() -> None:
    op.execute(drop_trigger)
