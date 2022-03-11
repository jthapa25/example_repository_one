from unittest.mock import MagicMock, Mock

from psycopg import OperationalError

from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.account_dao_postgres import AccountDAOImpPostgres
from entities.account_class_information import Account
from service_layer.account_services.account_service_postgres import AccountServiceImpPostgres

account_dao = AccountDAOImpPostgres()
account_service = AccountServiceImpPostgres(account_dao)
duplicate_account_type = Account(0, "Saving", 2000)
non_string_account_type = Account(0, 52, 2000)
duplicate_account_type_update = Account(29, "type is fine", 2000)
non_string_account_type_update = Account(29, 52, 2000)


def test_check_no_duplicate_account_create_account():
    try:
        account_service.account_dao.get_all_accounts_information = MagicMock(
            return_value=[Account(29, "Something else", 2000)])
        account_service.service_create_account(duplicate_account_type_update)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "This account type is already exists in the database"


"""
the test below do not need stubbing because this is never supposed to reach the method that pings our database
"""


def test_catch_non_string_account_type_create_account():
    try:
        account_service.service_create_account(non_string_account_type)
    except BadAccountInfo as e:
        assert str(e) == "Please pass a valid account type"


""" 
select account test
"""


def account_cant_typecast_to_int():  # because of the new features I need to add, I actually need to change this test
    try:
        account_service.service_get_account_by_id("one")
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid account Id"


"""
I will come back to this to see why my stubbed result is not giving me my expected value
"""


def test_get_account_successfully_typecast_string():
    account_service.account_dao.get_account_by_id = MagicMock(result_value="just need to call method")
    result = account_service.service_get_account_by_id("1")
    account_service.account_dao.get_account_by_id.assert_called_with(1)


"""
update account tests
"""


def test_catch_non_string_account_type_update_account():
    try:
        account_service.service_update_account_by_id(non_string_account_type_update)
    except BadAccountInfo as e:
        assert str(e) == "Please pass a valid account type"


def test_no_accounts_in_database():
    try:
        account_service.account_dao.get_all_accounts_information = MagicMock(result_value=[])
        account_service.service_update_account_by_id(duplicate_account_type_update)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "There are no accounts to update!"


# delete account test

def test_catch_non_numeric_id_delete_account():
    try:
        account_service.service_delete_account_by_id("one")
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid account Id"


def test_pass_int_into_delete_method():
    account_service.account_dao.delete_account_by_id = MagicMock(return_value="just need to check int was used")
    account_service.service_delete_account_by_id("1")
    account_service.account_dao.delete_account_by_id.assert_called_with(1)
