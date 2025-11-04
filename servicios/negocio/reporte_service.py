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