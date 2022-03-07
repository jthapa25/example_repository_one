from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.account_doa_imp import AccountDAOImp
from entities.account_class_information import Account
from service_layer.account_services.account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)
negative_amount = Account(1, -1000.00, 2)
string_value = Account(1, "abc", 2)
negative_amount_update = Account(1, -1000.00, 2)
string_value_update = Account("abcd", 123, 2)


def test_check_no_negative_amount_create_account():
    try:
        account_service.service_create_account_by_id(negative_amount)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain negative amount"


def test_check_no_string_create_account():
    try:
        account_service.service_create_account_by_id(string_value)
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain string value "


def test_check_no_string_get_account():
    try:
        account_service.service_get_account_id("one")
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain string value "


def test_check_no_negative_amount_update_account():
    try:
        account_service.service_update_account_by_id(negative_amount_update)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain negative amount"


def test_check_no_string_update_account():
    try:
        account_service.service_update_account_by_id(string_value_update)
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain string value "


def test_catch_non_numeric_id_account():
    try:
        account_service.service_delete_account_by_id("one")
    except BadAccountInfo as e:
        assert str(e) == "This account does not contain string value "
