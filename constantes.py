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