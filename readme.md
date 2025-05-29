# 🧪 Ecowatch

Este proyecto tiene como objetivo realizar la lectura, validación y almacenamiento temporal de datos provenientes de distintas fuentes, asegurando su integridad y permitiendo un procesamiento eficiente.

---

## 📌 Características Principales

### 🧠 Diseño de la Solución

#### 🧮 Cache Temporal (Sliding Window)

Aunque no se llegó a implementar completamente, el diseño contempla el uso de una estrategia de **ventana deslizante** para mantener los datos de los últimos 5 minutos en memoria.  
Se propone el uso de un `OrderedDict` o `SortedDict`, lo cual permite:

- Mantener orden cronológico eficiente.
- Facilitar el descarte de datos antiguos.
- Consultas rápidas por timestamp o por clave (por ejemplo, sala).

#### ✅ Validación de Columnas (Builder Pattern)

La validación de datos se construye mediante el **patrón Builder**, lo que permite agregar nuevas reglas de validación de forma modular y fluida. Actualmente, se incluyen:

- `with_column_check`: Verifica que las columnas requeridas estén presentes.
- `with_non_nulls`: Asegura que los valores de las columnas críticas no sean nulos.

Esto facilita la escalabilidad del sistema de validación, permitiendo incorporar futuras reglas sin alterar el flujo actual.

#### 🗃️ Lectura de Fuentes (Factory Pattern)

El sistema de lectura de datos se implementa utilizando el **patrón Factory**, lo que habilita el soporte a múltiples orígenes sin acoplar la lógica del lector a un único tipo de fuente.  
Actualmente se soportan rutas locales, pero el diseño permite extender fácilmente a:

- APIs REST
- Bases de datos SQL/NoSQL
- Archivos Excel, JSON, etc.

#### 🗃️ UI (Decorator Pattern)
La función `pretty_print_df` se usa como un decorador para embellecer la salida en la línea de comandos.

