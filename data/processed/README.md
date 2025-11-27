# Carpeta `data/processed/`

En esta carpeta se almacenan todos los conjuntos de datos derivados del procesamiento
de los datos crudos.

Incluye:

- `retornos_logaritmicos.parquet`: retornos logarítmicos diarios de BTC, ETH, LTC y DOGE.
- `tda_landscapes_H1_norms.csv`: normas L1 y L2 de los paisajes de persistencia para H1.
- `tda_landscapes_H0_norms.csv`: normas correspondientes a H0 (si se incluyen).
- `pca_nube_R4.csv`: proyección en componentes principales de la nube embebida en R^4.

Estos archivos se generan mediante los notebooks en la carpeta `code/`.

### Archivos generados

- `criptos_precios_2018_2020.csv`  
  Precios diarios limpios y ordenados.

- `criptos_retornos_log_2018_2020.csv`  
  Retornos logarítmicos diarios calculados como:
  \[
  r_t = \ln(p_t) - \ln(p_{t-1})
  \]

- `tda_landscapes_H1_norms.csv`  
  Resultado del pipeline TDA con:
  - Normas L¹ de paisajes de persistencia (H₁)
  - Normas L² de paisajes de persistencia (H₁)
  - Fecha asociada a cada ventana deslizante

### Clasificación como “processed data”

Estos datos ya:
- No contienen valores faltantes
- Están normalizados temporalmente
- Son insumo directo para modelos o análisis posteriores

### Trazabilidad

Cada archivo incluye metadatos temporales para asegurar reproducibilidad.
