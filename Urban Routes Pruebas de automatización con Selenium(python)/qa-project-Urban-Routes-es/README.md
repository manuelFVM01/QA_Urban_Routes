      Pruebas automatizadas para Urban Routes con Selenium (Python)

Necesitas tener instalados los paquetes de selenium, pytest y request para ejecutar las pruebas.

Necesitas instalar el driver de Selenium, puedes encontrarlo en el siguiente
 enlace: https://googlechromelabs.github.io/chrome-for-testing/

Abre la carpeta del proyecto en Pycharm.

Para instalar Selenium abre la consola y ejecuta el comando: pip install selenium

Para instalar Pytest abre la consola y ejecuta el comando: pip install -U pytest

Descripción: En este proyecto, se evalúan las funciones clave de la tarifa "Comfort"
 al solicitar un taxi. Verificamos que los números de teléfono y la tarjeta coincidan
con los datos ingresados, se respete la restricción de caracteres en los comentarios,
y que los botones para agregar mantas y helados funcionen correctamente. Además, se
comprueba la funcionalidad de solicitar el taxi y visualizar la información del 
conductor. La estructura del proyecto organiza las clases y métodos en distintas
páginas: una página contiene el método para recibir el código del celular, otra incluye
métodos y localizadores para las funcionalidades de la página, y la última página
centraliza el código de las pruebas. Se revisaron los casos de prueba que no pasaron