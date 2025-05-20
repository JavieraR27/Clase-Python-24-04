# Guía Completa de Amazon Linux para Estudiantes

## Índice
1. [Introducción a Amazon Linux](#introducción-a-amazon-linux)
2. [Creación de una Máquina Virtual en AWS](#creación-de-una-máquina-virtual-en-aws)
3. [Conexión a tu Instancia Amazon Linux](#conexión-a-tu-instancia-amazon-linux)
4. [Comandos Básicos de Linux](#comandos-básicos-de-linux)
5. [Gestión de Usuarios](#gestión-de-usuarios)
6. [Directorios y Archivos](#directorios-y-archivos)
7. [Permisos en Linux](#permisos-en-linux)
8. [Volúmenes en AWS](#volúmenes-en-aws)
9. [Entorno de Aprendizaje de Amazon](#entorno-de-aprendizaje-de-amazon)
10. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)

## Introducción a Amazon Linux

Amazon Linux es una distribución de Linux desarrollada por Amazon Web Services (AWS) específicamente para funcionar en su infraestructura en la nube. Está basada en Red Hat Enterprise Linux y está optimizada para entornos de nube.

**Características principales:**
- Diseñado para integrarse perfectamente con los servicios de AWS
- Actualizaciones de seguridad regulares
- Configurado para alta performance en la nube
- Incluye herramientas específicas para gestionar servicios AWS
- Versiones actuales: Amazon Linux 2 y Amazon Linux 2023

## Creación de una Máquina Virtual en AWS

### Requisitos Previos
Antes de comenzar, necesitas:
- Una cuenta de AWS (puedes crear una cuenta gratuita)
- Conocimientos básicos de redes (IP, puertos, etc.)
- Un navegador web moderno

### Paso a Paso para Crear una Instancia EC2 con Amazon Linux

1. **Iniciar sesión en la consola de AWS**
   - Visita [https://aws.amazon.com/](https://aws.amazon.com/)
   - Haz clic en "Iniciar sesión en la consola"
   - Ingresa tus credenciales

2. **Navegar al servicio EC2**
   - En la página principal de la consola, busca y selecciona "EC2" bajo la sección "Servicios" o utiliza la barra de búsqueda

3. **Lanzar una instancia**
   - En el panel de EC2, haz clic en el botón "Lanzar instancia"
   - Selecciona "Lanzar instancia" en el menú desplegable

4. **Nombrar tu instancia**
   - Ingresa un nombre descriptivo para tu instancia, por ejemplo "AmazonLinuxEstudiante"

5. **Seleccionar la imagen de Amazon Linux**
   - En la sección "Imágenes de aplicaciones y SO (Amazon Machine Image)", busca y selecciona "Amazon Linux"
   - Recomendación: Elige "Amazon Linux 2023" para tener la versión más reciente

6. **Seleccionar el tipo de instancia**
   - Para prácticas educativas, el nivel gratuito "t2.micro" o "t3.micro" es suficiente
   - Este tipo de instancia incluye 1 CPU virtual y 1 GB de RAM

7. **Configurar el par de claves**
   - Crear un nuevo par de claves haciendo clic en "Crear nuevo par de claves"
   - Asigna un nombre al par de claves
   - Selecciona el formato: RSA y .pem (para macOS/Linux) o .ppk (para Windows con PuTTY)
   - Haz clic en "Crear par de claves" y guarda el archivo en un lugar seguro
   - **IMPORTANTE**: Este archivo es crucial para acceder a tu instancia y no podrás recuperarlo si lo pierdes

8. **Configurar la red**
   - En "Configuración de red", deja la opción "Crear grupo de seguridad"
   - Asegúrate de que esté marcado "Permitir tráfico SSH desde" y selecciona "Mi IP" o "Cualquier lugar" (menos seguro)
   - Para entornos educativos, puedes seleccionar "Cualquier lugar" para facilitar el acceso, pero en entornos de producción siempre limita el acceso

9. **Configurar almacenamiento**
   - En la sección "Configurar almacenamiento", el valor predeterminado de 8 GB es suficiente para prácticas
   - El tipo de volumen será "gp3" (SSD de propósito general)

10. **Revisar y lanzar**
    - Revisa toda la configuración
    - Haz clic en "Lanzar instancia"

11. **Esperar a que la instancia esté en ejecución**
    - Haz clic en "Ver todas las instancias" para monitorear el estado
    - Espera hasta que el "Estado de la instancia" cambie a "En ejecución" (toma aproximadamente 1-2 minutos)

12. **Obtener información de la instancia**
    - Una vez que la instancia esté en ejecución, selecciónala para ver sus detalles
    - Anota la "Dirección IPv4 pública" y el "Nombre DNS público" (los necesitarás para conectarte)

## Conexión a tu Instancia Amazon Linux

### Desde Windows

1. **Usando PuTTY**
   - Descarga e instala PuTTY desde [https://www.putty.org/](https://www.putty.org/)
   - Abre PuTTY
   - En el campo "Host Name", escribe: `ec2-user@tu-ip-publica` (reemplaza "tu-ip-publica" con la dirección IP de tu instancia)
   - En el panel izquierdo, navega a Connection > SSH > Auth > Credentials
   - En "Private key file for authentication", haz clic en "Browse" y selecciona tu archivo .ppk
   - Regresa a "Session", ingresa un nombre en "Saved Sessions" y haz clic en "Save"
   - Haz clic en "Open" para conectarte

2. **Usando Windows Subsystem for Linux (WSL) o PowerShell**
   - Abre WSL o PowerShell
   - Asegúrate de que tu archivo .pem tenga permisos adecuados:
     ```
     icacls tuarchivo.pem /inheritance:r
     icacls tuarchivo.pem /grant:r "$($env:USERNAME):(R)"
     ```
   - Conéctate usando SSH:
     ```
     ssh -i ruta/a/tu/archivo.pem ec2-user@tu-ip-publica
     ```

### Desde macOS o Linux

1. **Usando Terminal**
   - Abre Terminal
   - Cambia los permisos del archivo de clave:
     ```
     chmod 400 ruta/a/tu/archivo.pem
     ```
   - Conéctate usando SSH:
     ```
     ssh -i ruta/a/tu/archivo.pem ec2-user@tu-ip-publica
     ```

### Verificar la Conexión
Una vez conectado, verás un mensaje de bienvenida similar a este:

```
       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|
```

Ahora estás conectado a tu instancia Amazon Linux y puedes comenzar a trabajar con ella.

## Comandos Básicos de Linux

Linux es un sistema operativo basado en comandos de texto. Aquí te presentamos los comandos más importantes que necesitarás conocer:

### Navegación y Exploración

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `pwd` | **P**rint **W**orking **D**irectory - Muestra la ruta del directorio actual | `pwd` |
| `ls` | **L**i**s**t - Lista archivos y directorios | `ls` |
| `ls -l` | Lista con formato detallado (permisos, tamaño, fecha) | `ls -l` |
| `ls -a` | Lista todos los archivos (incluyendo ocultos) | `ls -a` |
| `ls -la` | Combina -l y -a | `ls -la` |
| `cd` | **C**hange **D**irectory - Cambia de directorio | `cd /ruta/al/directorio` |
| `cd ..` | Sube un nivel en la jerarquía de directorios | `cd ..` |
| `cd ~` | Va al directorio home del usuario | `cd ~` |
| `cd /` | Va al directorio raíz | `cd /` |
| `clear` | Limpia la pantalla de la terminal | `clear` |

### Manejo de Archivos y Directorios

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `mkdir` | **M**a**k**e **Dir**ectory - Crea un directorio | `mkdir nuevo_directorio` |
| `rmdir` | **R**e**m**ove **Dir**ectory - Elimina un directorio vacío | `rmdir directorio_vacio` |
| `touch` | Crea un archivo vacío o actualiza la fecha de uno existente | `touch archivo.txt` |
| `cp` | **C**o**p**y - Copia archivos o directorios | `cp origen.txt destino.txt` |
| `cp -r` | Copia recursivamente (directorios y su contenido) | `cp -r dir1 dir2` |
| `mv` | **M**o**v**e - Mueve o renombra archivos o directorios | `mv viejo.txt nuevo.txt` |
| `rm` | **R**e**m**ove - Elimina archivos | `rm archivo.txt` |
| `rm -r` | Elimina directorios y su contenido recursivamente | `rm -r directorio` |
| `rm -f` | Fuerza la eliminación sin confirmación | `rm -f archivo.txt` |
| `cat` | Con**cat**enate - Muestra el contenido de un archivo | `cat archivo.txt` |
| `less` | Visualiza archivos con desplazamiento | `less archivo_largo.txt` |
| `head` | Muestra las primeras líneas de un archivo | `head -n 10 archivo.txt` |
| `tail` | Muestra las últimas líneas de un archivo | `tail -n 10 archivo.txt` |
| `nano` | Editor de texto simple | `nano archivo.txt` |
| `vi` o `vim` | Editor de texto avanzado | `vi archivo.txt` |

### Información del Sistema

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `uname -a` | Muestra información del sistema | `uname -a` |
| `whoami` | Muestra el nombre del usuario actual | `whoami` |
| `df -h` | Muestra el espacio en disco en formato legible | `df -h` |
| `free -h` | Muestra la memoria libre y usada | `free -h` |
| `top` | Muestra los procesos en ejecución | `top` |
| `ps aux` | Lista todos los procesos | `ps aux` |
| `history` | Muestra el historial de comandos | `history` |

### Redes

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `ping` | Comprueba la conectividad con un host | `ping google.com` |
| `ifconfig` o `ip addr` | Muestra la configuración de red | `ifconfig` |
| `netstat -tuln` | Muestra las conexiones de red | `netstat -tuln` |
| `ssh` | Se conecta a un servidor remoto | `ssh usuario@servidor` |
| `scp` | Copia archivos entre hosts | `scp archivo.txt usuario@servidor:/ruta` |

### Gestión de Paquetes en Amazon Linux

Amazon Linux 2 usa `yum` como gestor de paquetes, mientras que Amazon Linux 2023 utiliza `dnf`:

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `sudo yum update` | Actualiza todos los paquetes | `sudo yum update` |
| `sudo yum install` | Instala un paquete | `sudo yum install nginx` |
| `sudo yum remove` | Elimina un paquete | `sudo yum remove nginx` |
| `sudo yum search` | Busca paquetes | `sudo yum search python` |
| `sudo dnf update` | Actualiza todos los paquetes (AL2023) | `sudo dnf update` |
| `sudo dnf install` | Instala un paquete (AL2023) | `sudo dnf install nginx` |

### Comandos para Redirección y Tuberías

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `>` | Redirige la salida a un archivo (sobrescribe) | `ls > lista.txt` |
| `>>` | Redirige la salida a un archivo (añade) | `echo "texto" >> archivo.txt` |
| `<` | Redirige la entrada desde un archivo | `comando < archivo.txt` |
| `\|` | Tubería: pasa la salida de un comando como entrada a otro | `ls -l \| grep ".txt"` |
| `grep` | Busca patrones en archivos o salidas | `grep "palabra" archivo.txt` |

## Gestión de Usuarios

Linux es un sistema multi-usuario. En Amazon Linux, el usuario por defecto es `ec2-user`. Sin embargo, a menudo necesitarás crear usuarios adicionales, especialmente en un entorno educativo o de producción.

### Comandos Principales para Gestión de Usuarios

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `sudo useradd` | Crea un nuevo usuario | `sudo useradd estudiante` |
| `sudo passwd` | Establece/cambia la contraseña de un usuario | `sudo passwd estudiante` |
| `sudo userdel` | Elimina un usuario | `sudo userdel estudiante` |
| `sudo userdel -r` | Elimina un usuario y su directorio home | `sudo userdel -r estudiante` |
| `sudo usermod` | Modifica un usuario | `sudo usermod -aG grupo usuario` |
| `id` | Muestra los IDs de usuario y grupo | `id estudiante` |
| `who` | Muestra quién está conectado | `who` |
| `su` | Cambia a otro usuario | `su estudiante` |
| `sudo` | Ejecuta un comando como superusuario | `sudo comando` |

### Ejemplo Práctico: Crear un Usuario para Estudiante

```bash
# Crear nuevo usuario
sudo useradd -m -s /bin/bash estudiante

# Establecer contraseña
sudo passwd estudiante

# Añadir al grupo sudo para darle privilegios de administrador (opcional)
sudo usermod -aG wheel estudiante
```

#### Explicación:
- `-m`: Crea el directorio home para el usuario
- `-s /bin/bash`: Establece bash como shell por defecto
- `wheel`: En Amazon Linux, el grupo `wheel` tiene privilegios sudo

### Archivos Importantes para la Gestión de Usuarios

| Archivo | Descripción |
|---------|-------------|
| `/etc/passwd` | Contiene información básica de los usuarios |
| `/etc/shadow` | Contiene las contraseñas cifradas |
| `/etc/group` | Contiene información de los grupos |
| `/etc/sudoers` | Configura los privilegios de sudo |

### Ver Información de Usuario

```bash
# Ver todos los usuarios
cat /etc/passwd

# Ver a qué grupos pertenece un usuario
groups estudiante

# Ver información detallada de un usuario
id estudiante
```

## Directorios y Archivos

La estructura de directorios en Linux sigue un estándar específico. En Amazon Linux, como en la mayoría de distribuciones, se sigue el estándar Filesystem Hierarchy Standard (FHS).

### Estructura de Directorios Principal

| Directorio | Descripción |
|------------|-------------|
| `/` | Directorio raíz - Todo el sistema de archivos comienza aquí |
| `/bin` | Comandos binarios esenciales para todos los usuarios |
| `/boot` | Archivos para el arranque del sistema (kernel, initrd) |
| `/dev` | Archivos de dispositivos |
| `/etc` | Archivos de configuración del sistema |
| `/home` | Directorios home de los usuarios |
| `/lib` | Bibliotecas compartidas esenciales |
| `/media` | Punto de montaje para medios removibles |
| `/mnt` | Punto de montaje temporal |
| `/opt` | Software opcional adicional |
| `/proc` | Sistema de archivos virtual para información del proceso |
| `/root` | Directorio home del usuario root |
| `/run` | Datos de tiempo de ejecución |
| `/sbin` | Binarios del sistema para el administrador |
| `/srv` | Datos para servicios proporcionados por el sistema |
| `/sys` | Sistema de archivos virtual para información del kernel |
| `/tmp` | Archivos temporales |
| `/usr` | Programas y datos de usuario |
| `/var` | Datos variables (logs, bases de datos, sitios web) |

### Operaciones con Directorios

#### Crear Directorios

```bash
# Crear un directorio
mkdir mi_directorio

# Crear directorios anidados
mkdir -p ruta/a/mi/nuevo/directorio
```

Explicación:
- `-p`: Crea los directorios padre si no existen

#### Eliminar Directorios

```bash
# Eliminar un directorio vacío
rmdir directorio_vacio

# Eliminar un directorio y su contenido
rm -r mi_directorio

# Eliminar forzadamente (¡cuidado!)
rm -rf mi_directorio
```

### Operaciones con Archivos

#### Crear y Editar Archivos

```bash
# Crear un archivo vacío
touch archivo.txt

# Crear un archivo con contenido
echo "Hola Mundo" > archivo.txt

# Añadir contenido a un archivo existente
echo "Línea adicional" >> archivo.txt

# Editar un archivo con nano (editor amigable para principiantes)
nano archivo.txt

# Editar un archivo con vi (editor avanzado)
vi archivo.txt
```

#### Comandos Básicos de Nano

Una vez dentro del editor nano:
- `Ctrl + O`: Guardar el archivo
- `Ctrl + X`: Salir
- `Ctrl + K`: Cortar la línea actual
- `Ctrl + U`: Pegar texto cortado
- `Ctrl + W`: Buscar en el archivo
- `Ctrl + G`: Mostrar ayuda

#### Comandos Básicos de Vi/Vim

Vi tiene dos modos principales:
1. **Modo Comando**: El modo por defecto, para navegar y ejecutar comandos
2. **Modo Inserción**: Para editar y añadir texto

Comandos importantes:
- `i`: Entrar en modo inserción
- `Esc`: Volver al modo comando
- `:w`: Guardar
- `:q`: Salir
- `:wq`: Guardar y salir
- `:q!`: Salir sin guardar cambios
- `/texto`: Buscar "texto"
- `dd`: Eliminar la línea actual
- `yy`: Copiar la línea actual
- `p`: Pegar

#### Ver Contenido de Archivos

```bash
# Ver todo el contenido
cat archivo.txt

# Ver con paginación
less archivo.txt

# Ver las primeras 10 líneas
head -n 10 archivo.txt

# Ver las últimas 10 líneas
tail -n 10 archivo.txt

# Monitorear un archivo (útil para logs)
tail -f /var/log/syslog
```

## Permisos en Linux

El sistema de permisos en Linux es fundamental para la seguridad. Cada archivo y directorio tiene permisos que controlan quién puede leer, escribir o ejecutar.

### Estructura de Permisos

Los permisos se representan de dos formas:
1. **Simbólica**: `rwxrwxrwx`
2. **Numérica**: `777`

La representación simbólica se divide en tres grupos:
- El primero para el propietario (u)
- El segundo para el grupo (g)
- El tercero para otros usuarios (o)

Cada grupo tiene tres bits:
- `r` (4): Permiso de lectura
- `w` (2): Permiso de escritura
- `x` (1): Permiso de ejecución

### Ver Permisos

```bash
ls -l archivo.txt
```

Ejemplo de salida:
```
-rw-r--r-- 1 ec2-user ec2-user 24 May 10 10:30 archivo.txt
```

Explicación:
- `-rw-r--r--`: Los permisos (el primer - indica que es un archivo, d sería un directorio)
- `1`: Número de enlaces duros
- `ec2-user`: Propietario
- `ec2-user`: Grupo
- `24`: Tamaño en bytes
- `May 10 10:30`: Fecha y hora de última modificación
- `archivo.txt`: Nombre del archivo

Desglose de permisos `-rw-r--r--`:
- `-`: Tipo de archivo (archivo regular)
- `rw-`: Permisos del propietario (lectura y escritura)
- `r--`: Permisos del grupo (solo lectura)
- `r--`: Permisos para otros (solo lectura)

### Cambiar Permisos

#### Usando Modo Simbólico

```bash
# Dar permiso de ejecución al propietario
chmod u+x archivo.sh

# Quitar permiso de escritura al grupo
chmod g-w archivo.txt

# Dar todos los permisos al propietario, lectura y ejecución al grupo, nada a otros
chmod u=rwx,g=rx,o= archivo.sh
```

#### Usando Modo Numérico

```bash
# Equivalente a rwxr-xr-- (propietario: todo, grupo: lectura y ejecución, otros: solo lectura)
chmod 754 archivo.sh

# Equivalente a rwxrwxrwx (todos los permisos para todos - ¡cuidado!)
chmod 777 archivo.sh

# Equivalente a rw-r--r-- (típico para archivos de datos)
chmod 644 archivo.txt
```

### Permisos Comunes

| Permiso Numérico | Simbólico | Descripción | Uso Típico |
|------------------|-----------|-------------|------------|
| 644 | rw-r--r-- | Propietario puede leer/escribir, los demás solo leer | Archivos de datos |
| 755 | rwxr-xr-x | Propietario todo, los demás leer/ejecutar | Scripts, programas |
| 600 | rw------- | Solo el propietario puede leer/escribir | Archivos privados |
| 700 | rwx------ | Solo el propietario tiene todos los permisos | Directorios privados |
| 777 | rwxrwxrwx | Todos tienen todos los permisos | Uso temporal o compartido |

### Cambiar Propietario y Grupo

```bash
# Cambiar el propietario
sudo chown usuario archivo.txt

# Cambiar el grupo
sudo chgrp grupo archivo.txt

# Cambiar ambos
sudo chown usuario:grupo archivo.txt

# Cambiar recursivamente (para directorios)
sudo chown -R usuario:grupo directorio/
```

### Permisos Especiales

| Permiso | Simbólico | Numérico | Descripción |
|---------|-----------|----------|-------------|
| SUID | s en lugar de x para usuario | 4000 | Ejecuta con privilegios del propietario |
| SGID | s en lugar de x para grupo | 2000 | Ejecuta con privilegios del grupo |
| Sticky Bit | t en el bit de otros | 1000 | Solo el propietario puede eliminar/renombrar |

Ejemplo:
```bash
# Establecer SUID
chmod u+s archivo

# Establecer SGID
chmod g+s directorio

# Establecer Sticky Bit (común en /tmp)
chmod +t directorio
```

## Volúmenes en AWS

En AWS, los volúmenes son dispositivos de almacenamiento que puedes adjuntar a tus instancias EC2. Amazon Elastic Block Store (EBS) es el servicio que proporciona estos volúmenes.

### Tipos de Volúmenes EBS

| Tipo | Descripción | Uso Recomendado |
|------|-------------|-----------------|
| gp3, gp2 | SSD de Propósito General | Carga de trabajo equilibrada, sistemas operativos |
| io2, io1 | SSD con IOPS Aprovisionadas | Bases de datos, aplicaciones de alta I/O |
| st1 | HDD Optimizado para Throughput | Big data, data warehouses |
| sc1 | HDD Frío | Almacenamiento de acceso infrecuente |
| standard | HDD Magnético (anterior) | Cargas de trabajo de menor costo y acceso infrecuente |

### Gestión de Volúmenes desde la Consola AWS

1. **Crear un volumen EBS**:
   - Navega a EC2 > Volúmenes > Crear volumen
   - Selecciona tipo, tamaño y zona de disponibilidad (debe ser la misma que tu instancia)
   - Haz clic en "Crear volumen"

2. **Adjuntar un Volumen a una Instancia**:
   - Selecciona el volumen > Acciones > Adjuntar volumen
   - Selecciona la instancia
   - Especifica el nombre del dispositivo (ej. /dev/sdf)
   - Haz clic en "Adjuntar"

3. **Preparar el Volumen para su Uso**:
   Después de adjuntar, conéctate a tu instancia y:
   
   a. **Ver los volúmenes disponibles**:
   ```bash
   lsblk
   ```
   
   b. **Formatear el volumen** (solo la primera vez):
   ```bash
   sudo mkfs -t xfs /dev/nvme1n1  # Ajusta el nombre del dispositivo según lsblk
   ```
   
   c. **Crear un punto de montaje**:
   ```bash
   sudo mkdir /datos
   ```
   
   d. **Montar el volumen**:
   ```bash
   sudo mount /dev/nvme1n1 /datos
   ```
   
   e. **Configurar montaje automático en el inicio**:
   ```bash
   # Obtener el UUID del volumen
   sudo blkid
   
   # Editar fstab
   sudo nano /etc/fstab
   
   # Añadir línea como:
   # UUID=tu-uuid-aquí  /datos  xfs  defaults,nofail  0  2
   ```

### Comandos para Gestionar Volúmenes en Linux

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `lsblk` | Lista bloques de almacenamiento | `lsblk` |
| `df -h` | Muestra espacio usado en sistemas de archivos | `df -h` |
| `sudo fdisk -l` | Lista particiones | `sudo fdisk -l` |
| `sudo mkfs` | Formatea un sistema de archivos | `sudo mkfs -t xfs /dev/nvme1n1` |
| `sudo mount` | Monta un sistema de archivos | `sudo mount /dev/nvme1n1 /datos` |
| `sudo umount` | Desmonta un sistema de archivos | `sudo umount /datos` |

### Ampliación de Volúmenes EBS

Si necesitas más espacio, puedes ampliar un volumen EBS:

1. **Desde la consola AWS**:
   - Selecciona el volumen > Acciones > Modificar volumen
   - Aumenta el tamaño
   - Haz clic en "Modificar"

2. **En la instancia**:
   - Para sistemas de archivos XFS:
   ```bash
   sudo xfs_growfs /punto/de/montaje
   ```
   
   - Para sistemas de archivos ext4:
   ```bash
   sudo resize2fs /dev/dispositivo
   ```

## Entorno de Aprendizaje de Amazon

Amazon ofrece varios recursos educativos para aprender sobre AWS y Amazon Linux:

### AWS Academy

AWS Academy proporciona a instituciones educativas un plan de estudios sobre la nube:
- Materiales de curso completos
- Laboratorios prácticos
- Preparación para certificaciones
- Acceso a créditos AWS para estudiantes

### AWS Educate

Programa gratuito para estudiantes y educadores:
- Cursos autoguiados
- Laboratorios prácticos
- Caminos de formación por roles
- Insignias digitales y credenciales

### Laboratorios Prácticos de AWS

1. **AWS Free Tier**:
   - Acceso gratuito a muchos servicios de AWS durante 12 meses
   - Algunos servicios son siempre gratuitos
   - Perfecto para aprender sin costos iniciales

2. **AWS Skill Builder**:
   - Plataforma de aprendizaje digital
   - Cursos gratuitos y de pago
   - Incluye laboratorios prácticos

3. **Qwiklabs**:
   - Entornos de laboratorio temporales
   - Instrucciones paso a paso
   - Evaluación automática

### Recursos de Aprendizaje para Amazon Linux

1. **Documentación Oficial**:
   - [Guía del Usuario de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)
   - [Documentación de Amazon Linux](https://docs.aws.amazon.com/linux/)

2. **AWS Workshops**:
   - Talleres guiados con instrucciones detalladas
   - [https://workshops.aws/](https://workshops.aws/)

3. **AWS Samples en GitHub**:
   - Ejemplos de código y configuraciones
   - [https://github.com/aws-samples](https://github.com/aws-samples)

4. **AWS Training and Certification**:
   - Cursos oficiales de AWS
   - Algunos son gratuitos, otros de pago
   - [https://aws.amazon.com/training/](https://aws.amazon.com/training/)

## Consejos y Mejores Prácticas

### Seguridad

1. **Actualiza regularmente**:
   ```bash
   sudo yum update -y
   ```

2. **Usa grupos de seguridad restrictivos**:
   - Limita el acceso SSH solo a tu IP
   - Abre solo los puertos necesarios

3. **Usa IAM con principio de privilegio mínimo**:
   - Crea usuarios IAM en lugar de usar root
   - Asigna solo los permisos necesarios

4. **Habilita la autenticación de dos factores**:
   - Para tu cuenta de AWS
   - Para usuarios IAM importantes

5. **Monitorea los logs**:
   - Revisa `/var/log/secure` para intentos de acceso
   - Considera usar CloudWatch Logs

### Rendimiento

1. **Elige el tipo de instancia adecuado**:
   - t3.micro para aprendizaje
   - Tipos especializados para cargas específicas

2. **Usa volúmenes EBS apropiados**:
   - gp3 para uso general
   - io2 para aplicaciones que requieren alta I/O

3. **Monitorea el rendimiento**:
   ```bash
   top
   vmstat
   iostat
   ```

4. **Usa CloudWatch para alertas**:
   - Configura alarmas para alta utilización de CPU
   - Monitorea el uso de memoria y disco

### Costo

1. **Detén instancias cuando no las uses**:
   - Especialmente para entornos de prueba
   - Usa programación para iniciar/detener automáticamente

2. **Usa el nivel gratuito de AWS**:
   - t2.micro/t3.micro están en el nivel gratuito
   - 750 horas por mes durante 12 meses

3. **Configura presupuestos y alertas**:
   - Usa AWS Budgets para establecer límites
   - Configura alertas por correo electrónico

4. **Elimina recursos no utilizados**:
   - Volúmenes EBS sin adjuntar
   - Direcciones IP elásticas sin usar

### Backup y Recuperación

1. **Crea snapshots regulares**:
   - De tus volúmenes EBS
   - Antes de cambios importantes

2. **Automatiza backups**:
   - Usa AWS Backup
   - O crea scripts personalizados con cron

3. **Prueba la recuperación**:
   - Crea una nueva instancia desde un snapshot
   - Verifica que todo funcione correctamente

4. **Documenta procedimientos**:
   - Escribe guías paso a paso para recuperación
   - Incluye comandos específicos

## Conclusión

Esta guía ha cubierto los aspectos fundamentales de Amazon Linux para estudiantes, desde la creación de una máquina virtual hasta la gestión de usuarios, directorios, archivos, permisos y volúmenes. Además, hemos explorado los recursos educativos que Amazon ofrece.

A medida que continúes tu aprendizaje, recuerda que la práctica es esencial. Experimenta con diferentes comandos y configuraciones en un entorno controlado antes de implementarlos en entornos de producción.

Para mantenerte actualizado:
- Sigue el [Blog de AWS](https://aws.amazon.com/blogs/)
- Únete a la [Comunidad de AWS](https://aws.amazon.com/developer/community/)
- Participa en eventos de [AWS Events](https://aws.amazon.com/events/)

¡Buena suerte en tu viaje de aprendizaje con Amazon Linux y AWS!
