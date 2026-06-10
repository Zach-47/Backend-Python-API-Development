"""add last few columns to posts table

Revision ID: 3304235e1d6d
Revises: ea7e9e2b7927
Create Date: 2026-06-10 11:35:43.421500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3304235e1d6d'
down_revision = 'ea7e9e2b7927'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', 
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
