import pytest
from rest_framework.reverse import reverse
from rest_framework import status
from tests.conftest import api_client, product_factory, order_factory
from orders.models import OrderStatusChoices

pytestmark = [
    pytest.mark.django_db
]


def test_get_orders(api_client, order_factory, admin_user):
    order1 = order_factory()
    order2 = order_factory()
    assert order2.id

    url = reverse('orders-list')
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    api_client.force_authenticate(admin_user)
    resp = api_client.get(url)
    resp_json = resp.json()
    assert len(resp_json) == 2


def test_get_orders_by_owner(api_client, order_factory, django_user_model):
    order1 = order_factory()

    user = django_user_model.objects.create_user(username='user1', password='bar')
    api_client.force_authenticate(user)
    order2 = order_factory(user=user)

    url = reverse('orders-list')
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['id'] == order2.id


def test_update_order(api_client, order_factory, admin_user):
    order = order_factory()
    assert order.id
    url = reverse('orders-detail', args=(order.id,))
    resp = api_client.patch(url, {status: OrderStatusChoices.DONE})
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    api_client.force_authenticate(admin_user)
    resp = api_client.patch(url, {status: OrderStatusChoices.DONE})
    assert resp.status_code == status.HTTP_200_OK


def test_add_order(api_client, product_factory, django_user_model):
    user = django_user_model.objects.create_user(username='user1', password='bar')
    api_client.force_authenticate(user)
    product = product_factory(price=10)
    url = reverse('orders-list')
    order_payload = {
        'user': user.id,
        'products': [ {'product': product.id, 'quantity': 5} ]
    }
    resp = api_client.post(url, order_payload, format='json')
    assert resp.status_code == status.HTTP_201_CREATED
