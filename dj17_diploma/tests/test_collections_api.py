import pytest
from rest_framework.reverse import reverse
from rest_framework import status
from tests.conftest import api_client, collection_factory

pytestmark = [
    pytest.mark.django_db
]


def test_collection_retrieve(api_client, collection_factory):
    collection = collection_factory(name='Just some collection')
    assert collection.id
    url = reverse('collections-detail', args=(collection.id,))
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['name'] == 'Just some collection'


def test_collection_list(api_client, collection_factory):
    collections = collection_factory(_quantity=2)
    url = reverse('collections-list')
    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 2