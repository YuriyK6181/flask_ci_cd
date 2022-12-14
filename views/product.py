"""
Doc String
"""
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound
from views.forms.products import CreateProductForm

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Desktop"
}

@products_app.route("/", endpoint="list")
def get_products():
    """
    Doc String
    """
    # return "<h1>Products List</h1>"
    return render_template("/products/list.html", products=PRODUCTS)

@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    """
    Doc String
    """
    product_name = PRODUCTS[product_id]
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")
    return render_template(
        "/products/details.html",
        product_id=product_id,
        product_name=product_name)

@products_app.route("/add/", methods=["GET","POST"], endpoint="add")
def add_product():
    """
    Doc String
    """
    form = CreateProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    print(request.form)
#    product_name = request.form.get("product-name", "")
#    product_name=product_name.strip()
#    if not product_name:
#        raise BadRequest("Field product name is required!")
    product_name=form.name.data
    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name
    url = url_for("products_app.details", product_id=product_id)
    return redirect(url)
