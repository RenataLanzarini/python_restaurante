"""
Clase abstracta base para todos los platos del menú.
"""

from abc import ABC, abstractmethod


class Plato(ABC):
    """
    Clase abstracta que representa un plato genérico del menú.
    Todos los tipos de platos deben heredar de esta clase.
    """

    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un plato.
        
        Args:
            nombre: Nombre del plato
            precio: Precio del plato (debe ser positivo)
            
        Raises:
            ValueError: Si el precio es negativo o cero
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrar_detalle(self) -> None:
        """
        Muestra los detalles específicos del plato.
        Cada tipo de plato debe implementar su propia versión.
        """
        pass

    def get_nombre(self) -> str:
        """Retorna el nombre del plato."""
        return self._nombre

    def get_precio(self) -> float:
        """Retorna el precio del plato."""
        return self._precio

    def set_precio(self, precio: float) -> None:
        """
        Establece un nuevo precio para el plato.
        
        Args:
            precio: Nuevo precio (debe ser positivo)
            
        Raises:
            ValueError: Si el precio es negativo o cero
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio = precio