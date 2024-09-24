# Proyecto Blog

Este proyecto busca servir de practica para entender los conceptos claves del CRUD en Django ya sea basados en clases o funciones, asi como el uso de Middlewares que vienen con el framework y Middlewares de nuestra propia creacion para el control de requests y responses HTTP. En el proyecto se pueden enviar posteos entre varios usuarios, teniendo estos la posibilidad de leerlos, actualizarlos y, si son propietarios de dichos posteos, eliminarlos. Se puede por tanto, ingresar a la aplicacion con varios usuarios, no sin antes registrarse e iniciar sesion.

Para poder correr este proyecto correctamente se necesita tener Python y Django, y las dependencias del archivo requirements.txt. 

Instrucciones para correr el proyecto:

1. Primero conar este repositorio remoto a uno local con `git clone`
2. Asegurarse que se tenga Python 3.10 instalado en su pc, de lo contrario instalar esa version o superior.
3. Instalar virtualenv con `pip install virtualenv`
3. Crear un entorno virtual de Python con el comando `virtualenv venv`
4. Activar el entorno con `source venv/bin/activate`
5. Instalar Django con `pip install django==4.2` (o la version que aparezca en el requirements.txt)
6. Una vez hecho esto, asegurarse que todas las demas dependencias del archivo requirements.txt esten instaladas, de lo contrario hacerlo.
7. Ya podemos ejecutar el servidor. Hacerlo con el comando `python manage.py runserver`
8. El servidor estara en ejecucion en el directorio raiz `http://127.0.0.1:8000/` (el que viene por defecto) y no será necesario ingresar otra url. Se navega perfectamente por medio de la interfaz.

Una vez ejecutado el servidor, ya se puede interactuar con la aplicacion. Hay dos usuarios ya creados: `franco` y `agustin`. Ambos tienen de password: `12345678qwert`. Y ambos tienen ya algunos posteos hechos.

De ser necesario eliminar estos usuarios y crear nuevos, o ir probando.