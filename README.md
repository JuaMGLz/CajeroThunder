# CajeroThunder 🌩️

Sistema de cajero automático (ATM) desarrollado en Python para la gestión integral de operaciones bancarias, enfocado en la seguridad de la información y el control de transacciones. 

Este proyecto implementa operaciones lógicas de bases de datos y manejo seguro de credenciales, demostrando habilidades clave en el desarrollo de software y arquitectura de aplicaciones.

## 🚀 Características Principales

- **Gestión de Usuarios y Seguridad Avanzada:** Control de acceso estricto y seguro. Las credenciales de los usuarios están protegidas mediante técnicas de hashing y manejo de código binario, garantizando que la información sensible no sea expuesta.
- **Operaciones Bancarias Completas (CRUD):**
  - Depósitos de efectivo a cuentas.
  - Retiros seguros desde el cajero.
  - Transferencias de fondos entre distintos usuarios.
- **Sistema de Respaldo (Backup):** Funcionalidad de copia de seguridad integrada para resguardar los datos del sistema y evitar cualquier pérdida de información crítica.
- **Generación de Comprobantes:** Registro detallado de cada movimiento y transacción, almacenado organizadamente en el directorio de `comprobantes`.

## 🛠️ Tecnologías y Herramientas

- **Lenguaje Principal:** Python
- **Gestión de Datos:** Conexión y manipulación de datos a través del módulo `conexion.py`.
- **Seguridad:** Algoritmos de encriptación y hashing para la protección de accesos.

## 📂 Estructura del Proyecto

* `app.py`: Archivo principal y punto de entrada que ejecuta la lógica central del cajero.
* `conexion.py`: Módulo encargado de establecer y gestionar la conexión de las operaciones bancarias.
* `comprobantes/`: Directorio destinado a almacenar los recibos y registros generados por las transacciones de los usuarios.
* `Imagenes/`: Recursos gráficos y visuales utilizados en la interfaz del sistema.

## 🎓 Contexto Académico

* **Institución:** UAEM Valle de Chalco
* **Carrera:** Ingeniería en Computación
* **Autor:** Juan Manuel González Espinosa

## 💡 Instalación y Uso

1. Clona este repositorio en tu entorno local:
   ```bash
   git clone [https://github.com/JuaMGLz/CajeroThunder.git](https://github.com/JuaMGLz/CajeroThunder.git)
