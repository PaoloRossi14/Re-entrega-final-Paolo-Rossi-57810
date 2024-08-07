#### Autor: Paolo Rossi CI - 

## Entrega Final del curso de Python

#### La tarea consiste en una webapp enfocada al backend con Django, consiste administrar un gimnasio.
#### Particularmente: alumnos, profesores, proveedores y las compras
#### Sólo los usuarios registrados y logueados gestionan la información


## Aclaraciones

El proyecto se implementa siguiendo el patrón de diseño [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) para la implementación del patrón [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) que maneja las siguientes tablas de la base de datos:
- Alumnos
- Profesores
- Compras
- Proveedores
  
Estas tablas **no están relacionadas entre sí**, sus claves primarias son el identificador autoincremental que se crea por defecto ante un ingreso de datos en SQLite (no visible al usuario).
Todos los campos de estas tablas son obligatorios (no permite crear o editar con campos vacios)

Las actualizaciones de los datos de la tabla usan la clase de vista lógica *UpdateView*.
Las eliminaciones usan la vista lógica de una instancia particular de la tabla dada por *DeleteView*
Se optó por hacer una eliminación/ingreso de datos basados en clases y no en funciones, por su simplicidad y eficiencia, es una opción adecuada al problema dado.


#### Búsqueda de profesores por profesión
Se realiza mediante un filtrado en el modelo de Profesiones


#### Autenticación y Autorización
La autenticación usa las funcionalidades el framework de Django ```django.contrib.auth``` y sus tablas para almacenar los usuarios.
Sólo los usuarios registrados y logueados pueden modificar (CRUD) y realizar la búsqueda de los datos.