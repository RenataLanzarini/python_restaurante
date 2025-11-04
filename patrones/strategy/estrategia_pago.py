"""
Patrón Strategy: Interfaz EstrategiaPago
Define el contrato para diferentes formas de pago.
"""

from abc import ABC, abstractmethod


class EstrategiaPago(ABC):
    """
    Interfaz abstracta para estrategias de pago.
    Cada forma de pago implementa esta interfaz con su lógica específica.
    """

    @abstractmethod
    def procesar_pago(self, monto: float) -> None:
        """
        Procesa el pago según la estrategia específica.
        
        Args:
            monto: Monto total a pagar
        """
        pass

    @abstractmethod
    def get_nombre(self) -> str:
        """
        Retorna el nombre descriptivo de la forma de pago.
        
        Returns:
            str: Nombre de la forma de pago
        """
        pass