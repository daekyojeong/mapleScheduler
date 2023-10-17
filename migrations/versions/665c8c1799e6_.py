"""empty message

Revision ID: 665c8c1799e6
Revises: 590bff7306bf
Create Date: 2023-08-07 00:09:24.368117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665c8c1799e6'
down_revision = '590bff7306bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.add_column(sa.Column('daily_UnionCoin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.drop_column('daily_UnionCoin')

    # ### end Alembic commands ###