from maple.models import UserDetail, dbToDictFormatting, createDetailCol, updateDetailCol, updateDetailColVisible, updateDetailColCheckbox
from datetime import datetime
from maple.models import DBNameList
from maple import db
def total_reset(userID):
    id_list = UserDetail.query.filter(UserDetail.userid==userID).all()
    now_time = datetime.now()
    now_year = now_time.year
    now_month = now_time.month
    now_day = now_time.day
    now_week = now_time.weekday()
    for id in id_list:
        lu = id.last_update
        print('is Here!!!', id.last_update)
        print(id.last_update.day, now_day)
        if (now_year == lu.year) and (now_day == lu.day) and (now_month == lu.month):
            continue

        if now_week == 3:
            db_weakly_init(id, now_time)
        
        db_daily_init(id, now_time)

def db_daily_init(userObj, now_time):
    print('start daily init')
    for dicAttr in DBNameList['symbol']:
        if 'daily' in dicAttr:
            print(dicAttr)
            setattr(userObj, dicAttr, False)
        
    for dicAttr in DBNameList['boss']:
        if 'daily' in dicAttr:
            print(dicAttr)
            setattr(userObj, dicAttr, False)
        
    for dicAttr in DBNameList['basic']:
        setattr(userObj, dicAttr, False)
    
    userObj.last_update = now_time
    db.session.commit()
def db_weakly_init(userObj, now_time):
    print('start weekly init')
    for dicAttr in DBNameList['symbol']:
        if 'weekly' in dicAttr:
            print(dicAttr)
            setattr(userObj, dicAttr, False)
        
    for dicAttr in DBNameList['boss']:
        if 'weekly' in dicAttr:
            print(dicAttr)
            setattr(userObj, dicAttr, False)
    userObj.last_update = now_time
    db.session.commit()
