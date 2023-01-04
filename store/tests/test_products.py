import pytest
from model_bakery import baker
from rest_framework import status

from store.models import Collection, Product

@pytest.fixture
def create_product(api_client):
    def do_create_product(valid):
        collection = Collection.objects.create(title='a')
        product = {
            'id': 1,
            'title': 'a',
            'slug': 'a',
            'inventory': 1,
            'unit_price': 1,
            'collection': collection.id
        }
        if valid == False:
            product['title'] = ''

        return api_client.post('/store/products/', product)
    return do_create_product



@pytest.mark.django_db
class TestCreateProduct:

    def test_if_anonymous_user_returns_401(self, create_product):
        response = create_product(valid=True)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_not_admin_user_returns_403(self, create_product, authenticate_user):
        authenticate_user()
        response = create_product(valid=True)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_invalid_data_returns_400(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)
        response = create_product(valid=False)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_valid_data_returns_201(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)
        response = create_product(valid=True)
        assert response.status_code == status.HTTP_201_CREATED
