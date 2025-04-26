# Guía Completa de GitHub

## Índice
1. [Introducción a GitHub](#introducción-a-github)
2. [Instalación y Configuración](#instalación-y-configuración)
3. [Conceptos Fundamentales](#conceptos-fundamentales)
4. [Crear un Repositorio](#crear-un-repositorio)
5. [Clonar un Repositorio](#clonar-un-repositorio)
6. [Flujo de Trabajo Básico](#flujo-de-trabajo-básico)
7. [Gestión de Commits](#gestión-de-commits)
8. [Ramas (Branches)](#ramas-branches)
9. [Fusiones (Merges)](#fusiones-merges)
10. [Resolución de Conflictos](#resolución-de-conflictos)
11. [Trabajo Remoto (Pull/Push)](#trabajo-remoto-pullpush)
12. [Pull Requests](#pull-requests)
13. [Issues y Proyectos](#issues-y-proyectos)
14. [GitHub Pages](#github-pages)
15. [Acciones de GitHub (GitHub Actions)](#acciones-de-github-github-actions)
16. [GitHub para Equipos](#github-para-equipos)
17. [Mejores Prácticas](#mejores-prácticas)
18. [Recursos Adicionales](#recursos-adicionales)

## Introducción a GitHub

### ¿Qué es GitHub?

GitHub es una plataforma basada en la nube que aloja repositorios de Git y añade funcionalidades colaborativas adicionales. Mientras que Git es un sistema de control de versiones distribuido que permite realizar un seguimiento de los cambios en el código fuente durante el desarrollo de software, GitHub proporciona una interfaz web para Git, además de herramientas de gestión de proyectos, control de acceso y colaboración.

### ¿Por qué usar GitHub?

- **Control de versiones**: Seguimiento detallado de los cambios en el código
- **Colaboración**: Facilita el trabajo en equipo en proyectos de desarrollo
- **Open Source**: Centro para proyectos de código abierto
- **Portfolio**: Muestra tu trabajo a potenciales empleadores
- **Comunidad**: Acceso a millones de proyectos y desarrolladores
- **Integración**: Se integra con muchas herramientas de desarrollo

## Instalación y Configuración

### Instalación de Git

Antes de comenzar con GitHub, necesitas instalar Git en tu sistema:

**Windows**:
1. Descarga el instalador desde [git-scm.com](https://git-scm.com/)
2. Ejecuta el instalador y sigue las instrucciones
3. Verifica la instalación abriendo Git Bash y escribiendo `git --version`

**macOS**:
1. Instala Homebrew si no lo tienes: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Instala Git con Homebrew: `brew install git`
3. Verifica la instalación: `git --version`

**Linux (Ubuntu/Debian)**:
1. Abre la terminal
2. Actualiza los paquetes: `sudo apt update`
3. Instala Git: `sudo apt install git`
4. Verifica la instalación: `git --version`

### Configuración Inicial de Git

Una vez instalado Git, configura tu identidad:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

Esta información se utilizará en cada commit que hagas.

### Crear una Cuenta en GitHub

1. Visita [github.com](https://github.com/)
2. Haz clic en "Sign up" (Registrarse)
3. Sigue el proceso de registro proporcionando un nombre de usuario, correo electrónico y contraseña
4. Verifica tu correo electrónico

### Configurar SSH para GitHub (Recomendado)

La autenticación SSH te permite conectarte a GitHub sin introducir tu nombre de usuario/contraseña cada vez.

**Generar una clave SSH**:
1. Abre la terminal o Git Bash
2. Ejecuta: `ssh-keygen -t ed25519 -C "tu.email@ejemplo.com"`
3. Presiona Enter para aceptar la ubicación predeterminada del archivo
4. Introduce una contraseña (opcional pero recomendado)

**Añadir la clave SSH a GitHub**:
1. Copia tu clave pública: `cat ~/.ssh/id_ed25519.pub` (o usa `clip < ~/.ssh/id_ed25519.pub` en Windows)
2. Accede a GitHub y ve a Settings > SSH and GPG keys
3. Haz clic en "New SSH key"
4. Añade un título descriptivo y pega tu clave pública
5. Haz clic en "Add SSH key"

**Verificar la conexión**:
```bash
ssh -T git@github.com
```

Si todo está configurado correctamente, verás un mensaje de autenticación exitosa.

## Conceptos Fundamentales

### ¿Qué es Git?

Git es un sistema de control de versiones distribuido que registra los cambios en archivos a lo largo del tiempo. Permite revertir archivos a estados anteriores, comparar cambios, ver quién modificó algo y más.

### Terminología Clave

- **Repositorio**: Espacio donde se almacena el proyecto y su historial
- **Commit**: Captura del estado actual de los archivos
- **Rama (Branch)**: Línea independiente de desarrollo
- **Fusión (Merge)**: Combinar cambios de diferentes ramas
- **Remoto (Remote)**: Versión del repositorio alojada en un servidor (como GitHub)
- **Fork**: Copia personal de un repositorio de otro usuario
- **Clone**: Copia local de un repositorio remoto
- **Pull**: Obtener cambios del repositorio remoto
- **Push**: Enviar cambios al repositorio remoto
- **Pull Request**: Solicitud para fusionar cambios entre ramas o repositorios

## Crear un Repositorio

### Desde GitHub (Nuevo Repositorio)

1. Inicia sesión en GitHub
2. Haz clic en "+" en la esquina superior derecha y selecciona "New repository"
3. Introduce un nombre para tu repositorio
4. (Opcional) Añade una descripción
5. Elige si el repositorio será público o privado
6. (Opcional) Selecciona "Initialize this repository with a README"
7. (Opcional) Añade un archivo .gitignore y elige una licencia
8. Haz clic en "Create repository"

### Desde un Proyecto Existente (Local)

Si ya tienes un proyecto local que quieres subir a GitHub:

```bash
# Navega hasta la carpeta de tu proyecto
cd ruta/a/tu/proyecto

# Inicializa un repositorio Git
git init

# Añade todos los archivos al stage
git add .

# Realiza el primer commit
git commit -m "Commit inicial"

# Conecta con el repositorio remoto en GitHub (reemplaza con tu URL)
git remote add origin https://github.com/tu-usuario/tu-repo.git

# Sube los cambios a GitHub
git push -u origin main
```

## Clonar un Repositorio

Clonar significa crear una copia local de un repositorio remoto.

```bash
# Sintaxis básica
git clone url-del-repositorio

# Ejemplo con HTTPS
git clone https://github.com/usuario/repositorio.git

# Ejemplo con SSH
git clone git@github.com:usuario/repositorio.git

# Clonar a una carpeta específica
git clone url-del-repositorio nombre-carpeta
```

## Flujo de Trabajo Básico

El flujo de trabajo típico en Git sigue estos pasos:

1. **Obtener cambios recientes** (si trabajas en equipo)
   ```bash
   git pull origin main
   ```

2. **Crear/editar archivos** en tu proyecto

3. **Ver estado** de los archivos modificados
   ```bash
   git status
   ```

4. **Añadir cambios** al área de preparación
   ```bash
   # Añadir un archivo específico
   git add nombre-archivo

   # Añadir todos los archivos modificados
   git add .
   ```

5. **Confirmar cambios** con un commit
   ```bash
   git commit -m "Descripción de los cambios realizados"
   ```

6. **Enviar cambios** al repositorio remoto
   ```bash
   git push origin main
   ```

## Gestión de Commits

### Anatomía de un Buen Commit

Un buen commit debe:
- Ser autocontenido (representar un cambio lógico único)
- Tener un mensaje descriptivo
- Ser pequeño y enfocado

### Estructura del Mensaje de Commit

Una convención popular es:

```
<tipo>: <descripción corta>

<descripción detallada opcional>

<referencias a issues o notas opcionales>
```

Donde `<tipo>` puede ser:
- `feat`: Nueva característica
- `fix`: Corrección de errores
- `docs`: Cambios en la documentación
- `style`: Cambios de formato (espacios, indentación, etc.)
- `refactor`: Refactorización del código
- `test`: Adición o corrección de pruebas
- `chore`: Cambios en el proceso de construcción, herramientas, etc.

### Ejemplos de Buenos Mensajes de Commit

```
feat: añadir función de búsqueda avanzada

Implementa la interfaz de búsqueda avanzada con filtros por fecha, categoría y etiquetas.
Incluye tests unitarios para los nuevos componentes.

Closes #42
```

```
fix: corregir cálculo incorrecto en facturación

El impuesto se calculaba sobre el total incluyendo descuentos en lugar del subtotal.
```

### Comandos Útiles para Commits

```bash
# Ver historial de commits
git log

# Ver historial en formato compacto
git log --oneline

# Ver historial con gráfico de ramas
git log --graph --oneline --all

# Modificar el último commit (si no se ha subido)
git commit --amend

# Revertir un commit (crea un nuevo commit que deshace los cambios)
git revert <hash-del-commit>

# Visualizar diferencias en archivos
git diff

# Visualizar diferencias entre commits
git diff <commit1> <commit2>
```

## Ramas (Branches)

Las ramas permiten desarrollar funcionalidades aisladas sin afectar al código principal.

### Comandos Básicos de Ramas

```bash
# Ver todas las ramas
git branch

# Crear una nueva rama
git branch nombre-rama

# Cambiar a una rama
git checkout nombre-rama

# Crear y cambiar a una nueva rama (atajo)
git checkout -b nombre-rama

# Eliminar una rama
git branch -d nombre-rama

# Eliminar una rama forzosamente
git branch -D nombre-rama
```

### Estrategias de Ramificación

#### Git Flow
Una estrategia popular con ramas específicas:
- `main`: Código en producción
- `develop`: Código en desarrollo
- `feature/*`: Nuevas funcionalidades
- `release/*`: Preparación para lanzamientos
- `hotfix/*`: Correcciones urgentes

#### GitHub Flow
Un enfoque más simple:
- `main`: Siempre listo para desplegar
- Ramas de funcionalidades/correcciones
- Pull Requests para revisar cambios

## Fusiones (Merges)

Fusionar significa combinar los cambios de una rama en otra.

```bash
# Cambiar a la rama destino
git checkout rama-destino

# Fusionar otra rama en la actual
git merge rama-origen
```

### Tipos de Fusiones

- **Fast-forward**: Cuando la rama destino no tiene cambios propios
- **Recursive**: Cuando ambas ramas tienen cambios (crea un commit de fusión)
- **Squash**: Combina todos los commits de una rama en uno solo
  ```bash
  git merge --squash rama-origen
  git commit -m "Mensaje para el commit combinado"
  ```

## Resolución de Conflictos

Los conflictos ocurren cuando Git no puede fusionar automáticamente los cambios porque se modificaron las mismas líneas en diferentes ramas.

### Proceso de Resolución

1. Git marca los archivos con conflictos
2. Abre los archivos y busca marcadores como:
   ```
   <<<<<<< HEAD
   Código en la rama actual
   =======
   Código en la rama que estás fusionando
   >>>>>>> rama-origen
   ```
3. Edita el archivo para resolver el conflicto (elimina los marcadores)
4. Añade los archivos resueltos
   ```bash
   git add archivo-resuelto
   ```
5. Completa la fusión
   ```bash
   git commit
   ```

### Herramientas de Resolución

- Editores de código como VS Code ofrecen interfaces visuales para resolver conflictos
- Herramientas dedicadas como:
  ```bash
  git mergetool
  ```

## Trabajo Remoto (Pull/Push)

### Trabajar con Repositorios Remotos

```bash
# Ver repositorios remotos configurados
git remote -v

# Añadir un remoto
git remote add nombre-remoto url-remoto

# Eliminar un remoto
git remote remove nombre-remoto

# Renombrar un remoto
git remote rename nombre-antiguo nombre-nuevo
```

### Actualizar y Enviar Cambios

```bash
# Obtener cambios sin fusionar
git fetch origen

# Obtener cambios y fusionar automáticamente
git pull origen rama

# Enviar cambios locales al remoto
git push origen rama
```

### Opciones Útiles

```bash
# Forzar push (usar con precaución)
git push --force origen rama

# Push con seguimiento de rama
git push -u origen rama

# Pull con rebase en lugar de merge
git pull --rebase origen rama
```

## Pull Requests

Los Pull Requests (PR) son solicitudes para fusionar cambios de una rama o fork a otro repositorio o rama.

### Crear un Pull Request desde GitHub

1. Ve a tu repositorio en GitHub
2. Cambia a la rama que contiene tus cambios
3. Haz clic en "Compare & pull request"
4. Añade un título y descripción detallada
5. Asigna revisores si es necesario
6. Haz clic en "Create pull request"

### Revisar un Pull Request

1. Ve a la pestaña "Pull requests" en el repositorio
2. Selecciona el PR que quieres revisar
3. Revisa los cambios en la pestaña "Files changed"
4. Añade comentarios haciendo clic en líneas específicas
5. Aprueba, solicita cambios o comenta en la pestaña "Conversation"

### Fusionar un Pull Request

1. Una vez aprobado, haz clic en "Merge pull request"
2. Elige el método de fusión:
   - Merge commit: Preserva todo el historial
   - Squash and merge: Combina todos los commits en uno
   - Rebase and merge: Reaplica los commits en la base de la rama destino
3. Confirma la fusión

## Issues y Proyectos

### Gestión de Issues

Los Issues son usados para seguir tareas, mejoras y errores.

**Crear un Issue**:
1. Ve a la pestaña "Issues" del repositorio
2. Haz clic en "New issue"
3. Proporciona un título claro y una descripción detallada
4. Añade etiquetas, asignatarios, hitos, etc.
5. Haz clic en "Submit new issue"

**Mejores Prácticas para Issues**:
- Usa plantillas de issues (templates)
- Incluye pasos para reproducir errores
- Añade capturas de pantalla o videos cuando sea útil
- Referencia commits o PRs relacionados con `#número`

### Tableros de Proyectos

Los Proyectos de GitHub permiten organizar el trabajo con tableros estilo Kanban.

**Crear un Proyecto**:
1. Ve a la pestaña "Projects" del repositorio
2. Haz clic en "New project"
3. Elige una plantilla o comienza desde cero
4. Personaliza columnas (Por hacer, En progreso, Completado, etc.)

**Usar Proyectos Eficientemente**:
- Automatiza movimientos entre columnas con acciones
- Usa filtros para enfocarte en issues específicos
- Configura campos personalizados para prioridades o estimaciones

## GitHub Pages

GitHub Pages permite alojar sitios web directamente desde un repositorio.

### Configurar GitHub Pages

**Sitio para un usuario/organización**:
1. Crea un repositorio llamado `username.github.io`
2. Clona el repositorio localmente
3. Añade tu contenido HTML/CSS/JS
4. Sube los cambios a GitHub
5. Tu sitio estará disponible en `https://username.github.io`

**Sitio para un proyecto**:
1. Ve a Settings > Pages en tu repositorio
2. Selecciona la rama (normalmente `main` o `gh-pages`)
3. Elige la carpeta (normalmente `/` o `/docs`)
4. Guarda los cambios
5. Tu sitio estará disponible en `https://username.github.io/repository-name`

### Temas y Generadores

- Puedes usar temas predefinidos desde la configuración de Pages
- Jekyll se integra nativamente con GitHub Pages
- Otros generadores como Hugo, Gatsby, etc. también funcionan bien

## Acciones de GitHub (GitHub Actions)

GitHub Actions permite automatizar flujos de trabajo directamente en GitHub.

### Crear un Flujo de Trabajo Básico

1. Crea una carpeta `.github/workflows` en tu repositorio
2. Añade un archivo YAML, por ejemplo `ci.yml`
3. Define el flujo de trabajo:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run tests
      run: npm test
      
    - name: Build
      run: npm run build
```

### Casos de Uso Comunes

- Pruebas automatizadas (CI)
- Despliegue continuo (CD)
- Publicación de paquetes
- Automatización de PRs y issues
- Notificaciones personalizadas

## GitHub para Equipos

### Configuración de Organizaciones

Las organizaciones en GitHub proporcionan un espacio colaborativo para equipos.

**Crear una Organización**:
1. Haz clic en "+" en la esquina superior derecha
2. Selecciona "New organization"
3. Elige un plan (gratuito o de pago)
4. Proporciona un nombre y correo electrónico
5. Invita a miembros

### Equipos y Permisos

**Crear Equipos**:
1. Ve a la pestaña "Teams" en la organización
2. Haz clic en "New team"
3. Proporciona un nombre y descripción
4. Configura la visibilidad (secreta o visible)
5. Añade miembros

**Gestionar Permisos**:
- Asigna repositorios a equipos con diferentes niveles de acceso:
  - Read: Solo lectura
  - Write: Puede contribuir
  - Admin: Control total
- Configura reglas de ramas protegidas
- Establece revisiones obligatorias para PRs

## Mejores Prácticas

### Flujo de Trabajo Efectivo

1. **Mantén actualizadas tus ramas locales**
   ```bash
   git fetch --all
   git pull origin main
   ```

2. **Trabaja en ramas descriptivas**
   ```bash
   git checkout -b feature/login-system
   git checkout -b fix/navbar-alignment
   ```

3. **Realiza commits frecuentes y descriptivos**
   ```bash
   git commit -m "feat: implementar formulario de login"
   ```

4. **Revisa tus cambios antes de confirmar**
   ```bash
   git diff
   git status
   ```

5. **Usa Pull Requests para revisión de código**

### Documentación

- Mantén un README.md actualizado con:
  - Descripción del proyecto
  - Instrucciones de instalación
  - Guía de uso
  - Cómo contribuir
  - Licencia

- Considera añadir:
  - CONTRIBUTING.md: Directrices para contribuir
  - CODE_OF_CONDUCT.md: Normas de conducta
  - CHANGELOG.md: Registro de cambios

### Seguridad

- Nunca commits información sensible (contraseñas, claves API, etc.)
- Usa `.gitignore` para excluir archivos sensibles o innecesarios
- Configura análisis de seguridad en GitHub
- Revisa regularmente las dependencias por vulnerabilidades

## Recursos Adicionales

### Documentación Oficial
- [Documentación de Git](https://git-scm.com/doc)
- [Documentación de GitHub](https://docs.github.com/)
- [GitHub Learning Lab](https://lab.github.com/)

### Herramientas Útiles
- GitHub Desktop: Interfaz gráfica para Git
- GitKraken: Cliente Git avanzado
- Sourcetree: Alternativa visual a la línea de comandos

### Cursos y Tutoriales
- [GitHub Skills](https://skills.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2) (gratuito)
- [GitHub Learning Lab](https://lab.github.com/)

### Cheatsheets
- [Git Cheatsheet de GitHub](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)