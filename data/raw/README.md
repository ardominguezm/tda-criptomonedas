# Data raw(Datos crudos)

En esta carpeta se almacenan los datos originales sin ningún tipo de transformación.
Para esta investigación, los datos se obtienen desde Yahoo Finance utilizando la API
no oficial y corresponden a precios diarios de cierre (“Close”) de BTC, ETH, LTC y DOGE
entre el 1 de enero de 2018 y el 30 de diciembre de 2020.

El archivo `criptomonedas_2018_2020_raw.csv` contiene las columnas:

- Date
- BTC
- ETH
- LTC
- DOGE

Estos datos no deben ser modificados. Todas las transformaciones se realizan en la carpeta
`data/processed`.
