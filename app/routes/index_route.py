from flask import Blueprint,render_template

index_route = Blueprint("index_route", __name__, url_prefix="/home")


@index_route.route("/", methods=["GET"])
def index_view():
    return render_template("index.html")



