"""Initial migration

Revision ID: 3d060055c4a1
Revises: 
Create Date: 2024-07-12 22:18:33.252005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d060055c4a1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    CREATE TABLE customer (
        id INT,
        name STRING
    ) USING DELTA
    """)

def downgrade():
    op.execute("DROP TABLE IF EXISTS customer")
