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