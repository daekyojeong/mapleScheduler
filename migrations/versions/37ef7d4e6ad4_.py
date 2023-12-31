"""empty message

Revision ID: 37ef7d4e6ad4
Revises: 5b982f97058b
Create Date: 2023-08-06 17:40:47.324959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ef7d4e6ad4'
down_revision = '5b982f97058b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('last_update', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('daily_work_Ursus', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane1', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane2', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane3', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane4', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane5', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane6', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic1', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic2', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic3', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic4', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic5', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic6', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane1', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane2', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane3', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane4', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane5', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane6', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_farm_harvesting', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_MonsterPark', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Zaqqum_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Zaqqum_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Magnus_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Magnus_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Hilla_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Kaung_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Papulatus_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Papulatus_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Pierre_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Banban_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_BloodyQueen_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Bellum_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Arkarium_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Arkarium_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_PinkBean_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Zaqqum_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Magnus_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Hilla_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Papulatus_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Pierre_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Banban_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_BloodyQueen_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Bellum_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_PinkBean_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Cygnus_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Cygnus_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Swoo_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Swoo_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Damian_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Damian_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_GuardianAngelSlime_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_GuardianAngelSlime_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Will_Easy_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Will_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Will_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dusk_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dusk_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_ZinHilla_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_ZinHilla_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dunkel_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dunkel_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Extreme_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Kalos_Chaos_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Kaling_Normal_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('monthly_Boss_BlackMage_Hard_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('monthly_Boss_BlackMage_Extreme_clear', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_Event_Basic_Check', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_Deep_Check', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_Farm', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_PunchKing', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_Adventure', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.drop_column('weekly_Event_EXP_Adventure')
        batch_op.drop_column('weekly_Event_EXP_PunchKing')
        batch_op.drop_column('weekly_Event_EXP_Farm')
        batch_op.drop_column('weekly_Event_Deep_Check')
        batch_op.drop_column('daily_Event_Basic_Check')
        batch_op.drop_column('monthly_Boss_BlackMage_Extreme_clear')
        batch_op.drop_column('monthly_Boss_BlackMage_Hard_clear')
        batch_op.drop_column('weekly_Boss_Kaling_Normal_clear')
        batch_op.drop_column('weekly_Boss_Kalos_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Seren_Extreme_clear')
        batch_op.drop_column('weekly_Boss_Seren_Hard_clear')
        batch_op.drop_column('weekly_Boss_Seren_Normal_clear')
        batch_op.drop_column('weekly_Boss_Dunkel_Hard_clear')
        batch_op.drop_column('weekly_Boss_Dunkel_Normal_clear')
        batch_op.drop_column('weekly_Boss_ZinHilla_Hard_clear')
        batch_op.drop_column('weekly_Boss_ZinHilla_Normal_clear')
        batch_op.drop_column('weekly_Boss_Dusk_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Dusk_Normal_clear')
        batch_op.drop_column('weekly_Boss_Will_Hard_clear')
        batch_op.drop_column('weekly_Boss_Will_Normal_clear')
        batch_op.drop_column('weekly_Boss_Will_Easy_clear')
        batch_op.drop_column('weekly_Boss_Lucid_Hard_clear')
        batch_op.drop_column('weekly_Boss_Lucid_Normal_clear')
        batch_op.drop_column('weekly_Boss_Lucid_Easy_clear')
        batch_op.drop_column('weekly_Boss_GuardianAngelSlime_Chaos_clear')
        batch_op.drop_column('weekly_Boss_GuardianAngelSlime_Normal_clear')
        batch_op.drop_column('weekly_Boss_Damian_Hard_clear')
        batch_op.drop_column('weekly_Boss_Damian_Normal_clear')
        batch_op.drop_column('weekly_Boss_Swoo_Hard_clear')
        batch_op.drop_column('weekly_Boss_Swoo_Normal_clear')
        batch_op.drop_column('weekly_Boss_Cygnus_Normal_clear')
        batch_op.drop_column('weekly_Boss_Cygnus_Easy_clear')
        batch_op.drop_column('weekly_Boss_PinkBean_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Bellum_Chaos_clear')
        batch_op.drop_column('weekly_Boss_BloodyQueen_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Banban_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Pierre_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Papulatus_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Hilla_Hard_clear')
        batch_op.drop_column('weekly_Boss_Magnus_Hard_clear')
        batch_op.drop_column('weekly_Boss_Zaqqum_Chaos_clear')
        batch_op.drop_column('daily_Boss_PinkBean_Normal_clear')
        batch_op.drop_column('daily_Boss_Arkarium_Normal_clear')
        batch_op.drop_column('daily_Boss_Arkarium_Easy_clear')
        batch_op.drop_column('daily_Boss_Horntail_Chaos_clear')
        batch_op.drop_column('daily_Boss_Horntail_Normal_clear')
        batch_op.drop_column('daily_Boss_Horntail_Easy_clear')
        batch_op.drop_column('daily_Boss_VonLeon_Hard_clear')
        batch_op.drop_column('daily_Boss_VonLeon_Normal_clear')
        batch_op.drop_column('daily_Boss_VonLeon_Easy_clear')
        batch_op.drop_column('daily_Boss_Bellum_Normal_clear')
        batch_op.drop_column('daily_Boss_BloodyQueen_Normal_clear')
        batch_op.drop_column('daily_Boss_Banban_Normal_clear')
        batch_op.drop_column('daily_Boss_Pierre_Normal_clear')
        batch_op.drop_column('daily_Boss_Papulatus_Normal_clear')
        batch_op.drop_column('daily_Boss_Papulatus_Easy_clear')
        batch_op.drop_column('daily_Boss_Kaung_Normal_clear')
        batch_op.drop_column('daily_Boss_Hilla_Normal_clear')
        batch_op.drop_column('daily_Boss_Magnus_Normal_clear')
        batch_op.drop_column('daily_Boss_Magnus_Easy_clear')
        batch_op.drop_column('daily_Boss_Zaqqum_Normal_clear')
        batch_op.drop_column('daily_Boss_Zaqqum_Easy_clear')
        batch_op.drop_column('daily_MonsterPark')
        batch_op.drop_column('daily_farm_harvesting')
        batch_op.drop_column('weekly_work_Arcane6')
        batch_op.drop_column('weekly_work_Arcane5')
        batch_op.drop_column('weekly_work_Arcane4')
        batch_op.drop_column('weekly_work_Arcane3')
        batch_op.drop_column('weekly_work_Arcane2')
        batch_op.drop_column('weekly_work_Arcane1')
        batch_op.drop_column('daily_work_Authentic6')
        batch_op.drop_column('daily_work_Authentic5')
        batch_op.drop_column('daily_work_Authentic4')
        batch_op.drop_column('daily_work_Authentic3')
        batch_op.drop_column('daily_work_Authentic2')
        batch_op.drop_column('daily_work_Authentic1')
        batch_op.drop_column('daily_work_Arcane6')
        batch_op.drop_column('daily_work_Arcane5')
        batch_op.drop_column('daily_work_Arcane4')
        batch_op.drop_column('daily_work_Arcane3')
        batch_op.drop_column('daily_work_Arcane2')
        batch_op.drop_column('daily_work_Arcane1')
        batch_op.drop_column('daily_work_Ursus')
        batch_op.drop_column('last_update')
        batch_op.drop_column('job')

    # ### end Alembic commands ###
