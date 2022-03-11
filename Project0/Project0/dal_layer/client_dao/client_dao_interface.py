from abc import ABC, abstractmethod

from entities.client_class_information import Client


class ClientDAOInterface(ABC):

    # Create
    @abstractmethod
    def create_client(self, client: Client) -> Client:
        pass

    # Read
    @abstractmethod
    def get_client_by_id(self, client_id: int) -> Client:
        pass

    # update
    @abstractmethod
    def update_client_by_id(self, client: Client) -> Client:
        pass

    # delete

    @abstractmethod
    def delete_client_by_id(self, client_id: int) -> Client:
        pass
