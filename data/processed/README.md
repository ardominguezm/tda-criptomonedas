# Datos procesados (data processed)

En esta carpeta se almacenan todos los conjuntos de datos derivados del procesamiento
de los datos crudos.

Incluye:

- `retornos_logaritmicos.parquet`: retornos logarítmicos diarios de BTC, ETH, LTC y DOGE.
- `tda_landscapes_H1_norms.csv`: normas L1 y L2 de los paisajes de persistencia para H1.
- `tda_landscapes_H0_norms.csv`: normas correspondientes a H0 (si se incluyen).
- `pca_nube_R4.csv`: proyección en componentes principales de la nube embebida en R^4.

Estos archivos se generan mediante los notebooks en la carpeta `code/`.
