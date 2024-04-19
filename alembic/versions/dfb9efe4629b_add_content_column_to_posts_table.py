"""add content column to posts table

Revision ID: dfb9efe4629b
Revises: 94ab76a08d24
Create Date: 2024-04-19 12:58:44.384166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfb9efe4629b'
down_revision: Union[str, None] = '94ab76a08d24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
