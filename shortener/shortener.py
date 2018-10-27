from flask import (
    Blueprint, g, request, make_response, redirect
)
from werkzeug.exceptions import abort
from shortener.db import get_db
from hashlib import md5
import datetime

sh = Blueprint('shortener', __name__)

@sh.route('/shorten', methods=["POST"])
def shorten():
    user_id = request.form['user_id']

    # the long_url must be url escaped thus we must fix unescape that here
    long_url = request.form['url']

    # default expiry is 2 weeks from shortener date
    expires_at = datetime.datetime.now() + datetime.timedelta(days=14)

    short_link = 'temp '#TODO hash some value to make shortener value

    BASE_URL = 'http://www.akshaypall.me' #TODO: REPLACE
    full_short_link = BASE_URL #TODO: fix
    
    # insert to db
    db = get_db()
    if db is None:
        return abort(500, "DB Access Error")
    
    #TODO: check long_url isn't another shortened url
    #TODO: check this user hasn't already shortener this url, if so then update the expiry and return that

    # else: shorten and insert
    db.execute(
        'INSERT INTO surl (user_id, long_url, short_link, expires_at)'
        ' VALUES (?, ?, ?, ?)',
        (user_id, long_url, short_link, expires_at)
    )
    db.commit()

    #return full_short_link as a json response, not redirect
    return redirect(full_short_link)


#TODO: get link
        
