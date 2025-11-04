"""
Clase que representa el sistema de pedidos (Observable concreto).
"""

from patrones.observer.observable import Observable
from typing import Dict
from constantes import SEPARADOR_LINEA


class SistemaPedidos(Observable[Dict]):
    """
    Sistema centralizado de pedidos que notifica a las estaciones de cocina.
    Actúa como Observable en el patrón Observer.
    """

    def __init__(self):
        """Inicializa el sistema de pedidos."""
        super().__init__()

    def notificar_pedido(self, numero_mesa: int, plato: str, cantidad: int) -> None:
        """
        Notifica un nuevo pedido a todas las estaciones suscritas.
        
        Args:
            numero_mesa: Número de mesa que realizó el pedido
            plato: Nombre del plato pedido
            cantidad: Cantidad de platos
        """
        print(SEPARADOR_LINEA)
        print(f"Notificando pedido a {self.get_cantidad_observadores()} estaciones")
        print(SEPARADOR_LINEA)

        pedido = {
            'mesa': numero_mesa,
            'plato': plato,
            'cantidad': cantidad
        }

        self.notificar_observadores(pedido)