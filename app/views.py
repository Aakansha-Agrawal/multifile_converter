from app import app
from flask import render_template, flash

@app.route("/")
def index():
    # return render_template("download.html")
    return render_template("index.html")

@app.route("/icon")
def icon():
    # return render_template("test_nav.html")
    # return render_template("loading.html")
    return render_template("nav.html")

#Sign Up and Sign In part 
@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


# # Sessions working
# from flask import session
# from datetime import timedelta

# app.config['SECRET_KEY'] = 'super secret'
# @app.route("/start_counter")
# def start_counter():
#     var = 'aaaaa'
#     if not session.get("count") is None:
#         session['count'] = secrets.token_urlsafe(6)
#         session['count'] = session['count'] + '_' + var
#         print("created")
#         return str(session.get('count'))

#     else:
#         return str(session.get('count', 'No Counter set'))

# @app.route("/count")
# def count():
#     count = session.get('count')
#     if isinstance(count, int):
#         session['count'] += 'bb'
#         return str(session['count'])

#         # session.permanent = True
#         # app.permanent_session_lifetime = timedelta(minutes=1)
#         # print("session destroyed")
#     return 'No Counter set'