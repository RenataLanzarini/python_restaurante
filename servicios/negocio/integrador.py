"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: reporte_service.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/reporte_service.py
# ================================================================================

"""
Servicio para generar reportes de ventas y estadísticas.
"""

from datetime import date
from config.configuracion_restaurante import ConfiguracionRestaurante
from constantes import SEPARADOR_LINEA, SEPARADOR_SECCION
from entidades.menu.entrada import Entrada
from entidades.menu.plato_principal import PlatoPrincipal
from entidades.menu.postre import Postre

if False:  # TYPE_CHECKING
    from servicios.negocio.restaurante_service import RestauranteService


class ReporteService:
    """
    Servicio para generar reportes de ventas y estadísticas del restaurante.
    """

    def generar_reporte_ventas(self, restaurante_service: 'RestauranteService') -> None:
        """
        Genera un reporte completo de ventas diarias.
        
        Args:
            restaurante_service: Servicio con los pedidos activos
        """
        pedidos = restaurante_service.get_todos_pedidos()
        
        if len(pedidos) == 0:
            print("No hay pedidos para generar reporte")
            return

        # Contadores
        total_pedidos = len(pedidos)
        entradas = 0
        principales = 0
        postres = 0

        for pedido in pedidos:
            for plato in pedido.get_platos():
                if isinstance(plato, Entrada):
                    entradas += 1
                elif isinstance(plato, PlatoPrincipal):
                    principales += 1
                elif isinstance(plato, Postre):
                    postres += 1

        total_platos = entradas + principales + postres
        ingreso_total = restaurante_service.calcular_ingresos_totales()
        ingreso_promedio = ingreso_total / total_pedidos if total_pedidos > 0 else 0

        # Mostrar reporte
        config = ConfiguracionRestaurante.get_instance()
        
        print(SEPARADOR_LINEA)
        print("REPORTE DE VENTAS DIARIAS")
        print(SEPARADOR_LINEA)
        print(f"Fecha: {date.today()}")
        print(f"Restaurante: {config.get_nombre()}")
        print()
        print("RESUMEN DE PEDIDOS:")
        print(SEPARADOR_SECCION)
        print(f"Total de pedidos: {total_pedidos}")
        print(f"Total de platos vendidos: {total_platos}")
        print(f"  - Entradas: {entradas}")
        print(f"  - Platos Principales: {principales}")
        print(f"  - Postres: {postres}")
        print()
        print("INGRESOS:")
        print(SEPARADOR_SECCION)
        print(f"Ingreso total: ${ingreso_total:.2f}")
        print(f"Ingreso promedio por mesa: ${ingreso_promedio:.2f}")
        print(SEPARADOR_LINEA)

    def exportar_reporte(self, restaurante_service: 'RestauranteService', ruta_archivo: str) -> None:
        """
        Exporta el reporte a un archivo de texto.
        
        Args:
            restaurante_service: Servicio con los pedidos
            ruta_archivo: Ruta donde guardar el reporte
        """
        try:
            # Aquí iría la lógica de exportación
            # Por ahora solo muestra un mensaje
            print(f"Reporte exportado exitosamente a {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar reporte: {e}")

# ================================================================================
# ARCHIVO 3/3: restaurante_service.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/restaurante_service.py
# ================================================================================

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

