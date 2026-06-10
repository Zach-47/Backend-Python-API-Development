"""add content column to posts table

Revision ID: 0e352b4200c6
Revises: 37456ddf251e
Create Date: 2026-06-10 10:42:01.569285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e352b4200c6'
down_revision = '37456ddf251e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
