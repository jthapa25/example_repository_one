from custom_exceptions.id_not_found import IdNotFound
from dal_layer.client_dao.client_dao_imp import ClientDAOImp
from entities.client_class_information import Client

client_dao = ClientDAOImp()


def test_create_client_success():
    test_client = Client(0, 1, "New", "Client", 10)
    result = client_dao.create_client(test_client)
    assert result.client_id != 0


def test_catch_non_unique_id():
    test_client = Client(0, 1, "first", "Client1", 10)
    result = client_dao.create_client(test_client)
    assert result.client_id != 1

    # get client tests


def test_get_client_info_by_id_success():
    result = client_dao.get_client_information_by_id(1)
    assert result.client_id == 1


def test_get_client_using_non_existant_id():
    try:
        client_dao.get_client_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"


# update team tests
def test_update_client_by_id_success():
    new_client_name = Client(1, "good", "Dallas")
    result = client_dao.update_client_by_id(new_client_name)
    assert result.client_name == "good"


def client_update_client_using_non_existant_id():
    try:
        new_client_name = Client(0, "good", "Dallas")
        client_dao.update_client_by_id(new_client_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"


def test_delete_client_by_id_success():
    result = client_dao.detete_client_by_id(1)
    assert result


def test_delete_client_with_non_existant_id():
    try:
        client_dao.delete_client_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No client matches the id given: please try again!"
