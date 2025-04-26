# Guía Completa de Docker

## Índice
1. [Introducción a Docker](#introducción-a-docker)
2. [Instalación de Docker](#instalación-de-docker)
3. [Conceptos Fundamentales](#conceptos-fundamentales)
4. [Imágenes de Docker](#imágenes-de-docker)
5. [Contenedores](#contenedores)
6. [Dockerfile](#dockerfile)
7. [Docker Compose](#docker-compose)
8. [Redes en Docker](#redes-en-docker)
9. [Volúmenes y Persistencia](#volúmenes-y-persistencia)
10. [Docker Hub y Registros](#docker-hub-y-registros)
11. [Docker en Producción](#docker-en-producción)
12. [Orquestación con Docker Swarm](#orquestación-con-docker-swarm)
13. [Docker y Kubernetes](#docker-y-kubernetes)
14. [Buenas Prácticas](#buenas-prácticas)
15. [Seguridad en Docker](#seguridad-en-docker)
16. [Solución de Problemas Comunes](#solución-de-problemas-comunes)
17. [Recursos Adicionales](#recursos-adicionales)

## Introducción a Docker

### ¿Qué es Docker?

Docker es una plataforma de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software. Los contenedores permiten empaquetar una aplicación junto con todas sus dependencias en una unidad estandarizada para el desarrollo de software.

### ¿Por qué usar Docker?

- **Consistencia**: "Funciona en mi máquina" deja de ser un problema. Si funciona en un contenedor Docker, funcionará en cualquier lugar donde Docker esté instalado.
- **Aislamiento**: Las aplicaciones y sus dependencias se ejecutan en entornos aislados, evitando conflictos.
- **Eficiencia**: Los contenedores comparten el kernel del sistema operativo y utilizan menos recursos que las máquinas virtuales.
- **Portabilidad**: Las aplicaciones empaquetadas en contenedores pueden ejecutarse en cualquier plataforma que soporte Docker.
- **Escalabilidad**: Facilita el escalado horizontal de aplicaciones.
- **Desarrollo rápido**: Agiliza el ciclo de desarrollo, pruebas y despliegue.

### Diferencia entre contenedores y máquinas virtuales

**Máquinas Virtuales (VMs)**:
- Virtualizan un sistema completo, incluyendo el sistema operativo.
- Cada VM tiene su propio kernel y sistema operativo.
- Requieren más recursos (CPU, memoria, espacio en disco).
- Tiempo de inicio más lento.

**Contenedores Docker**:
- Virtualizan solo la aplicación y sus dependencias, no el sistema operativo completo.
- Comparten el kernel del sistema operativo host.
- Uso más eficiente de recursos.
- Inicio casi instantáneo.
- Ocupan menos espacio.

![Comparación entre VMs y Contenedores](https://www.docker.com/sites/default/files/d8/2018-11/docker-containerized-and-vm-transparent-bg.png)

## Instalación de Docker

### Windows

**Requisitos**:
- Windows 10 64-bit: Pro, Enterprise, o Education (Build 16299 o posterior).
- Habilitar la característica Hyper-V y Contenedores de Windows.

**Pasos**:
1. Descarga [Docker Desktop para Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).
2. Ejecuta el instalador y sigue las instrucciones.
3. Una vez instalado, inicia Docker Desktop.
4. Verifica la instalación ejecutando en PowerShell o CMD:
   ```bash
   docker --version
   docker run hello-world
   ```

### macOS

**Requisitos**:
- macOS 10.14 (Mojave) o posterior.

**Pasos**:
1. Descarga [Docker Desktop para Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/).
2. Arrastra el ícono de Docker a la carpeta Aplicaciones.
3. Inicia Docker desde Aplicaciones.
4. Verifica la instalación ejecutando en Terminal:
   ```bash
   docker --version
   docker run hello-world
   ```

### Linux (Ubuntu)

**Pasos**:
1. Actualiza los repositorios:
   ```bash
   sudo apt update
   ```

2. Instala paquetes necesarios:
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Añade la clave GPG oficial de Docker:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

4. Añade el repositorio de Docker:
   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

5. Actualiza los repositorios nuevamente:
   ```bash
   sudo apt update
   ```

6. Instala Docker CE:
   ```bash
   sudo apt install docker-ce
   ```

7. Verifica la instalación:
   ```bash
   sudo docker --version
   sudo docker run hello-world
   ```

8. (Opcional) Añade tu usuario al grupo docker para ejecutar comandos sin sudo:
   ```bash
   sudo usermod -aG docker ${USER}
   ```
   Cierra sesión y vuelve a iniciarla para que los cambios surtan efecto.

## Conceptos Fundamentales

### Arquitectura de Docker

La arquitectura de Docker sigue un modelo cliente-servidor:

- **Docker Daemon (dockerd)**: El servicio en segundo plano que gestiona la construcción, ejecución y distribución de contenedores Docker.
- **Cliente Docker (docker)**: La herramienta de línea de comandos que permite interactuar con Docker.
- **Registros Docker**: Almacenes de imágenes Docker (ej. Docker Hub).
- **Objetos Docker**: Imágenes, contenedores, redes, volúmenes, plugins y otros objetos.

![Arquitectura de Docker](https://docs.docker.com/engine/images/architecture.svg)

### Terminología clave

- **Imagen**: Plantilla de solo lectura con instrucciones para crear un contenedor. Una imagen puede estar basada en otras imágenes, con capas adicionales.
- **Contenedor**: Instancia ejecutable de una imagen. Un contenedor está aislado del host y de otros contenedores.
- **Dockerfile**: Archivo de texto con instrucciones para construir una imagen Docker.
- **Docker Compose**: Herramienta para definir y ejecutar aplicaciones multi-contenedor.
- **Volumen**: Mecanismo para persistir datos generados y utilizados por contenedores Docker.
- **Red (Network)**: Canal de comunicación entre contenedores o con el exterior.
- **Registro (Registry)**: Repositorio donde se almacenan las imágenes Docker.
- **Swarm**: Grupo de máquinas que ejecutan Docker y se agrupan para formar un cluster.
- **Servicio**: Definición de cómo ejecutar las imágenes de contenedor y las instrucciones para hacerlo.

## Imágenes de Docker

### ¿Qué son las imágenes?

Las imágenes son plantillas de solo lectura que contienen:
- Un sistema operativo base o mínimo
- Dependencias de la aplicación
- Configuración de la aplicación
- Aplicación en sí

### Trabajando con imágenes

**Listar imágenes:**
```bash
docker images
# o
docker image ls
```

**Buscar imágenes en Docker Hub:**
```bash
docker search ubuntu
```

**Descargar una imagen:**
```bash
docker pull ubuntu:20.04
```

**Eliminar una imagen:**
```bash
docker rmi ubuntu:20.04
# o
docker image rm ubuntu:20.04
```

**Ver detalles de una imagen:**
```bash
docker inspect ubuntu:20.04
```

**Construcción de imágenes:**
```bash
docker build -t mi-app:1.0 .
```

### Sistema de capas

Las imágenes Docker se construyen mediante un sistema de capas superpuestas:
- Cada instrucción en un Dockerfile crea una nueva capa.
- Las capas son inmutables.
- Solo la capa superior es de escritura cuando se convierte en un contenedor.
- Las capas se almacenan en caché y se comparten entre imágenes, ahorrando espacio.

![Sistema de capas de Docker](https://docs.docker.com/storage/storagedriver/images/container-layers.jpg)

### Etiquetas (tags)

Las etiquetas permiten versionar las imágenes:
- `ubuntu:20.04` - Ubuntu versión 20.04
- `nginx:latest` - La última versión de Nginx
- `node:14-alpine` - Node.js 14 basado en Alpine Linux

Es una buena práctica usar etiquetas específicas en lugar de `latest` para garantizar consistencia.

## Contenedores

### Ciclo de vida de un contenedor

Los estados de un contenedor incluyen:
- **Creado**: El contenedor ha sido creado pero no iniciado.
- **En ejecución**: El contenedor está en funcionamiento.
- **Pausado**: El contenedor está pausado.
- **Detenido**: El contenedor ha sido detenido.
- **Eliminado**: El contenedor ha sido eliminado.

### Comandos básicos de contenedores

**Crear y ejecutar un contenedor:**
```bash
docker run nginx
```

**Crear un contenedor interactivo:**
```bash
docker run -it ubuntu bash
```

**Ejecutar un contenedor en segundo plano:**
```bash
docker run -d nginx
```

**Listar contenedores en ejecución:**
```bash
docker ps
```

**Listar todos los contenedores:**
```bash
docker ps -a
```

**Detener un contenedor:**
```bash
docker stop <container_id>
```

**Iniciar un contenedor detenido:**
```bash
docker start <container_id>
```

**Reiniciar un contenedor:**
```bash
docker restart <container_id>
```

**Eliminar un contenedor:**
```bash
docker rm <container_id>
```

**Eliminar un contenedor en ejecución:**
```bash
docker rm -f <container_id>
```

**Ver logs de un contenedor:**
```bash
docker logs <container_id>
```

**Seguir logs en tiempo real:**
```bash
docker logs -f <container_id>
```

**Ejecutar comandos en un contenedor en ejecución:**
```bash
docker exec -it <container_id> bash
```

### Opciones comunes de docker run

- `-d, --detach`: Ejecutar en segundo plano
- `-p, --publish`: Mapear puertos (host:contenedor)
- `-v, --volume`: Montar volúmenes
- `-e, --env`: Establecer variables de entorno
- `--name`: Asignar un nombre al contenedor
- `--network`: Conectar a una red
- `--restart`: Política de reinicio (no, on-failure, always, unless-stopped)
- `--memory`: Limitar uso de memoria
- `--cpus`: Limitar uso de CPU

**Ejemplos:**

```bash
# Ejecutar Nginx mapeando el puerto 8080 del host al 80 del contenedor
docker run -d -p 8080:80 --name mi-nginx nginx

# Ejecutar MySQL con variables de entorno
docker run -d --name mi-mysql -e MYSQL_ROOT_PASSWORD=secret mysql:8

# Ejecutar un contenedor con límites de recursos
docker run -d --name resource-limited --memory=512m --cpus=0.5 ubuntu
```

## Dockerfile

### ¿Qué es un Dockerfile?

Un Dockerfile es un archivo de texto que contiene instrucciones para construir una imagen Docker. Permite automatizar el proceso de creación de imágenes.

### Instrucciones básicas del Dockerfile

- **FROM**: Establece la imagen base
- **LABEL**: Añade metadatos a la imagen
- **ENV**: Establece variables de entorno
- **ARG**: Define variables durante la construcción
- **WORKDIR**: Establece el directorio de trabajo
- **COPY/ADD**: Copia archivos al contenedor
- **RUN**: Ejecuta comandos durante la construcción
- **EXPOSE**: Documenta los puertos que se utilizarán
- **CMD**: Comando predeterminado al ejecutar el contenedor
- **ENTRYPOINT**: Configura el contenedor para ejecutarse como un ejecutable

### Ejemplo de Dockerfile para una aplicación Node.js

```dockerfile
# Imagen base
FROM node:14-alpine

# Metadatos
LABEL maintainer="tu-email@ejemplo.com"
LABEL version="1.0"

# Variables de entorno
ENV NODE_ENV=production

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install --production

# Copiar código fuente
COPY . .

# Exponer puerto
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "app.js"]
```

### Construcción de imágenes

```bash
# Construir una imagen desde el Dockerfile del directorio actual
docker build -t nombre-imagen:tag .

# Construir con un Dockerfile específico
docker build -f MiDockerfile -t nombre-imagen:tag .

# Construir pasando variables ARG
docker build --build-arg VERSION=1.0 -t nombre-imagen:tag .
```

### Buenas prácticas para Dockerfiles

1. **Usar imágenes base específicas y ligeras**: Preferir Alpine o Debian slim cuando sea posible.
2. **Minimizar el número de capas**: Agrupar comandos RUN relacionados.
3. **Eliminar archivos innecesarios** después de usarlos.
4. **No instalar paquetes de desarrollo** en imágenes de producción.
5. **Usar .dockerignore** para excluir archivos innecesarios.
6. **Establecer versiones específicas** de dependencias.
7. **Organizar instrucciones** de menos a más frecuentes en cambiar.
8. **Usar COPY en lugar de ADD** (a menos que necesites extraer archivos).
9. **Ejecutar procesos como usuarios no-root**.
10. **Usar multi-stage builds** para reducir el tamaño final de la imagen.

### Ejemplo de .dockerignore

```
.git
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.dockerignore
.env
.gitignore
README.md
LICENSE
.vscode
```

### Multi-stage builds

Permiten crear imágenes más pequeñas separando el entorno de compilación del de ejecución:

```dockerfile
# Etapa de compilación
FROM node:14 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Etapa de producción
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Docker Compose

### ¿Qué es Docker Compose?

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker multi-contenedor. Con un archivo YAML, se configuran todos los servicios de la aplicación y con un solo comando se crean e inician todos los servicios.

### Instalación de Docker Compose

**En Linux**:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

**En Windows y macOS**: Docker Compose viene incluido con Docker Desktop.

### Estructura del archivo docker-compose.yml

```yaml
version: '3'  # Versión de la sintaxis

services:     # Definición de servicios (contenedores)
  web:        # Nombre del servicio
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - api

  api:        # Otro servicio
    build: ./api
    environment:
      - NODE_ENV=production
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:         # Servicio de base de datos
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_USER=myuser
      - POSTGRES_DB=mydb

volumes:      # Definición de volúmenes
  postgres_data:
```

### Comandos principales de Docker Compose

**Iniciar servicios**:
```bash
docker-compose up
```

**Iniciar en segundo plano**:
```bash
docker-compose up -d
```

**Detener servicios**:
```bash
docker-compose down
```

**Detener y eliminar volúmenes**:
```bash
docker-compose down -v
```

**Ver logs**:
```bash
docker-compose logs
```

**Seguir logs**:
```bash
docker-compose logs -f
```

**Ver servicios en ejecución**:
```bash
docker-compose ps
```

**Ejecutar comandos en un servicio**:
```bash
docker-compose exec web bash
```

**Construir o reconstruir servicios**:
```bash
docker-compose build
```

**Escalar servicios**:
```bash
docker-compose up -d --scale web=3
```

### Configuraciones avanzadas

#### Redes personalizadas

```yaml
services:
  web:
    image: nginx
    networks:
      - frontend

  api:
    build: ./api
    networks:
      - frontend
      - backend

  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
  backend:
```

#### Variables de entorno y .env

```yaml
services:
  web:
    image: nginx
    environment:
      - DEBUG=1
      - API_URL=${API_URL}
```

En un archivo `.env` separado:
```
API_URL=http://api:3000
```

#### Servicios con healthcheck

```yaml
services:
  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

#### Dependencias y orden de inicio

```yaml
services:
  web:
    image: nginx
    depends_on:
      api:
        condition: service_healthy
      cache:
        condition: service_started
```

## Redes en Docker

### Tipos de redes en Docker

Docker incluye varios controladores de red (network drivers):

- **bridge**: Red predeterminada para contenedores en un solo host.
- **host**: Elimina el aislamiento de red entre el contenedor y el host.
- **none**: Desactiva toda la red para el contenedor.
- **overlay**: Conecta múltiples daemons de Docker, permitiendo comunicación entre nodos en un Swarm.
- **macvlan**: Asigna direcciones MAC a contenedores, apareciendo como dispositivos físicos.
- **Redes definidas por plugins**: Permite usar plugins de red de terceros.

### Comandos básicos de redes

**Listar redes**:
```bash
docker network ls
```

**Crear una red**:
```bash
docker network create mi-red
```

**Crear una red con configuración específica**:
```bash
docker network create --driver overlay --subnet=10.0.0.0/24 mi-red-overlay
```

**Eliminar una red**:
```bash
docker network rm mi-red
```

**Inspeccionar una red**:
```bash
docker network inspect mi-red
```

**Conectar un contenedor existente a una red**:
```bash
docker network connect mi-red mi-contenedor
```

**Desconectar un contenedor de una red**:
```bash
docker network disconnect mi-red mi-contenedor
```

### Uso de redes en contenedores

**Ejecutar un contenedor en una red específica**:
```bash
docker run --network=mi-red --name web nginx
```

**Ejemplo de comunicación entre contenedores**:
```bash
# Crear una red
docker network create app-network

# Ejecutar una base de datos
docker run -d --name db --network app-network postgres

# Ejecutar una aplicación web que se conecta a la base de datos
docker run -d --name web --network app-network -p 8080:80 mi-app-web
```

En este ejemplo, el contenedor `web` puede conectarse a `db` usando el nombre del contenedor como nombre de host.

### Configuración de redes en Docker Compose

```yaml
version: '3'

services:
  web:
    image: nginx
    networks:
      - frontend

  api:
    build: ./api
    networks:
      - frontend
      - backend

  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # Solo accesible desde contenedores, no desde el host
```

## Volúmenes y Persistencia

### Tipos de almacenamiento en Docker

Docker ofrece tres opciones principales para persistir datos:

1. **Volúmenes**: La forma preferida de persistir datos. Gestionados por Docker.
2. **Bind mounts**: Mapeo directo de un directorio del host al contenedor.
3. **tmpfs mounts**: Almacenamiento en memoria (volátil).

![Tipos de montaje](https://docs.docker.com/storage/images/types-of-mounts.png)

### Trabajando con volúmenes

**Crear un volumen**:
```bash
docker volume create mi-volumen
```

**Listar volúmenes**:
```bash
docker volume ls
```

**Inspeccionar un volumen**:
```bash
docker volume inspect mi-volumen
```

**Eliminar un volumen**:
```bash
docker volume rm mi-volumen
```

**Eliminar volúmenes no utilizados**:
```bash
docker volume prune
```

### Uso de volúmenes con contenedores

**Ejecutar un contenedor con un volumen**:
```bash
docker run -d --name mi-mysql -v mi-datos-mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret mysql
```

**Bind mount (directorio del host)**:
```bash
docker run -d --name mi-nginx -v $(pwd)/html:/usr/share/nginx/html:ro -p 8080:80 nginx
```

**Volumen de solo lectura**:
```bash
docker run -d --name mi-app -v mi-config:/app/config:ro mi-imagen
```

**Volumen temporal en memoria**:
```bash
docker run -d --name mi-app --tmpfs /app/temp mi-imagen
```

### Volúmenes en Docker Compose

```yaml
version: '3'

services:
  db:
    image: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    environment:
      - POSTGRES_PASSWORD=secret

  web:
    image: nginx
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro

volumes:
  postgres_data:
```

### Respaldo y restauración de volúmenes

**Respaldo**:
```bash
# Crear un contenedor temporal para copiar los datos
docker run --rm -v mi-volumen:/source -v $(pwd):/backup alpine tar czvf /backup/mi-volumen-backup.tar.gz -C /source .
```

**Restauración**:
```bash
# Crear un nuevo volumen si es necesario
docker volume create nuevo-volumen

# Restaurar datos desde el respaldo
docker run --rm -v nuevo-volumen:/target -v $(pwd):/backup alpine sh -c "tar xzvf /backup/mi-volumen-backup.tar.gz -C /target"
```

## Docker Hub y Registros

### Docker Hub

Docker Hub es el registro público de imágenes Docker, con más de 100,000 imágenes disponibles.

**Registro en Docker Hub**:
1. Crear una cuenta en [hub.docker.com](https://hub.docker.com/)
2. Autenticarse localmente:
   ```bash
   docker login
   ```

**Buscar imágenes**:
```bash
docker search nginx
```

**Subir imágenes a Docker Hub**:
```bash
# Etiquetar una imagen local con tu nombre de usuario
docker tag mi-app:latest usuario/mi-app:latest

# Subir la imagen
docker push usuario/mi-app:latest
```

### Registros privados

**Ejecutar un registro local**:
```bash
docker run -d -p 5000:5000 --name registry registry:2
```

**Usar un registro local**:
```bash
# Etiquetar imagen para el registro local
docker tag mi-app:latest localhost:5000/mi-app:latest

# Subir imagen al registro local
docker push localhost:5000/mi-app:latest

# Descargar imagen del registro local
docker pull localhost:5000/mi-app:latest
```

**Configurar autenticación para registros privados**:
1. Crear archivo de autenticación:
   ```bash
   docker login mi-registro.ejemplo.com
   ```
2. Usar credenciales con Docker Compose:
   ```yaml
   services:
     app:
       image: mi-registro.ejemplo.com/mi-app:latest
   ```

### Registros comunes

- **Docker Hub**: Público, con límites de descargas para usuarios gratuitos
- **Amazon ECR**: Servicio de registro de Amazon
- **Google Container Registry**: Servicio de registro de Google
- **Azure Container Registry**: Servicio de registro de Microsoft
- **GitHub Container Registry**: Servicio de registro de GitHub
- **GitLab Container Registry**: Integrado con GitLab

## Docker en Producción

### Consideraciones para entornos de producción

1. **Seguridad**:
   - Ejecutar contenedores como usuario no-root
   - Escanear imágenes en busca de vulnerabilidades
   - Usar imágenes oficiales o verificadas
   - Implementar el principio de mínimo privilegio

2. **Rendimiento**:
   - Limitar recursos (CPU, memoria)
   - Monitorizar el uso de recursos
   - Optimizar el tamaño de las imágenes

3. **Disponibilidad**:
   - Implementar réplicas de servicios
   - Configurar políticas de reinicio
   - Usar health checks

4. **Persistencia**:
   - Planificar la estrategia de backup
   - Usar volúmenes adecuados
   - Considerar el almacenamiento distribuido

5. **Redes**:
   - Configurar redes seguras
   - Limitar la exposición de puertos
   - Usar redes overlay para multi-host

### Configuraciones para producción

**Limitar recursos**:
```bash
docker run -d --name app \
  --memory="512m" \
  --memory-swap="1g" \
  --cpus="0.5" \
  mi-app
```

**Health checks**:
```bash
docker run -d --name web \
  --health-cmd="curl -f http://localhost/ || exit 1" \
  --health-interval=5s \
  --health-retries=3 \
  --health-timeout=2s \
  --health-start-period=15s \
  nginx
```

**Políticas de reinicio**:
```bash
docker run -d --name app \
  --restart=always \
  mi-app
```

**Opciones de reinicio**:
- `no`: No reiniciar automáticamente (predeterminado)
- `on-failure[:max-retries]`: Reiniciar si sale con código distinto a 0
- `always`: Siempre reiniciar, incluso al detener manualmente (reiniciará al iniciar Docker)
- `unless-stopped`: Similar a always, pero no reinicia si fue detenido manualmente

### Docker Compose para producción

```yaml
version: '3.8'

services:
  app:
    image: mi-app:1.0.2
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
      restart_policy:
        condition: on-failure
        max_attempts: 3
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

### Monitorización

**Comandos básicos**:
```bash
# Ver estadísticas en tiempo real
docker stats

# Ver procesos en un contenedor
docker top mi-contenedor
```

**Herramientas de monitorización**:
- Prometheus + Grafana
- cAdvisor
- Datadog
- New Relic
- Sysdig

**Ejemplo de configuración de Prometheus y cAdvisor**:
```yaml
version: '3'

services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  cadvisor:
    image: gcr.io/google-containers/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
```

## Orquestación con Docker Swarm

### ¿Qué es Docker Swarm?

Docker Swarm es el sistema de orquestación nativo de Docker que permite gestionar un cluster de nodos Docker. Facilita la implementación, escalado y gestión de servicios en múltiples hosts.

### Configuración de Docker Swarm

**Inicializar un Swarm**:
```bash
docker swarm init --advertise-addr <IP-DEL-MANAGER>
```

**Añadir nodos worker**:
```bash
# En el nodo manager, obtener el token
docker swarm join-token worker

# En los nodos worker, usar el comando proporcionado
docker swarm join --token <TOKEN> <IP-DEL-MANAGER>:2377
```

**Añadir nodos manager**:
```bash
# En el nodo manager actual, obtener el token
docker swarm join-token manager

# En el nuevo nodo, usar el comando proporcionado
docker swarm join --token <TOKEN> <IP-DEL-MANAGER>:2377
```

**Listar nodos**:
```bash
docker node ls
```

**Promover un worker a manager**:
```bash
docker node promote <ID-NODO>
```

**Degradar un manager a worker**:
```bash
docker node demote <ID-NODO>
```

### Servicios en Docker Swarm

**Crear un servicio**:
```bash
docker service create --name web --replicas 3 -p 80:80 nginx
```

**Listar servicios**:
```bash
docker service ls
```

**Ver detalles de un servicio**:
```bash
docker service ps web
```

**Escalar un servicio**:
```bash
docker service scale web=5
```

**Actualizar un servicio**:
```bash
docker service update --image nginx:alpine web
```

**Actualizar con rolling update**:
```bash
docker service update --update-parallelism 2 --update-delay 20s --image nginx:alpine web
```

**Eliminar un servicio**:
```bash
docker service rm web
```

### Stack en Docker Swarm

Un stack es un grupo de servicios relacionados que comparten dependencias y se pueden escalar juntos.

**Desplegar un stack con docker-compose.yml**:
```bash
docker stack deploy -c docker-compose.yml mi-stack
```

**Listar stacks**:
```bash
docker stack ls
```

**Listar servicios de un stack**:
```bash
docker stack services mi-stack
```

**Ver tareas de un stack**:
```bash
docker stack ps mi-stack
```

**Eliminar un stack**:
```bash
docker stack rm mi-stack
```

### Ejemplo de docker-compose.yml para Swarm

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    deploy:
      mode: replicated
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    networks:
      - webnet

  visualizer:
    image: dockersamples/visualizer
    ports:
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet

networks:
  webnet:
```

### Secretos en Docker Swarm

**Crear un secreto**:
```bash
echo "mi_contraseña_segura" | docker secret create db_password -
```

**Crear un secreto desde un archivo**:
```bash
docker secret create ssl_cert ./cert.pem
```

**Listar secretos**:
```bash
docker secret ls
```

**Usar secretos en un servicio**:
```bash
docker service create --name db \
  --secret db_password \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/db_password \
  postgres
```

**Secretos en docker-compose.yml**:
```yaml
version: '3.8'

services:
  db:
    image: postgres
    secrets:
      - db_password
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    external: true
```

## Docker y Kubernetes

### Comparación entre Docker Swarm y Kubernetes

**Docker Swarm**:
- Integrado en Docker
- Más fácil de configurar y usar
- Curva de aprendizaje más suave
- Menos funcionalidades avanzadas
- Bueno para equipos pequeños y cargas de trabajo simples

**Kubernetes**:
- Estándar de la industria
- Más complejo de configurar
- Más potente y flexible
- Mejor para grandes equipos y aplicaciones complejas
- Más opciones de orquestación avanzada

### Uso de Docker con Kubernetes

Aunque Kubernetes está reemplazando gradualmente Docker como runtime de contenedores (con containerd), Docker sigue siendo una herramienta valiosa para desarrollar y construir imágenes que luego se ejecutarán en Kubernetes.

**Flujo típico**:
1. Desarrollar aplicación y definir Dockerfile
2. Construir imagen con Docker
3. Publicar imagen en un registro
4. Definir manifiestos de Kubernetes (YAML)
5. Desplegar en Kubernetes

**Ejemplo de manifiesto Kubernetes para una imagen Docker**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
```

### Migración de Docker Compose a Kubernetes

Herramientas como `kompose` pueden ayudar a convertir archivos docker-compose.yml a recursos de Kubernetes:

```bash
# Instalar kompose
curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv kompose /usr/local/bin/

# Convertir docker-compose.yml
kompose convert -f docker-compose.yml
```

Esto generará los archivos YAML de Kubernetes correspondientes a los servicios definidos en el archivo docker-compose.yml.

## Buenas Prácticas

### Seguridad

1. **Mantén Docker y las imágenes actualizadas**
2. **Usa imágenes oficiales o de confianza**
3. **Escanea imágenes en busca de vulnerabilidades**:
   ```bash
   docker scan mi-imagen
   ```
4. **Limita capacidades y recursos**:
   ```bash
   docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx
   ```
5. **No ejecutes contenedores como root**:
   ```dockerfile
   FROM ubuntu
   RUN groupadd -r myuser && useradd -r -g myuser myuser
   USER myuser
   ```
6. **Usa secretos para información sensible**
7. **Configura políticas de red restrictivas**
8. **Usa read-only filesystems cuando sea posible**:
   ```bash
   docker run --read-only nginx
   ```

### Rendimiento

1. **Construye imágenes ligeras**:
   - Usa imágenes base Alpine
   - Implementa multi-stage builds
   - Minimiza el número de capas

2. **Optimiza el almacenamiento en caché de capas**:
   - Coloca las instrucciones que cambian con menos frecuencia al principio del Dockerfile
   - Agrupa comandos RUN relacionados

3. **Limita los recursos de los contenedores**:
   ```bash
   docker run --memory=512m --cpus=0.5 mi-app
   ```

4. **Usa volúmenes para datos que cambian frecuentemente**

5. **Implementa health checks adecuados**

### Desarrollo y CI/CD

1. **Usa Docker para desarrollo local**:
   - Garantiza consistencia entre entornos
   - Evita problemas de "funciona en mi máquina"

2. **Implementa un flujo de CI/CD con Docker**:
   - Construye imágenes en cada commit
   - Ejecuta pruebas en contenedores
   - Publica imágenes etiquetadas con versiones

3. **Versiona tus imágenes adecuadamente**:
   - No uses la etiqueta `latest` en producción
   - Usa etiquetas semánticas (ej. `1.2.3`)
   - Considera usar el hash del commit como etiqueta

4. **Documenta tus imágenes y contenedores**:
   - Usa etiquetas LABEL en el Dockerfile
   - Mantén un README actualizado

### Gestión de configuración

1. **Externaliza la configuración**:
   - Usa variables de entorno para configuración básica
   - Usa volúmenes para archivos de configuración
   - Usa secretos para información sensible

2. **Implementa configuración por entorno**:
   - Usa archivos .env diferentes por entorno
   - Usa Docker Compose override files:
     ```bash
     docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
     ```

3. **Centraliza la gestión de logs**:
   ```bash
   docker run --log-driver=fluentd --log-opt fluentd-address=localhost:24224 nginx
   ```

## Seguridad en Docker

### Vulnerabilidades comunes

1. **Imágenes con software obsoleto o vulnerable**
2. **Acceso privilegiado innecesario**
3. **Secretos expuestos en imágenes**
4. **Contenedores sin recursos limitados**
5. **Contenedores con demasiados privilegios**
6. **Daemons de Docker expuestos sin autenticación**

### Escaneo de vulnerabilidades

**Docker Scout** (integrado en Docker Hub):
```bash
docker scan mi-imagen
```

**Trivy**:
```bash
trivy image mi-imagen
```

**Clair**:
Un escáner de vulnerabilidades de código abierto que se puede integrar en una canalización CI/CD.

### Hardening de Docker

1. **Configurar el daemon de Docker de forma segura**:
   - Usar TLS para la comunicación
   - Limitar quién puede conectarse al socket de Docker

2. **Ejemplo de configuración segura** `/etc/docker/daemon.json`:
   ```json
   {
     "icc": false,
     "userns-remap": "default",
     "log-driver": "syslog",
     "no-new-privileges": true,
     "live-restore": true,
     "userland-proxy": false,
     "seccomp-profile": "/etc/docker/seccomp-profile.json"
   }
   ```

3. **Usar redes seguras**:
   - Crear redes aisladas para distintos grupos de contenedores
   - Permitir solo las comunicaciones necesarias

4. **Aplicar políticas de seguridad**:
   ```bash
   docker run --security-opt=no-new-privileges --cap-drop=ALL nginx
   ```

### AppArmor y SELinux

**AppArmor**:
```bash
docker run --security-opt apparmor=docker-default nginx
```

**SELinux**:
```bash
docker run --security-opt label=level:s0:c100,c200 nginx
```

## Solución de Problemas Comunes

### Problemas de instalación

1. **Docker no inicia**:
   - Verificar que el servicio está ejecutándose:
     ```bash
     systemctl status docker
     ```
   - Verificar logs:
     ```bash
     journalctl -u docker
     ```

2. **Permisos insuficientes**:
   - Añadir usuario al grupo docker:
     ```bash
     sudo usermod -aG docker $USER
     ```
   - Cerrar sesión y volver a iniciarla

### Problemas con contenedores

1. **Contenedor se detiene inesperadamente**:
   - Verificar logs:
     ```bash
     docker logs mi-contenedor
     ```
   - Verificar estado:
     ```bash
     docker inspect mi-contenedor
     ```
   - Verificar uso de recursos:
     ```bash
     docker stats mi-contenedor
     ```

2. **No se puede eliminar una imagen o contenedor**:
   - Forzar eliminación:
     ```bash
     docker rm -f mi-contenedor
     docker rmi -f mi-imagen
     ```
   - Limpiar recursos no utilizados:
     ```bash
     docker system prune
     ```

3. **Problemas de red**:
   - Verificar configuración de red:
     ```bash
     docker network inspect bridge
     ```
   - Verificar reglas de firewall
   - Probar conectividad desde dentro del contenedor:
     ```bash
     docker exec -it mi-contenedor ping google.com
     ```

### Problemas de espacio en disco

1. **Docker usa demasiado espacio**:
   - Ver uso de espacio:
     ```bash
     docker system df
     ```
   - Limpiar recursos no utilizados:
     ```bash
     docker system prune -a --volumes
     ```

2. **Contenedor se queda sin espacio**:
   - Usar volúmenes para datos persistentes
   - Usar imágenes más pequeñas
   - Eliminar archivos temporales en Dockerfile

### Problemas de rendimiento

1. **Contenedor lento o con alto uso de CPU**:
   - Limitar recursos:
     ```bash
     docker update --cpus=0.5 --memory=512m mi-contenedor
     ```
   - Verificar logs en busca de problemas
   - Optimizar la aplicación dentro del contenedor

2. **Inicio lento de contenedores**:
   - Usar imágenes más pequeñas
   - Implementar multi-stage builds
   - Reducir número de capas

## Recursos Adicionales

### Documentación Oficial
- [Documentación de Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Blog](https://www.docker.com/blog/)

### Herramientas Útiles
- [Docker Compose](https://docs.docker.com/compose/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Portainer](https://www.portainer.io/) - Interfaz gráfica para gestionar Docker
- [ctop](https://github.com/bcicen/ctop) - Monitorización de contenedores en terminal
- [lazydocker](https://github.com/jesseduffield/lazydocker) - Interfaz de terminal para Docker

### Cursos y Tutoriales
- [Play with Docker](https://labs.play-with-docker.com/) - Entorno de pruebas online
- [Docker for Beginners](https://training.play-with-docker.com/beginner-linux/)
- [Docker Curriculum](https://docker-curriculum.com/)

### Libros Recomendados
- "Docker: Up & Running" por Karl Matthias y Sean P. Kane
- "Docker Deep Dive" por Nigel Poulton
- "Docker in Practice" por Ian Miell y Aidan Hobson Sayers

### Comunidad
- [Docker Forums](https://forums.docker.com/)
- [Stack Overflow - Docker](https://stackoverflow.com/questions/tagged/docker)
- [Reddit - r/docker](https://www.reddit.com/r/docker/)

### Cheatsheets
- [Docker Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)
- [Dockerfile Cheatsheet](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)

---

¡Ahora estás listo para comenzar tu viaje con Docker! Esta guía cubre los conceptos fundamentales y te proporciona los comandos y ejemplos necesarios para trabajar con Docker de manera efectiva. A medida que te familiarices con estas herramientas, podrás construir, desplegar y gestionar aplicaciones en contenedores con confianza.