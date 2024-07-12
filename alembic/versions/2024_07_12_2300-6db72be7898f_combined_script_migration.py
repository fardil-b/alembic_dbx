"""combined_script_migration

Revision ID: 6db72be7898f
Revises: 3d060055c4a1
Create Date: 2024-07-12 23:00:50.104866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision: str = '6db72be7898f'
down_revision: Union[str, None] = '3d060055c4a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def read_sql_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def split_sql_commands(sql_content):
    """Splits the SQL content into upgrade and downgrade parts."""
    upgrade_sql = []
    downgrade_sql = []
    in_upgrade = True

    for line in sql_content.splitlines():
        if line.strip().lower() == '-- downgrade':
            in_upgrade = False
            continue
        if in_upgrade:
            upgrade_sql.append(line)
        else:
            downgrade_sql.append(line)

    return "\n".join(upgrade_sql), "\n".join(downgrade_sql)

def upgrade():
    sql_path = os.path.join(os.path.dirname(__file__), '../sql/customer_migration.sql')
    sql_content = read_sql_file(sql_path)
    upgrade_sql, _ = split_sql_commands(sql_content)
    op.execute(upgrade_sql)

def downgrade():
    sql_path = os.path.join(os.path.dirname(__file__), '../sql/customer_migration.sql')
    sql_content = read_sql_file(sql_path)
    _, downgrade_sql = split_sql_commands(sql_content)
    op.execute(downgrade_sql)