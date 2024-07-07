"""add column updated_at in post

Revision ID: 978ba4dc27a3
Revises: 
Create Date: 2024-07-02 16:13:31.457728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '978ba4dc27a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###