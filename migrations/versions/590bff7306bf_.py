"""empty message

Revision ID: 590bff7306bf
Revises: 37ef7d4e6ad4
Create Date: 2023-08-06 17:42:47.510967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '590bff7306bf'
down_revision = '37ef7d4e6ad4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.add_column(sa.Column('daily_gift', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.drop_column('daily_gift')

    # ### end Alembic commands ###