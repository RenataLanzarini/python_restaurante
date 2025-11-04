"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./cocina
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: estacion_cocina.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/estacion_cocina.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: sistema_pedidos.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/sistema_pedidos.py
# ================================================================================

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

