"""empty message

Revision ID: 7637a4ba094c
Revises: 665c8c1799e6
Create Date: 2023-08-13 00:39:06.649050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7637a4ba094c'
down_revision = '665c8c1799e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tabOrder', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('visible_symbol', sa.String(length=2048), nullable=True))
        batch_op.add_column(sa.Column('visible_boss', sa.String(length=2048), nullable=True))
        batch_op.add_column(sa.Column('visible_basic', sa.String(length=2048), nullable=True))
        batch_op.add_column(sa.Column('visible_event', sa.String(length=2048), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane1_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane2_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane3_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane4_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane5_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane6_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane7_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane8_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane9_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic1_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic2_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic3_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic4_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic5_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_authentic6_daily', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane1_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane2_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane3_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane4_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane5_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('symbol_arcane6_weekly', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('ursusCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('farmHarvestCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('dailyGiftCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('monsterParkCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('UnionCoinCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Zaqqum_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Zaqqum_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Magnus_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Magnus_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Hilla_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Kaung_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Papulatus_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Papulatus_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Pierre_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Banban_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_BloodyQueen_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Bellum_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_VonLeon_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_VonLeon_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_VonLeon_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Horntail_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Horntail_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Horntail_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Arkarium_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_Arkarium_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_daily_PinkBean_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Zaqqum_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Magnus_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Hilla_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Papulatus_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Pierre_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Banban_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_BloodyQueen_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Bellum_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_PinkBean_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Cygnus_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Cygnus_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Swoo_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Swoo_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Damian_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Damian_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_GuardianAngelSlime_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_GuardianAngelSlime_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Lucid_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Lucid_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Lucid_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Will_Easy', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Will_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Will_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Dusk_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Dusk_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_ZinHilla_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_ZinHilla_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Dunkel_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Dunkel_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Seren_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Seren_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Seren_Extreme', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Kalos_Chaos', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_weekly_Kaling_Normal', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_monthly_BlackMage_Hard', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('boss_monthly_BlackMage_Extreme', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('eventAttendanceCheckbox', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('eventDeepAttendanceCheckbox', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('eventEXPFarmCheckbox', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('eventEXPPunchKingCheckbox', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('eventEXPAdventureCheckbox', sa.Integer(), nullable=True))
        batch_op.alter_column('nickname',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
        batch_op.drop_column('daily_work_Authentic2')
        batch_op.drop_column('daily_Boss_Bellum_Normal_clear')
        batch_op.drop_column('weekly_Boss_BloodyQueen_Chaos_clear')
        batch_op.drop_column('weekly_work_Arcane6')
        batch_op.drop_column('weekly_Boss_Damian_Hard_clear')
        batch_op.drop_column('daily_Boss_Hilla_Normal_clear')
        batch_op.drop_column('weekly_work_Arcane4')
        batch_op.drop_column('weekly_Boss_Lucid_Hard_clear')
        batch_op.drop_column('weekly_work_Arcane1')
        batch_op.drop_column('weekly_Boss_Magnus_Hard_clear')
        batch_op.drop_column('daily_Boss_Magnus_Easy_clear')
        batch_op.drop_column('daily_Boss_Papulatus_Easy_clear')
        batch_op.drop_column('daily_work_Authentic1')
        batch_op.drop_column('weekly_Boss_Papulatus_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Cygnus_Normal_clear')
        batch_op.drop_column('weekly_Boss_Dusk_Normal_clear')
        batch_op.drop_column('weekly_work_Arcane2')
        batch_op.drop_column('daily_Boss_Magnus_Normal_clear')
        batch_op.drop_column('weekly_Event_EXP_Adventure')
        batch_op.drop_column('daily_Boss_VonLeon_Easy_clear')
        batch_op.drop_column('weekly_Boss_Dunkel_Normal_clear')
        batch_op.drop_column('weekly_Event_Deep_Check')
        batch_op.drop_column('daily_work_Authentic5')
        batch_op.drop_column('daily_Boss_VonLeon_Normal_clear')
        batch_op.drop_column('weekly_Boss_ZinHilla_Hard_clear')
        batch_op.drop_column('daily_work_Authentic3')
        batch_op.drop_column('daily_Boss_Papulatus_Normal_clear')
        batch_op.drop_column('weekly_Boss_Seren_Extreme_clear')
        batch_op.drop_column('weekly_Boss_Zaqqum_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Lucid_Easy_clear')
        batch_op.drop_column('daily_work_Arcane5')
        batch_op.drop_column('weekly_Boss_ZinHilla_Normal_clear')
        batch_op.drop_column('daily_work_Arcane6')
        batch_op.drop_column('daily_Boss_Zaqqum_Easy_clear')
        batch_op.drop_column('weekly_Boss_Will_Normal_clear')
        batch_op.drop_column('weekly_Boss_Dusk_Chaos_clear')
        batch_op.drop_column('daily_gift')
        batch_op.drop_column('weekly_Event_EXP_Farm')
        batch_op.drop_column('weekly_Boss_Kaling_Normal_clear')
        batch_op.drop_column('daily_Boss_Pierre_Normal_clear')
        batch_op.drop_column('monthly_Boss_BlackMage_Hard_clear')
        batch_op.drop_column('daily_Boss_Horntail_Easy_clear')
        batch_op.drop_column('daily_Event_Basic_Check')
        batch_op.drop_column('daily_work_Arcane3')
        batch_op.drop_column('weekly_work_Arcane5')
        batch_op.drop_column('daily_Boss_Arkarium_Easy_clear')
        batch_op.drop_column('weekly_Boss_Lucid_Normal_clear')
        batch_op.drop_column('weekly_Boss_Swoo_Hard_clear')
        batch_op.drop_column('daily_Boss_Horntail_Chaos_clear')
        batch_op.drop_column('daily_MonsterPark')
        batch_op.drop_column('weekly_Boss_Swoo_Normal_clear')
        batch_op.drop_column('daily_work_Authentic4')
        batch_op.drop_column('daily_Boss_VonLeon_Hard_clear')
        batch_op.drop_column('weekly_Boss_Dunkel_Hard_clear')
        batch_op.drop_column('daily_Boss_PinkBean_Normal_clear')
        batch_op.drop_column('daily_work_Arcane4')
        batch_op.drop_column('monthly_Boss_BlackMage_Extreme_clear')
        batch_op.drop_column('weekly_Boss_GuardianAngelSlime_Chaos_clear')
        batch_op.drop_column('weekly_Boss_GuardianAngelSlime_Normal_clear')
        batch_op.drop_column('weekly_Boss_Bellum_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Seren_Normal_clear')
        batch_op.drop_column('daily_Boss_Zaqqum_Normal_clear')
        batch_op.drop_column('daily_work_Authentic6')
        batch_op.drop_column('weekly_Boss_Will_Hard_clear')
        batch_op.drop_column('daily_UnionCoin')
        batch_op.drop_column('daily_Boss_Arkarium_Normal_clear')
        batch_op.drop_column('weekly_Boss_Hilla_Hard_clear')
        batch_op.drop_column('weekly_Boss_Banban_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Seren_Hard_clear')
        batch_op.drop_column('weekly_Boss_PinkBean_Chaos_clear')
        batch_op.drop_column('daily_Boss_Horntail_Normal_clear')
        batch_op.drop_column('daily_Boss_Banban_Normal_clear')
        batch_op.drop_column('daily_work_Ursus')
        batch_op.drop_column('daily_Boss_Kaung_Normal_clear')
        batch_op.drop_column('weekly_Boss_Kalos_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Pierre_Chaos_clear')
        batch_op.drop_column('weekly_Boss_Cygnus_Easy_clear')
        batch_op.drop_column('daily_work_Arcane1')
        batch_op.drop_column('weekly_Event_EXP_PunchKing')
        batch_op.drop_column('daily_work_Arcane2')
        batch_op.drop_column('weekly_work_Arcane3')
        batch_op.drop_column('daily_Boss_BloodyQueen_Normal_clear')
        batch_op.drop_column('weekly_Boss_Damian_Normal_clear')
        batch_op.drop_column('daily_farm_harvesting')
        batch_op.drop_column('weekly_Boss_Will_Easy_clear')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserDetail', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weekly_Boss_Will_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_farm_harvesting', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Damian_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_BloodyQueen_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane3', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane2', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_PunchKing', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane1', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Cygnus_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Pierre_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Kalos_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Kaung_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Ursus', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Banban_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_PinkBean_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Banban_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Hilla_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Arkarium_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_UnionCoin', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Will_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic6', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Zaqqum_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Bellum_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_GuardianAngelSlime_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_GuardianAngelSlime_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('monthly_Boss_BlackMage_Extreme_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane4', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_PinkBean_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dunkel_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic4', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Swoo_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_MonsterPark', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Swoo_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Arkarium_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane5', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane3', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Event_Basic_Check', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Horntail_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('monthly_Boss_BlackMage_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Pierre_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Kaling_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_Farm', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('daily_gift', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dusk_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Will_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Zaqqum_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane6', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_ZinHilla_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Arcane5', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Zaqqum_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Seren_Extreme_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Papulatus_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic3', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_ZinHilla_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic5', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_Deep_Check', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dunkel_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_VonLeon_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Event_EXP_Adventure', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Magnus_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane2', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Dusk_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Cygnus_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Papulatus_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic1', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Papulatus_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Magnus_Easy_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Magnus_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane1', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Lucid_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane4', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Hilla_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_Damian_Hard_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_work_Arcane6', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('weekly_Boss_BloodyQueen_Chaos_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_Boss_Bellum_Normal_clear', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('daily_work_Authentic2', sa.BOOLEAN(), nullable=True))
        batch_op.alter_column('nickname',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
        batch_op.drop_column('eventEXPAdventureCheckbox')
        batch_op.drop_column('eventEXPPunchKingCheckbox')
        batch_op.drop_column('eventEXPFarmCheckbox')
        batch_op.drop_column('eventDeepAttendanceCheckbox')
        batch_op.drop_column('eventAttendanceCheckbox')
        batch_op.drop_column('boss_monthly_BlackMage_Extreme')
        batch_op.drop_column('boss_monthly_BlackMage_Hard')
        batch_op.drop_column('boss_weekly_Kaling_Normal')
        batch_op.drop_column('boss_weekly_Kalos_Chaos')
        batch_op.drop_column('boss_weekly_Seren_Extreme')
        batch_op.drop_column('boss_weekly_Seren_Hard')
        batch_op.drop_column('boss_weekly_Seren_Normal')
        batch_op.drop_column('boss_weekly_Dunkel_Hard')
        batch_op.drop_column('boss_weekly_Dunkel_Normal')
        batch_op.drop_column('boss_weekly_ZinHilla_Hard')
        batch_op.drop_column('boss_weekly_ZinHilla_Normal')
        batch_op.drop_column('boss_weekly_Dusk_Chaos')
        batch_op.drop_column('boss_weekly_Dusk_Normal')
        batch_op.drop_column('boss_weekly_Will_Hard')
        batch_op.drop_column('boss_weekly_Will_Normal')
        batch_op.drop_column('boss_weekly_Will_Easy')
        batch_op.drop_column('boss_weekly_Lucid_Hard')
        batch_op.drop_column('boss_weekly_Lucid_Normal')
        batch_op.drop_column('boss_weekly_Lucid_Easy')
        batch_op.drop_column('boss_weekly_GuardianAngelSlime_Chaos')
        batch_op.drop_column('boss_weekly_GuardianAngelSlime_Normal')
        batch_op.drop_column('boss_weekly_Damian_Hard')
        batch_op.drop_column('boss_weekly_Damian_Normal')
        batch_op.drop_column('boss_weekly_Swoo_Hard')
        batch_op.drop_column('boss_weekly_Swoo_Normal')
        batch_op.drop_column('boss_weekly_Cygnus_Normal')
        batch_op.drop_column('boss_weekly_Cygnus_Easy')
        batch_op.drop_column('boss_weekly_PinkBean_Chaos')
        batch_op.drop_column('boss_weekly_Bellum_Chaos')
        batch_op.drop_column('boss_weekly_BloodyQueen_Chaos')
        batch_op.drop_column('boss_weekly_Banban_Chaos')
        batch_op.drop_column('boss_weekly_Pierre_Chaos')
        batch_op.drop_column('boss_weekly_Papulatus_Chaos')
        batch_op.drop_column('boss_weekly_Hilla_Hard')
        batch_op.drop_column('boss_weekly_Magnus_Hard')
        batch_op.drop_column('boss_weekly_Zaqqum_Chaos')
        batch_op.drop_column('boss_daily_PinkBean_Normal')
        batch_op.drop_column('boss_daily_Arkarium_Normal')
        batch_op.drop_column('boss_daily_Arkarium_Easy')
        batch_op.drop_column('boss_daily_Horntail_Chaos')
        batch_op.drop_column('boss_daily_Horntail_Normal')
        batch_op.drop_column('boss_daily_Horntail_Easy')
        batch_op.drop_column('boss_daily_VonLeon_Hard')
        batch_op.drop_column('boss_daily_VonLeon_Normal')
        batch_op.drop_column('boss_daily_VonLeon_Easy')
        batch_op.drop_column('boss_daily_Bellum_Normal')
        batch_op.drop_column('boss_daily_BloodyQueen_Normal')
        batch_op.drop_column('boss_daily_Banban_Normal')
        batch_op.drop_column('boss_daily_Pierre_Normal')
        batch_op.drop_column('boss_daily_Papulatus_Normal')
        batch_op.drop_column('boss_daily_Papulatus_Easy')
        batch_op.drop_column('boss_daily_Kaung_Normal')
        batch_op.drop_column('boss_daily_Hilla_Normal')
        batch_op.drop_column('boss_daily_Magnus_Normal')
        batch_op.drop_column('boss_daily_Magnus_Easy')
        batch_op.drop_column('boss_daily_Zaqqum_Normal')
        batch_op.drop_column('boss_daily_Zaqqum_Easy')
        batch_op.drop_column('UnionCoinCheckbox')
        batch_op.drop_column('monsterParkCheckbox')
        batch_op.drop_column('dailyGiftCheckbox')
        batch_op.drop_column('farmHarvestCheckbox')
        batch_op.drop_column('ursusCheckbox')
        batch_op.drop_column('symbol_arcane6_weekly')
        batch_op.drop_column('symbol_arcane5_weekly')
        batch_op.drop_column('symbol_arcane4_weekly')
        batch_op.drop_column('symbol_arcane3_weekly')
        batch_op.drop_column('symbol_arcane2_weekly')
        batch_op.drop_column('symbol_arcane1_weekly')
        batch_op.drop_column('symbol_authentic6_daily')
        batch_op.drop_column('symbol_authentic5_daily')
        batch_op.drop_column('symbol_authentic4_daily')
        batch_op.drop_column('symbol_authentic3_daily')
        batch_op.drop_column('symbol_authentic2_daily')
        batch_op.drop_column('symbol_authentic1_daily')
        batch_op.drop_column('symbol_arcane9_daily')
        batch_op.drop_column('symbol_arcane8_daily')
        batch_op.drop_column('symbol_arcane7_daily')
        batch_op.drop_column('symbol_arcane6_daily')
        batch_op.drop_column('symbol_arcane5_daily')
        batch_op.drop_column('symbol_arcane4_daily')
        batch_op.drop_column('symbol_arcane3_daily')
        batch_op.drop_column('symbol_arcane2_daily')
        batch_op.drop_column('symbol_arcane1_daily')
        batch_op.drop_column('visible_event')
        batch_op.drop_column('visible_basic')
        batch_op.drop_column('visible_boss')
        batch_op.drop_column('visible_symbol')
        batch_op.drop_column('tabOrder')

    # ### end Alembic commands ###