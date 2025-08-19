# Guía Completa de Matplotlib - Visualización de Datos en Python

## Tabla de Contenidos
1. [Introducción y Configuración](#introducción-y-configuración)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Gráficos Básicos](#gráficos-básicos)
4. [Personalización de Gráficos](#personalización-de-gráficos)
5. [Tipos de Gráficos Avanzados](#tipos-de-gráficos-avanzados)
6. [Subplots y Layouts](#subplots-y-layouts)
7. [Anotaciones y Texto](#anotaciones-y-texto)
8. [Estilos y Temas](#estilos-y-temas)
9. [Exportación de Gráficos](#exportación-de-gráficos)
10. [Casos de Uso Prácticos](#casos-de-uso-prácticos)

---

## 1. Introducción y Configuración

### ¿Qué es Matplotlib?
Matplotlib es la biblioteca de visualización de datos más popular en Python. Proporciona una interfaz similar a MATLAB para crear gráficos estáticos, animados e interactivos.

### Instalación
```bash
pip install matplotlib
```

### Importación Básica
```python
import matplotlib.pyplot as plt
import numpy as np  # Útil para generar datos de ejemplo
```

### Configuración Inicial Recomendada
```python
# Configuración para mejor visualización en notebooks
%matplotlib inline

# Configuración de alta resolución
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300

# Configuración de fuentes para español
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False  # Para mostrar el signo menos correctamente
```

---

## 2. Conceptos Fundamentales

### Anatomía de una Figura

```python
# Componentes principales
fig = plt.figure()  # Contenedor principal (Figure)
ax = fig.add_subplot(111)  # Área de dibujo (Axes)

# Elementos del gráfico:
# - Title (título)
# - Labels (etiquetas de ejes)
# - Legend (leyenda)
# - Grid (cuadrícula)
# - Ticks (marcas en los ejes)
# - Spines (bordes del gráfico)
```

### Dos Interfaces de Matplotlib

#### 1. Interfaz de Estado (pyplot)
```python
# Estilo MATLAB - más simple para gráficos rápidos
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
```

#### 2. Interfaz Orientada a Objetos
```python
# Mayor control y flexibilidad
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
plt.show()
```

---

## 3. Gráficos Básicos

### Gráfico de Líneas
```python
# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Seno', color='blue', linewidth=2)
plt.plot(x, y2, label='Coseno', color='red', linewidth=2, linestyle='--')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Funciones Trigonométricas')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Gráfico de Dispersión
```python
# Generar datos aleatorios
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

# Crear gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=y, cmap='viridis', alpha=0.6, edgecolors='black')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Diagrama de Dispersión con Mapa de Color')
plt.colorbar(label='Valores de Y')
plt.show()
```

### Gráfico de Barras
```python
# Datos
categorias = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
valores = [85, 72, 68, 55, 40]
colores = ['#3776AB', '#F7DF1E', '#007396', '#00599C', '#CC342D']

# Gráfico de barras verticales
plt.figure(figsize=(10, 6))
barras = plt.bar(categorias, valores, color=colores, edgecolor='black', linewidth=1.5)

# Añadir valores encima de las barras
for barra, valor in zip(barras, valores):
    plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 1,
             str(valor), ha='center', va='bottom', fontweight='bold')

plt.xlabel('Lenguaje de Programación')
plt.ylabel('Popularidad (%)')
plt.title('Popularidad de Lenguajes de Programación 2024')
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Histograma
```python
# Generar datos con distribución normal
np.random.seed(42)
datos = np.random.normal(100, 15, 1000)

# Crear histograma
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(datos, bins=30, density=True, 
                            alpha=0.7, color='skyblue', 
                            edgecolor='black')

# Añadir curva de distribución normal
mu, sigma = datos.mean(), datos.std()
x = np.linspace(datos.min(), datos.max(), 100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * 
         np.exp(-0.5 * ((x - mu) / sigma)**2),
         'r-', linewidth=2, label='Distribución Normal')

plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title(f'Histograma con Curva Normal\nμ={mu:.2f}, σ={sigma:.2f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 4. Personalización de Gráficos

### Colores y Estilos de Línea
```python
# Diferentes formas de especificar colores
colores = [
    'red',           # Nombre
    '#FF5733',       # Hexadecimal
    (0.2, 0.4, 0.6), # RGB tuple
    'C0'             # Ciclo de colores por defecto
]

# Estilos de línea
estilos = ['-', '--', '-.', ':', 'None']

# Ejemplo práctico
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(12, 6))

for i, (color, estilo) in enumerate(zip(colores[:4], estilos[:4])):
    ax.plot(x, np.sin(x + i), color=color, linestyle=estilo, 
            linewidth=2, label=f'Línea {i+1}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Personalización de Colores y Estilos')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
```

### Marcadores
```python
# Tipos de marcadores comunes
marcadores = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
nombres = ['Círculo', 'Cuadrado', 'Triángulo arriba', 'Diamante', 
           'Triángulo abajo', 'Triángulo izq', 'Triángulo der', 
           'Pentágono', 'Estrella', 'Hexágono']

# Visualización de marcadores
fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(marcadores))

for i, (marcador, nombre) in enumerate(zip(marcadores, nombres)):
    y = np.ones_like(x) * i
    ax.plot(x, y, marker=marcador, markersize=15, linestyle='', 
            label=f'{marcador}: {nombre}')

ax.set_xlabel('Posición')
ax.set_ylabel('Tipo de Marcador')
ax.set_title('Tipos de Marcadores en Matplotlib')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Personalización de Ejes
```python
# Crear datos
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2)

# Personalizar ejes
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Configurar ticks del eje X
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Configurar ticks del eje Y
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

# Añadir líneas de referencia
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=np.pi, color='r', linestyle='--', alpha=0.5)

# Etiquetas y título
ax.set_xlabel('Ángulo (radianes)', fontsize=12)
ax.set_ylabel('Amplitud', fontsize=12)
ax.set_title('Función Seno con Ejes Personalizados', fontsize=14, fontweight='bold')

# Mover spines al centro
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.show()
```

---

## 5. Tipos de Gráficos Avanzados

### Gráfico de Pastel (Pie Chart)
```python
# Datos
sizes = [30, 25, 20, 15, 10]
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Otros']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)  # Separar el primer segmento

# Crear gráfico de pastel
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, 
                                   colors=colors, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

# Mejorar el aspecto del texto
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

ax.set_title('Distribución de Uso de Lenguajes de Programación', 
             fontsize=14, fontweight='bold')
plt.show()
```

### Gráfico de Caja (Box Plot)
```python
# Generar datos de ejemplo
np.random.seed(42)
data = [np.random.normal(100, 10, 200),
        np.random.normal(90, 20, 200),
        np.random.normal(110, 15, 200),
        np.random.normal(95, 25, 200)]

# Crear box plot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, labels=['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D'],
                patch_artist=True, notch=True, showmeans=True)

# Personalizar colores
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Personalizar otros elementos
for whisker in bp['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle=':')

ax.set_xlabel('Grupos', fontsize=12)
ax.set_ylabel('Valores', fontsize=12)
ax.set_title('Comparación de Distribuciones entre Grupos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
plt.show()
```

### Mapa de Calor (Heatmap)
```python
# Generar matriz de correlación de ejemplo
np.random.seed(42)
data = np.random.randn(10, 10)
correlation_matrix = np.corrcoef(data)

# Crear mapa de calor
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)

# Añadir barra de color
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Correlación', rotation=270, labelpad=20)

# Configurar ticks
ticks = np.arange(10)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels([f'Var {i+1}' for i in ticks])
ax.set_yticklabels([f'Var {i+1}' for i in ticks])

# Rotar etiquetas del eje x
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Añadir valores en cada celda
for i in range(10):
    for j in range(10):
        text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                      ha="center", va="center", color="black", fontsize=8)

ax.set_title('Matriz de Correlación', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Gráfico de Violín
```python
# Generar datos
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Crear gráfico de violín
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Violín básico
parts1 = ax1.violinplot(data, positions=range(1, 5), widths=0.7,
                        showmeans=True, showmedians=True)
ax1.set_title('Gráfico de Violín Básico')
ax1.set_xlabel('Grupo')
ax1.set_ylabel('Valores')

# Violín personalizado
parts2 = ax2.violinplot(data, positions=range(1, 5), widths=0.7,
                        showmeans=False, showmedians=False, showextrema=False)

# Personalizar colores
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for pc, color in zip(parts2['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_alpha(0.7)

# Añadir cuartiles
quartile1, medians, quartile3 = [], [], []
for d in data:
    quartile1.append(np.percentile(d, 25))
    medians.append(np.percentile(d, 50))
    quartile3.append(np.percentile(d, 75))

ax2.scatter(range(1, 5), medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(range(1, 5), quartile1, quartile3, color='k', linestyle='-', lw=5)

ax2.set_title('Gráfico de Violín Personalizado')
ax2.set_xlabel('Grupo')
ax2.set_ylabel('Valores')

plt.tight_layout()
plt.show()
```

---

## 6. Subplots y Layouts

### Subplots Básicos
```python
# Crear una figura con 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Datos
x = np.linspace(0, 10, 100)

# Subplot 1: Línea
axes[0, 0].plot(x, np.sin(x), 'b-')
axes[0, 0].set_title('Gráfico de Línea')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('sin(x)')

# Subplot 2: Dispersión
axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.5)
axes[0, 1].set_title('Gráfico de Dispersión')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')

# Subplot 3: Barras
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values, color='green', alpha=0.7)
axes[1, 0].set_title('Gráfico de Barras')
axes[1, 0].set_ylabel('Valores')

# Subplot 4: Histograma
data = np.random.normal(100, 15, 500)
axes[1, 1].hist(data, bins=20, color='orange', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('Histograma')
axes[1, 1].set_xlabel('Valor')
axes[1, 1].set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()
```

### GridSpec para Layouts Complejos
```python
import matplotlib.gridspec as gridspec

# Crear figura y GridSpec
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, figure=fig)

# Subplot grande (2x2)
ax1 = fig.add_subplot(gs[0:2, 0:2])
ax1.plot(np.random.randn(100).cumsum())
ax1.set_title('Gráfico Principal')

# Subplots pequeños
ax2 = fig.add_subplot(gs[0, 2])
ax2.bar(['A', 'B', 'C'], [3, 7, 5])
ax2.set_title('Barras')

ax3 = fig.add_subplot(gs[1, 2])
ax3.pie([30, 40, 30], labels=['X', 'Y', 'Z'])
ax3.set_title('Pastel')

# Subplot largo horizontal
ax4 = fig.add_subplot(gs[2, :])
x = np.linspace(0, 10, 100)
ax4.fill_between(x, np.sin(x), alpha=0.3)
ax4.plot(x, np.sin(x), 'r-', linewidth=2)
ax4.set_title('Gráfico con Área Sombreada')
ax4.set_xlabel('X')

plt.tight_layout()
plt.show()
```

### Subplots con Ejes Compartidos
```python
# Crear subplots con ejes compartidos
fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

# Datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Graficar en cada subplot
axes[0].plot(x, y1, 'b-', label='sin(x)')
axes[0].set_ylabel('sin(x)')
axes[0].legend(loc='upper right')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, y2, 'r-', label='cos(x)')
axes[1].set_ylabel('cos(x)')
axes[1].legend(loc='upper right')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, y3, 'g-', label='sin(x)·cos(x)')
axes[2].set_xlabel('X')
axes[2].set_ylabel('sin(x)·cos(x)')
axes[2].legend(loc='upper right')
axes[2].grid(True, alpha=0.3)

# Título general
fig.suptitle('Funciones Trigonométricas con Ejes X Compartidos', 
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()
```

---

## 7. Anotaciones y Texto

### Anotaciones Básicas
```python
# Crear datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x, y, 'b-', linewidth=2)

# Encontrar máximo
max_idx = np.argmax(y)
max_x, max_y = x[max_idx], y[max_idx]

# Anotación con flecha
ax.annotate('Máximo local',
            xy=(max_x, max_y),  # Punto a señalar
            xytext=(max_x + 1, max_y - 0.5),  # Posición del texto
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, color='red',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Encontrar mínimo
min_idx = np.argmin(y)
min_x, min_y = x[min_idx], y[min_idx]

# Anotación simple
ax.annotate('Mínimo local',
            xy=(min_x, min_y),
            xytext=(min_x - 1.5, min_y + 0.5),
            arrowprops=dict(arrowstyle='fancy', color='blue', lw=1.5),
            fontsize=12, color='blue')

# Añadir texto simple
ax.text(5, 0.5, 'Función Seno', fontsize=16, 
        bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Anotaciones en Matplotlib')
ax.grid(True, alpha=0.3)
plt.show()
```

### Flechas y Formas
```python
fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar diferentes tipos de flechas
arrow_styles = ['->', '-[', '|-|', '-|>', '<->', 'fancy', 'simple', 'wedge']
y_positions = np.arange(len(arrow_styles))

for i, style in enumerate(arrow_styles):
    ax.annotate('', xy=(0.8, i), xytext=(0.2, i),
                arrowprops=dict(arrowstyle=style, lw=2, color=f'C{i}'))
    ax.text(0.85, i, style, va='center', fontsize=12)

# Añadir formas
from matplotlib.patches import Circle, Rectangle, Ellipse, FancyBboxPatch

circle = Circle((0.5, 8), 0.2, color='lightblue', alpha=0.7)
ax.add_patch(circle)
ax.text(0.5, 8, 'Círculo', ha='center', va='center')

rect = Rectangle((0.3, 9), 0.4, 0.5, color='lightgreen', alpha=0.7)
ax.add_patch(rect)
ax.text(0.5, 9.25, 'Rectángulo', ha='center', va='center')

ax.set_xlim(0, 1)
ax.set_ylim(-1, 10)
ax.set_title('Tipos de Flechas y Formas', fontsize=14, fontweight='bold')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
```

---

## 8. Estilos y Temas

### Estilos Predefinidos
```python
# Listar estilos disponibles
print("Estilos disponibles:", plt.style.available)

# Ejemplos de diferentes estilos
styles = ['default', 'seaborn', 'ggplot', 'bmh', 'dark_background']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

x = np.linspace(0, 10, 100)
y = np.sin(x)

for ax, style in zip(axes[:5], styles):
    with plt.style.context(style):
        ax.plot(x, y, label='sin(x)')
        ax.plot(x, np.cos(x), label='cos(x)')
        ax.set_title(f'Estilo: {style}')
        ax.legend()
        ax.grid(True)

# Ocultar el último subplot vacío
axes[5].set_visible(False)

plt.tight_layout()
plt.show()
```

### Crear Estilo Personalizado
```python
# Definir parámetros personalizados
custom_params = {
    'figure.figsize': (10, 6),
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'lines.linewidth': 2,
    'lines.markersize': 8,
    'axes.prop_cycle': plt.cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', 
                                         '#d62728', '#9467bd']),
}

# Aplicar estilo personalizado
plt.rcParams.update(custom_params)

# Ejemplo con estilo personalizado
x = np.linspace(0, 10, 50)
fig, ax = plt.subplots()

for i in range(5):
    ax.plot(x, np.sin(x + i*0.5), label=f'Serie {i+1}')

ax.set_xlabel('Tiempo')
ax.set_ylabel('Valor')
ax.set_title('Gráfico con Estilo Personalizado')
ax.legend()
plt.show()

# Resetear a valores por defecto
plt.rcdefaults()
```

---

## 9. Exportación de Gráficos

### Guardar en Diferentes Formatos
```python
# Crear un gráfico de ejemplo
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', label='sin(x)')
ax.plot(x, np.cos(x), 'r-', label='cos(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Gráfico para Exportar')
ax.legend()
ax.grid(True, alpha=0.3)

# Guardar en diferentes formatos
# PNG - Mejor para web y presentaciones
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')

# PDF - Mejor para documentos LaTeX
plt.savefig('grafico.pdf', bbox_inches='tight')

# SVG - Formato vectorial escalable
plt.savefig('grafico.svg', bbox_inches='tight')

# EPS - Para publicaciones científicas
plt.savefig('grafico.eps', bbox_inches='tight')

# Con fondo transparente
plt.savefig('grafico_transparente.png', dpi=300, 
            bbox_inches='tight', transparent=True)

plt.show()
```

### Configuración Avanzada de Exportación
```python
# Parámetros de exportación
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.random.randn(100).cumsum())

# Opciones de guardado
plt.savefig('grafico_avanzado.png',
            dpi=300,                    # Resolución
            bbox_inches='tight',        # Ajustar márgenes
            pad_inches=0.1,            # Padding adicional
            facecolor='white',         # Color de fondo
            edgecolor='none',          # Color del borde
            transparent=False,         # Fondo transparente
            metadata={'Author': 'Tu Nombre',  # Metadatos
                     'Title': 'Mi Gráfico',
                     'Subject': 'Visualización de Datos'})
```

---

## 10. Casos de Uso Prácticos

### Caso 1: Análisis de Ventas Mensuales
```python
# Datos de ventas
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas_2023 = [45000, 52000, 48000, 61000, 58000, 67000,
                72000, 69000, 63000, 59000, 55000, 71000]
ventas_2024 = [48000, 54000, 51000, 63000, 62000, 70000,
                75000, 73000, 68000, 64000, 60000, 76000]

# Crear figura con múltiples visualizaciones
fig = plt.figure(figsize=(16, 10))

# 1. Gráfico de líneas comparativo
ax1 = plt.subplot(2, 3, 1)
ax1.plot(meses, ventas_2023, marker='o', label='2023', linewidth=2)
ax1.plot(meses, ventas_2024, marker='s', label='2024', linewidth=2)
ax1.set_title('Comparación de Ventas 2023 vs 2024')
ax1.set_xlabel('Mes')
ax1.set_ylabel('Ventas ($)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# 2. Gráfico de barras agrupadas
ax2 = plt.subplot(2, 3, 2)
x = np.arange(len(meses))
width = 0.35
ax2.bar(x - width/2, ventas_2023, width, label='2023', alpha=0.8)
ax2.bar(x + width/2, ventas_2024, width, label='2024', alpha=0.8)
ax2.set_title('Ventas Mensuales por Año')
ax2.set_xticks(x)
ax2.set_xticklabels(meses, rotation=45)
ax2.legend()
ax2.set_ylabel('Ventas ($)')

# 3. Diferencia entre años
ax3 = plt.subplot(2, 3, 3)
diferencia = np.array(ventas_2024) - np.array(ventas_2023)
colors = ['green' if d > 0 else 'red' for d in diferencia]
ax3.bar(meses, diferencia, color=colors, alpha=0.7)
ax3.set_title('Diferencia de Ventas (2024 - 2023)')
ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax3.set_ylabel('Diferencia ($)')
ax3.tick_params(axis='x', rotation=45)

# 4. Gráfico de área acumulada
ax4 = plt.subplot(2, 3, 4)
ax4.fill_between(range(len(meses)), ventas_2023, alpha=0.3, label='2023')
ax4.fill_between(range(len(meses)), ventas_2024, alpha=0.3, label='2024')
ax4.set_title('Área de Ventas')
ax4.set_xticks(range(len(meses)))
ax4.set_xticklabels(meses, rotation=45)
ax4.legend()
ax4.set_ylabel('Ventas ($)')

# 5. Box plot trimestral
ax5 = plt.subplot(2, 3, 5)
q1_2023 = ventas_2023[:3]
q2_2023 = ventas_2023[3:6]
q3_2023 = ventas_2023[6:9]
q4_2023 = ventas_2023[9:]
data_trimestral = [q1_2023, q2_2023, q3_2023, q4_2023]
ax5.boxplot(data_trimestral, labels=['Q1', 'Q2', 'Q3', 'Q4'])
ax5.set_title('Distribución de Ventas por Trimestre 2023')
ax5.set_ylabel('Ventas ($)')

# 6. Gráfico circular de proporción anual
ax6 = plt.subplot(2, 3, 6)
total_2023 = sum(ventas_2023)
total_2024 = sum(ventas_2024)
sizes = [total_2023, total_2024]
labels = ['2023', '2024']
colors = ['#ff9999', '#66b3ff']
ax6.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, explode=(0, 0.1))
ax6.set_title('Proporción de Ventas Totales')

plt.suptitle('Dashboard de Análisis de Ventas', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Caso 2: Visualización de Datos Científicos
```python
# Simular datos de experimento
np.random.seed(42)
tiempo = np.linspace(0, 10, 1000)
señal = np.sin(2 * np.pi * tiempo) + 0.5 * np.sin(10 * np.pi * tiempo)
ruido = np.random.normal(0, 0.2, len(tiempo))
señal_con_ruido = señal + ruido

# Crear visualización científica
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

# 1. Señal original vs con ruido
axes[0, 0].plot(tiempo, señal, 'b-', label='Señal limpia', alpha=0.7)
axes[0, 0].plot(tiempo, señal_con_ruido, 'r-', label='Señal con ruido', 
                alpha=0.5, linewidth=0.5)
axes[0, 0].set_xlabel('Tiempo (s)')
axes[0, 0].set_ylabel('Amplitud')
axes[0, 0].set_title('Comparación de Señales')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 2. Distribución del ruido
axes[0, 1].hist(ruido, bins=50, density=True, alpha=0.7, 
                color='green', edgecolor='black')
axes[0, 1].set_xlabel('Valor del ruido')
axes[0, 1].set_ylabel('Densidad')
axes[0, 1].set_title('Distribución del Ruido')
mu, sigma = ruido.mean(), ruido.std()
x = np.linspace(ruido.min(), ruido.max(), 100)
axes[0, 1].plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * 
                np.exp(-0.5 * ((x - mu) / sigma)**2),
                'r-', linewidth=2, label=f'Normal(μ={mu:.3f}, σ={sigma:.3f})')
axes[0, 1].legend()

# 3. Análisis de Fourier
from scipy import signal as sp_signal
frecuencias, potencia = sp_signal.periodogram(señal_con_ruido, 
                                              fs=len(tiempo)/10)
axes[1, 0].semilogy(frecuencias, potencia)
axes[1, 0].set_xlabel('Frecuencia (Hz)')
axes[1, 0].set_ylabel('Densidad Espectral de Potencia')
axes[1, 0].set_title('Espectro de Frecuencias')
axes[1, 0].grid(True, alpha=0.3)

# 4. Espectrograma
axes[1, 1].specgram(señal_con_ruido, Fs=len(tiempo)/10, cmap='viridis')
axes[1, 1].set_xlabel('Tiempo (s)')
axes[1, 1].set_ylabel('Frecuencia (Hz)')
axes[1, 1].set_title('Espectrograma')

# 5. Autocorrelación
from scipy import signal as scipy_signal
correlacion = scipy_signal.correlate(señal_con_ruido[:200], 
                                     señal_con_ruido[:200], mode='full')
lags = scipy_signal.correlation_lags(200, 200, mode='full')
axes[2, 0].plot(lags, correlacion)
axes[2, 0].set_xlabel('Retraso')
axes[2, 0].set_ylabel('Autocorrelación')
axes[2, 0].set_title('Función de Autocorrelación')
axes[2, 0].grid(True, alpha=0.3)

# 6. Diagrama de fase
axes[2, 1].plot(señal[:-1], señal[1:], 'b.', markersize=1, alpha=0.5)
axes[2, 1].set_xlabel('x(t)')
axes[2, 1].set_ylabel('x(t+1)')
axes[2, 1].set_title('Diagrama de Fase')
axes[2, 1].grid(True, alpha=0.3)

plt.suptitle('Análisis de Señales', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Caso 3: Dashboard Financiero
```python
# Generar datos financieros simulados
np.random.seed(42)
fechas = pd.date_range('2024-01-01', periods=365, freq='D')
precio_inicial = 100
retornos = np.random.normal(0.001, 0.02, len(fechas))
precios = precio_inicial * np.exp(np.cumsum(retornos))
volumen = np.random.uniform(1000000, 5000000, len(fechas))
media_movil_20 = pd.Series(precios).rolling(window=20).mean()
media_movil_50 = pd.Series(precios).rolling(window=50).mean()

# Crear dashboard financiero
fig = plt.figure(figsize=(16, 12))
gs = gridspec.GridSpec(4, 2, height_ratios=[2, 1, 1, 1])

# 1. Gráfico de precios principal
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(fechas, precios, label='Precio', color='black', linewidth=1)
ax1.plot(fechas, media_movil_20, label='MA20', color='blue', alpha=0.7)
ax1.plot(fechas, media_movil_50, label='MA50', color='red', alpha=0.7)
ax1.fill_between(fechas, precios, precio_inicial, 
                 where=(precios >= precio_inicial), 
                 facecolor='green', alpha=0.3, interpolate=True)
ax1.fill_between(fechas, precios, precio_inicial, 
                 where=(precios < precio_inicial), 
                 facecolor='red', alpha=0.3, interpolate=True)
ax1.set_title('Precio de la Acción - 2024', fontsize=14, fontweight='bold')
ax1.set_ylabel('Precio ($)')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# 2. Volumen de transacciones
ax2 = fig.add_subplot(gs[1, :], sharex=ax1)
ax2.bar(fechas, volumen, color='gray', alpha=0.5)
ax2.set_ylabel('Volumen')
ax2.set_title('Volumen de Transacciones')
ax2.grid(True, alpha=0.3)

# 3. Retornos diarios
ax3 = fig.add_subplot(gs[2, 0])
ax3.hist(retornos, bins=50, color='blue', alpha=0.7, edgecolor='black')
ax3.set_xlabel('Retorno Diario')
ax3.set_ylabel('Frecuencia')
ax3.set_title('Distribución de Retornos')
ax3.axvline(x=0, color='red', linestyle='--', alpha=0.5)

# 4. Q-Q Plot
from scipy import stats
ax4 = fig.add_subplot(gs[2, 1])
stats.probplot(retornos, dist="norm", plot=ax4)
ax4.set_title('Q-Q Plot')

# 5. Retornos acumulados
ax5 = fig.add_subplot(gs[3, 0])
retornos_acum = (1 + pd.Series(retornos)).cumprod() - 1
ax5.plot(fechas, retornos_acum * 100)
ax5.set_xlabel('Fecha')
ax5.set_ylabel('Retorno Acumulado (%)')
ax5.set_title('Retorno Acumulado')
ax5.grid(True, alpha=0.3)

# 6. Métricas clave
ax6 = fig.add_subplot(gs[3, 1])
ax6.axis('off')
metrics_text = f"""
MÉTRICAS CLAVE:

Precio Actual: ${precios[-1]:.2f}
Cambio Diario: {(precios[-1]/precios[-2] - 1)*100:.2f}%
Máximo 52 sem: ${max(precios):.2f}
Mínimo 52 sem: ${min(precios):.2f}
Volatilidad: {np.std(retornos)*np.sqrt(252)*100:.2f}%
Sharpe Ratio: {(np.mean(retornos)/np.std(retornos))*np.sqrt(252):.2f}
"""
ax6.text(0.1, 0.5, metrics_text, fontsize=11, 
         bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5),
         verticalalignment='center')

plt.tight_layout()
plt.show()
```

### Caso 4: Análisis Geográfico con Mapas de Calor
```python
# Crear datos geográficos simulados
estados = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
           'Illinois', 'Ohio', 'Georgia', 'Michigan', 'North Carolina']
poblacion = [39.5, 29.1, 21.5, 19.5, 12.8, 12.7, 11.7, 10.7, 10.0, 10.5]
pib_per_capita = [85, 61, 48, 92, 65, 69, 57, 51, 49, 55]
desempleo = [4.2, 3.8, 3.2, 4.1, 4.4, 4.5, 4.2, 3.5, 4.1, 3.8]

# Crear visualización
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Población por estado
axes[0, 0].barh(estados, poblacion, color='skyblue')
axes[0, 0].set_xlabel('Población (millones)')
axes[0, 0].set_title('Población por Estado')
for i, v in enumerate(poblacion):
    axes[0, 0].text(v + 0.5, i, f'{v}M', va='center')

# 2. PIB per cápita
axes[0, 1].scatter(poblacion, pib_per_capita, s=200, alpha=0.6, c=desempleo, 
                   cmap='RdYlGn_r')
axes[0, 1].set_xlabel('Población (millones)')
axes[0, 1].set_ylabel('PIB per cápita (miles $)')
axes[0, 1].set_title('PIB per cápita vs Población')
cbar = plt.colorbar(axes[0, 1].collections[0], ax=axes[0, 1])
cbar.set_label('Tasa de Desempleo (%)')
for i, txt in enumerate(estados):
    axes[0, 1].annotate(txt[:2], (poblacion[i], pib_per_capita[i]), 
                        ha='center', va='center')

# 3. Matriz de correlación
data_matrix = np.array([poblacion, pib_per_capita, desempleo])
correlation = np.corrcoef(data_matrix)
im = axes[1, 0].imshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
axes[1, 0].set_xticks([0, 1, 2])
axes[1, 0].set_yticks([0, 1, 2])
axes[1, 0].set_xticklabels(['Población', 'PIB/capita', 'Desempleo'])
axes[1, 0].set_yticklabels(['Población', 'PIB/capita', 'Desempleo'])
axes[1, 0].set_title('Matriz de Correlación')
for i in range(3):
    for j in range(3):
        text = axes[1, 0].text(j, i, f'{correlation[i, j]:.2f}',
                              ha="center", va="center", color="black")

# 4. Comparación múltiple
x = np.arange(len(estados))
width = 0.25
axes[1, 1].bar(x - width, poblacion, width, label='Población (×10)', alpha=0.8)
axes[1, 1].bar(x, np.array(pib_per_capita)/10, width, label='PIB/capita (÷10)', alpha=0.8)
axes[1, 1].bar(x + width, desempleo, width, label='Desempleo (%)', alpha=0.8)
axes[1, 1].set_xlabel('Estado')
axes[1, 1].set_ylabel('Valor')
axes[1, 1].set_title('Comparación de Métricas por Estado')
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels([e[:3] for e in estados], rotation=45)
axes[1, 1].legend()

plt.suptitle('Análisis Socioeconómico por Estado', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Consejos y Mejores Prácticas

### 1. Optimización de Rendimiento
```python
# Para grandes conjuntos de datos, usar rasterización
import matplotlib.pyplot as plt
import numpy as np

# Generar muchos puntos
n_points = 100000
x = np.random.randn(n_points)
y = np.random.randn(n_points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Sin rasterización (puede ser lento)
ax1.scatter(x, y, alpha=0.1, s=1)
ax1.set_title('Sin Rasterización')

# Con rasterización (más rápido)
ax2.scatter(x, y, alpha=0.1, s=1, rasterized=True)
ax2.set_title('Con Rasterización')

plt.show()
```

### 2. Paletas de Colores Accesibles
```python
# Usar paletas de colores accesibles para daltónicos
from matplotlib import cm

# Paletas recomendadas
paletas_accesibles = ['viridis', 'plasma', 'cividis', 'twilight']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

x = np.linspace(0, 10, 100)
for ax, paleta in zip(axes, paletas_accesibles):
    colors = cm.get_cmap(paleta)
    for i in range(5):
        color = colors(i/4)
        ax.plot(x, np.sin(x + i), color=color, linewidth=2, label=f'Serie {i+1}')
    ax.set_title(f'Paleta: {paleta}')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 3. Manejo de Fechas
```python
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Crear datos de serie temporal
fechas = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
valores = np.cumsum(np.random.randn(365))

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(fechas, valores)

# Formatear eje x para fechas
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_minor_locator(mdates.WeekdayLocator())

# Rotar etiquetas de fecha
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

ax.set_xlabel('Fecha')
ax.set_ylabel('Valor')
ax.set_title('Serie Temporal con Formato de Fechas')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Recursos Adicionales

### Documentación Oficial
- **Matplotlib Documentation**: https://matplotlib.org/stable/contents.html
- **Galería de Ejemplos**: https://matplotlib.org/stable/gallery/index.html
- **Tutoriales**: https://matplotlib.org/stable/tutorials/index.html

### Librerías Complementarias
- **Seaborn**: Visualización estadística de alto nivel
- **Plotly**: Gráficos interactivos
- **Bokeh**: Visualizaciones web interactivas
- **Altair**: Visualización declarativa

### Tips Finales
1. **Siempre añade etiquetas y títulos** para hacer tus gráficos autoexplicativos
2. **Usa colores consistentes** a lo largo de tu análisis
3. **Considera tu audiencia** al elegir el tipo de visualización
4. **Menos es más**: evita sobrecargar los gráficos con información
5. **Guarda tus gráficos en alta resolución** para publicaciones
6. **Experimenta con diferentes estilos** para encontrar el que mejor se adapte a tu trabajo
7. **Usa subplots** para comparar múltiples visualizaciones
8. **Documenta tu código** para futuras referencias

---

## Conclusión

Matplotlib es una herramienta extremadamente poderosa y flexible para la visualización de datos en Python. Esta guía cubre desde los conceptos más básicos hasta técnicas avanzadas que te permitirán crear visualizaciones profesionales y efectivas.

Recuerda que la práctica es clave para dominar Matplotlib. Experimenta con los ejemplos proporcionados, modifícalos según tus necesidades y no dudes en consultar la documentación oficial para casos más específicos.

¡Feliz visualización de datos!
