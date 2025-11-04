# 📋 Historias de Usuario - Sistema de Gestión de Restaurante (Python)

## Información del Proyecto

**Proyecto:** PythonRestaurante
**Versión:** 1.0.0
**Fecha:** Noviembre 2025
**Metodología:** User Story Mapping
**Equipo:** Desarrollo Gastronomía Digital

---

## Índice

1. [Epic 1: Gestión de Configuración del Sistema](#epic-1-gestion-de-configuracion-del-sistema)
2. [Epic 2: Menú del Restaurante](#epic-2-menu-del-restaurante)
3. [Epic 3: Sistema de Alertas de Cocina](#epic-3-sistema-de-alertas-de-cocina)
4. [Epic 4: Proceso de Pedido y Pago](#epic-4-proceso-de-pedido-y-pago)
5. [Epic 5: Operaciones de Negocio](#epic-5-operaciones-de-negocio)
6. [Epic 6: Persistencia y Reportes](#epic-6-persistencia-y-reportes)
7. [Historias Técnicas (Patrones de Diseño)](#historias-tecnicas-patrones-de-diseno)
8. [Resumen de Prioridades](#resumen-de-prioridades)
9. [Estimación Total](#estimacion-total)
10. [Definición de Terminado](#definicion-de-terminado)
11. [Glosario](#glosario)

---

## Epic 1: Gestión de Configuración del Sistema

### US-001: Configuración Única del Restaurante (Patrón Singleton)

**Como** administrador del restaurante
**Quiero** que exista una única instancia de configuración del sistema
**Para** garantizar consistencia en parámetros como nombre, dirección y horarios

#### Criterios de Aceptación

- [x] Solo puede existir una instancia de `ConfiguracionRestaurante` en todo el sistema
- [x] Todas las solicitudes de configuración retornan la misma instancia
- [x] La configuración se carga de forma lazy (solo cuando se solicita por primera vez)
- [x] El constructor `__new__` controla la instanciación
- [x] El método `get_instance()` es thread-safe con Lock
- [x] Almacena: nombre del restaurante, dirección, teléfono, horario apertura/cierre, capacidad de mesas

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** Ninguna

#### Detalles Técnicos

**Clase**: `ConfiguracionRestaurante` (`python_restaurante/config/configuracion_restaurante.py`)
**Patrón**: Singleton

**Trazabilidad**: `main.py` líneas 15-25

---

## Epic 2: Menú del Restaurante

### US-002: Creación de Platos mediante Factory (Patrón Factory)

**Como** chef del restaurante
**Quiero** crear diferentes tipos de platos de forma estandarizada
**Para** mantener consistencia en la creación de elementos del menú

#### Criterios de Aceptación

- [x] `PlatoFactory` puede crear Entradas con nombre, precio e ingredientes principales
- [x] `PlatoFactory` puede crear PlatosPrincipales con nombre, precio y tiempo de preparación
- [x] `PlatoFactory` puede crear Postres con nombre, precio y calorías
- [x] Método estático `crear_plato()` acepta tipo como string
- [x] Métodos estáticos `_crear_entrada()`, `_crear_principal()` y `_crear_postre()`
- [x] Se lanza `ValueError` para tipos no válidos
- [x] Todos los platos heredan de clase abstracta `Plato`
- [x] NO usar lambdas - usar métodos estáticos dedicados

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** Ninguna

#### Detalles Técnicos

**Clase**: `PlatoFactory` (`python_restaurante/patrones/factory/plato_factory.py`)
**Patrón**: Factory Method

**Trazabilidad**: `main.py` líneas 30-55

---

### US-003: Visualización de Detalles de Platos

**Como** mesero del restaurante
**Quiero** ver la información detallada de cada plato
**Para** informar correctamente a los clientes sobre el menú

#### Criterios de Aceptación

- [x] Las Entradas muestran: nombre, ingredientes principales y precio
- [x] Los Platos Principales muestran: nombre, tiempo de preparación en minutos y precio
- [x] Los Postres muestran: nombre, calorías y precio
- [x] El formato de salida es legible y consistente
- [x] Los precios se muestran con símbolo $ y 2 decimales
- [x] Cada tipo implementa método abstracto `mostrar_detalle()`

**Prioridad:** Media
**Estimación:** 2 puntos
**Dependencias:** US-002

**Trazabilidad**: `main.py` líneas 58-65

---

## Epic 3: Sistema de Alertas de Cocina

### US-004: Suscripción de Estaciones de Cocina a Alertas (Patrón Observer)

**Como** jefe de cocina
**Quiero** que las estaciones de cocina se suscriban a alertas de pedidos
**Para** coordinar la preparación de platos de manera eficiente

#### Criterios de Aceptación

- [x] Las estaciones (Parrilla, Ensaladas, Postres) pueden suscribirse al sistema de pedidos
- [x] Las estaciones pueden desuscribirse en cualquier momento
- [x] Un sistema de pedidos puede tener múltiples estaciones suscritas
- [x] Al suscribirse se confirma la acción con mensaje indicando la estación
- [x] Al desuscribirse se confirma la acción con mensaje
- [x] Implementar patrón Observer con clase genérica `Observable[T]`
- [x] Thread-safe en las operaciones de suscripción

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** Ninguna

**Trazabilidad**: `main.py` líneas 70-85

---

### US-005: Notificación de Nuevos Pedidos a Estaciones

**Como** sistema de pedidos
**Quiero** notificar nuevos pedidos a todas las estaciones suscritas
**Para** que cada área de cocina prepare los platos correspondientes

#### Criterios de Aceptación

- [x] Al recibir un nuevo pedido, todas las estaciones suscritas reciben notificación
- [x] Las estaciones no suscritas no reciben notificaciones
- [x] El mensaje de pedido incluye número de mesa y detalle del plato
- [x] Se muestra el número total de estaciones notificadas
- [x] Las notificaciones se envían de forma síncrona e inmediata
- [x] El sistema usa tipo genérico `Observable[dict]` para enviar datos del pedido

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** US-004

**Trazabilidad**: `main.py` líneas 88-100

---

## Epic 4: Proceso de Pedido y Pago

### US-006: Gestión de Pedido de Mesa

**Como** mesero
**Quiero** agregar platos al pedido de una mesa
**Para** registrar correctamente lo que ordenan los clientes

#### Criterios de Aceptación

- [x] Puedo agregar cualquier tipo de plato al pedido
- [x] El pedido confirma cada plato agregado con mensaje
- [x] El pedido calcula el total sumando precios de todos los platos
- [x] Puedo ver todos los platos en el pedido antes de facturar
- [x] El pedido valida que no esté vacío antes de procesar pago
- [x] Cada pedido tiene asociado un número de mesa (int positivo)
- [x] Lista de platos es inmutable (defensive copy)

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** US-002

**Trazabilidad**: `main.py` líneas 105-125

---

### US-007: Selección de Forma de Pago (Patrón Strategy)

**Como** cliente
**Quiero** seleccionar mi forma de pago preferida
**Para** abonar la cuenta de manera conveniente

#### Criterios de Aceptación

- [x] Puedo pagar con tarjeta de crédito/débito
- [x] Puedo pagar en efectivo con 10% descuento
- [x] Puedo pagar con transferencia bancaria usando CBU
- [x] La forma de pago se puede cambiar antes de procesar
- [x] El sistema valida que haya una forma de pago seleccionada
- [x] Implementar patrón Strategy con interfaz `EstrategiaPago`
- [x] Tres estrategias concretas: `PagoTarjeta`, `PagoEfectivo`, `PagoTransferencia`

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** US-006

**Trazabilidad**: `main.py` líneas 130-145

---

### US-008: Procesamiento de Pago con Tarjeta

**Como** cliente
**Quiero** pagar con tarjeta de crédito/débito
**Para** abonar mi cuenta de forma rápida y segura

#### Criterios de Aceptación

- [x] Se solicita número de tarjeta
- [x] Solo se muestran los últimos 4 dígitos por seguridad
- [x] Se procesa el pago por el monto total exacto
- [x] Se solicita número de cuotas (1, 3, 6, 12)
- [x] Se confirma el pago exitoso con detalles
- [x] Se valida que el número de cuotas sea válido

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** US-007

**Trazabilidad**: `main.py` líneas 150-165

---

### US-009: Procesamiento de Pago en Efectivo con Descuento

**Como** cliente
**Quiero** pagar en efectivo y recibir descuento
**Para** ahorrar dinero en mi consumo

#### Criterios de Aceptación

- [x] Se aplica 10% de descuento automático al pagar en efectivo
- [x] Se muestra el monto original
- [x] Se muestra el descuento aplicado en pesos
- [x] Se muestra el monto final con descuento
- [x] El cálculo del descuento es correcto (monto * 0.90)

**Prioridad:** Media
**Estimación:** 2 puntos
**Dependencias:** US-007

**Trazabilidad**: `main.py` líneas 170-180

---

### US-010: Procesamiento de Pago con Transferencia Bancaria

**Como** cliente
**Quiero** pagar con transferencia bancaria
**Para** utilizar mi método de pago digital preferido

#### Criterios de Aceptación

- [x] Se solicita CBU o Alias de cuenta del cliente
- [x] Se muestra el CBU del restaurante (desde configuración)
- [x] Se procesa el pago por el monto total exacto
- [x] Se genera un código de referencia único (timestamp)
- [x] Se confirma el pago exitoso con todos los detalles

**Prioridad:** Media
**Estimación:** 2 puntos
**Dependencias:** US-007

**Trazabilidad**: `main.py` líneas 185-195

---

### US-011: Proceso Completo de Facturación

**Como** mesero
**Quiero** completar el proceso de facturación de una mesa
**Para** cerrar correctamente la cuenta de los clientes

#### Criterios de Aceptación

- [x] Se muestra número de mesa
- [x] Se muestra resumen de platos consumidos con detalles
- [x] Se muestra el total a pagar
- [x] Se procesa el pago con la forma seleccionada
- [x] Se confirma que el pago fue completado exitosamente
- [x] El formato de salida es profesional y claro
- [x] Se muestra fecha y hora de la transacción

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** US-006, US-007

**Trazabilidad**: `main.py` líneas 200-220

---

## Epic 5: Operaciones de Negocio

### US-012: Gestionar Múltiples Mesas del Restaurante

**Como** administrador del restaurante
**Quiero** gestionar múltiples mesas desde un servicio centralizado
**Para** tener control unificado de todos los pedidos activos

#### Criterios de Aceptación

- [x] El servicio debe permitir agregar pedidos de diferentes mesas
- [x] Buscar pedido por número de mesa
- [x] Listar todas las mesas activas
- [x] Calcular ingresos totales
- [x] Debe manejar múltiples pedidos simultáneamente
- [x] Debe usar diccionario interno `{numero_mesa: PedidoMesa}`
- [x] Validar que no existan pedidos duplicados para la misma mesa

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** US-006

**Trazabilidad**: `main.py` líneas 225-245

---

### US-013: Generar Reporte de Ventas Diarias

**Como** administrador
**Quiero** generar un reporte de ventas diarias
**Para** analizar el rendimiento del restaurante

#### Criterios de Aceptación

- [x] El reporte debe mostrar fecha, cantidad de pedidos, platos por tipo
- [x] Ingreso total del día e ingreso promedio por mesa
- [x] El formato debe ser profesional y legible
- [x] Se debe poder exportar a archivo de texto

**Prioridad:** Media
**Estimación:** 5 puntos
**Dependencias:** US-012

**Trazabilidad**: `main.py` líneas 250-260

---

## Epic 6: Persistencia y Reportes

### US-014: Persistir Pedido de Mesa en Disco

**Como** administrador del sistema
**Quiero** guardar pedidos en disco
**Para** mantener registros permanentes de todas las transacciones

#### Criterios de Aceptación

- [x] Serializar `PedidoMesa` completo con Pickle
- [x] Guardar en directorio `data/pedidos/`
- [x] Nombre: `mesa_{numero}_{timestamp}.dat`
- [x] Crear directorio si no existe
- [x] Mostrar mensaje de confirmación
- [x] Si ocurre error, lanzar `PersistenciaException`

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** US-006

**Trazabilidad**: `main.py` líneas 265-275

---

### US-015: Recuperar Pedido desde Disco

**Como** auditor
**Quiero** recuperar pedidos guardados previamente
**Para** consultar históricos y realizar auditorías

#### Criterios de Aceptación

- [x] Deserializar archivo `.dat` con Pickle
- [x] Buscar en directorio `data/pedidos/`
- [x] Validar que el archivo exista
- [x] Retornar `PedidoMesa` completo
- [x] Si archivo no existe o corrupto, lanzar `PersistenciaException`

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** US-014

**Trazabilidad**: `main.py` líneas 280-290

---

### US-016: Listar Todos los Pedidos Guardados

**Como** administrador
**Quiero** listar todos los pedidos guardados en disco
**Para** tener una vista completa del histórico

#### Criterios de Aceptación

- [x] Listar todos los archivos `.dat` en `data/pedidos/`
- [x] Ordenar por fecha (más recientes primero)
- [x] Mostrar información resumida
- [x] Manejar directorio vacío correctamente

**Prioridad:** Baja
**Estimación:** 2 puntos
**Dependencias:** US-014

**Trazabilidad**: `main.py` líneas 295-305

---

## Historias Técnicas (Patrones de Diseño)

### US-TECH-001: Implementar Singleton para ConfiguracionRestaurante

**Como** arquitecto de software
**Quiero** garantizar una única instancia de la configuración
**Para** compartir estado consistente en todo el sistema

**Prioridad:** Alta
**Estimación:** 3 puntos
**Dependencias:** Ninguna

---

### US-TECH-002: Implementar Factory Method para Creación de Platos

**Como** arquitecto de software
**Quiero** centralizar creación de platos mediante Factory Method
**Para** desacoplar cliente de clases concretas

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** Ninguna

---

### US-TECH-003: Implementar Observer Pattern para Sistema de Pedidos

**Como** arquitecto de software
**Quiero** implementar patrón Observer con Generics
**Para** notificar cambios de pedidos de forma tipo-segura

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** Ninguna

---

### US-TECH-004: Implementar Strategy Pattern para Formas de Pago

**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de pago
**Para** permitir diferentes estrategias según preferencia del cliente

**Prioridad:** Alta
**Estimación:** 5 puntos
**Dependencias:** US-006

---

## Resumen de Prioridades

### Alta (14 historias)
- US-001, US-002, US-004, US-005, US-006, US-007, US-008, US-011, US-012, US-014, US-015
- US-TECH-001, US-TECH-002, US-TECH-003, US-TECH-004

### Media (5 historias)
- US-003, US-009, US-010, US-013

### Baja (1 historia)
- US-016

---

## Estimación Total

**Total Puntos:** 56 puntos
**Sprint sugerido:** 3 sprints de 2 semanas

### Sprint 1 (20 puntos)
- Epic 1: Configuración (3 pts)
- Epic 2: Menú (7 pts)
- Epic 3: Alertas (8 pts)
- US-TECH-001 (2 pts)

### Sprint 2 (21 puntos)
- Epic 4: Pedido y Pago (20 pts)
- US-TECH-004 (1 pt)

### Sprint 3 (15 puntos)
- Epic 5: Operaciones (10 pts)
- Epic 6: Persistencia (8 pts)

---

## Definición de Terminado (DoD)

- [ ] Código implementado según criterios de aceptación
- [ ] Código ejecutado sin errores ni warnings
- [ ] Patrón de diseño correctamente implementado
- [ ] Casos de prueba ejecutados manualmente con éxito
- [ ] Código documentado con docstrings
- [ ] Output en consola es claro y profesional
- [ ] Integración con main.py funcional
- [ ] PEP 8 compliance verificado
- [ ] Type hints completos
- [ ] Defensive copies implementadas
- [ ] Manejo de excepciones apropiado
- [ ] Revisión de código completada

---

## Glosario

**Singleton:** Patrón que garantiza una única instancia de una clase

**Factory Method:** Patrón que encapsula la creación de objetos

**Observer:** Patrón uno-a-muchos donde cambios notifican dependientes

**Strategy:** Patrón de algoritmos intercambiables

**Observable:** Objeto que puede ser observado

**Context:** Clase que utiliza una estrategia

**Facturación:** Proceso de cerrar cuenta

**Persistencia:** Almacenamiento permanente en disco

**Pickle:** Módulo Python para serialización

**Defensive Copy:** Retornar copias de colecciones internas

**Type Hints:** Anotaciones de tipos en Python

**Thread-safe:** Código que funciona con múltiples threads

**Lazy Initialization:** Creación diferida hasta ser necesario

**Double-checked Locking:** Patrón de sincronización en Singleton

---

## Contacto

**Product Owner:** Gastronomía Digital Team
**Scrum Master:** [A definir]
**Equipo de Desarrollo:** [A definir]

---

**Última actualización:** Noviembre 2025
**Estado:** COMPLETO
**Cobertura funcional:** 100%
**Patrones implementados:** 4/4
