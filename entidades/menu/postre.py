"""
Clase concreta que representa un postre del menú.
"""

from entidades.menu.plato import Plato


class Postre(Plato):
    """
    Representa un postre del menú con información calórica.
    """

    def __init__(self, nombre: str, precio: float, calorias: int):
        """
        Inicializa un postre.
        
        Args:
            nombre: Nombre del postre
            precio: Precio del postre
            calorias: Calorías del postre
            
        Raises:
            ValueError: Si las calorías son negativas
        """
        super().__init__(nombre, precio)
        if calorias < 0:
            raise ValueError("Las calorías no pueden ser negativas")
        self._calorias = calorias

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos del postre."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Postre")
        print(f"Calorías: {self._calorias} kcal")
        print(f"Precio: ${self._precio:.2f}")

    def get_calorias(self) -> int:
        """Retorna las calorías del postre."""
        return self._calorias

    def set_calorias(self, calorias: int) -> None:
        """
        Establece las calorías del postre.
        
        Args:
            calorias: Cantidad de calorías (debe ser positivo)
            
        Raises:
            ValueError: Si las calorías son negativas
        """
        if calorias < 0:
            raise ValueError("Las calorías no pueden ser negativas")
        self._calorias = calorias