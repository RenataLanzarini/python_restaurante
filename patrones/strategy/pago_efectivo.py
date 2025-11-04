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