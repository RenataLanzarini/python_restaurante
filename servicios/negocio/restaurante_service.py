"""
Servicio para gestionar múltiples mesas del restaurante.
"""

from typing import Dict, List, Optional

if False:  # TYPE_CHECKING
    from entidades.pedido.pedido_mesa import PedidoMesa


class RestauranteService:
    """
    Servicio centralizado para gestionar todos los pedidos activos del restaurante.
    """

    def __init__(self):
        """Inicializa el servicio con diccionario vacío de pedidos."""
        self._pedidos: Dict[int, 'PedidoMesa'] = {}

    def agregar_pedido(self, pedido: 'PedidoMesa') -> None:
        """
        Agrega un pedido al sistema.
        
        Args:
            pedido: Pedido a agregar
            
        Raises:
            ValueError: Si ya existe un pedido para esa mesa
        """
        numero_mesa = pedido.get_numero_mesa()
        
        if numero_mesa in self._pedidos:
            raise ValueError(
                f"Ya existe un pedido activo para la Mesa {numero_mesa}"
            )
        
        self._pedidos[numero_mesa] = pedido
        print(f"Pedido de Mesa {numero_mesa} agregado al sistema")

    def buscar_pedido(self, numero_mesa: int) -> Optional['PedidoMesa']:
        """
        Busca un pedido por número de mesa.
        
        Args:
            numero_mesa: Número de mesa a buscar
            
        Returns:
            PedidoMesa o None: Pedido encontrado o None si no existe
        """
        return self._pedidos.get(numero_mesa)

    def listar_mesas_activas(self) -> List[int]:
        """
        Lista todos los números de mesa con pedidos activos.
        
        Returns:
            List[int]: Lista ordenada de números de mesa activas
        """
        return sorted(self._pedidos.keys())

    def calcular_ingresos_totales(self) -> float:
        """
        Calcula los ingresos totales de todos los pedidos activos.
        
        Returns:
            float: Suma de todos los pedidos
        """
        return sum(pedido.calcular_total() for pedido in self._pedidos.values())

    def cerrar_mesa(self, numero_mesa: int) -> None:
        """
        Cierra una mesa eliminando su pedido del sistema.
        
        Args:
            numero_mesa: Número de mesa a cerrar
        """
        if numero_mesa in self._pedidos:
            del self._pedidos[numero_mesa]
            print(f"Mesa {numero_mesa} cerrada")
        else:
            print(f"Mesa {numero_mesa} no encontrada")

    def get_cantidad_pedidos(self) -> int:
        """
        Retorna la cantidad de pedidos activos.
        
        Returns:
            int: Cantidad de pedidos
        """
        return len(self._pedidos)

    def get_todos_pedidos(self) -> List['PedidoMesa']:
        """
        Retorna una lista con todos los pedidos activos.
        
        Returns:
            List[PedidoMesa]: Lista de pedidos
        """
        return list(self._pedidos.values())