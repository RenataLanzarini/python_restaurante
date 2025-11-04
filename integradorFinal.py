"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/renata/Diseño de Sistemas/python_restaurante/.
Fecha de generacion: 2025-11-04 16:43:29
Total de archivos integrados: 39
Total de directorios procesados: 16
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. buscar_paquete.py
#   3. constantes.py
#   4. main.py
#
# DIRECTORIO: cocina
#   5. __init__.py
#   6. estacion_cocina.py
#   7. sistema_pedidos.py
#
# DIRECTORIO: config
#   8. __init__.py
#   9. configuracion_restaurante.py
#
# DIRECTORIO: entidades
#   10. __init__.py
#
# DIRECTORIO: entidades/menu
#   11. __init__.py
#   12. entrada.py
#   13. plato.py
#   14. plato_principal.py
#   15. postre.py
#
# DIRECTORIO: entidades/pedido
#   16. __init__.py
#   17. pedido_mesa.py
#
# DIRECTORIO: excepciones
#   18. __init__.py
#   19. persistencia_exception.py
#
# DIRECTORIO: patrones
#   20. __init__.py
#
# DIRECTORIO: patrones/factory
#   21. __init__.py
#   22. plato_factory.py
#
# DIRECTORIO: patrones/observer
#   23. __init__.py
#   24. observable.py
#   25. observer.py
#
# DIRECTORIO: patrones/strategy
#   26. __init__.py
#   27. estrategia_pago.py
#   28. pago_efectivo.py
#   29. pago_tarjeta.py
#   30. pago_transferencia.py
#
# DIRECTORIO: servicios
#   31. __init__.py
#
# DIRECTORIO: servicios/negocio
#   32. __init__.py
#   33. reporte_service.py
#   34. restaurante_service.py
#
# DIRECTORIO: servicios/pedido
#   35. __init__.py
#   36. pedido_service.py
#
# DIRECTORIO: servicios/persistencia
#   37. __init__.py
#   38. persistencia_service.py
#
# DIRECTORIO: tests
#   39. __init__.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/39: __init__.py
# Directorio: .
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/39: buscar_paquete.py
# Directorio: .
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./buscar_paquete.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 3/39: constantes.py
# Directorio: .
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./constantes.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 4/39: main.py
# Directorio: .
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./main.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: cocina
################################################################################

# ==============================================================================
# ARCHIVO 5/39: __init__.py
# Directorio: cocina
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/39: estacion_cocina.py
# Directorio: cocina
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/estacion_cocina.py
# ==============================================================================

"""
Clase que representa una estación de cocina (Observer concreto).
"""

from patrones.observer.observer import Observer
from typing import Dict


class EstacionCocina(Observer[Dict]):
    """
    Representa una estación de cocina que observa el sistema de pedidos.
    Recibe notificaciones cuando hay nuevos pedidos.
    """

    def __init__(self, nombre: str):
        """
        Inicializa una estación de cocina.
        
        Args:
            nombre: Nombre de la estación (ej: "Parrilla", "Ensaladas")
        """
        self._nombre = nombre

    def actualizar(self, evento: Dict) -> None:
        """
        Recibe notificación de nuevo pedido.
        
        Args:
            evento: Diccionario con datos del pedido
                   Contiene: 'mesa', 'plato', 'cantidad'
        """
        print(f"[{self._nombre.upper()}] Nuevo pedido recibido:")
        print(f"  Mesa: {evento.get('mesa', 'N/A')}")
        print(f"  Plato: {evento.get('plato', 'N/A')}")
        print(f"  Cantidad: {evento.get('cantidad', 0)}")

    def get_nombre(self) -> str:
        """Retorna el nombre de la estación."""
        return self._nombre

# ==============================================================================
# ARCHIVO 7/39: sistema_pedidos.py
# Directorio: cocina
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./cocina/sistema_pedidos.py
# ==============================================================================

"""
Clase que representa el sistema de pedidos (Observable concreto).
"""

from patrones.observer.observable import Observable
from typing import Dict
from constantes import SEPARADOR_LINEA


class SistemaPedidos(Observable[Dict]):
    """
    Sistema centralizado de pedidos que notifica a las estaciones de cocina.
    Actúa como Observable en el patrón Observer.
    """

    def __init__(self):
        """Inicializa el sistema de pedidos."""
        super().__init__()

    def notificar_pedido(self, numero_mesa: int, plato: str, cantidad: int) -> None:
        """
        Notifica un nuevo pedido a todas las estaciones suscritas.
        
        Args:
            numero_mesa: Número de mesa que realizó el pedido
            plato: Nombre del plato pedido
            cantidad: Cantidad de platos
        """
        print(SEPARADOR_LINEA)
        print(f"Notificando pedido a {self.get_cantidad_observadores()} estaciones")
        print(SEPARADOR_LINEA)

        pedido = {
            'mesa': numero_mesa,
            'plato': plato,
            'cantidad': cantidad
        }

        self.notificar_observadores(pedido)


################################################################################
# DIRECTORIO: config
################################################################################

# ==============================================================================
# ARCHIVO 8/39: __init__.py
# Directorio: config
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./config/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 9/39: configuracion_restaurante.py
# Directorio: config
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./config/configuracion_restaurante.py
# ==============================================================================

"""
Patrón Singleton: ConfiguracionRestaurante
Garantiza una única instancia de configuración del sistema.
"""

from threading import Lock
from typing import Optional


class ConfiguracionRestaurante:
    """
    Configuración global del restaurante (Singleton).
    Mantiene datos como nombre, dirección, horarios, etc.
    Thread-safe mediante double-checked locking.
    """

    _instance: Optional['ConfiguracionRestaurante'] = None
    _lock: Lock = Lock()

    def __new__(cls) -> 'ConfiguracionRestaurante':
        """
        Controla la instanciación para garantizar singleton.
        
        Returns:
            ConfiguracionRestaurante: La única instancia del sistema
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance

    def _inicializar(self) -> None:
        """Inicializa los valores por defecto de la configuración."""
        self._nombre: str = "Mi Restaurante"
        self._direccion: str = ""
        self._telefono: str = ""
        self._horario_apertura: str = "09:00"
        self._horario_cierre: str = "22:00"
        self._capacidad_mesas: int = 10
        self._cbu: str = "9876543210987654321098"

    @classmethod
    def get_instance(cls) -> 'ConfiguracionRestaurante':
        """
        Obtiene la instancia única de configuración.
        
        Returns:
            ConfiguracionRestaurante: Instancia única
        """
        if cls._instance is None:
            cls()
        return cls._instance

    # ========================================================================
    # GETTERS
    # ========================================================================

    def get_nombre(self) -> str:
        """Retorna el nombre del restaurante."""
        return self._nombre

    def get_direccion(self) -> str:
        """Retorna la dirección del restaurante."""
        return self._direccion

    def get_telefono(self) -> str:
        """Retorna el teléfono del restaurante."""
        return self._telefono

    def get_horario_apertura(self) -> str:
        """Retorna el horario de apertura."""
        return self._horario_apertura

    def get_horario_cierre(self) -> str:
        """Retorna el horario de cierre."""
        return self._horario_cierre

    def get_capacidad_mesas(self) -> int:
        """Retorna la capacidad de mesas del restaurante."""
        return self._capacidad_mesas

    def get_cbu(self) -> str:
        """Retorna el CBU del restaurante para transferencias."""
        return self._cbu

    # ========================================================================
    # SETTERS
    # ========================================================================

    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre del restaurante."""
        self._nombre = nombre

    def set_direccion(self, direccion: str) -> None:
        """Establece la dirección del restaurante."""
        self._direccion = direccion

    def set_telefono(self, telefono: str) -> None:
        """Establece el teléfono del restaurante."""
        self._telefono = telefono

    def set_horario_apertura(self, horario: str) -> None:
        """Establece el horario de apertura."""
        self._horario_apertura = horario

    def set_horario_cierre(self, horario: str) -> None:
        """Establece el horario de cierre."""
        self._horario_cierre = horario

    def set_capacidad_mesas(self, capacidad: int) -> None:
        """
        Establece la capacidad de mesas.
        
        Args:
            capacidad: Número de mesas (debe ser positivo)
            
        Raises:
            ValueError: Si la capacidad es menor o igual a cero
        """
        if capacidad <= 0:
            raise ValueError("La capacidad de mesas debe ser mayor a cero")
        self._capacidad_mesas = capacidad

    def set_cbu(self, cbu: str) -> None:
        """Establece el CBU del restaurante."""
        self._cbu = cbu

    def mostrar_configuracion(self) -> None:
        """Muestra la configuración actual del restaurante."""
        print("═══════════════════════════════════")
        print("CONFIGURACIÓN DEL RESTAURANTE")
        print("═══════════════════════════════════")
        print(f"Nombre: {self._nombre}")
        print(f"Dirección: {self._direccion}")
        print(f"Teléfono: {self._telefono}")
        print(f"Horario: {self._horario_apertura} - {self._horario_cierre}")
        print(f"Capacidad: {self._capacidad_mesas} mesas")
        print(f"CBU: {self._cbu}")
        print("═══════════════════════════════════")


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 10/39: __init__.py
# Directorio: entidades
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/menu
################################################################################

# ==============================================================================
# ARCHIVO 11/39: __init__.py
# Directorio: entidades/menu
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 12/39: entrada.py
# Directorio: entidades/menu
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/entrada.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 13/39: plato.py
# Directorio: entidades/menu
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/plato.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/39: plato_principal.py
# Directorio: entidades/menu
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/plato_principal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/39: postre.py
# Directorio: entidades/menu
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/menu/postre.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/pedido
################################################################################

# ==============================================================================
# ARCHIVO 16/39: __init__.py
# Directorio: entidades/pedido
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/pedido/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/39: pedido_mesa.py
# Directorio: entidades/pedido
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./entidades/pedido/pedido_mesa.py
# ==============================================================================

"""
Clase que representa un pedido de una mesa.
Contexto del patrón Strategy para formas de pago.
"""

from typing import List, Optional

if False:  # TYPE_CHECKING
    from entidades.menu.plato import Plato
    from patrones.strategy.estrategia_pago import EstrategiaPago


class PedidoMesa:
    """
    Representa el pedido de una mesa con sus platos y forma de pago.
    Actúa como Context en el patrón Strategy.
    """

    def __init__(self, numero_mesa: int):
        """
        Inicializa un pedido para una mesa.
        
        Args:
            numero_mesa: Número de la mesa (debe ser positivo)
            
        Raises:
            ValueError: Si el número de mesa es menor o igual a cero
        """
        if numero_mesa <= 0:
            raise ValueError("El número de mesa debe ser mayor a cero")
        
        self._numero_mesa = numero_mesa
        self._platos: List['Plato'] = []
        self._estrategia_pago: Optional['EstrategiaPago'] = None

    def agregar_plato(self, plato: 'Plato') -> None:
        """
        Agrega un plato al pedido.
        
        Args:
            plato: Plato a agregar
        """
        self._platos.append(plato)

    def calcular_total(self) -> float:
        """
        Calcula el total del pedido sumando precios de todos los platos.
        
        Returns:
            float: Total del pedido
        """
        return sum(plato.get_precio() for plato in self._platos)

    def get_platos(self) -> List['Plato']:
        """
        Retorna una copia de la lista de platos (defensive copy).
        
        Returns:
            List[Plato]: Copia de la lista de platos
        """
        return self._platos.copy()

    def esta_vacio(self) -> bool:
        """
        Verifica si el pedido está vacío.
        
        Returns:
            bool: True si no tiene platos, False en caso contrario
        """
        return len(self._platos) == 0

    def get_numero_mesa(self) -> int:
        """Retorna el número de mesa del pedido."""
        return self._numero_mesa

    def set_estrategia_pago(self, estrategia: 'EstrategiaPago') -> None:
        """
        Establece la estrategia de pago (patrón Strategy).
        
        Args:
            estrategia: Estrategia de pago a utilizar
        """
        self._estrategia_pago = estrategia

    def get_estrategia_pago(self) -> Optional['EstrategiaPago']:
        """
        Retorna la estrategia de pago actual.
        
        Returns:
            EstrategiaPago o None: Estrategia actual o None si no está definida
        """
        return self._estrategia_pago

    def tiene_estrategia_pago(self) -> bool:
        """
        Verifica si el pedido tiene una estrategia de pago asignada.
        
        Returns:
            bool: True si tiene estrategia, False en caso contrario
        """
        return self._estrategia_pago is not None


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 18/39: __init__.py
# Directorio: excepciones
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/39: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./excepciones/persistencia_exception.py
# ==============================================================================

"""
Excepción personalizada para errores de persistencia.
"""


class PersistenciaException(Exception):
    """
    Excepción lanzada cuando ocurre un error durante operaciones de persistencia.
    """

    def __init__(self, mensaje: str, nombre_archivo: str, 
                 tipo_operacion: str, causa: str):
        """
        Inicializa la excepción.
        
        Args:
            mensaje: Mensaje descriptivo del error
            nombre_archivo: Nombre del archivo involucrado
            tipo_operacion: Tipo de operación (LECTURA/ESCRITURA)
            causa: Causa subyacente del error
        """
        self._mensaje = mensaje
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
        self._causa = causa
        super().__init__(self.get_mensaje_completo())

    def get_mensaje_completo(self) -> str:
        """
        Genera el mensaje completo del error.
        
        Returns:
            str: Mensaje formateado con todos los detalles
        """
        return (
            f"{self._mensaje}\n"
            f"Archivo: {self._nombre_archivo}\n"
            f"Operación: {self._tipo_operacion}\n"
            f"Causa: {self._causa}"
        )

    def get_mensaje(self) -> str:
        """Retorna el mensaje básico del error."""
        return self._mensaje

    def get_nombre_archivo(self) -> str:
        """Retorna el nombre del archivo."""
        return self._nombre_archivo

    def get_tipo_operacion(self) -> str:
        """Retorna el tipo de operación."""
        return self._tipo_operacion

    def get_causa(self) -> str:
        """Retorna la causa del error."""
        return self._causa


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 20/39: __init__.py
# Directorio: patrones
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 21/39: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/39: plato_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/factory/plato_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 23/39: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/39: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/observable.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/39: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/observer/observer.py
# ==============================================================================

"""
Patrón Observer: Interfaz Observer
Define el contrato para objetos que observan cambios.
"""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz genérica para observadores.
    Los observadores reciben notificaciones cuando el Observable cambia.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el Observable notifica un cambio.
        
        Args:
            evento: Datos del evento (tipo genérico T)
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 26/39: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 27/39: estrategia_pago.py
# Directorio: patrones/strategy
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/estrategia_pago.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 28/39: pago_efectivo.py
# Directorio: patrones/strategy
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_efectivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 29/39: pago_tarjeta.py
# Directorio: patrones/strategy
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_tarjeta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 30/39: pago_transferencia.py
# Directorio: patrones/strategy
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./patrones/strategy/pago_transferencia.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 31/39: __init__.py
# Directorio: servicios
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 32/39: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/39: reporte_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/reporte_service.py
# ==============================================================================

"""
Servicio para generar reportes de ventas y estadísticas.
"""

from datetime import date
from config.configuracion_restaurante import ConfiguracionRestaurante
from constantes import SEPARADOR_LINEA, SEPARADOR_SECCION
from entidades.menu.entrada import Entrada
from entidades.menu.plato_principal import PlatoPrincipal
from entidades.menu.postre import Postre

if False:  # TYPE_CHECKING
    from servicios.negocio.restaurante_service import RestauranteService


class ReporteService:
    """
    Servicio para generar reportes de ventas y estadísticas del restaurante.
    """

    def generar_reporte_ventas(self, restaurante_service: 'RestauranteService') -> None:
        """
        Genera un reporte completo de ventas diarias.
        
        Args:
            restaurante_service: Servicio con los pedidos activos
        """
        pedidos = restaurante_service.get_todos_pedidos()
        
        if len(pedidos) == 0:
            print("No hay pedidos para generar reporte")
            return

        # Contadores
        total_pedidos = len(pedidos)
        entradas = 0
        principales = 0
        postres = 0

        for pedido in pedidos:
            for plato in pedido.get_platos():
                if isinstance(plato, Entrada):
                    entradas += 1
                elif isinstance(plato, PlatoPrincipal):
                    principales += 1
                elif isinstance(plato, Postre):
                    postres += 1

        total_platos = entradas + principales + postres
        ingreso_total = restaurante_service.calcular_ingresos_totales()
        ingreso_promedio = ingreso_total / total_pedidos if total_pedidos > 0 else 0

        # Mostrar reporte
        config = ConfiguracionRestaurante.get_instance()
        
        print(SEPARADOR_LINEA)
        print("REPORTE DE VENTAS DIARIAS")
        print(SEPARADOR_LINEA)
        print(f"Fecha: {date.today()}")
        print(f"Restaurante: {config.get_nombre()}")
        print()
        print("RESUMEN DE PEDIDOS:")
        print(SEPARADOR_SECCION)
        print(f"Total de pedidos: {total_pedidos}")
        print(f"Total de platos vendidos: {total_platos}")
        print(f"  - Entradas: {entradas}")
        print(f"  - Platos Principales: {principales}")
        print(f"  - Postres: {postres}")
        print()
        print("INGRESOS:")
        print(SEPARADOR_SECCION)
        print(f"Ingreso total: ${ingreso_total:.2f}")
        print(f"Ingreso promedio por mesa: ${ingreso_promedio:.2f}")
        print(SEPARADOR_LINEA)

    def exportar_reporte(self, restaurante_service: 'RestauranteService', ruta_archivo: str) -> None:
        """
        Exporta el reporte a un archivo de texto.
        
        Args:
            restaurante_service: Servicio con los pedidos
            ruta_archivo: Ruta donde guardar el reporte
        """
        try:
            # Aquí iría la lógica de exportación
            # Por ahora solo muestra un mensaje
            print(f"Reporte exportado exitosamente a {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar reporte: {e}")

# ==============================================================================
# ARCHIVO 34/39: restaurante_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/negocio/restaurante_service.py
# ==============================================================================

"""
Servicio para gestionar múltiples mesas del restaurante.
"""

from typing import Dict, List, Optional

if False:  # TYPE_CHECKING
    from entidades.pedido.pedido_mesa import PedidoMesa


class RestauranteService:
    """
    Servicio centralizado para gestionar todos los pedidos activos del restaurante.
    """

    def __init__(self):
        """Inicializa el servicio con diccionario vacío de pedidos."""
        self._pedidos: Dict[int, 'PedidoMesa'] = {}

    def agregar_pedido(self, pedido: 'PedidoMesa') -> None:
        """
        Agrega un pedido al sistema.
        
        Args:
            pedido: Pedido a agregar
            
        Raises:
            ValueError: Si ya existe un pedido para esa mesa
        """
        numero_mesa = pedido.get_numero_mesa()
        
        if numero_mesa in self._pedidos:
            raise ValueError(
                f"Ya existe un pedido activo para la Mesa {numero_mesa}"
            )
        
        self._pedidos[numero_mesa] = pedido
        print(f"Pedido de Mesa {numero_mesa} agregado al sistema")

    def buscar_pedido(self, numero_mesa: int) -> Optional['PedidoMesa']:
        """
        Busca un pedido por número de mesa.
        
        Args:
            numero_mesa: Número de mesa a buscar
            
        Returns:
            PedidoMesa o None: Pedido encontrado o None si no existe
        """
        return self._pedidos.get(numero_mesa)

    def listar_mesas_activas(self) -> List[int]:
        """
        Lista todos los números de mesa con pedidos activos.
        
        Returns:
            List[int]: Lista ordenada de números de mesa activas
        """
        return sorted(self._pedidos.keys())

    def calcular_ingresos_totales(self) -> float:
        """
        Calcula los ingresos totales de todos los pedidos activos.
        
        Returns:
            float: Suma de todos los pedidos
        """
        return sum(pedido.calcular_total() for pedido in self._pedidos.values())

    def cerrar_mesa(self, numero_mesa: int) -> None:
        """
        Cierra una mesa eliminando su pedido del sistema.
        
        Args:
            numero_mesa: Número de mesa a cerrar
        """
        if numero_mesa in self._pedidos:
            del self._pedidos[numero_mesa]
            print(f"Mesa {numero_mesa} cerrada")
        else:
            print(f"Mesa {numero_mesa} no encontrada")

    def get_cantidad_pedidos(self) -> int:
        """
        Retorna la cantidad de pedidos activos.
        
        Returns:
            int: Cantidad de pedidos
        """
        return len(self._pedidos)

    def get_todos_pedidos(self) -> List['PedidoMesa']:
        """
        Retorna una lista con todos los pedidos activos.
        
        Returns:
            List[PedidoMesa]: Lista de pedidos
        """
        return list(self._pedidos.values())


################################################################################
# DIRECTORIO: servicios/pedido
################################################################################

# ==============================================================================
# ARCHIVO 35/39: __init__.py
# Directorio: servicios/pedido
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/pedido/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/39: pedido_service.py
# Directorio: servicios/pedido
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/pedido/pedido_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/persistencia
################################################################################

# ==============================================================================
# ARCHIVO 37/39: __init__.py
# Directorio: servicios/persistencia
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/persistencia/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 38/39: persistencia_service.py
# Directorio: servicios/persistencia
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./servicios/persistencia/persistencia_service.py
# ==============================================================================

"""
Servicio para persistir y recuperar pedidos en disco.
"""

import pickle
import os
from datetime import datetime
from constantes import DIRECTORIO_PEDIDOS, PREFIJO_ARCHIVO_PEDIDO, EXTENSION_DATA
from excepciones.persistencia_exception import PersistenciaException

if False:  # TYPE_CHECKING
    from entidades.pedido.pedido_mesa import PedidoMesa


class PersistenciaService:
    """
    Servicio para operaciones de persistencia con Pickle.
    """

    def guardar_pedido(self, pedido: 'PedidoMesa') -> None:
        """
        Guarda un pedido en disco usando Pickle.
        
        Args:
            pedido: Pedido a guardar
            
        Raises:
            PersistenciaException: Si ocurre un error al guardar
        """
        nombre_archivo = ""
        try:
            # Crear directorio si no existe
            os.makedirs(DIRECTORIO_PEDIDOS, exist_ok=True)

            # Generar nombre de archivo
            timestamp = int(datetime.now().timestamp())
            numero_mesa = pedido.get_numero_mesa()
            nombre_archivo = f"{PREFIJO_ARCHIVO_PEDIDO}{numero_mesa}_{timestamp}{EXTENSION_DATA}"
            ruta_completa = os.path.join(DIRECTORIO_PEDIDOS, nombre_archivo)

            # Serializar y guardar
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(pedido, archivo)

            print(f"Pedido de Mesa {numero_mesa} persistido exitosamente en {ruta_completa}")

        except Exception as e:
            raise PersistenciaException(
                mensaje="Error al guardar pedido",
                nombre_archivo=nombre_archivo,
                tipo_operacion="ESCRITURA",
                causa=str(e)
            )

    def cargar_pedido(self, nombre_archivo: str) -> 'PedidoMesa':
        """
        Carga un pedido desde disco.
        
        Args:
            nombre_archivo: Nombre del archivo a cargar
            
        Returns:
            PedidoMesa: Pedido recuperado
            
        Raises:
            PersistenciaException: Si ocurre un error al cargar
        """
        ruta_completa = os.path.join(DIRECTORIO_PEDIDOS, nombre_archivo)

        try:
            if not os.path.exists(ruta_completa):
                raise FileNotFoundError(f"Archivo no encontrado: {ruta_completa}")

            with open(ruta_completa, 'rb') as archivo:
                pedido = pickle.load(archivo)

            print(f"Pedido recuperado exitosamente desde {ruta_completa}")
            return pedido

        except FileNotFoundError as e:
            raise PersistenciaException(
                mensaje="Archivo de pedido no encontrado",
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA",
                causa=str(e)
            )
        except Exception as e:
            raise PersistenciaException(
                mensaje="Error al cargar pedido",
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA",
                causa=str(e)
            )

    def listar_pedidos_guardados(self) -> list:
        """
        Lista todos los archivos de pedidos guardados.
        
        Returns:
            list: Lista de nombres de archivos ordenados por fecha (más recientes primero)
        """
        if not os.path.exists(DIRECTORIO_PEDIDOS):
            return []

        archivos = [
            f for f in os.listdir(DIRECTORIO_PEDIDOS)
            if f.endswith(EXTENSION_DATA)
        ]

        # Ordenar por timestamp (más recientes primero)
        archivos.sort(reverse=True)

        return archivos


################################################################################
# DIRECTORIO: tests
################################################################################

# ==============================================================================
# ARCHIVO 39/39: __init__.py
# Directorio: tests
# Ruta completa: /home/renata/Diseño de Sistemas/python_restaurante/./tests/__init__.py
# ==============================================================================




################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 39
# Generado: 2025-11-04 16:43:29
################################################################################
