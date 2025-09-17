# EuRoc_GroundTruth

Este repositorio contiene scripts en Python para procesar el dataset [EuRoC MAV](https://projects.asl.ethz.ch/datasets/kmavvisualinertialdatasets)
y generar la trayectoria ground-truth de la cámara izquierda, a partir del ground-truth de la IMU, modificar el timestamp y generar una imagen de 
las trayectorias de la IMU vs la camara.

## Requisitos

- Ubuntu 24.04 (recomendado)
- Python 3.10+
  
## Trabajo Preliminar 

- Luego de las descarga del dataset en el link anterior (Machine Hall 01), recomendamos que la carpeta extraída MH_01_easy permanezca en el home.
- En Ubuntu 24.04 no es posible instalar las librerias a utilizar (matplotlib, transforms3d) con el comando pip3, se optó por utilizar un entorno virtual.
  Se debe crear el entorno virtual mediante los siguientes comandos en la terminal (aparecerá una carpeta euroc_env):
    cd ~/MH_01_easy
    python3 -m venv euroc_env
    source euroc_env/bin/activate
    pip install matplotlib transforms3d pandas pyyaml  
- Se descargan los archivos .py del repositorio dentro de la carpeta MH_01_easy

## Ejecución

- Se posiciona sobre la carpeta MH_01_easy
    cd ~/MH_01_easy
- Se activa el entorno virtual
    source euroc_env/bin/activate
- Se ejecuta
    python nombre_archivo.py   ejemplo: python left_cam.py
-Cuando finalice la ejecucion o se quiera salir de este modo
    deactivate
    cd
