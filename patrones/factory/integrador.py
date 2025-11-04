"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/factory
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: plato_factory.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/factory/plato_factory.py
# ================================================================================

"""
Patrón Factory Method: PlatoFactory
Centraliza la creación de diferentes tipos de platos.
"""

from constantes import TIEMPO_PREPARACION_DEFAULT, CALORIAS_DEFAULT_POSTRE


class PlatoFactory:
    """
    Factory para crear instancias de diferentes tipos de platos.
    Desacopla el código cliente de las clases concretas.
    """

    @staticmethod
    def crear_plato(tipo: str, nombre: str, precio: float, **kwargs) -> 'Plato':
        """
        Crea un plato según el tipo especificado.
        
        Args:
            tipo: Tipo de plato ("entrada", "principal", "postre")
            nombre: Nombre del plato
            precio: Precio del plato
            **kwargs: Argumentos adicionales específicos por tipo
            
        Returns:
            Plato: Instancia del tipo de plato solicitado
            
        Raises:
            ValueError: Si el tipo de plato no es válido
        """
        factories = {
            "entrada": PlatoFactory._crear_entrada,
            "principal": PlatoFactory._crear_principal,
            "postre": PlatoFactory._crear_postre
        }

        tipo_lower = tipo.lower()
        if tipo_lower not in factories:
            raise ValueError(f"Especie desconocida: {tipo}")

        return factories[tipo_lower](nombre, precio, **kwargs)

    @staticmethod
    def _crear_entrada(nombre: str, precio: float, **kwargs) -> 'Entrada':
        """
        Crea una entrada.
        
        Args:
            nombre: Nombre de la entrada
            precio: Precio de la entrada
            **kwargs: Debe incluir 'ingredientes'
            
        Returns:
            Entrada: Nueva instancia de Entrada
        """
        from entidades.menu.entrada import Entrada
        ingredientes = kwargs.get('ingredientes', 'ingredientes variados')
        return Entrada(nombre, precio, ingredientes)

    @staticmethod
    def _crear_principal(nombre: str, precio: float, **kwargs) -> 'PlatoPrincipal':
        """
        Crea un plato principal.
        
        Args:
            nombre: Nombre del plato principal
            precio: Precio del plato principal
            **kwargs: Puede incluir 'tiempo_preparacion'
            
        Returns:
            PlatoPrincipal: Nueva instancia de PlatoPrincipal
        """
        from entidades.menu.plato_principal import PlatoPrincipal
        tiempo_prep = kwargs.get('tiempo_preparacion', TIEMPO_PREPARACION_DEFAULT)
        return PlatoPrincipal(nombre, precio, tiempo_prep)

    @staticmethod
    def _crear_postre(nombre: str, precio: float, **kwargs) -> 'Postre':
        """
        Crea un postre.
        
        Args:
            nombre: Nombre del postre
            precio: Precio del postre
            **kwargs: Puede incluir 'calorias'
            
        Returns:
            Postre: Nueva instancia de Postre
        """
        from entidades.menu.postre import Postre
        calorias = kwargs.get('calorias', CALORIAS_DEFAULT_POSTRE)
        return Postre(nombre, precio, calorias)

