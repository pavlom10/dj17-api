import pytest
from rest_framework.reverse import reverse
from rest_framework import status
from tests.conftest import api_client, product_factory

pytestmark = [
    pytest.mark.django_db
]


def test_product_retrieve(api_client, product_factory):
    product = product_factory(name='Just some product')
    assert product.id
    url = reverse('products-detail', args=(product.id,))
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['name'] == 'Just some product'


def test_product_list(api_client, product_factory):
    products = product_factory(_quantity=2)
    url = reverse('products-list')
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 2


def test_add_product(api_client, admin_user):
    url = reverse('products-list')
    product_payload = {
        'name': 'Some product',
        'price': 100
    }
    resp = api_client.post(url, product_payload)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    api_client.force_authenticate(admin_user)
    resp = api_client.post(url, product_payload)
    assert resp.status_code == status.HTTP_201_CREATED


def test_product_filter(api_client, product_factory):
    product_1 = product_factory(name='Just some product', price=100)
    product_2 = product_factory(name='Another product', description='With description', price=300)
    url = reverse('products-list')

    resp = api_client.get(url, {'search': 'some product'})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['name'] == 'Just some product'

    resp = api_client.get(url, {'price_to': 200})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['name'] == 'Just some product'

    resp = api_client.get(url, {'price_from': 200, 'search': 'description'})
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['name'] == 'Another product'
