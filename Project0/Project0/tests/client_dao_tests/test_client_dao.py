from custom_exceptions.id_not_found import IdNotFound
from dal_layer.client_dao.client_dao_imp import ClientDAOImp
from entities.client_class_information import Client

client_dao = ClientDAOImp()

"""
create client tests
business logic:
    clients may not have same Id (this will be handled in the service layer)
    clients may not have the same account number on the same account (this will be handled in the service layer)
    
    The tests in this module where crafted to check two things:
1. when the correct data is provided to the method, the method returns the expected return value
2. when the data you want to work with does not exist, a message indicating it does not exist should be returned

"""


def test_create_client_success():
    test_client = Client(0, 1, "New", "client1", 10)
    result = client_dao.create_client(test_client)
    assert result.client_id != 0


def test_catch_non_unique_id():
    # because my database handles the ID, I need to check that providing an ID does not ruin the method
    test_client = Client(0, 1, "first", "client2", 10)
    result = client_dao.create_client(test_client)
    assert result.client_id != 1

    # get client tests


def test_get_client_info_by_id_success():
    result = client_dao.get_client_by_id(1)
    assert result.client_id == 1


def test_get_account_using_non_existent_id():
    try:
        client_dao.get_client_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"


# update client tests
def test_update_account_by_id_success():
    new_client_name = Client(0, 1, "second", "client3", 20)
    result = client_dao.update_client_by_id(new_client_name)
    assert result.first_name == "second"


def client_update_account_using_non_existent_id():
    try:
        new_client_name = Client(0, 1, "third", "client4", 40)
        client_dao.update_client_by_id(new_client_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"


# delete account tests
def test_delete_account_by_id_success():
    result = client_dao.delete_client_by_id(1)
    assert result


def test_delete_account_with_non_existent_id():
    try:
        client_dao.delete_client_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"
