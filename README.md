# Proyecto Urban Grocers 
## Por: Ximena Valeria Velasco

### Descripción
- Urban Routes es una plataforma que permite seleccionar un viaje en taxi entre 2 ubicaciones, seleccionar el tipo de viaje, agregar datos de contacto y hacer requerimientos adicionales para finalmente pedir un taxi.
- Se utilizan selectores por:
-- ID
-- CLASE
-- SELECTOR
-- XPATH
- Este proyecto automatiza el proceso para pedir un taxi con tarifa Comfort de acuerdo a la siguiente descripción:
-- Configurar las direcciones Desde y Hasta
-- Dar click en el botón Pedir taxi
-- Seleccionar la tarifa Comfort.
-- Rellenar el número de teléfono y validarlo por SMS
-- Agregar una tarjeta de crédito. 
-- Escribir un mensaje para el conductor.
-- Pedir una manta y pañuelos.
-- Pedir 2 helados.
-- Pedir el taxi
-- Validar que Aparece el modal para buscar un taxi.

### Requerimientos: 
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas realizadas.
- Si no tienes los paquetes instalados, realízalo ejecutando los siguientes comandos
``` pip install requests ```
``` pip install pytest ```

### Tecnologías utilizadas:
- El proyecto se lo automatiza utiizando Selenium y Selenium Web Driver utilizando Page Object Model para la construcción de las clases que permitan realizar las pruebas


### Instrucciones:
- Abre un terminal
- Ubícate en el terminal la carpeta del proyecto donde se encuentra el archivo test_page.py . 
- Ejecuta todas las pruebas con el comando ```pytest ```.

