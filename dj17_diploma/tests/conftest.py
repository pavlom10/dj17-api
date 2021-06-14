import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make('Product', **kwargs)
    return factory

@pytest.fixture
def order_factory():
    def factory(**kwargs):
        return baker.make('Order', **kwargs)
    return factory
