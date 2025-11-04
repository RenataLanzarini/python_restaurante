"""
Patrón Singleton: ConfiguracionRestaurante
Garantiza una única instancia de configuración del sistema.
"""

from threading import Lock
from typing import Optional


class ConfiguracionRestaurante:
    """
    Configuración global del restaurante (Singleton).
    Mantiene datos como nombre, dirección, horarios, etc.
    Thread-safe mediante double-checked locking.
    """

    _instance: Optional['ConfiguracionRestaurante'] = None
    _lock: Lock = Lock()

    def __new__(cls) -> 'ConfiguracionRestaurante':
        """
        Controla la instanciación para garantizar singleton.
        
        Returns:
            ConfiguracionRestaurante: La única instancia del sistema
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance

    def _inicializar(self) -> None:
        """Inicializa los valores por defecto de la configuración."""
        self._nombre: str = "Mi Restaurante"
        self._direccion: str = ""
        self._telefono: str = ""
        self._horario_apertura: str = "09:00"
        self._horario_cierre: str = "22:00"
        self._capacidad_mesas: int = 10
        self._cbu: str = "9876543210987654321098"

    @classmethod
    def get_instance(cls) -> 'ConfiguracionRestaurante':
        """
        Obtiene la instancia única de configuración.
        
        Returns:
            ConfiguracionRestaurante: Instancia única
        """
        if cls._instance is None:
            cls()
        return cls._instance

    # ========================================================================
    # GETTERS
    # ========================================================================

    def get_nombre(self) -> str:
        """Retorna el nombre del restaurante."""
        return self._nombre

    def get_direccion(self) -> str:
        """Retorna la dirección del restaurante."""
        return self._direccion

    def get_telefono(self) -> str:
        """Retorna el teléfono del restaurante."""
        return self._telefono

    def get_horario_apertura(self) -> str:
        """Retorna el horario de apertura."""
        return self._horario_apertura

    def get_horario_cierre(self) -> str:
        """Retorna el horario de cierre."""
        return self._horario_cierre

    def get_capacidad_mesas(self) -> int:
        """Retorna la capacidad de mesas del restaurante."""
        return self._capacidad_mesas

    def get_cbu(self) -> str:
        """Retorna el CBU del restaurante para transferencias."""
        return self._cbu

    # ========================================================================
    # SETTERS
    # ========================================================================

    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre del restaurante."""
        self._nombre = nombre

    def set_direccion(self, direccion: str) -> None:
        """Establece la dirección del restaurante."""
        self._direccion = direccion

    def set_telefono(self, telefono: str) -> None:
        """Establece el teléfono del restaurante."""
        self._telefono = telefono

    def set_horario_apertura(self, horario: str) -> None:
        """Establece el horario de apertura."""
        self._horario_apertura = horario

    def set_horario_cierre(self, horario: str) -> None:
        """Establece el horario de cierre."""
        self._horario_cierre = horario

    def set_capacidad_mesas(self, capacidad: int) -> None:
        """
        Establece la capacidad de mesas.
        
        Args:
            capacidad: Número de mesas (debe ser positivo)
            
        Raises:
            ValueError: Si la capacidad es menor o igual a cero
        """
        if capacidad <= 0:
            raise ValueError("La capacidad de mesas debe ser mayor a cero")
        self._capacidad_mesas = capacidad

    def set_cbu(self, cbu: str) -> None:
        """Establece el CBU del restaurante."""
        self._cbu = cbu

    def mostrar_configuracion(self) -> None:
        """Muestra la configuración actual del restaurante."""
        print("═══════════════════════════════════")
        print("CONFIGURACIÓN DEL RESTAURANTE")
        print("═══════════════════════════════════")
        print(f"Nombre: {self._nombre}")
        print(f"Dirección: {self._direccion}")
        print(f"Teléfono: {self._telefono}")
        print(f"Horario: {self._horario_apertura} - {self._horario_cierre}")
        print(f"Capacidad: {self._capacidad_mesas} mesas")
        print(f"CBU: {self._cbu}")
        print("═══════════════════════════════════")