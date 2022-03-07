"""
This module contains account doa unit tests

create account tests
"""
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_doa_imp import AccountDAOImp
from entities.account_class_information import Account

account_dao = AccountDAOImp()


def test_create_account_success():
    test_account = Account((1, 1000.00, 2))
    result = account_dao.create_account(test_account)
    assert result.account_id != 0


def test_catch_non_unique_id():
    test_account = Account((1, 1000.00, 2))
    result = account_dao.create_account(test_account)
    assert result.account_id != 1

    # get team tests


def test_get_account_info_by_id_success():
    result = account_dao.get_account_information_by_id(1)
    assert result.account_id == 1


def test_get_account_using_non_existant_id():
    try:
        account_dao.get_account_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


# update team tests
def test_update_account_by_id_success():
    new_account_name = Account(1, "Account of America", "Dallas")
    result = account_dao.update_account_by_id(new_account_name)
    assert result.account_name == "Account of America"


def account_update_account_using_non_existant_id():
    try:
        new_account_name = Account(0, "Account of America", "Dallas")
        account_dao.update_account_by_id(new_account_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No team matches the id given: please try again!"


def test_delete_account_by_id_success():
    result = account_dao.detete_account_by_id(1)
    assert result


def test_delete_account_with_non_existant_id():
    try:
        account_dao.delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No team matches the id given: please try again!"
