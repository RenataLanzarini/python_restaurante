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