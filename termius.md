# Guía Completa de Termius en Español

## Índice
1. [Introducción a Termius](#introducción-a-termius)
2. [Instalación](#instalación)
3. [Configuración inicial](#configuración-inicial)
4. [Administración de hosts](#administración-de-hosts)
5. [Conexión SSH](#conexión-ssh)
6. [Administración de claves SSH](#administración-de-claves-ssh)
7. [Organización con grupos y etiquetas](#organización-con-grupos-y-etiquetas)
8. [Transferencia de archivos (SFTP)](#transferencia-de-archivos-sftp)
9. [Snippets y comandos](#snippets-y-comandos)
10. [Funciones avanzadas](#funciones-avanzadas)
11. [Solución de problemas comunes](#solución-de-problemas-comunes)

## Introducción a Termius

Termius es un cliente SSH multiplataforma moderno que permite conectarse a servidores remotos de manera segura. Disponible para Windows, macOS, Linux, iOS y Android, ofrece una experiencia unificada en todos los dispositivos con sincronización en la nube (en la versión de pago).

### Versiones disponibles
- **Termius Free**: Versión gratuita con funciones básicas
- **Termius Premium**: Versión de pago con todas las funcionalidades

## Instalación

### Windows
1. Visita la página oficial de Termius (https://termius.com)
2. Haz clic en "Download" y selecciona la versión para Windows
3. Ejecuta el archivo descargado y sigue el asistente de instalación
4. Al finalizar, abre Termius desde el menú de inicio

### macOS
1. Visita la página oficial de Termius
2. Descarga la versión para macOS
3. Abre el archivo .dmg descargado
4. Arrastra el ícono de Termius a la carpeta de Aplicaciones
5. Abre Termius desde el Launchpad o la carpeta de Aplicaciones

### Linux
```bash
# Ubuntu/Debian
sudo snap install termius-app

# O descarga el archivo .deb o .rpm desde la página oficial
```

### iOS/Android
1. Abre la App Store (iOS) o Google Play Store (Android)
2. Busca "Termius"
3. Instala la aplicación

## Configuración inicial

### Crear una cuenta (opcional, pero recomendado para sincronización)
1. Abre Termius
2. Haz clic en "Crear cuenta" o "Iniciar sesión"
3. Completa el formulario con tu correo y contraseña
4. Verifica tu correo electrónico

### Configuración de preferencias
1. Abre Termius
2. Ve a "Preferencias" o "Configuración" (puede variar según plataforma)
3. Configura:
   - Tema (claro/oscuro)
   - Tamaño de fuente
   - Familia de fuente
   - Esquema de colores del terminal

## Administración de hosts

### Agregar un nuevo host
1. Haz clic en el botón "+" o "Nuevo"
2. Selecciona "Nuevo host"
3. Completa la información:
   - Alias: Un nombre descriptivo (p. ej., "Servidor Web")
   - Dirección: La dirección IP o nombre de dominio (p. ej., "192.168.1.100" o "miservidor.com")
   - Puerto: Por defecto es 22 para SSH
   - Usuario: Tu nombre de usuario en el servidor
   - Contraseña: Tu contraseña (o puedes usar claves SSH)
4. Haz clic en "Guardar"

### Editar un host existente
1. Selecciona el host de la lista
2. Haz clic en el ícono de edición (lápiz) o haz clic derecho y selecciona "Editar"
3. Modifica los campos necesarios
4. Guarda los cambios

### Eliminar un host
1. Selecciona el host
2. Haz clic derecho y selecciona "Eliminar" o usa el botón correspondiente
3. Confirma la eliminación

## Conexión SSH

### Conectarse a un servidor
1. En la lista de hosts, haz doble clic en el servidor al que deseas conectarte
2. O selecciona el servidor y haz clic en "Conectar"
3. Si es la primera vez que te conectas, aparecerá una advertencia de clave desconocida. Verifica la huella digital y acepta
4. Se abrirá una nueva pestaña con tu sesión SSH

### Comandos básicos en la terminal
```bash
# Ver contenido del directorio
ls -la

# Cambiar de directorio
cd /ruta/del/directorio

# Editar un archivo con nano
nano archivo.txt

# Ver contenido de un archivo
cat archivo.txt

# Ver espacio en disco
df -h
```

### Cerrar una conexión
1. Escribe `exit` en la terminal
2. O cierra la pestaña de la sesión

## Administración de claves SSH

### Crear un par de claves SSH
1. Ve a la sección "Claves" o "SSH Keys"
2. Haz clic en "+" o "Nueva clave"
3. Selecciona:
   - Tipo de clave (RSA, ED25519, etc.)
   - Longitud de bits (mínimo 2048, recomendado 4096 para RSA)
   - Frase de contraseña (opcional, pero recomendada)
4. Haz clic en "Generar"
5. Guarda la clave con un nombre descriptivo

### Importar claves existentes
1. Ve a la sección "Claves"
2. Haz clic en "Importar"
3. Selecciona el archivo de clave privada
4. Ingresa la frase de contraseña si está protegida
5. Guarda con un nombre descriptivo

### Asignar claves a hosts
1. Edita el host deseado
2. En la sección de autenticación, selecciona "Clave SSH"
3. Elige la clave que deseas usar
4. Guarda los cambios

## Organización con grupos y etiquetas

### Crear grupos
1. Haz clic en el botón "+" o "Nuevo"
2. Selecciona "Nuevo grupo"
3. Asigna un nombre descriptivo
4. Guarda el grupo

### Mover hosts a grupos
1. Arrastra y suelta el host en el grupo deseado
2. O edita el host y selecciona el grupo en la configuración

### Usar etiquetas (tags)
1. Edita el host
2. En la sección de etiquetas, añade las etiquetas deseadas (p. ej., "producción", "desarrollo", "base de datos")
3. Guarda los cambios
4. Usa la búsqueda de etiquetas para filtrar hosts

## Transferencia de archivos (SFTP)

### Abrir el navegador SFTP
1. Conéctate a un servidor
2. Haz clic en el ícono de SFTP o selecciona la opción "SFTP" desde el menú
3. Se abrirá el navegador de archivos

### Subir archivos
1. En el navegador SFTP, navega hasta la carpeta de destino
2. Haz clic en "Subir" o el ícono correspondiente
3. Selecciona el archivo en tu sistema local
4. Espera a que se complete la transferencia

### Descargar archivos
1. En el navegador SFTP, navega y selecciona el archivo que deseas descargar
2. Haz clic en "Descargar" o el ícono correspondiente
3. Selecciona la ubicación en tu sistema local
4. Espera a que se complete la transferencia

### Administrar permisos
1. Haz clic derecho en un archivo o carpeta
2. Selecciona "Permisos" o "Propiedades"
3. Modifica los permisos (lectura, escritura, ejecución)
4. Guarda los cambios

## Snippets y comandos

### Crear snippets (fragmentos de código)
1. Ve a la sección "Snippets"
2. Haz clic en "+" o "Nuevo snippet"
3. Ingresa:
   - Nombre: Un título descriptivo
   - Comando: El texto o comando que deseas guardar
4. Guarda el snippet

### Usar snippets durante una sesión
1. Durante una sesión SSH activa
2. Haz clic en el botón de snippets (generalmente en la barra lateral o superior)
3. Selecciona el snippet que deseas usar
4. El comando se insertará automáticamente en la terminal

## Funciones avanzadas

### Port forwarding (reenvío de puertos)
1. Edita un host
2. Ve a la sección "Port Forwarding"
3. Haz clic en "+" o "Añadir"
4. Configura:
   - Tipo: Local, remoto o dinámico
   - Puerto local
   - Puerto remoto
   - Host remoto (si es necesario)
5. Guarda la configuración

### Múltiples pestañas y terminales divididas
1. Abre varias conexiones en diferentes pestañas
2. Usa el botón de división (split) para dividir la terminal horizontal o verticalmente
3. Gestiona múltiples sesiones simultáneamente

### Variables de entorno
1. Edita un host
2. Ve a la sección "Environment"
3. Añade variables de entorno personalizadas
4. Estas variables estarán disponibles en tu sesión SSH

## Solución de problemas comunes

### No puedo conectarme a un servidor
- Verifica la dirección IP o nombre de dominio
- Confirma que el puerto SSH está abierto (generalmente el 22)
- Asegúrate de que tus credenciales son correctas
- Verifica que el servidor está en línea y accesible

### Problemas con la autenticación por clave
- Asegúrate de que la clave pública está añadida al archivo `~/.ssh/authorized_keys` del servidor
- Verifica los permisos de los archivos SSH en el servidor:
  ```bash
  chmod 700 ~/.ssh
  chmod 600 ~/.ssh/authorized_keys
  ```
- Confirma que estás usando la clave privada correcta

### La conexión se cierra inesperadamente
- Configura un keepalive en las preferencias de Termius
- Verifica la configuración del servidor SSH para aumentar el tiempo de inactividad

### No puedo transferir archivos
- Verifica que tienes permisos de escritura en la carpeta de destino
- Asegúrate de que hay suficiente espacio en disco
- Comprueba que el usuario tiene acceso SFTP habilitado

---

Con esta guía deberías poder utilizar Termius de manera efectiva para gestionar tus conexiones SSH. Si tienes dudas específicas o problemas no cubiertos aquí, consulta la documentación oficial o los foros de soporte de Termius.
