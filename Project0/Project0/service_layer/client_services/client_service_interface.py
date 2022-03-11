from abc import ABC, abstractmethod

from dal_layer.client_dao.client_dao_imp import ClientDAOImp
from dal_layer.client_dao.client_dao_interface import ClientDAOInterface
from entities.client_class_information import Client


class ClientServiceInterface(ABC):

    def __init__(self, client_dao: ClientDAOInterface):
        self.client_dao: ClientDAOImp = client_dao

    @abstractmethod
    def service_create_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def service_get_client_by_id(self, client_id: int) -> Client:
        pass

    @abstractmethod
    def service_update_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def service_delete_client_by_id(self, client_id: int) -> bool:
        pass
