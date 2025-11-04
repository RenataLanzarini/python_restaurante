"""
Clase concreta que representa un plato principal del menú.
"""

from entidades.menu.plato import Plato


class PlatoPrincipal(Plato):
    """
    Representa un plato principal del menú con tiempo de preparación.
    """

    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int):
        """
        Inicializa un plato principal.
        
        Args:
            nombre: Nombre del plato principal
            precio: Precio del plato principal
            tiempo_preparacion: Tiempo de preparación en minutos
            
        Raises:
            ValueError: Si el tiempo de preparación es negativo
        """
        super().__init__(nombre, precio)
        if tiempo_preparacion < 0:
            raise ValueError("El tiempo de preparación no puede ser negativo")
        self._tiempo_preparacion = tiempo_preparacion

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos del plato principal."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Plato Principal")
        print(f"Tiempo de preparación: {self._tiempo_preparacion} min")
        print(f"Precio: ${self._precio:.2f}")

    def get_tiempo_preparacion(self) -> int:
        """Retorna el tiempo de preparación en minutos."""
        return self._tiempo_preparacion

    def set_tiempo_preparacion(self, tiempo: int) -> None:
        """
        Establece el tiempo de preparación.
        
        Args:
            tiempo: Tiempo en minutos (debe ser positivo)
            
        Raises:
            ValueError: Si el tiempo es negativo
        """
        if tiempo < 0:
            raise ValueError("El tiempo de preparación no puede ser negativo")
        self._tiempo_preparacion = tiempo