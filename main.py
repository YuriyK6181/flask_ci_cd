"""
Main Module
"""

from flask import Flask, request, render_template
from views.product import products_app

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="lvbobvoadvludhlvoinrelhlrblivelovblruwev",
)

app.register_blueprint(products_app, url_prefix="/products")

@app.route("/")
def hello_world():
    """
    Doc String
    """
    # return "<h1>Hello World!</h1>"
    return render_template("base.html")


def print_request():
    """
    Doc String
    """
    print("request:", request, ", method=", request.method, ", path=", request.path)


@app.route("/hello/")  # In Flask Add / to the end of route
@app.route("/hello/<name>/")
def hello_view(name: str = None):
    """
    Doc String
    """
    print_request()
    if name is None:
        name = request.args.get("name", "")  # If expected only 1 arg with same name
    name = name.strip()
    if not name:
        name = "World"
    # names = request.args.getlist("name") # If expected more than 1 arg with same name

    # return {"message": "Hello!", "name": name, "names": names}
    return {"message": f"Hello {name}!"}


@app.route("/items/<int:item_id>/")
def get_item(item_id: int):
    """
    Doc String
    """
    return {"Item": {"id": item_id}, }


@app.route("/items/<item_id>/")
def get_item_str(item_id: str):
    """
    Doc String
    """
    return {"Item": {"id": item_id}, }


if __name__ == "__main__":
    app.run(debug=True)
