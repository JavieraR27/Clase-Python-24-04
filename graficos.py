#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GUÍA COMPLETA DE MATPLOTLIB - EJEMPLOS EJECUTABLES
Autor: Luciano Grandi
Fecha: 202
Descripción: Colección completa de ejemplos de Matplotlib en español
"""

import sys
import warnings
warnings.filterwarnings('ignore')

# Verificar dependencias
def verificar_dependencias():
    """Verifica que todas las librerías necesarias estén instaladas"""
    dependencias = {
        'matplotlib': False,
        'numpy': False,
        'pandas': False
    }
    
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        dependencias['matplotlib'] = matplotlib.__version__
    except ImportError:
        print("❌ matplotlib no está instalado. Instálalo con: pip install matplotlib")
        return False
    
    try:
        import numpy as np
        dependencias['numpy'] = np.__version__
    except ImportError:
        print("❌ numpy no está instalado. Instálalo con: pip install numpy")
        return False
    
    try:
        import pandas as pd
        dependencias['pandas'] = pd.__version__
    except ImportError:
        print("⚠️  pandas no está instalado (opcional). Instálalo con: pip install pandas")
        dependencias['pandas'] = 'No instalado (opcional)'
    
    print("\n📦 Verificación de dependencias:")
    print(f"  ✅ matplotlib: {dependencias['matplotlib']}")
    print(f"  ✅ numpy: {dependencias['numpy']}")
    print(f"  {'✅' if dependencias['pandas'] != 'No instalado (opcional)' else '⚠️ '} pandas: {dependencias['pandas']}")
    
    return True

# Verificar al inicio
if not verificar_dependencias():
    sys.exit(1)

# Importaciones necesarias
import matplotlib.pyplot as plt
import numpy as np
try:
    import pandas as pd
    PANDAS_DISPONIBLE = True
except ImportError:
    PANDAS_DISPONIBLE = False
    print("⚠️  Algunos ejemplos requieren pandas")

from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec
from matplotlib.patches import Circle, Rectangle, Ellipse, FancyBboxPatch

# Configuración global recomendada
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

def ejemplo_1_grafico_lineas():
    """Ejemplo 1: Gráfico de líneas básico"""
    print("Ejecutando Ejemplo 1: Gráfico de Líneas")
    
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

def ejemplo_2_grafico_dispersion():
    """Ejemplo 2: Gráfico de dispersión"""
    print("Ejecutando Ejemplo 2: Gráfico de Dispersión")
    
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

def ejemplo_3_grafico_barras():
    """Ejemplo 3: Gráfico de barras"""
    print("Ejecutando Ejemplo 3: Gráfico de Barras")
    
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

def ejemplo_4_histograma():
    """Ejemplo 4: Histograma con curva normal"""
    print("Ejecutando Ejemplo 4: Histograma")
    
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

def ejemplo_5_personalizacion_colores():
    """Ejemplo 5: Personalización de colores y estilos"""
    print("Ejecutando Ejemplo 5: Personalización de Colores y Estilos")
    
    # Diferentes formas de especificar colores
    colores = ['red', '#FF5733', (0.2, 0.4, 0.6), 'C0']
    estilos = ['-', '--', '-.', ':']
    
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for i, (color, estilo) in enumerate(zip(colores, estilos)):
        ax.plot(x, np.sin(x + i), color=color, linestyle=estilo, 
                linewidth=2, label=f'Línea {i+1}')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Personalización de Colores y Estilos')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

def ejemplo_6_marcadores():
    """Ejemplo 6: Tipos de marcadores"""
    print("Ejecutando Ejemplo 6: Tipos de Marcadores")
    
    marcadores = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
    nombres = ['Círculo', 'Cuadrado', 'Triángulo arriba', 'Diamante', 
               'Triángulo abajo', 'Triángulo izq', 'Triángulo der', 
               'Pentágono', 'Estrella', 'Hexágono']
    
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

def ejemplo_7_grafico_pastel():
    """Ejemplo 7: Gráfico de pastel (pie chart)"""
    print("Ejecutando Ejemplo 7: Gráfico de Pastel")
    
    sizes = [30, 25, 20, 15, 10]
    labels = ['Python', 'JavaScript', 'Java', 'C++', 'Otros']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    explode = (0.1, 0, 0, 0, 0)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, 
                                       colors=colors, autopct='%1.1f%%',
                                       shadow=True, startangle=90)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')
        autotext.set_fontsize(10)
    
    ax.set_title('Distribución de Uso de Lenguajes de Programación', 
                 fontsize=14, fontweight='bold')
    plt.show()

def ejemplo_8_boxplot():
    """Ejemplo 8: Box plot (diagrama de caja)"""
    print("Ejecutando Ejemplo 8: Box Plot")
    
    np.random.seed(42)
    data = [np.random.normal(100, 10, 200),
            np.random.normal(90, 20, 200),
            np.random.normal(110, 15, 200),
            np.random.normal(95, 25, 200)]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bp = ax.boxplot(data, labels=['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D'],
                    patch_artist=True, notch=True, showmeans=True)
    
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5, linestyle=':')
    
    ax.set_xlabel('Grupos', fontsize=12)
    ax.set_ylabel('Valores', fontsize=12)
    ax.set_title('Comparación de Distribuciones entre Grupos', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    plt.show()

def ejemplo_9_mapa_calor():
    """Ejemplo 9: Mapa de calor (heatmap)"""
    print("Ejecutando Ejemplo 9: Mapa de Calor")
    
    np.random.seed(42)
    data = np.random.randn(10, 10)
    correlation_matrix = np.corrcoef(data)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Correlación', rotation=270, labelpad=20)
    
    ticks = np.arange(10)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels([f'Var {i+1}' for i in ticks])
    ax.set_yticklabels([f'Var {i+1}' for i in ticks])
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    for i in range(10):
        for j in range(10):
            text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black", fontsize=8)
    
    ax.set_title('Matriz de Correlación', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def ejemplo_10_subplots():
    """Ejemplo 10: Múltiples subplots"""
    print("Ejecutando Ejemplo 10: Subplots")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
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

def ejemplo_11_anotaciones():
    """Ejemplo 11: Anotaciones y texto"""
    print("Ejecutando Ejemplo 11: Anotaciones")
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y, 'b-', linewidth=2)
    
    # Encontrar máximo
    max_idx = np.argmax(y)
    max_x, max_y = x[max_idx], y[max_idx]
    
    ax.annotate('Máximo local',
                xy=(max_x, max_y),
                xytext=(max_x + 1, max_y - 0.5),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    # Encontrar mínimo
    min_idx = np.argmin(y)
    min_x, min_y = x[min_idx], y[min_idx]
    
    ax.annotate('Mínimo local',
                xy=(min_x, min_y),
                xytext=(min_x - 1.5, min_y + 0.5),
                arrowprops=dict(arrowstyle='fancy', color='blue', lw=1.5),
                fontsize=12, color='blue')
    
    ax.text(5, 0.5, 'Función Seno', fontsize=16, 
            bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Anotaciones en Matplotlib')
    ax.grid(True, alpha=0.3)
    plt.show()

def ejemplo_12_dashboard_ventas():
    """Ejemplo 12: Dashboard de análisis de ventas"""
    print("Ejecutando Ejemplo 12: Dashboard de Ventas")
    
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ventas_2023 = [45000, 52000, 48000, 61000, 58000, 67000,
                    72000, 69000, 63000, 59000, 55000, 71000]
    ventas_2024 = [48000, 54000, 51000, 63000, 62000, 70000,
                    75000, 73000, 68000, 64000, 60000, 76000]
    
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

def ejemplo_13_series_temporales():
    """Ejemplo 13: Manejo de fechas y series temporales"""
    print("Ejecutando Ejemplo 13: Series Temporales")
    
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

def ejemplo_14_gridspec():
    """Ejemplo 14: GridSpec para layouts complejos"""
    print("Ejecutando Ejemplo 14: GridSpec")
    
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

def ejemplo_15_estilos():
    """Ejemplo 15: Diferentes estilos de Matplotlib"""
    print("Ejecutando Ejemplo 15: Estilos")
    
    # Obtener estilos disponibles y seleccionar algunos populares
    estilos_disponibles = plt.style.available
    
    # Estilos seguros que existen en todas las versiones
    estilos_a_mostrar = []
    estilos_preferidos = ['default', 'ggplot', 'bmh', 'fivethirtyeight', 
                         'seaborn-v0_8', 'seaborn-darkgrid', 'classic']
    
    # Verificar qué estilos están disponibles
    for estilo in estilos_preferidos:
        if estilo in estilos_disponibles:
            estilos_a_mostrar.append(estilo)
        elif estilo == 'default':  # default siempre existe
            estilos_a_mostrar.append('default')
    
    # Si tenemos menos de 4 estilos, completar con otros disponibles
    if len(estilos_a_mostrar) < 4:
        for estilo in estilos_disponibles:
            if estilo not in estilos_a_mostrar:
                estilos_a_mostrar.append(estilo)
                if len(estilos_a_mostrar) >= 4:
                    break
    
    # Asegurar que tenemos exactamente 4 estilos
    estilos_a_mostrar = estilos_a_mostrar[:4]
    
    print(f"Estilos disponibles en tu versión: {len(estilos_disponibles)}")
    print(f"Mostrando: {', '.join(estilos_a_mostrar)}")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    for ax, style in zip(axes, estilos_a_mostrar):
        try:
            with plt.style.context(style):
                ax.plot(x, y, label='sin(x)', linewidth=2)
                ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)
                ax.set_title(f'Estilo: {style}')
                ax.legend()
                ax.grid(True, alpha=0.3)
        except:
            # Si falla un estilo, usar default
            ax.plot(x, y, label='sin(x)', linewidth=2)
            ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)
            ax.set_title(f'Estilo: default (fallback)')
            ax.legend()
            ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def ejemplo_16_violin_plot():
    """Ejemplo 16: Gráfico de violín"""
    print("Ejecutando Ejemplo 16: Gráfico de Violín")
    
    np.random.seed(42)
    data = [np.random.normal(0, std, 100) for std in range(1, 5)]
    
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
    
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    for pc, color in zip(parts2['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_alpha(0.7)
    
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

def guardar_ejemplos():
    """Función para guardar todos los gráficos en archivos"""
    print("\n" + "="*50)
    print("GUARDANDO EJEMPLOS EN ARCHIVOS")
    print("="*50)
    
    # Crear directorio para guardar las imágenes
    import os
    if not os.path.exists('matplotlib_ejemplos'):
        os.makedirs('matplotlib_ejemplos')
    
    # Ejemplo de cómo guardar un gráfico
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
    plt.savefig('matplotlib_ejemplos/grafico.png', dpi=300, bbox_inches='tight')
    plt.savefig('matplotlib_ejemplos/grafico.pdf', bbox_inches='tight')
    plt.savefig('matplotlib_ejemplos/grafico.svg', bbox_inches='tight')
    plt.savefig('matplotlib_ejemplos/grafico_transparente.png', 
                dpi=300, bbox_inches='tight', transparent=True)
    
    print("✓ Archivos guardados en la carpeta 'matplotlib_ejemplos/'")
    print("  - grafico.png (300 DPI)")
    print("  - grafico.pdf")
    print("  - grafico.svg")
    print("  - grafico_transparente.png")
    plt.close()

def menu_principal():
    """Menú principal para ejecutar ejemplos"""
    ejemplos = {
        '1': ('Gráfico de Líneas', ejemplo_1_grafico_lineas),
        '2': ('Gráfico de Dispersión', ejemplo_2_grafico_dispersion),
        '3': ('Gráfico de Barras', ejemplo_3_grafico_barras),
        '4': ('Histograma', ejemplo_4_histograma),
        '5': ('Personalización de Colores', ejemplo_5_personalizacion_colores),
        '6': ('Tipos de Marcadores', ejemplo_6_marcadores),
        '7': ('Gráfico de Pastel', ejemplo_7_grafico_pastel),
        '8': ('Box Plot', ejemplo_8_boxplot),
        '9': ('Mapa de Calor', ejemplo_9_mapa_calor),
        '10': ('Subplots', ejemplo_10_subplots),
        '11': ('Anotaciones', ejemplo_11_anotaciones),
        '12': ('Dashboard de Ventas', ejemplo_12_dashboard_ventas),
        '13': ('Series Temporales', ejemplo_13_series_temporales),
        '14': ('GridSpec Layout', ejemplo_14_gridspec),
        '15': ('Estilos de Matplotlib', ejemplo_15_estilos),
        '16': ('Gráfico de Violín', ejemplo_16_violin_plot),
        '17': ('Guardar Gráficos', guardar_ejemplos),
    }
    
    print("\n" + "="*60)
    print(" GUÍA COMPLETA DE MATPLOTLIB - EJEMPLOS INTERACTIVOS")
    print("="*60)
    print("\nSelecciona un ejemplo para ejecutar:\n")
    
    for key, (nombre, _) in ejemplos.items():
        print(f"  [{key:>2}] {nombre}")
    
    print("\n  [0] Ejecutar TODOS los ejemplos")
    print("  [q] Salir")
    print("\n" + "-"*60)
    
    while True:
        opcion = input("\n➤ Ingresa tu opción: ").strip().lower()
        
        if opcion == 'q':
            print("\n¡Hasta luego! Happy plotting! 📊")
            break
        elif opcion == '0':
            print("\n" + "="*50)
            print("EJECUTANDO TODOS LOS EJEMPLOS")
            print("="*50)
            for key, (nombre, funcion) in ejemplos.items():
                print(f"\n--- {nombre} ---")
                try:
                    funcion()
                except Exception as e:
                    print(f"Error en {nombre}: {e}")
            print("\n✓ Todos los ejemplos ejecutados")
        elif opcion in ejemplos:
            nombre, funcion = ejemplos[opcion]
            print(f"\n--- {nombre} ---")
            try:
                funcion()
                print(f"✓ {nombre} ejecutado correctamente")
            except Exception as e:
                print(f"✗ Error: {e}")
        else:
            print("✗ Opción no válida. Intenta de nuevo.")

def ejemplo_completo_cientifico():
    """Ejemplo adicional: Análisis científico completo"""
    print("Ejecutando Ejemplo Científico Completo")
    
    # Simular datos de experimento
    np.random.seed(42)
    tiempo = np.linspace(0, 10, 1000)
    señal = np.sin(2 * np.pi * tiempo) + 0.5 * np.sin(10 * np.pi * tiempo)
    ruido = np.random.normal(0, 0.2, len(tiempo))
    señal_con_ruido = señal + ruido
    
    # Crear visualización científica
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
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
    
    # 3. FFT de la señal
    from numpy.fft import fft, fftfreq
    N = len(tiempo)
    yf = fft(señal_con_ruido)
    xf = fftfreq(N, tiempo[1] - tiempo[0])[:N//2]
    axes[0, 2].plot(xf, 2.0/N * np.abs(yf[:N//2]))
    axes[0, 2].set_xlabel('Frecuencia (Hz)')
    axes[0, 2].set_ylabel('Amplitud')
    axes[0, 2].set_title('Espectro de Frecuencias (FFT)')
    axes[0, 2].grid(True, alpha=0.3)
    
    # 4. Espectrograma
    axes[1, 0].specgram(señal_con_ruido, Fs=len(tiempo)/10, cmap='viridis')
    axes[1, 0].set_xlabel('Tiempo (s)')
    axes[1, 0].set_ylabel('Frecuencia (Hz)')
    axes[1, 0].set_title('Espectrograma')
    
    # 5. Correlación cruzada
    correlacion = np.correlate(señal[:100], señal_con_ruido[:100], mode='full')
    axes[1, 1].plot(correlacion)
    axes[1, 1].set_xlabel('Retraso')
    axes[1, 1].set_ylabel('Correlación')
    axes[1, 1].set_title('Correlación Cruzada')
    axes[1, 1].grid(True, alpha=0.3)
    
    # 6. Diagrama de fase
    axes[1, 2].plot(señal[:-1], señal[1:], 'b.', markersize=1, alpha=0.5)
    axes[1, 2].set_xlabel('x(t)')
    axes[1, 2].set_ylabel('x(t+1)')
    axes[1, 2].set_title('Diagrama de Fase')
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.suptitle('Análisis de Señales Científico', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

def ejemplo_dashboard_financiero():
    """Ejemplo adicional: Dashboard financiero profesional"""
    print("Ejecutando Dashboard Financiero")
    
    if not PANDAS_DISPONIBLE:
        print("⚠️  Este ejemplo requiere pandas. Mostrando versión simplificada...")
        # Versión simplificada sin pandas
        np.random.seed(42)
        dias = 252
        precio_inicial = 100
        retornos = np.random.normal(0.0005, 0.02, dias)
        precios = precio_inicial * np.exp(np.cumsum(retornos))
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(precios, label='Precio', color='black', linewidth=1)
        ax.set_title('Precio de la Acción (Versión Simplificada)')
        ax.set_xlabel('Días')
        ax.set_ylabel('Precio ($)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.show()
        return
    
    # Versión completa con pandas
    # Generar datos financieros simulados
    np.random.seed(42)
    dias = 252  # Días de trading en un año
    fechas = pd.date_range('2024-01-01', periods=dias, freq='B')  # Business days
    precio_inicial = 100
    retornos = np.random.normal(0.0005, 0.02, dias)
    precios = precio_inicial * np.exp(np.cumsum(retornos))
    volumen = np.random.uniform(1000000, 5000000, dias)
    
    # Calcular indicadores técnicos
    ma_20 = pd.Series(precios).rolling(window=20).mean()
    ma_50 = pd.Series(precios).rolling(window=50).mean()
    volatilidad = pd.Series(retornos).rolling(window=20).std() * np.sqrt(252)
    
    # Crear dashboard
    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(4, 3, height_ratios=[2, 1, 1, 1])
    
    # 1. Gráfico de precios principal
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(fechas, precios, label='Precio', color='black', linewidth=1)
    ax1.plot(fechas, ma_20, label='MA20', color='blue', alpha=0.7)
    ax1.plot(fechas, ma_50, label='MA50', color='red', alpha=0.7)
    ax1.fill_between(fechas, precios, precio_inicial, 
                     where=(precios >= precio_inicial), 
                     facecolor='green', alpha=0.3, interpolate=True)
    ax1.fill_between(fechas, precios, precio_inicial, 
                     where=(precios < precio_inicial), 
                     facecolor='red', alpha=0.3, interpolate=True)
    ax1.set_title('Precio de la Acción XYZ - 2024', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Precio ($)')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # 2. Volumen
    ax2 = fig.add_subplot(gs[1, :], sharex=ax1)
    ax2.bar(fechas, volumen, color='gray', alpha=0.5)
    ax2.set_ylabel('Volumen')
    ax2.set_title('Volumen de Transacciones')
    ax2.grid(True, alpha=0.3)
    
    # 3. Distribución de retornos
    ax3 = fig.add_subplot(gs[2, 0])
    ax3.hist(retornos, bins=30, color='blue', alpha=0.7, edgecolor='black')
    ax3.set_xlabel('Retorno Diario')
    ax3.set_ylabel('Frecuencia')
    ax3.set_title('Distribución de Retornos')
    ax3.axvline(x=0, color='red', linestyle='--', alpha=0.5)
    
    # 4. Volatilidad
    ax4 = fig.add_subplot(gs[2, 1])
    ax4.plot(fechas[19:], volatilidad[19:] * 100, color='orange')
    ax4.set_xlabel('Fecha')
    ax4.set_ylabel('Volatilidad (%)')
    ax4.set_title('Volatilidad Anualizada (20 días)')
    ax4.grid(True, alpha=0.3)
    
    # 5. Retornos acumulados
    ax5 = fig.add_subplot(gs[2, 2])
    retornos_acum = (1 + pd.Series(retornos)).cumprod() - 1
    ax5.plot(fechas, retornos_acum * 100, color='purple')
    ax5.set_xlabel('Fecha')
    ax5.set_ylabel('Retorno (%)')
    ax5.set_title('Retorno Acumulado')
    ax5.grid(True, alpha=0.3)
    
    # 6. Heatmap mensual de retornos
    ax6 = fig.add_subplot(gs[3, :2])
    # Crear matriz de retornos mensuales (simplificado)
    meses = 12
    semanas = 4
    retornos_mensuales = np.random.normal(0.01, 0.05, (semanas, meses))
    im = ax6.imshow(retornos_mensuales, cmap='RdYlGn', aspect='auto', vmin=-0.1, vmax=0.1)
    ax6.set_xticks(range(meses))
    ax6.set_xticklabels(['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    ax6.set_yticks(range(semanas))
    ax6.set_yticklabels([f'Sem {i+1}' for i in range(semanas)])
    ax6.set_title('Mapa de Calor - Retornos Semanales')
    plt.colorbar(im, ax=ax6, label='Retorno')
    
    # 7. Métricas clave
    ax7 = fig.add_subplot(gs[3, 2])
    ax7.axis('off')
    
    # Calcular métricas
    precio_actual = precios[-1]
    cambio_diario = (precios[-1]/precios[-2] - 1) * 100
    maximo_52 = max(precios)
    minimo_52 = min(precios)
    volatilidad_anual = np.std(retornos) * np.sqrt(252) * 100
    sharpe_ratio = (np.mean(retornos) * 252) / (np.std(retornos) * np.sqrt(252))
    max_drawdown = ((precios / np.maximum.accumulate(precios)) - 1).min() * 100
    
    metrics_text = f"""
    📊 MÉTRICAS CLAVE
    
    Precio Actual: ${precio_actual:.2f}
    Cambio Diario: {cambio_diario:+.2f}%
    Máximo 52 sem: ${maximo_52:.2f}
    Mínimo 52 sem: ${minimo_52:.2f}
    
    Volatilidad: {volatilidad_anual:.2f}%
    Sharpe Ratio: {sharpe_ratio:.2f}
    Max Drawdown: {max_drawdown:.2f}%
    
    Vol. Promedio: {np.mean(volumen)/1e6:.1f}M
    """
    
    ax7.text(0.1, 0.5, metrics_text, fontsize=10, 
             bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.3),
             verticalalignment='center', family='monospace')
    
    plt.suptitle('Dashboard Financiero Profesional', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

def ejemplo_3d_plot():
    """Ejemplo adicional: Gráficos 3D"""
    print("Ejecutando Ejemplo de Gráficos 3D")
    
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=(15, 10))
    
    # 1. Superficie 3D
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax1.set_title('Superficie 3D')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # 2. Wireframe
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    ax2.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)
    ax2.set_title('Wireframe 3D')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    
    # 3. Scatter 3D
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    n = 100
    xs = np.random.normal(0, 1, n)
    ys = np.random.normal(0, 1, n)
    zs = np.random.normal(0, 1, n)
    colors = np.random.random(n)
    ax3.scatter(xs, ys, zs, c=colors, marker='o', alpha=0.6)
    ax3.set_title('Scatter 3D')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    
    # 4. Contour 3D
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    ax4.contour3D(X, Y, Z, 50, cmap='plasma')
    ax4.set_title('Contorno 3D')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    
    # 5. Bar 3D
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    x3 = [1, 2, 3, 4, 5]
    y3 = [1, 2, 3, 4, 5]
    x3, y3 = np.meshgrid(x3, y3)
    x3, y3 = x3.ravel(), y3.ravel()
    z3 = np.zeros_like(x3)
    dx = dy = 0.5
    dz = np.random.randint(1, 10, len(x3))
    colors3 = plt.cm.jet(dz/10.0)
    ax5.bar3d(x3, y3, z3, dx, dy, dz, color=colors3, alpha=0.8)
    ax5.set_title('Barras 3D')
    ax5.set_xlabel('X')
    ax5.set_ylabel('Y')
    ax5.set_zlabel('Z')
    
    # 6. Superficie con proyecciones
    ax6 = fig.add_subplot(2, 3, 6, projection='3d')
    ax6.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.5)
    ax6.contourf(X, Y, Z, zdir='z', offset=-2, cmap='coolwarm', alpha=0.5)
    ax6.set_title('Superficie con Proyección')
    ax6.set_xlabel('X')
    ax6.set_ylabel('Y')
    ax6.set_zlabel('Z')
    ax6.set_zlim(-2, 2)
    
    plt.suptitle('Ejemplos de Gráficos 3D', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

def tips_y_trucos():
    """Tips y trucos útiles para Matplotlib"""
    print("\n" + "="*60)
    print(" TIPS Y TRUCOS DE MATPLOTLIB")
    print("="*60)
    
    tips = """
    🎨 PERSONALIZACIÓN:
    • Use plt.style.use('ggplot') o 'bmh' para estilos modernos
    • rcParams permite configuración global
    • Cree sus propios colormaps con LinearSegmentedColormap
    
    ⚡ RENDIMIENTO:
    • Use rasterized=True para grandes datasets
    • Blitting para animaciones más rápidas
    • Considere decimación de datos para visualización
    
    📊 MEJORES PRÁCTICAS:
    • Siempre añada labels y títulos descriptivos
    • Use colores consistentes en todo el análisis
    • Prefiera subplots sobre múltiples figuras
    • Guarde en vectorial (PDF/SVG) para publicaciones
    
    🔧 DEBUGGING:
    • plt.show(block=False) para modo no bloqueante
    • plt.ion() para modo interactivo
    • Use %matplotlib notebook en Jupyter
    
    💡 TRUCOS ÚTILES:
    • ax.secondary_yaxis() para doble eje Y
    • ax.annotate() con fancy arrows para destacar
    • plt.tight_layout() evita solapamientos
    • fig.savefig() con dpi=300 para alta calidad
    
    🎯 ESTILOS DISPONIBLES EN TU VERSIÓN:
    """
    
    print(tips)
    
    # Mostrar estilos disponibles
    estilos = plt.style.available
    print(f"    Total de estilos: {len(estilos)}")
    print(f"    Algunos populares: {', '.join(estilos[:8])}")
    print(f"\n    Para usar: plt.style.use('{estilos[0]}')")

# Función principal
if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     GUÍA COMPLETA DE MATPLOTLIB - EJEMPLOS EN PYTHON    ║
    ╠══════════════════════════════════════════════════════════╣
    ║  Biblioteca de visualización de datos más popular       ║
    ║  Versión: Matplotlib 3.x                                ║
    ║  Autor: Luciano G                                       ║
    ║  Fecha: 2025                                            ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    print("\n¿Qué deseas hacer?\n")
    print("  [1] Ejecutar menú interactivo")
    print("  [2] Ejecutar todos los ejemplos")
    print("  [3] Ver tips y trucos")
    print("  [4] Salir")
    
    opcion = input("\n➤ Selecciona una opción: ").strip()
    
    if opcion == '1':
        menu_principal()
    elif opcion == '2':
        print("\nEjecutando todos los ejemplos...")
        # Lista de todas las funciones de ejemplo
        ejemplos = [
            ejemplo_1_grafico_lineas,
            ejemplo_2_grafico_dispersion,
            ejemplo_3_grafico_barras,
            ejemplo_4_histograma,
            ejemplo_5_personalizacion_colores,
            ejemplo_6_marcadores,
            ejemplo_7_grafico_pastel,
            ejemplo_8_boxplot,
            ejemplo_9_mapa_calor,
            ejemplo_10_subplots,
            ejemplo_11_anotaciones,
            ejemplo_12_dashboard_ventas,
            ejemplo_13_series_temporales,
            ejemplo_14_gridspec,
            ejemplo_15_estilos,
            ejemplo_16_violin_plot,
            ejemplo_completo_cientifico,
            ejemplo_dashboard_financiero,
            ejemplo_3d_plot
        ]
        
        for ejemplo in ejemplos:
            try:
                ejemplo()
            except Exception as e:
                print(f"Error en {ejemplo.__name__}: {e}")
        
        guardar_ejemplos()
        print("\n✓ Todos los ejemplos ejecutados correctamente")
    elif opcion == '3':
        tips_y_trucos()
    else:
        print("\n¡Hasta luego! Happy plotting! 📊")
    
    print("\n" + "="*60)
    print(" Fin del programa")
    print("="*60)
