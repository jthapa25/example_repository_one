from custom_exceptions.bad_account_info import BadAccountInfo
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface):

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_id) != str:
            raise BadAccountInfo("Please pass a valid account number")
        for existing_account in self.account_dao_account_list:
            if existing_account.account_id == account.account_id:
                raise BadAccountInfo("This account id is already exists in the database")


def service_get_account_by_id(self, account_id: int) -> Account:
    if type(account_id) == int:
        return self.account_dao_get_account_by_id(account_id)
    else:
        raise BadAccountInfo("please provide a valid account id")


def service_update_account_by_id(self, account: Account) -> Account:
    pass


def service_delete_account_by_id(self, account_id: int) -> bool:
    pass
