from custom_exceptions.bad_client_info import BadClientInfo
from dal_layer.client_dao.client_dao_imp import ClientDAOImp
from entities.client_class_information import Client
from service_layer.client_services.client_service_imp import ClientServiceImp

client_dao = ClientDAOImp()
client_service = ClientServiceImp(client_dao)

"""
Note: this is not an exhaustive lists of tests: just some examples of different types of tests you could write
"""


def test_catch_first_name_too_long_create():
    client = Client(0, 1, "This is too long of a first name", "this is fine", 56780)
    try:
        client_service.service_create_client(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_create():
    client = Client(0, 1, "this is fine", "This is too long of a last name", 56780)
    try:
        client_service.service_create_client(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "Last name is too long"


def test_catch_account_number_already_exist_on_account_create():
    client = Client(0, 1, "this is fine", "this is fine", 22)
    try:
        client_service.service_create_client(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "Account number already exist"


def test_non_int_provided_for_id_get_client():
    try:
        client_service.service_get_client_by_id("1")
    except BadClientInfo as e:
        assert str(e) == "Please provide a valid Id"


def test_catch_first_name_too_long_update():
    client = Client(1, 1, "This is too long of a first name", "this is fine", 56780)
    try:
        client_service.service_update_client_information(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_update():
    client = Client(0, 1, "this is fine", "This is too long of a last name", 56780)
    try:
        client_service.service_update_client_information(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "Last name is too long"


def test_catch_account_number_already_exist_on_account_update():
    client = Client(0, 1, "this is fine", "this is fine", 22)
    try:
        client_service.service_update_client_information(client)
        assert False
    except BadClientInfo as e:
        assert str(e) == "Account number already exist"


def test_non_int_provided_for_id_delete():
    try:
        client_service.service_delete_client_by_id("1")
    except BadClientInfo as e:
        assert str(e) == "Please provide a valid Id"
