from flask import Blueprint, url_for
from werkzeug.utils import redirect
from maple.models import UserDetail
from maple.scripts import crawlingID
import json
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def maple():
    return redirect(url_for('homework.index'))

