# Mi primera aplicación con Pytorch

Autores: [Andrea Morales Garzón](https://andreamorgar.github.io/) y [Miguel López Pérez](https://wizmik12.netlify.app/).\
Taller organizado en el contexto de la [PyconES 2022](https://2022.es.pycon.org/).
¡Más información sobre este taller [aquí](https://charlas.2022.es.pycon.org/pycones2022/talk/BRKLNP/)!\
Granada · 30 de septiembre del 2022 · 15:30–19:30

### Descripción del taller



>Esto habría que arreglarlo, escribirlo mejor y sobre todo hacerlo cuando tengamos el taller acabado.



Este taller pretende que los asistentes, sin necesidad de tener conocimientos previos sobre la librería, desarrollen una aplicación en Pytorch, una de las librerías por excelencia en Python para desarrollar tareas de aprendizaje automático. En concreto, los asistentes abordarán el diseño y desarrollo de una aplicación de aprendizaje automático desde cero, partiendo de lo básico del funcionamiento del framework, y concluyendo con el despliegue de una aplicación propia en la web.

Este taller se divide en cuatro bloques:
* a\. **Introducción a Pytorch.** En este bloque se explica en qué consisten las librerías para redes neuronales como Pytorch y cómo funcionan. Se dará una idea general de qué son las redes neuronales y cómo esta librería nos ayuda. Se contará con un ejercicio sobre una red neuronal sencilla y problemas de optimización que permitan comprender las nociones más básicas de la librería. Para este bloque usaremos los siguientes notebooks:
	* [0_Introducción_a_Pytorch.ipynb](notebooks/0_Introducción_a_Pytorch.ipynb) contiene una breve introducción a Pytorch.
	* [1_tensores.ipynb](notebooks/1_tensores.ipynb) explica los elementos con los que se trabajan en Pytorch, los tensores.
	* [2_regresión.ipynb](notebooks/2_regresión.ipynb) contiene un ejemplo de regresión con un modelo lineal y con una red neuronal. Seremos capaces de ver como se definen y optimizan los 		modelos en pytorch.
* b\. **Pytorch para CV.** Se verán varios ejemplos de Pytorch en problemas reales, aplicados a clasificación y generación de imágenes y por último a tareas de texto como Question and Answering o generación de texto.
	* [3_clasificación_imágenes.ipynb](notebooks/3_clasificación_imágenes.ipynb) contiene un ejemplo de clasificación de imágenes de satélites. Para ello se entrenará tanto una red 			convolucional desde 0 como una arquitectura preentrenada (de las más potentes que hay!).
* c\. **Pytorch para NLP.**
	*  [4_procesamiento_lenguaje_natural.ipynb](notebooks/4_procesamiento_lenguaje_natural.ipynb) 
* d\. **Diseño y desarrollo de una aplicación ML con Pytorch. Despliegue de la aplicación desarrollada.** Ya con una visión general de la librería, se propondrán varios ejemplos de aplicaciones sencillas de aprendizaje automático a llevar a cabo con Pytorch, con la finalidad de aplicar los conocimientos. Se propondrán diversas opciones de tareas, aunque los asistentes podrán también realizar una de su elección. Por último, se hará un despliegue de una aplicación sencilla con el objetivo de desplegar en la nube un sistema de aprendizaje automático que pueda hacer una tarea sencilla.
	*  [5_aplicación_clasificación_imágenes.py](notebooks/5_aplicación_clasificación_imágenes.py) tiene el script en Python que lanza una aplicación en streamlit de la red neuronal de visión 			previamente entrenada en el notebook 3.


## Antes de comenzar...


#### ¡Empezando desde cero con Conda!

Lo primero es crear un entorno de trabajo para este taller. De esta forma partiremos de cero, con un entorno limpio, sobre el que trabajar y no interceder en otros proyectos en marcha.

~~~
$ conda create -n first_pytorch python=3.7
~~~

¡Lo primero es lo primero! Instala [Pytorch](https://pytorch.org/) con Conda:

~~~
$ conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
~~~

La forma más cómoda de trabajar es por medio de notebooks. Podemos utilizar *Jupyter*, una aplicación web de código abierto que nos permite llevar a cabo todo el proceso de desarrollo de un proyecto de forma interactiva, visual, intercalando textos y código.

~~~
$ conda install -c anaconda jupyter
~~~

Los proyectos de Machine Learning en Python suelen usar librerías comunes, como pueden ser aquellas que nos permiten trabajar con estructuras de datos (como *Pandas*) y realizar visualizaciones de datos (como *matplotlib*). ¡Las instalamos también, pues las usaremos como buenos científicos de datos que somos!

~~~
$ conda install -c conda-forge matplotlib
$ conda install -c anaconda pandas
~~~

Además, también necesitamos instalar *torchtext* para texto y *pillow* para tratar con imágenes. Por último, conseguiremos notebooks interactivos muy vistosos con *ipywidgets*.

~~~
$ conda install -c pytorch torchtext

conda install -c conda-forge ipywidgets

conda install -c anaconda pillow
~~~

¡Ya estamos acabando de preparar nuestro entorno! Nos falta Streamlit, una librería que nos permitirá desplegar nuestro proyecto. Para ello ejecutamos la siguiente orden:
~~~
$ conda install -c conda-forge streamlit
~~~


#### ¡Prefiero pip!

#### ¡No tengo Python instalado!

¡Pero qué poca vergüenza! Pero no pasa nada, en este caso [Google Colab](https://colab.research.google.com/) es tu mejor amigo! Puedes hacer uso de todos los recursos del taller a través de Google Colab sin tener que instalar Python en tu ordenador.
