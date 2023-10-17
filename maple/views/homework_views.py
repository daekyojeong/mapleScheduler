from flask import Blueprint, render_template, jsonify, request, g, session
from maple.models import UserDetail, dbToDictFormatting, createDetailCol, updateDetailCol, updateDetailColVisible, updateDetailColCheckbox
from maple.scripts import crawlingID
from maple.views.auth_views import login_required
import json
from datetime import datetime
bp = Blueprint('homework', __name__, url_prefix='/')

@bp.route('/homework')
def index():
    userID = session.get('user_id')
    print(userID)
    id_list = UserDetail.query.filter(UserDetail.userid==userID).all()
    
    data = []
    for id in id_list:
        #_dict = crawlingID.userIDCrawling(id.nickname)
        print('easy zaqqum',id.id)
        # if dict != -1:
        #     id.lvl = _dict['lvl']
        #     id.imgUrl = _dict['img_src']
        #     id.job = _dict['job']
        #     updateDetailCol(id, nickname=id.nickname, lvl=_dict['lvl'], imgUrl=_dict['img_src'], userid=userID, job=_dict['job'])
        # dictret = dict(id.__dict__)
        # print(dictret)
        dictret = dbToDictFormatting(id)
        
        # #print(dictret)
        # dictret.pop('_sa_instance_state', None)
        # dictret['last_update'] = dictret['last_update'].strftime("%m/%d/%Y,%H:%M:%S")
        # if dictret['visible_boss'] != '':
        #     dictret['visible_boss'] = json.loads(dictret['visible_boss'])
        # if dictret['visible_symbol'] != '':
        #     dictret['visible_symbol'] = json.loads(dictret['visible_symbol'])
        # if dictret['visible_basic'] != '':
        #     dictret['visible_basic'] = json.loads(dictret['visible_basic'])
        # if dictret['visible_event'] != '':
        #     dictret['visible_event'] = json.loads(dictret['visible_event'])
        data.append(dictret)
    data = json.dumps(data)
    return render_template('homework.html', id_list=data)

@bp.route('/new_char', methods=['POST', 'GET'])
@login_required
def new_character():
    _data = request.get_json()
    nickname = _data['nickname']
    tabOrder = 1
    last_update = datetime.now()
    print(last_update)
    try:
        dict = crawlingID.userIDCrawling(nickname)
    except:
        dict = -1
    _data = {}
    if dict != -1:
        _data['nickname'] = nickname
        _data['lvl'] = dict['lvl']
        _data['imgUrl'] = dict['img_src']
        _data['userid'] = g.user.id
        _data['job'] = dict['job']
        _data = json.dumps(_data)
        createDetailCol(nickname, dict['lvl'], dict['img_src'], g.user.id, dict['job'], tabOrder, last_update)
        return jsonify({'suc': True, 'data':_data}), 200
    return jsonify({'suc': False, 'data':''}), 200

@bp.route('/hw_visible_update', methods=['POST', 'GET'])
def visible_update_call():
    _data = request.get_json()
    nickname = _data['char']['nickname']
    print(nickname)
    print(session.get('user_id'))
    userObj = UserDetail.query.filter(UserDetail.userid==session.get('user_id'), UserDetail.nickname==nickname).first()
    updateDetailColVisible(userObj, _data['char'])
    print(userObj.nickname)
    return jsonify({'suc': True, 'data':''}), 200
    
    
@bp.route('/hw_checkbox_update', methods=['POST', 'GET'])
def checkbox_update_call():
    _data = request.get_json()
    nickname = _data['nickname']
    dbKey = _data['key']
    dbValue = _data['value']
    userObj = UserDetail.query.filter(UserDetail.userid==session.get('user_id'), UserDetail.nickname==nickname).first()
    updateDetailColCheckbox(userObj, dbKey, dbValue)
    
    return jsonify({'suc': True, 'data':''}), 200
            

