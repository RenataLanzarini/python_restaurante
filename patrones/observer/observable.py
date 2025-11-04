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