"""
Patrón Observer: Interfaz Observer
Define el contrato para objetos que observan cambios.
"""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz genérica para observadores.
    Los observadores reciben notificaciones cuando el Observable cambia.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el Observable notifica un cambio.
        
        Args:
            evento: Datos del evento (tipo genérico T)
        """
        pass