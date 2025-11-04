"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./excepciones
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: persistencia_exception.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./excepciones/persistencia_exception.py
# ================================================================================

"""
Excepción personalizada para errores de persistencia.
"""


class PersistenciaException(Exception):
    """
    Excepción lanzada cuando ocurre un error durante operaciones de persistencia.
    """

    def __init__(self, mensaje: str, nombre_archivo: str, 
                 tipo_operacion: str, causa: str):
        """
        Inicializa la excepción.
        
        Args:
            mensaje: Mensaje descriptivo del error
            nombre_archivo: Nombre del archivo involucrado
            tipo_operacion: Tipo de operación (LECTURA/ESCRITURA)
            causa: Causa subyacente del error
        """
        self._mensaje = mensaje
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
        self._causa = causa
        super().__init__(self.get_mensaje_completo())

    def get_mensaje_completo(self) -> str:
        """
        Genera el mensaje completo del error.
        
        Returns:
            str: Mensaje formateado con todos los detalles
        """
        return (
            f"{self._mensaje}\n"
            f"Archivo: {self._nombre_archivo}\n"
            f"Operación: {self._tipo_operacion}\n"
            f"Causa: {self._causa}"
        )

    def get_mensaje(self) -> str:
        """Retorna el mensaje básico del error."""
        return self._mensaje

    def get_nombre_archivo(self) -> str:
        """Retorna el nombre del archivo."""
        return self._nombre_archivo

    def get_tipo_operacion(self) -> str:
        """Retorna el tipo de operación."""
        return self._tipo_operacion

    def get_causa(self) -> str:
        """Retorna la causa del error."""
        return self._causa

