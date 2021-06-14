import pytest
from rest_framework.reverse import reverse
from rest_framework import status
from tests.conftest import api_client, product_factory

pytestmark = [
    pytest.mark.django_db
]


def test_add_review(api_client, django_user_model, product_factory):
    product = product_factory(name='Just some product')
    review_payload = {
        'product': product.id,
        'text': 'Awesome product',
        'mark': 5,
    }

    url = reverse('reviews-list')
    resp = api_client.post(url, review_payload)
    assert resp.status_code == status.HTTP_403_FORBIDDEN

    user = django_user_model.objects.create_user(username='user1', password='bar')
    api_client.force_login(user)
    review_payload['author'] = user.id
    resp = api_client.post(url, review_payload)
    assert resp.status_code == status.HTTP_201_CREATED


def test_unique_review(api_client, django_user_model, product_factory):
    product = product_factory(name='Just some product')
    user = django_user_model.objects.create_user(username='user1', password='bar')
    api_client.force_login(user)
    review_payload = {
        'author': user.id,
        'product': product.id,
        'text': 'Awesome product',
        'mark': 5,
    }

    url = reverse('reviews-list')
    resp = api_client.post(url, review_payload)
    assert resp.status_code == status.HTTP_201_CREATED

    review_payload['text'] = 'Another review'
    resp = api_client.post(url, review_payload)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST