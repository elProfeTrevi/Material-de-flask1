# 🏫 Práctica: Sistema de Comunidad Educativa - Nueva Escuela Mexicana

## 📋 **Actividad Práctica: "Construyendo Nuestra Comunidad Digital"**

### **🎯 Objetivo de la Práctica**
Desarrollar un sistema de autenticación que refleje los principios de la Nueva Escuela Mexicana, donde diferentes roles educativos tengan acceso a espacios digitales específicos según su función en la comunidad.

---

## 🧩 **Fase 1: Preparación del Entorno**

### **Paso 1.1: Configuración Inicial**
- Crear una carpeta llamada `comunidad_educativa` para el proyecto
- Dentro de esta carpeta, crear las subcarpetas: `templates`, `static`
- En la carpeta `templates`, crear las subcarpetas: `estudiante`, `docente`, `directivo`, `familia`

### **Paso 1.2: Instalación de Dependencias**
- Verificar que Python esté instalado
- Instalar Flask usando pip: `pip install flask`

---

## 🏗️ **Fase 2: Estructura Base de la Aplicación**

### **Paso 2.1: Crear el Archivo Principal**
- Crear el archivo `app.py` en la carpeta principal
- Importar los módulos necesarios de Flask
- Configurar una clave secreta para las sesiones

### **Paso 2.2: Definir los Miembros de la Comunidad**
- Crear un diccionario que simule una base de datos con 4 usuarios:
  - **1 Estudiante** con sus datos académicos
  - **1 Docente** con su materia y grupos
  - **1 Directivo** con su cargo
  - **1 Familiar** con el estudiante a su cargo

---

## 🎨 **Fase 3: Diseño de la Interfaz Comunitaria**

### **Paso 3.1: Plantilla Base con Enfoque NEM**
- Crear `base.html` con colores que representen la bandera de México
- Diseñar una barra de navegación que muestre:
  - Opciones para usuarios no autenticados
  - Opciones específicas para cada rol cuando estén autenticados
  - Información del usuario logueado

### **Paso 3.2: Página de Inicio**
- Crear `index.html` que herede de la plantilla base
- Incluir una sección sobre los pilares de la NEM
- Mostrar tarjetas representativas para cada rol educativo
- Agregar una sección sobre aprendizaje colaborativo

### **Paso 3.3: Página de Inicio de Sesión**
- Crear `login.html` con un formulario de autenticación
- Implementar botones para cargar credenciales de cada rol automáticamente
- Incluir una sección de reflexión sobre inclusión digital

---

## 🔐 **Fase 4: Sistema de Autenticación**

### **Paso 4.1: Ruta de Inicio de Sesión**
- Crear la ruta `/iniciar-sesion` que acepte métodos GET y POST
- En GET: Mostrar el formulario de login
- En POST: 
  - Validar que el email y contraseña coincidan con algún usuario
  - Si son correctos: almacenar información en sesión y redirigir al dashboard
  - Si son incorrectos: mostrar mensaje de error

### **Paso 4.2: Manejo de Sesiones**
- Usar `session` para almacenar información del usuario autenticado
- Incluir nombre, rol y datos específicos según el tipo de usuario

---

## 🚀 **Fase 5: Dashboard Principal**

### **Paso 5.1: Ruta del Espacio Personal**
- Crear la ruta `/mi-espacio` 
- Verificar que el usuario esté autenticado
- Si no está autenticado, redirigir al login con mensaje
- Mostrar un dashboard genérico con bienvenida e información del rol

### **Paso 5.2: Contenido del Dashboard**
- Mostrar el nombre del usuario y su rol
- Incluir enlaces a las secciones específicas de cada rol
- Usar condicionales en la plantilla para mostrar contenido según el rol

---

## 📚 **Fase 6: Espacios Específicos por Rol**

### **Paso 6.1: Panel del Estudiante**
- Crear ruta `/estudiante/aprendizaje`
- Verificar que el usuario sea estudiante
- Si no tiene permiso, redirigir con mensaje de error
- Crear plantilla `estudiante/mi_aprendizaje.html`

### **Paso 6.2: Panel del Docente**
- Crear ruta `/docente/aula`
- Verificar que el usuario sea docente
- Crear plantilla `docente/mi_aula.html`

### **Paso 6.3: Panel del Directivo**
- Crear ruta `/directivo/gestion`
- Verificar que el usuario sea directivo
- Crear plantilla `directivo/gestion.html`

### **Paso 6.4: Panel de la Familia**
- Crear ruta `/familia/acompanamiento`
- Verificar que el usuario sea familia
- Crear plantilla `familia/acompanamiento.html`

---

## 🛡️ **Fase 7: Control de Accesos y Seguridad**

### **Paso 7.1: Protección de Rutas**
- En cada ruta específica de rol, verificar:
  1. Que el usuario esté autenticado
  2. Que tenga el rol adecuado para acceder
- Si no cumple, redirigir al dashboard con mensaje de error

### **Paso 7.2: Cierre de Sesión**
- Crear ruta `/cerrar-sesion`
- Limpiar toda la información de sesión
- Redirigir a la página de inicio con mensaje de despedida

---

## 💡 **Fase 8: Mejoras y Validaciones**

### **Paso 8.1: Mensajes al Usuario**
- Implementar mensajes flash para:
  - Login exitoso/fallido
  - Accesos denegados
  - Cierre de sesión
- Usar categorías diferentes para éxito y error

### **Paso 8.2: Navegación Dinámica**
- En la plantilla base, usar condicionales para mostrar:
  - Solo las opciones de menú correspondientes al rol
  - Estado de autenticación del usuario

---

## 🧪 **Fase 9: Pruebas y Verificación**

### **Paso 9.1: Probar Todos los Roles**
- Verificar que cada usuario pueda:
  - Iniciar sesión con sus credenciales
  - Acceder a su dashboard específico
  - Ver solo las opciones de menú de su rol
  - No poder acceder a paneles de otros roles

### **Paso 9.2: Validar Seguridad**
- Intentar acceder directamente a rutas sin autenticación
- Verificar que usuarios de un rol no puedan acceder a rutas de otros roles
- Confirmar que el cierre de sesión funcione correctamente

---

## 📝 **Criterios de Evaluación**

### **Funcionalidad (40%)**
- [ ] Los 4 roles pueden autenticarse correctamente
- [ ] Cada rol accede solo a sus espacios autorizados
- [ ] La navegación muestra opciones según el rol
- [ ] Los mensajes de feedback funcionan adecuadamente

### **Implementación Técnica (30%)**
- [ ] Uso correcto de sesiones para autenticación
- [ ] Validación de permisos en cada ruta protegida
- [ ] Estructura adecuada de plantillas con herencia
- [ ] Código organizado y comentado

### **Enfoque NEM (20%)**
- [ ] Diseño refleja principios de inclusión
- [ ] Interfaz adecuada para cada rol educativo
- [ ] Elementos visuales que representan la comunidad

### **Creatividad (10%)**
- [ ] Contenido relevante para cada panel de rol
- [ ] Diseño atractivo y usable
- [ ] Elementos que enriquecen la experiencia

