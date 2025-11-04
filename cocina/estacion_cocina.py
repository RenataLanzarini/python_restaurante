"""
Clase que representa una estación de cocina (Observer concreto).
"""

from patrones.observer.observer import Observer
from typing import Dict


class EstacionCocina(Observer[Dict]):
    """
    Representa una estación de cocina que observa el sistema de pedidos.
    Recibe notificaciones cuando hay nuevos pedidos.
    """

    def __init__(self, nombre: str):
        """
        Inicializa una estación de cocina.
        
        Args:
            nombre: Nombre de la estación (ej: "Parrilla", "Ensaladas")
        """
        self._nombre = nombre

    def actualizar(self, evento: Dict) -> None:
        """
        Recibe notificación de nuevo pedido.
        
        Args:
            evento: Diccionario con datos del pedido
                   Contiene: 'mesa', 'plato', 'cantidad'
        """
        print(f"[{self._nombre.upper()}] Nuevo pedido recibido:")
        print(f"  Mesa: {evento.get('mesa', 'N/A')}")
        print(f"  Plato: {evento.get('plato', 'N/A')}")
        print(f"  Cantidad: {evento.get('cantidad', 0)}")

    def get_nombre(self) -> str:
        """Retorna el nombre de la estación."""
        return self._nombre