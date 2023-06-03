"""Add trigger for modified_at columns

Revision ID: 4e591052ea23
Revises: dce330416022
Create Date: 2023-06-04 01:13:36.760120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e591052ea23'
down_revision = 'dce330416022'
branch_labels = None
depends_on = None

create_trigger = """CREATE TRIGGER trig_calendars_modifiedat
AFTER UPDATE ON calendars
FOR EACH ROW
BEGIN
    UPDATE calendars SET modified_at = CURRENT_TIMESTAMP WHERE id = old.id;
END"""

drop_trigger = """DROP TRIGGER trig_calendars_modifiedat"""


def upgrade() -> None:
    op.execute(create_trigger)


def downgrade() -> None:
    op.execute(drop_trigger)
