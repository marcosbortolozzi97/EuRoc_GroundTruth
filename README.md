## Requisitos

- Ubuntu 24.04 (recomendado)
- Python 3.10+
  
## Trabajo pre Ejecución 

- Luego de las descarga del dataset en [EuRoC MAV](https://projects.asl.ethz.ch/datasets/kmavvisualinertialdatasets) (Machine Hall 01), recomendamos que la carpeta extraída MH_01_easy permanezca en el home.
- En Ubuntu 24.04 no es posible instalar las librerias a utilizar (matplotlib, transforms3d) con el comando pip3, se optó por utilizar un entorno virtual.
  Se debe crear el entorno virtual mediante los siguientes comandos en la terminal (aparecerá una carpeta llamada euroc_env dentro de MH_01_easy):  
      &nbsp;&nbsp;&nbsp;&nbsp;cd ~/MH_01_easy  
      &nbsp;&nbsp;&nbsp;&nbsp;python3 -m venv euroc_virtual  
      &nbsp;&nbsp;&nbsp;&nbsp;source euroc_virtual/bin/activate  
      &nbsp;&nbsp;&nbsp;&nbsp;pip install matplotlib transforms3d 
- Se descargan los archivos .py del repositorio dentro de la carpeta MH_01_easy.

## Ejecución

- Se posiciona sobre la carpeta MH_01_easy  
    &nbsp;&nbsp;&nbsp;&nbsp;cd ~/MH_01_easy  
- Se activa el entorno virtual  
    &nbsp;&nbsp;&nbsp;&nbsp;source euroc_env/bin/activate
- Se ejecuta  
    &nbsp;&nbsp;&nbsp;&nbsp;python nombre_archivo.py   ejemplo: python left_cam.py
- Cuando finalice la ejecucion o se quiera salir del modo virtual  
    &nbsp;&nbsp;&nbsp;&nbsp;deactivate  
    &nbsp;&nbsp;&nbsp;&nbsp;cd
##Nota
La ejecución de los scripts se corresponden con el enunciado de la siguiente manera  
&nbsp;&nbsp;&nbsp;&nbsp;a) left_cam.py
&nbsp;&nbsp;&nbsp;&nbsp;b) left_cam_nanoprecision.py
&nbsp;&nbsp;&nbsp;&nbsp;c) images_groundtruth.py
