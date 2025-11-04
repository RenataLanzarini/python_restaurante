"""
Clase concreta que representa una entrada del menú.
"""

from entidades.menu.plato import Plato


class Entrada(Plato):
    """
    Representa una entrada del menú con sus ingredientes principales.
    """

    def __init__(self, nombre: str, precio: float, ingredientes: str):
        """
        Inicializa una entrada.
        
        Args:
            nombre: Nombre de la entrada
            precio: Precio de la entrada
            ingredientes: Ingredientes principales
        """
        super().__init__(nombre, precio)
        self._ingredientes = ingredientes

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos de la entrada."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Entrada")
        print(f"Ingredientes: {self._ingredientes}")
        print(f"Precio: ${self._precio:.2f}")

    def get_ingredientes(self) -> str:
        """Retorna los ingredientes de la entrada."""
        return self._ingredientes

    def set_ingredientes(self, ingredientes: str) -> None:
        """Establece los ingredientes de la entrada."""
        self._ingredientes = ingredientes