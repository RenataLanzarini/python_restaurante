# 🍽️ PythonRestaurante - Sistema de Gestión de Restaurante

Sistema integral de gestión para restaurantes desarrollado en Python, implementando patrones de diseño profesionales para garantizar escalabilidad, mantenibilidad y robustez.

## 👨‍🎓 Información Académica

**Alumno:** María Renata Lanzarini
**Universidad:** Universidad de Mendoza 
**Materia:** Diseño de Sistemas
**Año Académico:** 2025  
**Carrera:** Ingeniería en Informática 

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Patrones de Diseño](#-patrones-de-diseño)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Funcionalidades Principales](#-funcionalidades-principales)
- [Ejemplos de Código](#-ejemplos-de-código)
- [Documentación](#-documentación)
- [Roadmap](#-roadmap)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

- **Gestión Centralizada**: Configuración única del restaurante mediante Singleton
- **Menú Flexible**: Sistema de creación de platos con Factory Method
- **Notificaciones en Tiempo Real**: Sistema de alertas a cocina con Observer Pattern
- **Múltiples Formas de Pago**: Strategy Pattern para tarjeta, efectivo y transferencia
- **Persistencia de Datos**: Serialización de pedidos con Pickle
- **Reportes de Ventas**: Análisis detallado de operaciones diarias
- **Gestión Multi-Mesa**: Control centralizado de pedidos activos
- **Thread-Safe**: Operaciones seguras en entornos concurrentes

## 🏗️ Patrones de Diseño

El sistema implementa 4 patrones de diseño creacionales y de comportamiento:

| Patrón | Implementación | Propósito |
|--------|---------------|-----------|
| **Singleton** | `ConfiguracionRestaurante` | Instancia única de configuración |
| **Factory Method** | `PlatoFactory` | Creación estandarizada de platos |
| **Observer** | `Observable<T>` + Estaciones de Cocina | Notificaciones de pedidos |
| **Strategy** | `EstrategiaPago` | Algoritmos intercambiables de pago |

## 🔧 Requisitos

- Python 3.8 o superior
- Sistema operativo: Windows, macOS o Linux
- Dependencias estándar de Python (incluidas en la biblioteca estándar)

## 📦 Instalación

### Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/python-restaurante.git
cd python-restaurante
```

### Configurar Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Verificar Instalación

```bash
python --version  # Debe ser 3.8+
python main.py
```

## 📁 Estructura del Proyecto

```
python_restaurante/
│
├── config/
│   └── configuracion_restaurante.py   # Singleton - Configuración única
│
├── patrones/
│   ├── factory/
│   │   ├── plato.py                   # Clase abstracta Plato
│   │   ├── plato_factory.py           # Factory Method
│   │   ├── entrada.py                 # Plato concreto
│   │   ├── plato_principal.py         # Plato concreto
│   │   └── postre.py                  # Plato concreto
│   │
│   ├── observer/
│   │   ├── observable.py              # Observable genérico
│   │   ├── observer.py                # Interfaz Observer
│   │   └── estacion_cocina.py         # Observador concreto
│   │
│   └── strategy/
│       ├── estrategia_pago.py         # Interfaz Strategy
│       ├── pago_tarjeta.py            # Strategy concreta
│       ├── pago_efectivo.py           # Strategy concreta
│       └── pago_transferencia.py      # Strategy concreta
│
├── modelos/
│   └── pedido_mesa.py                 # Gestión de pedidos
│
├── servicios/
│   ├── servicio_restaurante.py        # Lógica de negocio
│   └── persistencia_service.py        # Persistencia en disco
│
├── excepciones/
│   └── persistencia_exception.py      # Excepciones personalizadas
│
├── data/
│   └── pedidos/                       # Almacenamiento de pedidos
│
└── main.py                            # Punto de entrada
```

## 🚀 Uso

### Ejecución Básica

```bash
python main.py
```

### Flujo de Operación

1. **Configuración Inicial**: El sistema carga la configuración del restaurante
2. **Creación de Menú**: Se crean platos usando la fábrica
3. **Registro de Estaciones**: Las estaciones de cocina se suscriben a alertas
4. **Gestión de Pedidos**: Se procesan pedidos de múltiples mesas
5. **Procesamiento de Pagos**: Los clientes seleccionan su forma de pago
6. **Persistencia**: Los pedidos se guardan automáticamente
7. **Reportes**: Se generan análisis de ventas diarias

## 🎯 Funcionalidades Principales

### 1. Configuración del Restaurante (Singleton)

```python
from python_restaurante.config.configuracion_restaurante import ConfiguracionRestaurante

# Obtener instancia única
config = ConfiguracionRestaurante.get_instance()
print(f"Restaurante: {config.nombre}")
print(f"Horario: {config.horario_apertura} - {config.horario_cierre}")
```

### 2. Creación de Platos (Factory Method)

```python
from python_restaurante.patrones.factory.plato_factory import PlatoFactory

# Crear diferentes tipos de platos
entrada = PlatoFactory.crear_plato(
    tipo="entrada",
    nombre="Ensalada César",
    precio=850.0,
    ingredientes="Lechuga romana, parmesano, crutones"
)

principal = PlatoFactory.crear_plato(
    tipo="principal",
    nombre="Bife de Chorizo",
    precio=3500.0,
    tiempo_preparacion=25
)

postre = PlatoFactory.crear_plato(
    tipo="postre",
    nombre="Tiramisú",
    precio=1200.0,
    calorias=350
)
```

### 3. Sistema de Alertas (Observer)

```python
from python_restaurante.patrones.observer.observable import Observable
from python_restaurante.patrones.observer.estacion_cocina import EstacionCocina

# Crear sistema observable
sistema_pedidos = Observable()

# Suscribir estaciones
parrilla = EstacionCocina("Parrilla")
ensaladas = EstacionCocina("Ensaladas")

sistema_pedidos.suscribir(parrilla)
sistema_pedidos.suscribir(ensaladas)

# Notificar nuevo pedido
sistema_pedidos.notificar({
    "mesa": 5,
    "plato": "Bife de Chorizo"
})
```

### 4. Gestión de Pedidos y Pagos

```python
from python_restaurante.modelos.pedido_mesa import PedidoMesa
from python_restaurante.patrones.strategy.pago_efectivo import PagoEfectivo

# Crear pedido
pedido = PedidoMesa(numero_mesa=3)
pedido.agregar_plato(entrada)
pedido.agregar_plato(principal)
pedido.agregar_plato(postre)

# Seleccionar forma de pago (con 10% descuento)
pedido.establecer_forma_pago(PagoEfectivo())

# Facturar
pedido.facturar()
```

### 5. Persistencia de Datos

```python
from python_restaurante.servicios.persistencia_service import PersistenciaService

persistencia = PersistenciaService()

# Guardar pedido
persistencia.guardar_pedido(pedido)

# Recuperar pedido
pedido_recuperado = persistencia.cargar_pedido("mesa_3_20251104_143022.dat")

# Listar todos los pedidos
pedidos_guardados = persistencia.listar_pedidos()
```

### 6. Reportes de Ventas

```python
from python_restaurante.servicios.servicio_restaurante import ServicioRestaurante

servicio = ServicioRestaurante()

# Agregar múltiples pedidos
servicio.agregar_pedido(pedido_mesa_1)
servicio.agregar_pedido(pedido_mesa_2)

# Generar reporte
reporte = servicio.generar_reporte_ventas()
print(reporte)
```

## 💡 Ejemplos de Código

### Ejemplo Completo: Flujo de Pedido

```python
from python_restaurante.config.configuracion_restaurante import ConfiguracionRestaurante
from python_restaurante.patrones.factory.plato_factory import PlatoFactory
from python_restaurante.modelos.pedido_mesa import PedidoMesa
from python_restaurante.patrones.strategy.pago_tarjeta import PagoTarjeta

# 1. Configurar restaurante
config = ConfiguracionRestaurante.get_instance()

# 2. Crear platos
entrada = PlatoFactory.crear_plato("entrada", "Provoleta", 1200.0, "Queso provolone")
principal = PlatoFactory.crear_plato("principal", "Asado", 4500.0, 35)

# 3. Crear pedido
pedido = PedidoMesa(numero_mesa=8)
pedido.agregar_plato(entrada)
pedido.agregar_plato(principal)

# 4. Procesar pago con tarjeta
estrategia_tarjeta = PagoTarjeta(numero_tarjeta="4532-1234-5678-9010", cuotas=3)
pedido.establecer_forma_pago(estrategia_tarjeta)

# 5. Facturar
pedido.facturar()
```

### Ejemplo: Descuento en Efectivo

```python
from python_restaurante.patrones.strategy.pago_efectivo import PagoEfectivo

# Pago en efectivo con 10% descuento automático
pedido.establecer_forma_pago(PagoEfectivo())
pedido.facturar()
# Output: "Descuento aplicado: $570.00"
#         "Total a pagar: $5130.00"
```

### Ejemplo: Transferencia Bancaria

```python
from python_restaurante.patrones.strategy.pago_transferencia import PagoTransferencia

# Pago con transferencia
estrategia_transferencia = PagoTransferencia(
    cbu_cliente="0000003100010123456789",
    alias_cliente="mi.restaurante.favorito"
)
pedido.establecer_forma_pago(estrategia_transferencia)
pedido.facturar()
```

## 📚 Documentación

### Type Hints y Documentación

El proyecto utiliza type hints completos para mejor mantenibilidad:

```python
from typing import List, Optional
from decimal import Decimal

def agregar_plato(self, plato: Plato) -> None:
    """
    Agrega un plato al pedido.
    
    Args:
        plato: Instancia de Plato a agregar
        
    Raises:
        ValueError: Si el plato es None
    """
    if plato is None:
        raise ValueError("El plato no puede ser None")
    self._platos.append(plato)
```

### Defensive Copies

Se implementan copias defensivas para proteger colecciones internas:

```python
def obtener_platos(self) -> List[Plato]:
    """Retorna copia defensiva de la lista de platos."""
    return list(self._platos)
```

### Manejo de Excepciones

```python
from python_restaurante.excepciones.persistencia_exception import PersistenciaException

try:
    pedido = persistencia.cargar_pedido("archivo_inexistente.dat")
except PersistenciaException as e:
    print(f"Error al cargar pedido: {e}")
```

## 🗺️ Roadmap

### Versión 1.0.0 (Actual)
- ✅ Patrones de diseño fundamentales
- ✅ Gestión básica de pedidos
- ✅ Persistencia con Pickle
- ✅ Sistema de alertas

### Versión 1.1.0 (Próximo Release)
- ⏳ Interfaz gráfica con Tkinter
- ⏳ Base de datos SQLite
- ⏳ API REST con Flask
- ⏳ Autenticación de usuarios

### Versión 2.0.0 (Futuro)
- 📅 Sistema de reservas
- 📅 Integración con sistemas de delivery
- 📅 Dashboard de analíticas
- 📅 Aplicación móvil

## 📧 Contacto

**Alumno:** [Tu Nombre]  
**Email Institucional:** [tu.email@universidad.edu]  
**GitHub:** [tu-usuario]

## 🙏 Agradecimientos

- Universidad [Nombre Universidad] - Cátedra de [Materia]
- Comunidad Python por las excelentes herramientas
- Patrones de diseño basados en "Design Patterns" (Gang of Four)
- Profesor [Nombre] por la guía en el desarrollo

---

**Proyecto Académico** - [Nombre de la Materia]  
**Versión:** 1.0.0  
**Última Actualización:** Noviembre 2025  
**Estado del Proyecto:** ✅ Completado

Desarrollado como trabajo práctico para [Universidad] 🎓