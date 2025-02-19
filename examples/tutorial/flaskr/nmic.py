from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("nmic", __name__, url_prefix="/nmic")

@bp.route("/nmic")
def index():
	"""Show all the posts, most recent first."""
	db = get_db()
	posts = db.execute(
		"SELECT p.id, title, body, created, author_id, username"
		" FROM post p JOIN user u ON p.author_id = u.id"
		" ORDER BY created DESC"
	).fetchall()
	return render_template("nmic/index.html", posts=posts[-1:])
	# return render_template("nmic/index.html")
