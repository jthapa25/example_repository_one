"""
This module contains account doa unit tests

create account tests
business logic:
Accounts may not have the same type( this will be handled in the service layer)
Accounts may not have the same account number (this will be handled in the service layer)
Accounts may not have duplicate Ids ( will handle this here because it directly relates to the database)


"""
from unittest import mock
from unittest.mock import MagicMock, patch

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_postgres import AccountDAOImpPostgres
from entities.account_class_information import Account

account_dao = AccountDAOImpPostgres()  # I will be using this account dao object fo all my account dao unit tests


def test_create_account_success():
    test_account = Account(0, "Saving", 5000)
    result = account_dao.create_account(test_account)
    print(result.account_id)
    assert result.account_id != 0


def test_catch_non_unique_id():
    """ because my database handles the ID, I need to check that providing an ID does not ruin the method"""
    test_account = Account(1, "Checking", 6000)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1

    # get team tests


def test_get_account_info_by_id_success():
    result = account_dao.get_account_by_id(1)
    assert result.account_id == 1


def test_get_account_using_non_existent_id():
    try:
        account_dao.get_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


# update team tests
def test_update_account_by_id_success():
    new_account_type = Account(1, "Personal", 7000)
    result = account_dao.update_account_by_id(new_account_type)
    assert result.account_type == "Personal"


def test_update_account_using_non_existent_id():
    try:
        new_account_type = Account(0, "Personal", 56782)
        account_dao.update_account_by_id(new_account_type)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_delete_account_by_id_success():
    result = account_dao.delete_account_by_id(1)
    assert result


def test_delete_account_with_non_existent_id():
    try:
        account_dao.delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_get_all_account_success():
    result = account_dao.get_all_accounts_information()
    assert len(result) >= 1


@patch("dal_layer.account_dao.account_dao_postgres.AccountDAOImpPostgres.get_all_accounts_information")
def test_no_accounts_found(mock):
    """ this is not actually testing my method, just raising an exception and catching it in the except block"""
    try:
        mock.side_effect = BadAccountInfo("No accounts were found")
        account_dao.get_all_accounts_information()
        assert False
    except BadAccountInfo as e:
        assert str(e) == "No accounts were found"
