"""
Archivo integrador generado automaticamente
Directorio: /home/renata/Diseño de Sistemas/python_restaurante/.
Fecha: 2025-11-04 16:43:29
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: buscar_paquete.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./buscar_paquete.py
# ================================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ================================================================================
# ARCHIVO 3/4: constantes.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./constantes.py
# ================================================================================

"""
Constantes globales del sistema de gestión de restaurante.
Centraliza valores configurables para facilitar mantenimiento.
"""

# ============================================================================
# CONFIGURACIÓN DEL RESTAURANTE
# ============================================================================
NOMBRE_RESTAURANTE_DEFAULT = "Mi Restaurante"
HORARIO_APERTURA_DEFAULT = "09:00"
HORARIO_CIERRE_DEFAULT = "22:00"
CAPACIDAD_MESAS_DEFAULT = 10
CBU_RESTAURANTE_DEFAULT = "9876543210987654321098"

# ============================================================================
# PLATOS - CONFIGURACIÓN
# ============================================================================
TIEMPO_PREPARACION_DEFAULT = 15  # minutos
CALORIAS_DEFAULT_POSTRE = 200  # kcal

# ============================================================================
# PAGOS - CONFIGURACIÓN
# ============================================================================
DESCUENTO_EFECTIVO = 0.10  # 10%
CUOTAS_PERMITIDAS = [1, 3, 6, 12]
LONGITUD_CBU = 22  # caracteres

# ============================================================================
# PERSISTENCIA - CONFIGURACIÓN
# ============================================================================
DIRECTORIO_DATA = "data"
DIRECTORIO_PEDIDOS = "data/pedidos"
DIRECTORIO_REPORTES = "reportes"
EXTENSION_DATA = ".dat"
PREFIJO_ARCHIVO_PEDIDO = "mesa_"

# ============================================================================
# FORMATO Y PRESENTACIÓN
# ============================================================================
SEPARADOR_LINEA = "═══════════════════════════════════"
SEPARADOR_SECCION = "-----------------------------------"
SIMBOLO_MONEDA = "$"
DECIMALES_PRECIO = 2

# ================================================================================
# ARCHIVO 4/4: main.py
# Ruta: /home/renata/Diseño de Sistemas/python_restaurante/./main.py
# ================================================================================

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

