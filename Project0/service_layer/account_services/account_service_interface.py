from abc import ABC, abstractmethod

from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account


class AccountServiceInterface(ABC):
    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao = account_dao

    # create
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # read
    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    # update
    @abstractmethod
    def service_update_account_by_id(self, account: Account) -> Account:
        pass

    # delete
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
