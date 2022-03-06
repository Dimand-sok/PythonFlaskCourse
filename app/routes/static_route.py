from flask import Blueprint, render_template, make_response, abort, request, redirect, url_for

from app.database import session
from app.models import ForumModel, ReplyModel

from app.database import session
from app.models import ForumModel, ReplyModel

static_route = Blueprint("static_route",__name__)

#home page
@static_route.route("/", methods=["GET"])
def home():
    forums=session.query(ForumModel).all()
    return render_template("index.html",title="home",forums=forums)


#display single forum based on slush
@static_route.route("</slush>", methods=["GET"])
def single_forum(slush):
    forum=session.query(ForumModel).filter(ForumModel.slush == slush).one_or_none()
    if not forum:
        abort(404)

    replies = session.query(ReplyModel).filter(ReplyModel.forum_id == forum.id).all()
    return render_template("single-forum.html", title=forum.title, forum=forum, replies=replies, reply=None)

#create new reply to single forum
@static_route.route("/<slush>", methods=["POST"])
def create_reply(slush):
    forum = session.query(ForumModel).filter(ForumModel.slush == slush).one_or_none()
    if not forum:
        abort(400)

    reply = request.form.to_dict()
    reply.update({"forum_id": forum.id})

    new_reply = ReplyModel(reply)
    session.add(new_reply)
    session.commit()

    redirect_url = f"{url_for('static_route.home')}{forum.slush}"

    return redirect(redirect_url)


#Add static data into forum table
@static_route.route("/new", methods=["GET"])
def new_forum():
    forum=[ForumModel({"title":"Web hosting","description":"anything related to hosting","slush":"web hosting"})]
    session.add_all(forum)
    session.commit()
    return make_response({"Add forum":"Successfully"},200)




   


