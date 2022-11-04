"""
Doc String
"""
import random
from flask import url_for



def test_get_item(client):
    """
    Doc String
    """
    random_id = random.randint(1, 100)
    url = url_for("get_item", item_id=random_id)
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['Item']['id'] == random_id
