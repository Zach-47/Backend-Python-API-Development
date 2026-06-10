"""add foreign-key to posts table

Revision ID: ea7e9e2b7927
Revises: 0e47fb152b87
Create Date: 2026-06-10 11:23:26.958401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea7e9e2b7927'
down_revision = '0e47fb152b87'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', tablename="posts")
    op.drop_column('posts', 'owner_id')
    pass
