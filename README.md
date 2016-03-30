# moduloOdoo-1
Práctica módulo DAM

> Odoo nos permite crear un modulo vacio con el siguiente comando:
odoo.py scaffold <module name> <where to put it>
Ejemplo:
/opt/odoo/odoo.py scaffold openacademy /opt/odoo/addons/

> Adaptamos el archivo manifest(__openerp__.py) para nuestro módulo.

##Modelos
Los campos de un modelo definen lo que pueden almacenar y donde.
> Definimos el modelo Course que tiene un nombre y una descripción.

##Archivos de Datos
Los datos de los modelos son declarados en los archivos de datos, esto es, archivos XML con elementos <record>. Cada <record> hace referencia a un registro de la base de datos.
Estos archivos son declarados en el manifest, en el apartado ‘data’.

> Definimos datos de demostración para los Cursos. Editamos el archivo openacademy/demo.xml e introducimos algunos datos.

##Acciones y Menus
Las acciones y los menus son registros de la base de datos, declarados en archivos de datos.

Los menus son declarados con la etiqueta <menuitem> que declara un ir.ui.menu y lo conecta con su accion.

Ojo!!
La acción debe ser declarada antes del archivo XML del menú. Los archivos de datos son ejecutados secuencialmente y los ids de las acciones deben estar presentes en la base de datos antes de que el menú sea creado.

> Definimos un menú para acceder a los cursos y sesiones. Un usuario será capaz de:
mostrar la lista de cursos
crear/modificar los cursos.

Creamos el archivo openacademy/views/openacademy.xml con una acción y un menú. Lo añadimos al campo ‘data’ del manifest.

##Vistas
Las vistas definen la manera en el que los registros de los modelos son mostrados. Cada tipo de vista representa una forma de visualización(una lista, un gráfico,...).

> Creamos un formulario para los Cursos. Los datos mostrados serán el nombre y la descripción del curso.

Los formularios puedes usar HTML para hacer plantillas más flexibles.

> Ponemos la descripción de los Cursos en una pestaña, para que sea más fácil añadir otras pestañas con información adicional.

##Vistas de búsqueda
Podemos personalizar el campo de búsqueda asociado con la lista. La etiqueta utilizada es <search> y está compuesta de campos que definen que campos pueden ser buscados.

Si no hay una vista de búsqueda para un modelo, Odoo crea una por defecto que permite buscar por el campo nombre.

> Creamos una vista de búsqueda para los cursos a partir del titulo o de su descripción.

##Relaciones entre modelos
Un registro de un modelo puede estar relacionado con otro registro de otro modelo. Tipos de relaciones:
Many2one(other_model, ondelete='set null').
One2many(other_model, related_field). Debe haber un campo Many2one en other_model y su nombre debe ser related_field.
Many2many(other_model). Cada registro de un lado puede ser relacionado con cualquier número de registros del otro lado.

> Creamos un modelo Session y su vista.

> Modificamos Curso y Sesion para definir su relación.

##Herencia
Odoo permite dos mecanismos para heredar de un módulo:
Uno permite a un módulo modificar el comportamiento de un modelo definido en otro módulo.
El otro permite relacionar cada registro de un modelo a un registro de un modelo padre, y le da acceso a los campos del registro padre.

> Usando herencia modificamos el modelo Partner para añadir un campo instructor y una relación con el modelo Sesion.
Usando la herencia , mostramos los campos en el formulario.

##Dominios
Los dominios son valores con condiciones. Un dominio es una lista de criterios compuestos por un nombre del campo, un operador y un valor.

> Realizamos un dominio para que cuando se seleccione un instructor para una Sesion, solo los instructores deben ser visibles.

> Creamos nuevas categorias padres Tacher/Level 1 y Teacher/Level2
El instructor de una sesión puede ser un instructor o un profesor.

##Campos estimados
Los campos suelen estar guardados directamente en la base de datos y ser recogidos directamente desde ella. Sin embargo también pueden ser calculados. En este caso se llama a un método del modelo para calcular el valor del campo.

Para crear un campo estimado se crea un campo y se pone el atributo ‘compute’ en el nombre del método.

##Dependencias 
El valor del campos estimado suele depender de valores de otros campos. Debemos especificar esto campos en el método con ‘depends()’.

> Añadimos el porcentaje de los sitios ocupados en el modelo Sesion. Mostramos ese campo en las vistas como una barra de progreso.

##Onchange
Permite actualizar el formulario de la interfaz cuando un usuario lo rellena con un valor, sin guardar nada en la base de datos.

> Creamos un mensaje para advertir sobre valores no válidos cuando se introduzca un número de asiento negativo o más participantes que asientos.




