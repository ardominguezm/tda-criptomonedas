# Análisis Topológico de Datos en el Mercado de Criptomonedas mediante *Persistence Landscape* 

Este repositorio contiene los datos, algoritmos y código desarrollados para la investigación presentada en la ponencia del Congreso SEIO 2023, Elche, España, 7-10 noviembre, titulada:

Domínguez-Monterroza A, Mateos-Caballero A, Jiménez-Martín A, *Análisis Topológico de Datos Aplicado al Mercado de Criptomonedas*

El objetivo de esta investigación es caracterizar la dinámica conjunta de las criptomonedas Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC) y Dogecoin (DOGE) mediante técnicas de  Topological Data Analysis (TDA), específicamente a través de diagramas de persistencia y  paisajes de persistencia (persistence landscapes). 

Se calculan normas L1 y L2 de los paisajes de persistencia asociados a la homología 1 (H1), que capturan la presencia de ciclos en la nube de puntos embebida en R^4.

La estructura del repositorio es:

- `data/raw`: Datos crudos descargados desde Yahoo Finance (API *yfinance* Python).
- `data/processed`: Datos limpios, retornos y descriptores TDA.
- `data/metadata`: Diccionario de variables, procedencia y documentación.
- `data/analysis`: Figuras, tablas y resultados del análisis.
- `code`: Notebooks y scripts de procesamiento y análisis.
- `docs`: Documentación extendida del proyecto.

