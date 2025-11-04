"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: estrategia_pago.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/estrategia_pago.py
# ================================================================================

"""
Patrón Strategy: Interfaz EstrategiaPago
Define el contrato para diferentes formas de pago.
"""

from abc import ABC, abstractmethod


class EstrategiaPago(ABC):
    """
    Interfaz abstracta para estrategias de pago.
    Cada forma de pago implementa esta interfaz con su lógica específica.
    """

    @abstractmethod
    def procesar_pago(self, monto: float) -> None:
        """
        Procesa el pago según la estrategia específica.
        
        Args:
            monto: Monto total a pagar
        """
        pass

    @abstractmethod
    def get_nombre(self) -> str:
        """
        Retorna el nombre descriptivo de la forma de pago.
        
        Returns:
            str: Nombre de la forma de pago
        """
        pass

# ================================================================================
# ARCHIVO 3/5: pago_efectivo.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_efectivo.py
# ================================================================================

"""
Estrategia concreta: Pago en Efectivo con Descuento
"""

from patrones.strategy.estrategia_pago import EstrategiaPago
from constantes import SEPARADOR_LINEA, DESCUENTO_EFECTIVO


class PagoEfectivo(EstrategiaPago):
    """
    Estrategia de pago en efectivo.
    Aplica descuento automático del 10%.
    """

    def __init__(self):
        """Inicializa la estrategia de pago en efectivo."""
        pass

    def procesar_pago(self, monto: float) -> None:
        """
        Procesa el pago en efectivo aplicando descuento.
        
        Args:
            monto: Monto original a pagar
        """
        descuento = monto * DESCUENTO_EFECTIVO
        monto_final = monto - descuento

        print(SEPARADOR_LINEA)
        print("PROCESANDO PAGO EN EFECTIVO")
        print(SEPARADOR_LINEA)
        print(f"Monto original: ${monto:.2f}")
        print(f"Descuento por pago en efectivo: ${descuento:.2f}")
        print(f"Total a pagar: ${monto_final:.2f}")
        print("¡Pago procesado exitosamente!")

    def get_nombre(self) -> str:
        """Retorna el nombre de la forma de pago."""
        return "Efectivo"

    def calcular_descuento(self, monto: float) -> float:
        """
        Calcula el descuento a aplicar.
        
        Args:
            monto: Monto original
            
        Returns:
            float: Monto del descuento
        """
        return monto * DESCUENTO_EFECTIVO

    def calcular_monto_final(self, monto: float) -> float:
        """
        Calcula el monto final después del descuento.
        
        Args:
            monto: Monto original
            
        Returns:
            float: Monto final con descuento aplicado
        """
        return monto * (1 - DESCUENTO_EFECTIVO)

# ================================================================================
# ARCHIVO 4/5: pago_tarjeta.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_tarjeta.py
# ================================================================================

"""
Estrategia concreta: Pago con Tarjeta de Crédito/Débito
"""

from patrones.strategy.estrategia_pago import EstrategiaPago
from constantes import SEPARADOR_LINEA, CUOTAS_PERMITIDAS


class PagoTarjeta(EstrategiaPago):
    """
    Estrategia de pago con tarjeta de crédito/débito.
    Permite pagar en cuotas.
    """

    def __init__(self, numero_tarjeta: str, cuotas: int):
        """
        Inicializa la estrategia de pago con tarjeta.
        
        Args:
            numero_tarjeta: Número de tarjeta (se mostrarán solo últimos 4 dígitos)
            cuotas: Cantidad de cuotas (debe estar en CUOTAS_PERMITIDAS)
            
        Raises:
            ValueError: Si las cuotas no son válidas
        """
        if cuotas not in CUOTAS_PERMITIDAS:
            raise ValueError(
                f"Cuotas inválidas. Valores permitidos: {CUOTAS_PERMITIDAS}"
            )
        self._numero_tarjeta = numero_tarjeta
        self._cuotas = cuotas

    def procesar_pago(self, monto: float) -> None:
        """
        Procesa el pago con tarjeta mostrando detalles y cuotas.
        
        Args:
            monto: Monto total a pagar
        """
        ultimos_digitos = self._numero_tarjeta[-4:]
        monto_cuota = monto / self._cuotas

        print(SEPARADOR_LINEA)
        print("PROCESANDO PAGO CON TARJETA")
        print(SEPARADOR_LINEA)
        print(f"Tarjeta terminada en: {ultimos_digitos}")
        print(f"Monto: ${monto:.2f}")
        print(f"Cuotas: {self._cuotas}")
        print(f"Monto por cuota: ${monto_cuota:.2f}")
        print("¡Pago procesado exitosamente!")

    def get_nombre(self) -> str:
        """Retorna el nombre de la forma de pago."""
        return "Tarjeta de Crédito/Débito"

    def get_numero_tarjeta(self) -> str:
        """Retorna el número de tarjeta (completo)."""
        return self._numero_tarjeta

    def get_cuotas(self) -> int:
        """Retorna la cantidad de cuotas."""
        return self._cuotas

# ================================================================================
# ARCHIVO 5/5: pago_transferencia.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_transferencia.py
# ================================================================================

"""
Estrategia concreta: Pago con Transferencia Bancaria
"""

from patrones.strategy.estrategia_pago import EstrategiaPago
from constantes import SEPARADOR_LINEA, LONGITUD_CBU
from config.configuracion_restaurante import ConfiguracionRestaurante
import time


class PagoTransferencia(EstrategiaPago):
    """
    Estrategia de pago con transferencia bancaria.
    Genera código de referencia único.
    """

    def __init__(self, cbu_cliente: str):
        """
        Inicializa la estrategia de pago con transferencia.
        
        Args:
            cbu_cliente: CBU del cliente (debe tener 22 dígitos)
            
        Raises:
            ValueError: Si el CBU no tiene 22 dígitos
        """
        if len(cbu_cliente) != LONGITUD_CBU:
            raise ValueError(f"El CBU debe tener {LONGITUD_CBU} dígitos")
        self._cbu_cliente = cbu_cliente

    def procesar_pago(self, monto: float) -> None:
        """
        Procesa el pago con transferencia mostrando datos y código.
        
        Args:
            monto: Monto total a pagar
        """
        config = ConfiguracionRestaurante.get_instance()
        cbu_restaurante = config.get_cbu()
        codigo_referencia = self._generar_codigo_referencia()

        print(SEPARADOR_LINEA)
        print("PROCESANDO PAGO CON TRANSFERENCIA")
        print(SEPARADOR_LINEA)
        print(f"CBU Restaurante: {cbu_restaurante}")
        print(f"CBU Cliente: {self._cbu_cliente}")
        print(f"Monto: ${monto:.2f}")
        print(f"Código de referencia: {codigo_referencia}")
        print("¡Pago procesado exitosamente!")

    def _generar_codigo_referencia(self) -> str:
        """
        Genera un código de referencia único basado en timestamp.
        
        Returns:
            str: Código de referencia único
        """
        timestamp = int(time.time())
        return f"REF-{timestamp}"

    def get_nombre(self) -> str:
        """Retorna el nombre de la forma de pago."""
        return "Transferencia Bancaria"

    def get_cbu_cliente(self) -> str:
        """Retorna el CBU del cliente."""
        return self._cbu_cliente

