# Mi primera aplicación con Pytorch (En construcción)

Autores: [Andrea Morales Garzón](https://andreamorgar.github.io/) y [Miguel López Pérez](https://wizmik12.netlify.app/).\
Taller organizado en el contexto de la [PyconES 2022](https://2022.es.pycon.org/).
¡Más información sobre este taller [aquí](https://charlas.2022.es.pycon.org/pycones2022/talk/BRKLNP/)!\
Granada · 30 de septiembre del 2022 · 15:30–19:30

### Descripción del taller

Este taller pretende que los asistentes, sin necesidad de tener conocimientos previos sobre la librería, desarrollen una aplicación en Pytorch, una de las librerías por excelencia en Python para desarrollar tareas de aprendizaje automático. En concreto, los asistentes abordarán el diseño y desarrollo de una aplicación de aprendizaje automático desde cero, partiendo de lo básico del funcionamiento del framework, y concluyendo con el despliegue de una aplicación propia en la web.

Este taller se divide en tres bloques:
* a\. **Introducción a Pytorch.** Este bloque explica en qué consisten las librerías para redes neuronales como Pytorch y cómo funcionan, dando una idea general de qué son las redes neuronales y cómo esta librería nos ayuda. Se contará con un ejercicio sobre una red neuronal sencilla y problemas de optimización que permitan comprender las nociones más básicas de la librería. Para este bloque usaremos los siguientes notebooks:
	* [0_Introducción_a_Pytorch.ipynb](notebooks/0_Introducción_a_Pytorch.ipynb) contiene una breve introducción al framework Pytorch.
	* [1_tensores.ipynb](notebooks/1_tensores.ipynb) introduce los tensores, estos son los elementos con los que trabaja Pytorch.
	* [2_regresión.ipynb](notebooks/2_regresión.ipynb) contiene un ejemplo de regresión con un modelo lineal y con una red neuronal sencilla. Nos servirá para ver cómo se definen y optimizan modelos en Pytorch.
* b\. **Pytorch para CV y NLP.** Este bloque abordará ejemplos prácticos dónde podremos usar Pytorch. Veremos su aplicación en imágenes y en texto. Para ello se usarán los siguientes notebooks:
	* [3_clasificación_imágenes.ipynb](notebooks/3_clasificación_imágenes.ipynb) contiene un ejemplo de clasificación de imágenes de satélites. Para ello se entrenará tanto una red 			convolucional desde 0 como una arquitectura preentrenada (de las más potentes que hay!).
	*  [4_procesamiento_lenguaje_natural.ipynb](notebooks/4_procesamiento_lenguaje_natural.ipynb) se generará poemas con una red neuronal de manera automática!
* c\. **Despliegue de una aplicación en Pytorch.** Ya con una visión general de la librería, se explicará como se puede construir una aplicación sencilla con Pytorch, con el objetivo de hacer un despliegue en la nube de un sistema de aprendizaje automático que pueda hacer una tarea sencilla. Para ello usaremos el siguiente script:
	*  [5_aplicación_clasificación_imágenes.py](notebooks/5_aplicación_clasificación_imágenes.py) tiene el script en Python que lanza una aplicación en streamlit de la red neuronal de visión 			previamente entrenada en el notebook 3.


> Todos los notebooks y scripts contienen ejercicios con los que hacer la experiencia más interactiva y poder adquirir los conocimientos de forma adecuada.

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

$ conda install -c conda-forge ipywidgets

$ conda install -c anaconda pillow
~~~

¡Ya estamos acabando de preparar nuestro entorno! Nos falta Streamlit, una librería que nos permitirá desplegar nuestro proyecto. Para ello ejecutamos la siguiente orden:
~~~
$ conda install -c conda-forge streamlit
~~~


#### ¡Prefiero pip!

#### ¡No tengo Python instalado!

¡Pero qué poca vergüenza! Pero no pasa nada, en este caso [Google Colab](https://colab.research.google.com/) es tu mejor amigo! Puedes hacer uso de todos los recursos del taller a través de Google Colab sin tener que instalar Python en tu ordenador.
