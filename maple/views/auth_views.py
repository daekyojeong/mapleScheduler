from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from maple import db
from maple.forms import UserCreateForm, UserLoginForm
from maple.models import UserLogin
from maple.scripts import db_init
import functools
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = UserLogin.query.filter_by(userid=form.username.data).first()
        if not user:
            user = UserLogin(userid=form.username.data,
                        password=generate_password_hash(form.password1.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.maple'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('signup.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = UserLogin.query.filter_by(userid=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            _next = request.args.get('next', '')
            db_init.total_reset(user.id)
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.maple'))
        flash(error)
    return render_template('login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = UserLogin.query.get(user_id)
        
@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.maple'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view