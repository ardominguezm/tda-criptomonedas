# Carpeta `data/analysis/`

Esta carpeta contiene resultados derivados del análisis del proyecto, tales como:

### Figuras generadas por `04_visualizaciones.ipynb`

- `retornos_logaritmicos.png`
- `normas_L1_L2_H1.png`
- `comparacion_L1_ventanas.png` (si existen varias ventanas)
- `comparacion_L2_ventanas.png`
- `normas_suavizadas.png`

### Características de estos archivos

- No son datos crudos ni procesados, sino **resultados finales**.
- Se utilizan en informes, presentaciones (incluida la ponencia del SEIO 2023) y para publicación en Zenodo.
- Pueden recrearse al volver a ejecutar los notebooks.

### Nota sobre reproducibilidad

Los archivos de esta carpeta **pueden ser regenerados** desde cero ejecutando toda la cadena:

1. 01_descarga_datos.ipynb  
2. 02_preprocesamiento.ipynb  
3. 03_pipeline_TDA.ipynb  
4. 04_visualizaciones.ipynb
