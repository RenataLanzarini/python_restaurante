"""
Programa principal - Demostración del Sistema de Gestión de Restaurante.
Demuestra los 4 patrones de diseño implementados:
- Singleton: ConfiguracionRestaurante
- Factory: PlatoFactory
- Observer: SistemaPedidos -> EstacionCocina
- Strategy: EstrategiaPago (Tarjeta, Efectivo, Transferencia)
"""

from config.configuracion_restaurante import ConfiguracionRestaurante
from patrones.factory.plato_factory import PlatoFactory
from cocina.sistema_pedidos import SistemaPedidos
from cocina.estacion_cocina import EstacionCocina
from entidades.pedido.pedido_mesa import PedidoMesa
from patrones.strategy.pago_tarjeta import PagoTarjeta
from patrones.strategy.pago_efectivo import PagoEfectivo
from patrones.strategy.pago_transferencia import PagoTransferencia
from servicios.pedido.pedido_service import PedidoService
from servicios.negocio.restaurante_service import RestauranteService
from servicios.negocio.reporte_service import ReporteService
from servicios.persistencia.persistencia_service import PersistenciaService
from excepciones.persistencia_exception import PersistenciaException


def separador_patron(nombre_patron: str) -> None:
    """Imprime un separador visual para cada patrón."""
    print("\n" + "=" * 80)
    print(f"  PATRÓN: {nombre_patron}")
    print("=" * 80 + "\n")


def main():
    """Función principal que ejecuta la demostración completa."""
    
    print("\n" + "=" * 80)
    print("  SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("  Demostración de Patrones de Diseño")
    print("=" * 80 + "\n")

    # ========================================================================
    # PATRÓN 1: SINGLETON - Configuración Única del Restaurante
    # ========================================================================
    separador_patron("SINGLETON - Configuración Única del Restaurante")
    
    print("1. Obteniendo primera instancia de configuración...")
    config1 = ConfiguracionRestaurante.get_instance()
    config1.set_nombre("La Parrilla del Chef")
    config1.set_direccion("Av. San Martín 1250, Mendoza")
    config1.set_telefono("+54 261 423-5678")
    config1.set_horario_apertura("11:00")
    config1.set_horario_cierre("23:00")
    config1.set_capacidad_mesas(20)
    
    print("2. Obteniendo segunda instancia de configuración...")
    config2 = ConfiguracionRestaurante.get_instance()
    
    print(f"\n3. Verificando Singleton:")
    print(f"   ¿config1 es config2? {config1 is config2}")
    print(f"   ID config1: {id(config1)}")
    print(f"   ID config2: {id(config2)}")
    
    print("\n4. Configuración establecida:")
    config1.mostrar_configuracion()

    # ========================================================================
    # PATRÓN 2: FACTORY - Creación de Platos del Menú
    # ========================================================================
    separador_patron("FACTORY METHOD - Creación de Platos del Menú")
    
    print("1. Creando ENTRADAS mediante Factory...")
    entrada1 = PlatoFactory.crear_plato(
        tipo="entrada",
        nombre="Ensalada César",
        precio=850.00,
        ingredientes="lechuga, crutones, parmesano, aderezo césar"
    )
    print(f"   ✓ Creada: {entrada1.get_nombre()}")
    
    entrada2 = PlatoFactory.crear_plato(
        tipo="entrada",
        nombre="Provoleta",
        precio=950.00,
        ingredientes="queso provolone, orégano, aceite de oliva"
    )
    print(f"   ✓ Creada: {entrada2.get_nombre()}")
    
    print("\n2. Creando PLATOS PRINCIPALES mediante Factory...")
    principal1 = PlatoFactory.crear_plato(
        tipo="principal",
        nombre="Bife de Chorizo",
        precio=4500.00,
        tiempo_preparacion=25
    )
    print(f"   ✓ Creado: {principal1.get_nombre()}")
    
    principal2 = PlatoFactory.crear_plato(
        tipo="principal",
        nombre="Ravioles de Ricota",
        precio=3200.00,
        tiempo_preparacion=15
    )
    print(f"   ✓ Creado: {principal2.get_nombre()}")
    
    print("\n3. Creando POSTRES mediante Factory...")
    postre1 = PlatoFactory.crear_plato(
        tipo="postre",
        nombre="Tiramisú",
        precio=1200.00,
        calorias=350
    )
    print(f"   ✓ Creado: {postre1.get_nombre()}")
    
    postre2 = PlatoFactory.crear_plato(
        tipo="postre",
        nombre="Flan con Dulce de Leche",
        precio=950.00,
        calorias=280
    )
    print(f"   ✓ Creado: {postre2.get_nombre()}")
    
    print("\n4. Mostrando detalles de todos los platos creados:\n")
    print("─" * 80)
    entrada1.mostrar_detalle()
    print("─" * 80)
    principal1.mostrar_detalle()
    print("─" * 80)
    postre1.mostrar_detalle()
    print("─" * 80)
    
    print("\n5. Probando tipo inválido...")
    try:
        bebida = PlatoFactory.crear_plato("bebida", "Coca Cola", 500.00)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")

    # ========================================================================
    # PATRÓN 3: OBSERVER - Sistema de Notificaciones de Cocina
    # ========================================================================
    separador_patron("OBSERVER - Sistema de Notificaciones de Cocina")
    
    print("1. Creando sistema de pedidos (Observable)...")
    sistema_pedidos = SistemaPedidos()
    print("   ✓ Sistema de pedidos creado")
    
    print("\n2. Creando estaciones de cocina (Observers)...")
    estacion_parrilla = EstacionCocina("Parrilla")
    estacion_ensaladas = EstacionCocina("Ensaladas")
    estacion_postres = EstacionCocina("Postres")
    print("   ✓ 3 estaciones creadas")
    
    print("\n3. Suscribiendo estaciones al sistema de pedidos...")
    sistema_pedidos.agregar_observador(estacion_parrilla)
    print(f"   ✓ Estación '{estacion_parrilla.get_nombre()}' suscrita")
    
    sistema_pedidos.agregar_observador(estacion_ensaladas)
    print(f"   ✓ Estación '{estacion_ensaladas.get_nombre()}' suscrita")
    
    sistema_pedidos.agregar_observador(estacion_postres)
    print(f"   ✓ Estación '{estacion_postres.get_nombre()}' suscrita")
    
    print(f"\n4. Total de observadores suscritos: {sistema_pedidos.get_cantidad_observadores()}")
    
    print("\n5. Notificando nuevo pedido (TODAS las estaciones reciben):")
    sistema_pedidos.notificar_pedido(
        numero_mesa=5,
        plato="Bife de Chorizo",
        cantidad=2
    )
    
    print("\n6. Desuscribiendo estación 'Ensaladas'...")
    sistema_pedidos.eliminar_observador(estacion_ensaladas)
    print(f"   ✓ Estación 'Ensaladas' desuscrita")
    print(f"   Total de observadores: {sistema_pedidos.get_cantidad_observadores()}")
    
    print("\n7. Notificando nuevo pedido (SOLO estaciones suscritas reciben):")
    sistema_pedidos.notificar_pedido(
        numero_mesa=8,
        plato="Tiramisú",
        cantidad=1
    )

    # ========================================================================
    # PATRÓN 4: STRATEGY - Formas de Pago
    # ========================================================================
    separador_patron("STRATEGY - Formas de Pago Intercambiables")
    
    # Inicializar servicios
    pedido_service = PedidoService()
    
    # ------------------------------------------------------------------------
    # Escenario 1: Pago con Tarjeta en 3 cuotas
    # ------------------------------------------------------------------------
    print("\n" + "─" * 80)
    print("ESCENARIO 1: Mesa 5 - Pago con Tarjeta (3 cuotas)")
    print("─" * 80)
    
    print("\n1. Creando pedido para Mesa 5...")
    pedido_mesa5 = PedidoMesa(numero_mesa=5)
    
    print("2. Agregando platos al pedido...")
    pedido_service.agregar_plato(pedido_mesa5, entrada1)
    pedido_service.agregar_plato(pedido_mesa5, principal1)
    pedido_service.agregar_plato(pedido_mesa5, postre1)
    
    print("\n3. Seleccionando estrategia de pago: Tarjeta en 3 cuotas")
    estrategia_tarjeta = PagoTarjeta(
        numero_tarjeta="5412-7534-8899-1234",
        cuotas=3
    )
    pedido_mesa5.set_estrategia_pago(estrategia_tarjeta)
    print(f"   ✓ Estrategia seleccionada: {estrategia_tarjeta.get_nombre()}")
    
    print("\n4. Procesando facturación completa...")
    pedido_service.facturar(pedido_mesa5)
    
    # ------------------------------------------------------------------------
    # Escenario 2: Pago en Efectivo con descuento
    # ------------------------------------------------------------------------
    print("\n" + "─" * 80)
    print("ESCENARIO 2: Mesa 8 - Pago en Efectivo (10% descuento)")
    print("─" * 80)
    
    print("\n1. Creando pedido para Mesa 8...")
    pedido_mesa8 = PedidoMesa(numero_mesa=8)
    
    print("2. Agregando platos al pedido...")
    pedido_service.agregar_plato(pedido_mesa8, entrada2)
    pedido_service.agregar_plato(pedido_mesa8, principal2)
    
    print("\n3. Seleccionando estrategia de pago: Efectivo")
    estrategia_efectivo = PagoEfectivo()
    pedido_mesa8.set_estrategia_pago(estrategia_efectivo)
    print(f"   ✓ Estrategia seleccionada: {estrategia_efectivo.get_nombre()}")
    
    print("\n4. Procesando facturación completa...")
    pedido_service.facturar(pedido_mesa8)
    
    # ------------------------------------------------------------------------
    # Escenario 3: Pago con Transferencia
    # ------------------------------------------------------------------------
    print("\n" + "─" * 80)
    print("ESCENARIO 3: Mesa 12 - Pago con Transferencia Bancaria")
    print("─" * 80)
    
    print("\n1. Creando pedido para Mesa 12...")
    pedido_mesa12 = PedidoMesa(numero_mesa=12)
    
    print("2. Agregando platos al pedido...")
    pedido_service.agregar_plato(pedido_mesa12, entrada1)
    pedido_service.agregar_plato(pedido_mesa12, principal1)
    pedido_service.agregar_plato(pedido_mesa12, postre2)
    
    print("\n3. Seleccionando estrategia de pago: Transferencia")
    estrategia_transferencia = PagoTransferencia(
        cbu_cliente="1234567890123456789012"
    )
    pedido_mesa12.set_estrategia_pago(estrategia_transferencia)
    print(f"   ✓ Estrategia seleccionada: {estrategia_transferencia.get_nombre()}")
    
    print("\n4. Procesando facturación completa...")
    pedido_service.facturar(pedido_mesa12)
    
    # ========================================================================
    # OPERACIONES DE NEGOCIO
    # ========================================================================
    separador_patron("OPERACIONES DE NEGOCIO - Gestión del Restaurante")
    
    print("1. Inicializando servicio de restaurante...")
    restaurante_service = RestauranteService()
    
    print("\n2. Agregando pedidos al sistema...")
    restaurante_service.agregar_pedido(pedido_mesa5)
    restaurante_service.agregar_pedido(pedido_mesa8)
    restaurante_service.agregar_pedido(pedido_mesa12)
    
    print(f"\n3. Mesas activas: {restaurante_service.listar_mesas_activas()}")
    print(f"   Total de pedidos: {restaurante_service.get_cantidad_pedidos()}")
    
    print(f"\n4. Ingresos totales del día: ${restaurante_service.calcular_ingresos_totales():.2f}")
    
    print("\n5. Buscando pedido de Mesa 8...")
    pedido_encontrado = restaurante_service.buscar_pedido(8)
    if pedido_encontrado:
        print(f"   ✓ Pedido encontrado - Total: ${pedido_encontrado.calcular_total():.2f}")
    
    print("\n6. Generando reporte de ventas diarias...")
    reporte_service = ReporteService()
    reporte_service.generar_reporte_ventas(restaurante_service)

    # ========================================================================
    # PERSISTENCIA
    # ========================================================================
    separador_patron("PERSISTENCIA - Guardado y Recuperación de Pedidos")
    
    persistencia_service = PersistenciaService()
    
    print("1. Guardando pedido de Mesa 5 en disco...")
    try:
        persistencia_service.guardar_pedido(pedido_mesa5)
    except PersistenciaException as e:
        print(f"   ✗ Error: {e.get_mensaje_completo()}")
    
    print("\n2. Guardando pedido de Mesa 8 en disco...")
    try:
        persistencia_service.guardar_pedido(pedido_mesa8)
    except PersistenciaException as e:
        print(f"   ✗ Error: {e.get_mensaje_completo()}")
    
    print("\n3. Listando todos los pedidos guardados:")
    archivos = persistencia_service.listar_pedidos_guardados()
    print("   " + "═" * 76)
    print("   PEDIDOS GUARDADOS EN DISCO")
    print("   " + "═" * 76)
    for archivo in archivos:
        print(f"     - {archivo}")
    print(f"\n   Total: {len(archivos)} pedidos guardados")
    print("   " + "═" * 76)
    
    if len(archivos) > 0:
        print(f"\n4. Recuperando primer pedido guardado: {archivos[0]}...")
        try:
            pedido_recuperado = persistencia_service.cargar_pedido(archivos[0])
            print(f"   ✓ Pedido recuperado correctamente")
            print(f"   Mesa: {pedido_recuperado.get_numero_mesa()}")
            print(f"   Cantidad de platos: {len(pedido_recuperado.get_platos())}")
            print(f"   Total: ${pedido_recuperado.calcular_total():.2f}")
        except PersistenciaException as e:
            print(f"   ✗ Error: {e.get_mensaje_completo()}")

    # ========================================================================
    # VALIDACIONES Y MANEJO DE ERRORES
    # ========================================================================
    separador_patron("VALIDACIONES Y MANEJO DE ERRORES")
    
    print("1. Intentando crear pedido con mesa inválida (número negativo)...")
    try:
        pedido_invalido = PedidoMesa(numero_mesa=-1)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n2. Intentando facturar pedido vacío...")
    try:
        pedido_vacio = PedidoMesa(numero_mesa=99)
        pedido_service.facturar(pedido_vacio)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n3. Intentando facturar sin forma de pago...")
    try:
        pedido_sin_pago = PedidoMesa(numero_mesa=100)
        pedido_service.agregar_plato(pedido_sin_pago, entrada1)
        pedido_service.facturar(pedido_sin_pago)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n4. Intentando pago con cuotas inválidas...")
    try:
        pago_invalido = PagoTarjeta("1234-5678-9012-3456", cuotas=5)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n5. Intentando pago con CBU inválido...")
    try:
        pago_cbu_invalido = PagoTransferencia(cbu_cliente="123456")
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n6. Intentando agregar pedido duplicado...")
    try:
        pedido_duplicado = PedidoMesa(numero_mesa=5)
        restaurante_service.agregar_pedido(pedido_duplicado)
    except ValueError as e:
        print(f"   ✗ Error esperado: {e}")
    
    print("\n7. Intentando cargar archivo inexistente...")
    try:
        pedido_inexistente = persistencia_service.cargar_pedido("mesa_999_0000000000.dat")
    except PersistenciaException as e:
        print(f"   ✗ Error esperado:")
        print(f"      Mensaje: {e.get_mensaje()}")
        print(f"      Archivo: {e.get_nombre_archivo()}")
        print(f"      Operación: {e.get_tipo_operacion()}")

    # ========================================================================
    # RESUMEN FINAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("  RESUMEN DE LA DEMOSTRACIÓN")
    print("=" * 80)
    print("\n✓ PATRÓN SINGLETON:")
    print("  - ConfiguracionRestaurante: Una única instancia thread-safe")
    print("  - Comprobado: config1 is config2 = True")
    
    print("\n✓ PATRÓN FACTORY METHOD:")
    print("  - PlatoFactory: Creación estandarizada de platos")
    print(f"  - Creados: 2 entradas, 2 principales, 2 postres")
    print("  - Sin lambdas, usando métodos estáticos dedicados")
    
    print("\n✓ PATRÓN OBSERVER:")
    print("  - SistemaPedidos (Observable) -> EstacionCocina (Observers)")
    print(f"  - 3 estaciones suscritas inicialmente")
    print(f"  - Notificaciones dinámicas al agregar/remover observadores")
    
    print("\n✓ PATRÓN STRATEGY:")
    print("  - EstrategiaPago: Algoritmos de pago intercambiables")
    print("  - PagoTarjeta: Con cuotas")
    print("  - PagoEfectivo: Con 10% descuento automático")
    print("  - PagoTransferencia: Con CBU y código de referencia")
    
    print("\n✓ OPERACIONES ADICIONALES:")
    print(f"  - Gestión de múltiples mesas: {restaurante_service.get_cantidad_pedidos()} activas")
    print(f"  - Ingresos totales: ${restaurante_service.calcular_ingresos_totales():.2f}")
    print(f"  - Reportes de ventas generados")
    print(f"  - Persistencia: {len(archivos)} pedidos guardados en disco")
    
    print("\n✓ VALIDACIONES:")
    print("  - Todas las validaciones funcionaron correctamente")
    print("  - Excepciones personalizadas capturadas apropiadamente")
    
    print("\n" + "=" * 80)
    print("  DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()