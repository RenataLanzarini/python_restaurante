"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/observable.py
# ================================================================================

"""
Patrón Observer: Clase Observable
Define el objeto que puede ser observado.
"""

from typing import Generic, TypeVar, List
from abc import ABC

if False:  # TYPE_CHECKING
    from patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase genérica para objetos observables.
    Mantiene una lista de observadores y los notifica cuando hay cambios.
    """

    def __init__(self):
        """Inicializa la lista de observadores."""
        self._observadores: List['Observer[T]'] = []

    def agregar_observador(self, observador: 'Observer[T]') -> None:
        """
        Agrega un observador a la lista.
        
        Args:
            observador: Observer a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        """
        Elimina un observador de la lista.
        
        Args:
            observador: Observer a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores con el evento.
        
        Args:
            evento: Datos del evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

    def get_cantidad_observadores(self) -> int:
        """Retorna la cantidad de observadores suscritos."""
        return len(self._observadores)

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/observer.py
# ================================================================================

"""
Patrón Observer: Interfaz Observer
Define el contrato para objetos que observan cambios.
"""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz genérica para observadores.
    Los observadores reciben notificaciones cuando el Observable cambia.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el Observable notifica un cambio.
        
        Args:
            evento: Datos del evento (tipo genérico T)
        """
        pass

