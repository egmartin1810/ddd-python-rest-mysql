# ddd-python-rest-mysql
Proyecto que consiste en armar un servicio web que exponga un endpoint para leer un archivo, consultar una serie de APIs públicas y cargar una base de datos con los datos del archivo y las consultas a las APIs, construido con patrones de diseño, concurrencia y Domain Driven Design.

### Prerequisitos

**1:** Clonar el proyecto a través del cliente git o desde desde un navegador.
```
git clone https://github.com/egmartin1810/ddd-python-rest-mysql.git
```
**2:** Tener Docker instalado de la página oficial: https://docs.docker.com/get-docker/. (instalar la última versión de Docker en su sistema operativo).

### Instalación

**Paso 1:** Estar dentro del directorio del proyecto que fue clonado:

```
cd ddd-python-rest-mysql
```

**Paso 2:** Ejecutar los contenedores:

```
docker-compose up -d --build 
```
**Step 3:** Verificar que los contenedores estén ejecutando.

```
docker-compose ps -a
```

**Step 3:** Verificar que los contenedores estén ejecutando.
