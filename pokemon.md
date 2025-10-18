# 🎮 Práctica: "Explorando el Mundo Pokémon con APIs y Autenticación"

## 📋 **Actividad Práctica: "Pokedex Comunitaria"**

### **🎯 Objetivo de la Práctica**
Desarrollar un sistema de autenticación con roles que consuma la PokeAPI para mostrar información de Pokémon, aplicando los principios de la Nueva Escuela Mexicana en el diseño de la experiencia.

---

## 🧩 **Fase 1: Preparación del Entorno**

### **Paso 1.1: Configuración Inicial**
- Crear una carpeta llamada `pokedex_comunitaria` para el proyecto
- Dentro de esta carpeta, crear las subcarpetas: `templates`, `static`
- En `templates`, crear subcarpetas: `entrenador`, `investigador`, `lider_gimnasio`

### **Paso 1.2: Instalación de Dependencias**
- Verificar que Python esté instalado
- Instalar Flask: `pip install flask`
- Instalar requests para consumir la API: `pip install requests`

---

## 🏗️ **Fase 2: Estructura Base de la Aplicación**

### **Paso 2.1: Crear el Archivo Principal**
- Crear `app.py` en la carpeta principal
- Importar módulos necesarios: Flask, requests
- Configurar clave secreta para sesiones

### **Paso 2.2: Definir los Roles de la Comunidad Pokémon**
- Crear diccionario con 3 tipos de usuarios:
  - **Entrenador Pokémon** (acceso básico a información)
  - **Investigador Pokémon** (acceso con análisis detallado)
  - **Líder de Gimnasio** (acceso premium con estadísticas avanzadas)

---

## 🎨 **Fase 3: Diseño de la Interfaz con Bootstrap 5**

### **Paso 3.1: Plantilla Base con Bootstrap**
- Crear `base.html` usando solo clases de Bootstrap 5
- Implementar navbar responsive con colores temáticos Pokémon
- Incluir container principal y sistema de mensajes

### **Paso 3.2: Página de Inicio Temática**
- Crear `index.html` que herede de la plantilla base
- Diseñar hero section con temática Pokémon
- Usar cards de Bootstrap para presentar los diferentes roles
- Incluir sección sobre el trabajo colaborativo en investigación Pokémon

### **Paso 3.3: Página de Inicio de Sesión**
- Crear `login.html` con formulario de Bootstrap
- Implementar botones para cargar credenciales de cada rol
- Diseñar con componentes de Bootstrap (cards, buttons, forms)

---

## 🔐 **Fase 4: Sistema de Autenticación por Roles**

### **Paso 4.1: Ruta de Inicio de Sesión**
- Crear ruta `/iniciar-sesion` que maneje GET y POST
- Validar credenciales contra el diccionario de usuarios
- Al autenticar, almacenar rol y datos en sesión
- Redirigir al dashboard correspondiente

### **Paso 4.2: Manejo de Sesiones y Permisos**
- Usar `session` para guardar información del usuario
- Incluir rol específico y preferencias de visualización

---

## 🌐 **Fase 5: Integración con PokeAPI**

### **Paso 5.1: Función para Consumir la API**
- Crear función que haga request a: `https://pokeapi.co/api/v2/pokemon?limit=20`
- Manejar posibles errores de conexión
- Procesar la respuesta JSON para extraer datos de los Pokémon

### **Paso 5.2: Ruta Principal de Pokémon**
- Crear ruta `/pokemon` que muestre los primeros 20 Pokémon
- Usar la función de API para obtener los datos
- Pasar la lista de Pokémon a la plantilla

---

## 🎮 **Fase 6: Dashboards Específicos por Rol**

### **Paso 6.1: Dashboard del Entrenador**
- Crear ruta `/entrenador/dashboard`
- Verificar rol de entrenador
- Mostrar grid de Pokémon con información básica: nombre e imagen
- Usar cards de Bootstrap para mostrar cada Pokémon

### **Paso 6.2: Dashboard del Investigador**
- Crear ruta `/investigador/dashboard`
- Verificar rol de investigador
- Mostrar información extendida: tipos, habilidades
- Implementar acordeones o tabs de Bootstrap para organizar información

### **Paso 6.3: Dashboard del Líder de Gimnasio**
- Crear ruta `/lider/dashboard`
- Verificar rol de líder
- Mostrar información completa: estadísticas, movimientos
- Usar progress bars de Bootstrap para mostrar stats

---

## 🃏 **Fase 7: Visualización de Pokémon con Bootstrap**

### **Paso 7.1: Componente de Tarjeta Pokémon**
- Crear componente reutilizable para mostrar Pokémon
- Usar sistema de grid de Bootstrap para layout responsive
- Implementar diferentes niveles de detalle según el rol

### **Paso 7.2: Diseño Responsive**
- Asegurar que la pokedex se vea bien en móviles y desktop
- Usar clases responsive de Bootstrap (col-md, col-sm, etc.)
- Implementar navbar toggler para dispositivos móviles

---

## 🛡️ **Fase 8: Control de Accesos y Funcionalidades**

### **Paso 8.1: Protección de Rutas por Rol**
- En cada dashboard, verificar el rol del usuario
- Implementar redirecciones y mensajes de error apropiados
- Usar condicionales en plantillas para mostrar/u ocultar features

### **Paso 8.2: Funcionalidades por Rol**
- **Entrenador**: Solo ver nombre e imagen
- **Investigador**: Ver tipos y habilidades
- **Líder**: Ver estadísticas completas y movimientos

---

## 💡 **Fase 9: Mejoras de Experiencia de Usuario**

### **Paso 9.1: Mensajes y Feedback**
- Implementar mensajes flash para acciones del usuario
- Mostrar loading states mientras se carga la API
- Manejar errores de API con mensajes amigables

### **Paso 9.2: Navegación y UX**
- Breadcrumb navigation con Bootstrap
- Botones con iconos de Bootstrap Icons
- Tooltips para información adicional

---

## 🧪 **Fase 10: Pruebas y Verificación**

### **Paso 10.1: Pruebas de Autenticación**
- Verificar que cada rol acceda solo a su dashboard
- Confirmar que la información mostrada sea la correcta para cada rol
- Probar navegación entre diferentes secciones

### **Paso 10.2: Pruebas de API**
- Verificar que se muestren exactamente 20 Pokémon
- Confirmar que los datos de la API se muestren correctamente
- Probar el manejo de errores de conexión

---

## 📊 **Criterios de Evaluación**

### **Consumo de API (30%)**
- [ ] Conexión exitosa con PokeAPI
- [ ] Manejo adecuado de respuestas y errores
- [ ] Mostrar 20 Pokémon correctamente
- [ ] Procesamiento adecuado de datos JSON

### **Sistema de Autenticación (25%)**
- [ ] Tres roles funcionando correctamente
- [ ] Control de accesos por rol implementado
- [ ] Sesiones manejadas apropiadamente
- [ ] Navegación dinámica según rol

### **Diseño con Bootstrap (25%)**
- [ ] Uso correcto de componentes de Bootstrap 5
- [ ] Diseño responsive y mobile-friendly
- [ ] Estética coherente y atractiva
- [ ] Organización visual de información

### **Funcionalidad por Rol (20%)**
- [ ] Información diferenciada por rol
- [ ] Features específicas implementadas
- [ ] Experiencia de usuario adaptada
- [ ] Navegación intuitiva

---

## 🔍 **Puntos Clave a Observar por el Instructor**

Durante el desarrollo, observar si los estudiantes:

1. **Manejan correctamente las peticiones HTTP** a APIs externas
2. **Procesan datos JSON** y los integran en las plantillas
3. **Aplican condicionales complejos** para mostrar información por rol
4. **Utilizan componentes de Bootstrap** de manera efectiva
5. **Estructuran el código** para manejar la lógica de API separadamente

---

## 🎯 **Habilidades Técnicas a Evaluar**

### **Backend**
- Consumo de APIs REST con requests
- Manejo de sesiones y autenticación
- Control de accesos y autorización
- Procesamiento de datos JSON

### **Frontend**
- Bootstrap 5: Grid system, Components, Utilities
- Plantillas dinámicas con Jinja2
- Diseño responsive
- Organización de información

### **Conceptos**
- Separación de concerns (lógica vs presentación)
- Manejo de errores en APIs
- User Experience diferenciada
- Principios de diseño responsive

---

## 💬 **Reflexión de Aprendizaje**

Al finalizar, los estudiantes deben responder:

1. ¿Qué desafíos presentó el consumo de la API externa?
2. ¿Cómo el sistema de roles mejora la experiencia de usuario?
3. ¿Qué ventajas ofrece Bootstrap en el desarrollo frontend?
4. ¿Cómo se podría escalar este sistema para incluir más funcionalidades?

---

## 🚀 **Desafíos Opcionales para Avanzados**

### **Desafío 1: Búsqueda de Pokémon**
- Implementar barra de búsqueda para Pokémon específicos
- Consumir endpoint individual de Pokémon

### **Desafío 2: Paginación**
- Implementar paginación para ver más de 20 Pokémon
- Usar parámetros offset y limit de la API

### **Desafío 3: Favoritos**
- Sistema para marcar Pokémon como favoritos
- Almacenar preferencias en sesión

---

## ⏱️ **Información de la Actividad**

**Tiempo estimado:** 4-5 horas  
**Dificultad:** Intermedia-Avanzada  
**API utilizada:** PokeAPI (https://pokeapi.co)  
**Framework CSS:** Bootstrap 5 exclusivamente

**¡Atrápalos a todos en esta aventura de programación!** 🎮✨

---

## 📝 **Notas para el Instructor**

Esta actividad permite evaluar:
- Comprensión de consumo de APIs REST
- Implementación de sistemas de autenticación
- Uso de frameworks CSS (Bootstrap)
- Diseño de interfaces diferenciadas por usuario
- Manejo de datos JSON y estructuras complejas

Los estudiantes demostrarán su capacidad para integrar múltiples tecnologías en un proyecto cohesivo y funcional.