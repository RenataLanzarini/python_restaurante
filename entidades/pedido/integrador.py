"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/pedido
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/pedido/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: pedido_mesa.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/pedido/pedido_mesa.py
# ================================================================================

"""
Clase que representa un pedido de una mesa.
Contexto del patrón Strategy para formas de pago.
"""

from typing import List, Optional

if False:  # TYPE_CHECKING
    from entidades.menu.plato import Plato
    from patrones.strategy.estrategia_pago import EstrategiaPago


class PedidoMesa:
    """
    Representa el pedido de una mesa con sus platos y forma de pago.
    Actúa como Context en el patrón Strategy.
    """

    def __init__(self, numero_mesa: int):
        """
        Inicializa un pedido para una mesa.
        
        Args:
            numero_mesa: Número de la mesa (debe ser positivo)
            
        Raises:
            ValueError: Si el número de mesa es menor o igual a cero
        """
        if numero_mesa <= 0:
            raise ValueError("El número de mesa debe ser mayor a cero")
        
        self._numero_mesa = numero_mesa
        self._platos: List['Plato'] = []
        self._estrategia_pago: Optional['EstrategiaPago'] = None

    def agregar_plato(self, plato: 'Plato') -> None:
        """
        Agrega un plato al pedido.
        
        Args:
            plato: Plato a agregar
        """
        self._platos.append(plato)

    def calcular_total(self) -> float:
        """
        Calcula el total del pedido sumando precios de todos los platos.
        
        Returns:
            float: Total del pedido
        """
        return sum(plato.get_precio() for plato in self._platos)

    def get_platos(self) -> List['Plato']:
        """
        Retorna una copia de la lista de platos (defensive copy).
        
        Returns:
            List[Plato]: Copia de la lista de platos
        """
        return self._platos.copy()

    def esta_vacio(self) -> bool:
        """
        Verifica si el pedido está vacío.
        
        Returns:
            bool: True si no tiene platos, False en caso contrario
        """
        return len(self._platos) == 0

    def get_numero_mesa(self) -> int:
        """Retorna el número de mesa del pedido."""
        return self._numero_mesa

    def set_estrategia_pago(self, estrategia: 'EstrategiaPago') -> None:
        """
        Establece la estrategia de pago (patrón Strategy).
        
        Args:
            estrategia: Estrategia de pago a utilizar
        """
        self._estrategia_pago = estrategia

    def get_estrategia_pago(self) -> Optional['EstrategiaPago']:
        """
        Retorna la estrategia de pago actual.
        
        Returns:
            EstrategiaPago o None: Estrategia actual o None si no está definida
        """
        return self._estrategia_pago

    def tiene_estrategia_pago(self) -> bool:
        """
        Verifica si el pedido tiene una estrategia de pago asignada.
        
        Returns:
            bool: True si tiene estrategia, False en caso contrario
        """
        return self._estrategia_pago is not None

