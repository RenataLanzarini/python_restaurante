"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/persistencia
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/persistencia/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: persistencia_service.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/persistencia/persistencia_service.py
# ================================================================================

"""
Servicio para persistir y recuperar pedidos en disco.
"""

import pickle
import os
from datetime import datetime
from constantes import DIRECTORIO_PEDIDOS, PREFIJO_ARCHIVO_PEDIDO, EXTENSION_DATA
from excepciones.persistencia_exception import PersistenciaException

if False:  # TYPE_CHECKING
    from entidades.pedido.pedido_mesa import PedidoMesa


class PersistenciaService:
    """
    Servicio para operaciones de persistencia con Pickle.
    """

    def guardar_pedido(self, pedido: 'PedidoMesa') -> None:
        """
        Guarda un pedido en disco usando Pickle.
        
        Args:
            pedido: Pedido a guardar
            
        Raises:
            PersistenciaException: Si ocurre un error al guardar
        """
        nombre_archivo = ""
        try:
            # Crear directorio si no existe
            os.makedirs(DIRECTORIO_PEDIDOS, exist_ok=True)

            # Generar nombre de archivo
            timestamp = int(datetime.now().timestamp())
            numero_mesa = pedido.get_numero_mesa()
            nombre_archivo = f"{PREFIJO_ARCHIVO_PEDIDO}{numero_mesa}_{timestamp}{EXTENSION_DATA}"
            ruta_completa = os.path.join(DIRECTORIO_PEDIDOS, nombre_archivo)

            # Serializar y guardar
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(pedido, archivo)

            print(f"Pedido de Mesa {numero_mesa} persistido exitosamente en {ruta_completa}")

        except Exception as e:
            raise PersistenciaException(
                mensaje="Error al guardar pedido",
                nombre_archivo=nombre_archivo,
                tipo_operacion="ESCRITURA",
                causa=str(e)
            )

    def cargar_pedido(self, nombre_archivo: str) -> 'PedidoMesa':
        """
        Carga un pedido desde disco.
        
        Args:
            nombre_archivo: Nombre del archivo a cargar
            
        Returns:
            PedidoMesa: Pedido recuperado
            
        Raises:
            PersistenciaException: Si ocurre un error al cargar
        """
        ruta_completa = os.path.join(DIRECTORIO_PEDIDOS, nombre_archivo)

        try:
            if not os.path.exists(ruta_completa):
                raise FileNotFoundError(f"Archivo no encontrado: {ruta_completa}")

            with open(ruta_completa, 'rb') as archivo:
                pedido = pickle.load(archivo)

            print(f"Pedido recuperado exitosamente desde {ruta_completa}")
            return pedido

        except FileNotFoundError as e:
            raise PersistenciaException(
                mensaje="Archivo de pedido no encontrado",
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA",
                causa=str(e)
            )
        except Exception as e:
            raise PersistenciaException(
                mensaje="Error al cargar pedido",
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA",
                causa=str(e)
            )

    def listar_pedidos_guardados(self) -> list:
        """
        Lista todos los archivos de pedidos guardados.
        
        Returns:
            list: Lista de nombres de archivos ordenados por fecha (más recientes primero)
        """
        if not os.path.exists(DIRECTORIO_PEDIDOS):
            return []

        archivos = [
            f for f in os.listdir(DIRECTORIO_PEDIDOS)
            if f.endswith(EXTENSION_DATA)
        ]

        # Ordenar por timestamp (más recientes primero)
        archivos.sort(reverse=True)

        return archivos

