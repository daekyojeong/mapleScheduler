"""empty message

Revision ID: e64937d9154d
Revises: 
Create Date: 2023-08-06 16:49:25.642078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64937d9154d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserLogin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('userid')
    )
    op.create_table('UserDetail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=32), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=True),
    sa.Column('imgUrl', sa.String(length=256), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['UserLogin.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserDetail')
    op.drop_table('UserLogin')
    # ### end Alembic commands ###
