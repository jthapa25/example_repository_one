from psycopg import OperationalError

from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.account_dao_postgres import AccountDAOImpPostgres
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImpPostgres(AccountServiceInterface):

    def __init__(self, account_dao):
        self.account_dao: AccountDAOImpPostgres = account_dao

    def service_create_account(self, account: Account) -> Account:

        if type(account.account_type) != str:
            raise BadAccountInfo("Please pass a valid account type")
        accounts = self.account_dao.get_all_accounts_information()
        if len(accounts) >= 1:
            for existing_account in accounts:
                if existing_account.account_id == account.account_id:
                    raise BadAccountInfo("This account type is already exists in the database")
            return self.account_dao.create_account(account)
        else:
            return self.account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int) -> Account:
        try:
            id_as_int = int(account_id)
            return self.account_dao.get_account_by_id(int(id_as_int))
        except ValueError:
            raise BadAccountInfo("Please provide a valid account Id")

    def service_update_account_by_id(self, account: Account) -> Account:
        if type(account.account_type) != str:
            raise BadAccountInfo("Please pass a valid account type")
        accounts = self.account_dao.get_all_accounts_information()
        if len(accounts) >= 1:
            for existing_account in accounts:
                if existing_account.account_id != account.account_id:
                    if existing_account.account_id == account.account_type:
                        raise BadAccountInfo("This account type is already exists in the database")
                return self.account_dao.update_account_by_id(account)
        else:
            raise BadAccountInfo("There are no accounts to update!")

    def service_delete_account_by_id(self, account_id: int) -> bool:
        try:
            return self.account_dao.delete_account_by_id(int(account_id))
        except ValueError:
            raise BadAccountInfo("Please provide a valid account Id")

    def service_deposit_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "deposit":
            return self.account_dao.deposit_amount_by_id(value, account_id)

    def service_withdraw_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "withdraw":
            return self.account_dao.withdraw_amount_by_id(value, account_id)

    def service_transfer_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "transfer":
            return self.account_dao.transfer_amount_by_id(value, account_id)
