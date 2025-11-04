"""
Servicio para gestionar operaciones de pedidos.
"""

from datetime import datetime
from constantes import SEPARADOR_LINEA, SEPARADOR_SECCION

if False:  # TYPE_CHECKING
    from entidades.pedido.pedido_mesa import PedidoMesa
    from entidades.menu.plato import Plato


class PedidoService:
    """
    Servicio que proporciona operaciones de negocio para pedidos.
    """

    def agregar_plato(self, pedido: 'PedidoMesa', plato: 'Plato') -> None:
        """
        Agrega un plato al pedido y confirma la acción.
        
        Args:
            pedido: Pedido al que agregar el plato
            plato: Plato a agregar
        """
        pedido.agregar_plato(plato)
        print(f"Plato '{plato.get_nombre()}' agregado al pedido de Mesa {pedido.get_numero_mesa()}")

    def facturar(self, pedido: 'PedidoMesa') -> None:
        """
        Realiza el proceso completo de facturación.
        
        Args:
            pedido: Pedido a facturar
            
        Raises:
            ValueError: Si el pedido está vacío o no tiene forma de pago
        """
        # Validaciones
        if pedido.esta_vacio():
            raise ValueError(
                "El pedido está vacío, agregue platos antes de facturar"
            )

        if not pedido.tiene_estrategia_pago():
            raise ValueError(
                "Debe seleccionar una forma de pago antes de facturar"
            )

        # Mostrar encabezado
        print()
        print(SEPARADOR_LINEA)
        print(f"FACTURA - MESA {pedido.get_numero_mesa()}")
        print(SEPARADOR_LINEA)
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Mostrar platos
        print("PLATOS CONSUMIDOS:")
        print(SEPARADOR_SECCION)
        for plato in pedido.get_platos():
            plato.mostrar_detalle()
            print(SEPARADOR_SECCION)

        # Mostrar subtotal
        total = pedido.calcular_total()
        print()
        print(f"SUBTOTAL: ${total:.2f}")
        print(SEPARADOR_LINEA)
        print()

        # Procesar pago con estrategia seleccionada
        estrategia = pedido.get_estrategia_pago()
        estrategia.procesar_pago(total)

        # Confirmar
        print()
        print(SEPARADOR_LINEA)
        print("¡PAGO COMPLETADO!")
        print("Gracias por su visita")
        print(SEPARADOR_LINEA)

    def calcular_total(self, pedido: 'PedidoMesa') -> float:
        """
        Calcula el total del pedido.
        
        Args:
            pedido: Pedido a calcular
            
        Returns:
            float: Total del pedido
        """
        return pedido.calcular_total()

    def mostrar_resumen(self, pedido: 'PedidoMesa') -> None:
        """
        Muestra un resumen del pedido sin procesarlo.
        
        Args:
            pedido: Pedido a mostrar
        """
        print(SEPARADOR_LINEA)
        print(f"RESUMEN PEDIDO - MESA {pedido.get_numero_mesa()}")
        print(SEPARADOR_LINEA)
        print(f"Cantidad de platos: {len(pedido.get_platos())}")
        print(f"Total: ${pedido.calcular_total():.2f}")
        
        if pedido.tiene_estrategia_pago():
            estrategia = pedido.get_estrategia_pago()
            print(f"Forma de pago: {estrategia.get_nombre()}")
        else:
            print("Forma de pago: No seleccionada")
        
        print(SEPARADOR_LINEA)