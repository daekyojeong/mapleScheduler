from maple import db
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime
import json



class UserLogin(db.Model):
    __tablename__ = 'UserLogin'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    
    
class UserDetail(db.Model): 
    __tablename__ = 'UserDetail'
    id = db.Column(db.Integer, primary_key=True)   
    tabOrder = db.Column(db.Integer, nullable=False)
    nickname = db.Column(db.String(32), unique=True)
    lvl = db.Column(db.Integer)
    job = db.Column(db.String(32))
    imgUrl = db.Column(db.String(256))
    last_update = db.Column(db.DateTime(), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('UserLogin.id', ondelete='CASCADE'))
    
    visible_symbol = db.Column(db.String(2048), default='')
    visible_boss = db.Column(db.String(2048), default='')
    visible_basic = db.Column(db.String(2048), default='')
    visible_event = db.Column(db.String(2048), default='')
    
    symbol_arcane1_daily = db.Column(db.Boolean, default=False)
    symbol_arcane2_daily = db.Column(db.Boolean, default=False)
    symbol_arcane3_daily = db.Column(db.Boolean, default=False)
    symbol_arcane4_daily = db.Column(db.Boolean, default=False)
    symbol_arcane5_daily = db.Column(db.Boolean, default=False)
    symbol_arcane6_daily = db.Column(db.Boolean, default=False)
    symbol_arcane7_daily = db.Column(db.Boolean, default=False)
    symbol_arcane8_daily = db.Column(db.Boolean, default=False)
    symbol_arcane9_daily = db.Column(db.Boolean, default=False)
    
    symbol_authentic1_daily = db.Column(db.Boolean, default=False)
    symbol_authentic2_daily = db.Column(db.Boolean, default=False)
    symbol_authentic3_daily = db.Column(db.Boolean, default=False)
    symbol_authentic4_daily = db.Column(db.Boolean, default=False)
    symbol_authentic5_daily = db.Column(db.Boolean, default=False)
    symbol_authentic6_daily = db.Column(db.Boolean, default=False)
    
    symbol_arcane1_weekly = db.Column(db.Boolean, default=False)
    symbol_arcane2_weekly = db.Column(db.Boolean, default=False)
    symbol_arcane3_weekly = db.Column(db.Boolean, default=False)
    symbol_arcane4_weekly = db.Column(db.Boolean, default=False)
    symbol_arcane5_weekly = db.Column(db.Boolean, default=False)
    symbol_arcane6_weekly = db.Column(db.Boolean, default=False)
    
    ursusCheckbox = db.Column(db.Boolean, default=False)
    farmHarvestCheckbox = db.Column(db.Boolean, default=False)
    dailyGiftCheckbox = db.Column(db.Boolean, default=False)
    monsterParkCheckbox = db.Column(db.Boolean, default=False)
    UnionCoinCheckbox = db.Column(db.Boolean, default=False)
    
    boss_daily_Zaqqum_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_Zaqqum_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Magnus_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_Magnus_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Hilla_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Kaung_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Papulatus_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_Papulatus_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Pierre_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Banban_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_BloodyQueen_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Bellum_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_VonLeon_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_VonLeon_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_VonLeon_Hard = db.Column(db.Boolean, default=False) 
    boss_daily_Horntail_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_Horntail_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_Horntail_Chaos = db.Column(db.Boolean, default=False) 
    boss_daily_Arkarium_Easy = db.Column(db.Boolean, default=False) 
    boss_daily_Arkarium_Normal = db.Column(db.Boolean, default=False) 
    boss_daily_PinkBean_Normal = db.Column(db.Boolean, default=False) 
    
    boss_weekly_Zaqqum_Chaos = db.Column(db.Boolean, default=False)
    boss_weekly_Magnus_Hard = db.Column(db.Boolean, default=False)  
    boss_weekly_Hilla_Hard = db.Column(db.Boolean, default=False)  
    boss_weekly_Papulatus_Chaos = db.Column(db.Boolean, default=False)  
    boss_weekly_Pierre_Chaos = db.Column(db.Boolean, default=False)  
    boss_weekly_Banban_Chaos = db.Column(db.Boolean, default=False)  
    boss_weekly_BloodyQueen_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_Bellum_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_PinkBean_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_Cygnus_Easy = db.Column(db.Boolean, default=False) 
    boss_weekly_Cygnus_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Swoo_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Swoo_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Damian_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Damian_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_GuardianAngelSlime_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_GuardianAngelSlime_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_Lucid_Easy = db.Column(db.Boolean, default=False) 
    boss_weekly_Lucid_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Lucid_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Will_Easy = db.Column(db.Boolean, default=False) 
    boss_weekly_Will_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Will_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Dusk_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Dusk_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_ZinHilla_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_ZinHilla_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Dunkel_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Dunkel_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Seren_Normal = db.Column(db.Boolean, default=False) 
    boss_weekly_Seren_Hard = db.Column(db.Boolean, default=False) 
    boss_weekly_Seren_Extreme = db.Column(db.Boolean, default=False) 
    boss_weekly_Kalos_Chaos = db.Column(db.Boolean, default=False) 
    boss_weekly_Kaling_Normal = db.Column(db.Boolean, default=False)     
    
    boss_monthly_BlackMage_Hard = db.Column(db.Boolean, default=False) 
    boss_monthly_BlackMage_Extreme = db.Column(db.Boolean, default=False) 
    
    eventAttendanceCheckbox = db.Column(db.Boolean, default=False) 
    
    eventDeepAttendanceCheckbox = db.Column(db.Integer, default=0) 
    eventEXPFarmCheckbox = db.Column(db.Integer, default=0) 
    eventEXPPunchKingCheckbox = db.Column(db.Integer, default=0) 
    eventEXPAdventureCheckbox = db.Column(db.Integer, default=0) 
    
DBNameList = {
    'BaseInfo':['id', 'tabOrder', 'nickname', 'lvl', 'job', 'imgUrl', 'last_update', 'userid'],
    'visibleInfo':['visible_symbol', 'visible_boss', 'visible_basic', 'visible_event'],
    'symbol':['symbol_arcane1_daily', 'symbol_arcane2_daily', 'symbol_arcane3_daily', 'symbol_arcane4_daily',\
            'symbol_arcane5_daily', 'symbol_arcane6_daily', 'symbol_arcane7_daily', 'symbol_arcane8_daily', 'symbol_arcane9_daily',\
            'symbol_authentic1_daily', 'symbol_authentic2_daily', 'symbol_authentic3_daily', 'symbol_authentic4_daily', 'symbol_authentic5_daily', 'symbol_authentic6_daily',\
            'symbol_arcane1_weekly', 'symbol_arcane2_weekly', 'symbol_arcane3_weekly', 'symbol_arcane4_weekly', 'symbol_arcane5_weekly', 'symbol_arcane6_weekly'],
    'basic':['ursusCheckbox', 'farmHarvestCheckbox', 'dailyGiftCheckbox', 'monsterParkCheckbox', 'UnionCoinCheckbox'],
    'boss':['boss_daily_Zaqqum_Easy','boss_daily_Zaqqum_Normal','boss_daily_Magnus_Easy','boss_daily_Magnus_Normal', 'boss_daily_Hilla_Normal',\
            'boss_daily_Kaung_Normal','boss_daily_Papulatus_Easy','boss_daily_Papulatus_Normal','boss_daily_Pierre_Normal','boss_daily_Banban_Normal',\
            'boss_daily_BloodyQueen_Normal','boss_daily_Bellum_Normal','boss_daily_VonLeon_Easy','boss_daily_VonLeon_Normal','boss_daily_VonLeon_Hard',\
            'boss_daily_Horntail_Easy','boss_daily_Horntail_Normal','boss_daily_Horntail_Chaos','boss_daily_Arkarium_Easy','boss_daily_Arkarium_Normal',\
            'boss_daily_PinkBean_Normal','boss_weekly_Zaqqum_Chaos','boss_weekly_Magnus_Hard','boss_weekly_Hilla_Hard','boss_weekly_Papulatus_Chaos','boss_weekly_Pierre_Chaos',\
            'boss_weekly_Banban_Chaos','boss_weekly_BloodyQueen_Chaos','boss_weekly_Bellum_Chaos','boss_weekly_PinkBean_Chaos','boss_weekly_Cygnus_Easy','boss_weekly_Cygnus_Normal',\
            'boss_weekly_Swoo_Normal','boss_weekly_Swoo_Hard','boss_weekly_Damian_Normal','boss_weekly_Damian_Hard','boss_weekly_GuardianAngelSlime_Normal','boss_weekly_GuardianAngelSlime_Chaos',\
            'boss_weekly_Lucid_Easy','boss_weekly_Lucid_Normal','boss_weekly_Lucid_Hard','boss_weekly_Will_Easy','boss_weekly_Will_Normal','boss_weekly_Will_Hard','boss_weekly_Dusk_Normal',\
            'boss_weekly_Dusk_Chaos','boss_weekly_ZinHilla_Normal','boss_weekly_ZinHilla_Hard','boss_weekly_Dunkel_Normal','boss_weekly_Dunkel_Hard','boss_weekly_Seren_Normal',\
            'boss_weekly_Seren_Hard','boss_weekly_Seren_Extreme','boss_weekly_Kalos_Chaos','boss_weekly_Kaling_Normal','boss_monthly_BlackMage_Hard','boss_monthly_BlackMage_Extreme'],
    'event':['eventAttendanceCheckbox','eventDeepAttendanceCheckbox','eventEXPFarmCheckbox','eventEXPPunchKingCheckbox','eventEXPAdventureCheckbox']
}

def createDetailCol(nickname, lvl, imgUrl, userid, job, tabOrder, last_update):
    de = UserDetail(nickname=nickname, lvl=lvl, imgUrl=imgUrl, userid=userid, job=job, tabOrder=tabOrder, last_update=last_update)
    db.session.add(de)
    db.session.commit()
    
def updateDetailCol(userObj, nickname=None, lvl=None, imgUrl=None, userid=None, tabOrder=None, job=None):
    isEdited = False
    if nickname:
        userObj.nickname=nickname
        isEdited = True
    if lvl:
        userObj.lvl = lvl
        isEdited = True
    if imgUrl:
        userObj.imgUrl = imgUrl
        isEdited = True
    if userid:
        userObj.userid = userid
        isEdited = True
    if tabOrder:
        userObj.tabOrder = tabOrder
        isEdited = True
    if job:
        userObj.job = job
        isEdited = True

    
    if isEdited:
        userObj.last_update = datetime.now()
        
    db.session.commit()
    
def updateDetailColVisible(userObj, data):
    userObj.visible_symbol = json.dumps(data['visible_symbol'])
    userObj.visible_boss = json.dumps(data['visible_boss'])
    userObj.visible_basic = json.dumps(data['visible_basic'])
    userObj.visible_event = json.dumps(data['visible_event'])
    userObj.last_update = datetime.now()
        
    db.session.commit()
    
def updateDetailColCheckbox(userObj, key, val):
    setattr(userObj, key, val)
    userObj.last_update = datetime.now()
        
    db.session.commit()

def deleteDetailCol(userObj):
    db.session.delete(userObj)
    db.session.commit()  
def dbToDictFormatting(userObj):
    userDict = {
        'symbol':{},
        'event':{},
        'basic':{},
        'boss':{}
    }
    for dicAttr in DBNameList['BaseInfo']:
        userDict[dicAttr] = getattr(userObj, dicAttr)
        
    userDict['last_update'] = userDict['last_update'].strftime("%m/%d/%Y,%H:%M:%S")
    
    for dicAttr in DBNameList['visibleInfo']:
        val = getattr(userObj, dicAttr)
        userDict[dicAttr] = '' if val == '' else json.loads(val)
        
    for dicAttr in DBNameList['symbol']:
        userDict['symbol'][dicAttr] = getattr(userObj, dicAttr)
        
    for dicAttr in DBNameList['boss']:
        userDict['boss'][dicAttr] = getattr(userObj, dicAttr)
        
    for dicAttr in DBNameList['event']:
        userDict['boss'][dicAttr] = getattr(userObj, dicAttr)
        
    for dicAttr in DBNameList['basic']:
        userDict['basic'][dicAttr] = getattr(userObj, dicAttr)
        
    return userDict