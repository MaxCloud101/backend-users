from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
import random


@app.route('/', methods=['GET'])
def create_user():
    """Create a user via query string parameters."""
    username = "usuerio" + str(random.randint(0, 10000))
    email = "user@gmail.com" + str(random.randint(0, 10000))
    new_user = User(username=username,
                    email=email,
                    created=dt.now())
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return {"status": 200}