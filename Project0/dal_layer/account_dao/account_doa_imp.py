from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account


class AccountDAOImp(AccountDAOInterface):

    def __init__(self):
        account_needed_for_id_catch = Account(1, 1000.00, 2)
        self.account_List.append(account_needed_for_id_catch)
        self.account_List = []
        self.id_generator = 2

    def create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.id_generator += 1
        self.account_List.append(account)
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_List:
            if account.account_id == account_id:
                return account
        raise IdNotFound("No bank matches the id given: please try again!")

    def update_account_by_id(self, account: Account):
        for old_account in self.account_List:
            if account.account_id == old_account.account_id:
                old_account = account
                return old_account
        raise IdNotFound("No bank matches id given: please try again!")

    def delete_account_by_id(self, account_id: int):
        for account in self.account_List:
            if account.account_id == account_id:
                self.account_List.remove(account)
                return True
        raise IdNotFound("Np bank matches the id given: please try again!")
