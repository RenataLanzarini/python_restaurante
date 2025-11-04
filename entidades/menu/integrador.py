"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: entrada.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/entrada.py
# ================================================================================

"""
Clase concreta que representa una entrada del menú.
"""

from entidades.menu.plato import Plato


class Entrada(Plato):
    """
    Representa una entrada del menú con sus ingredientes principales.
    """

    def __init__(self, nombre: str, precio: float, ingredientes: str):
        """
        Inicializa una entrada.
        
        Args:
            nombre: Nombre de la entrada
            precio: Precio de la entrada
            ingredientes: Ingredientes principales
        """
        super().__init__(nombre, precio)
        self._ingredientes = ingredientes

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos de la entrada."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Entrada")
        print(f"Ingredientes: {self._ingredientes}")
        print(f"Precio: ${self._precio:.2f}")

    def get_ingredientes(self) -> str:
        """Retorna los ingredientes de la entrada."""
        return self._ingredientes

    def set_ingredientes(self, ingredientes: str) -> None:
        """Establece los ingredientes de la entrada."""
        self._ingredientes = ingredientes

# ================================================================================
# ARCHIVO 3/5: plato.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/plato.py
# ================================================================================

"""
Clase abstracta base para todos los platos del menú.
"""

from abc import ABC, abstractmethod


class Plato(ABC):
    """
    Clase abstracta que representa un plato genérico del menú.
    Todos los tipos de platos deben heredar de esta clase.
    """

    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un plato.
        
        Args:
            nombre: Nombre del plato
            precio: Precio del plato (debe ser positivo)
            
        Raises:
            ValueError: Si el precio es negativo o cero
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrar_detalle(self) -> None:
        """
        Muestra los detalles específicos del plato.
        Cada tipo de plato debe implementar su propia versión.
        """
        pass

    def get_nombre(self) -> str:
        """Retorna el nombre del plato."""
        return self._nombre

    def get_precio(self) -> float:
        """Retorna el precio del plato."""
        return self._precio

    def set_precio(self, precio: float) -> None:
        """
        Establece un nuevo precio para el plato.
        
        Args:
            precio: Nuevo precio (debe ser positivo)
            
        Raises:
            ValueError: Si el precio es negativo o cero
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio = precio

# ================================================================================
# ARCHIVO 4/5: plato_principal.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/plato_principal.py
# ================================================================================

"""
Clase concreta que representa un plato principal del menú.
"""

from entidades.menu.plato import Plato


class PlatoPrincipal(Plato):
    """
    Representa un plato principal del menú con tiempo de preparación.
    """

    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int):
        """
        Inicializa un plato principal.
        
        Args:
            nombre: Nombre del plato principal
            precio: Precio del plato principal
            tiempo_preparacion: Tiempo de preparación en minutos
            
        Raises:
            ValueError: Si el tiempo de preparación es negativo
        """
        super().__init__(nombre, precio)
        if tiempo_preparacion < 0:
            raise ValueError("El tiempo de preparación no puede ser negativo")
        self._tiempo_preparacion = tiempo_preparacion

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos del plato principal."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Plato Principal")
        print(f"Tiempo de preparación: {self._tiempo_preparacion} min")
        print(f"Precio: ${self._precio:.2f}")

    def get_tiempo_preparacion(self) -> int:
        """Retorna el tiempo de preparación en minutos."""
        return self._tiempo_preparacion

    def set_tiempo_preparacion(self, tiempo: int) -> None:
        """
        Establece el tiempo de preparación.
        
        Args:
            tiempo: Tiempo en minutos (debe ser positivo)
            
        Raises:
            ValueError: Si el tiempo es negativo
        """
        if tiempo < 0:
            raise ValueError("El tiempo de preparación no puede ser negativo")
        self._tiempo_preparacion = tiempo

# ================================================================================
# ARCHIVO 5/5: postre.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/postre.py
# ================================================================================

"""
Clase concreta que representa un postre del menú.
"""

from entidades.menu.plato import Plato


class Postre(Plato):
    """
    Representa un postre del menú con información calórica.
    """

    def __init__(self, nombre: str, precio: float, calorias: int):
        """
        Inicializa un postre.
        
        Args:
            nombre: Nombre del postre
            precio: Precio del postre
            calorias: Calorías del postre
            
        Raises:
            ValueError: Si las calorías son negativas
        """
        super().__init__(nombre, precio)
        if calorias < 0:
            raise ValueError("Las calorías no pueden ser negativas")
        self._calorias = calorias

    def mostrar_detalle(self) -> None:
        """Muestra los detalles específicos del postre."""
        print(f"Plato: {self._nombre}")
        print(f"Tipo: Postre")
        print(f"Calorías: {self._calorias} kcal")
        print(f"Precio: ${self._precio:.2f}")

    def get_calorias(self) -> int:
        """Retorna las calorías del postre."""
        return self._calorias

    def set_calorias(self, calorias: int) -> None:
        """
        Establece las calorías del postre.
        
        Args:
            calorias: Cantidad de calorías (debe ser positivo)
            
        Raises:
            ValueError: Si las calorías son negativas
        """
        if calorias < 0:
            raise ValueError("Las calorías no pueden ser negativas")
        self._calorias = calorias

