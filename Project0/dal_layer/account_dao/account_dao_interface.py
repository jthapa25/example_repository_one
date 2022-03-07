from abc import ABC, abstractmethod

from entities.account_class_information import Account


class AccountDAOInterface(ABC):
    # create
    @abstractmethod
    def create_account(self, account: Account):
        pass

    # read
    @abstractmethod
    def get_account_by_id(self, account_id: int):
        pass

    # update
    @abstractmethod
    def update_account_by_id(self, account: Account):
        pass

    # delete
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
