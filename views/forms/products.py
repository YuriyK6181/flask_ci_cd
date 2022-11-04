"""
Doc String
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CreateProductForm(FlaskForm):
    """
    Doc String
    """
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
