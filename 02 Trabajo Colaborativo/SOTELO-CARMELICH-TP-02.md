
---
# Trabajo Práctico-02: Git y GitHub

<!-- Autor: SOTELO CARMELICH AGUSTIN -->

---

## ¿Qué es GitHub?

GitHub es una plataforma de desarrollo colaborativo basada en la web que utiliza Git como sistema de control de versiones. Permite a los desarrolladores almacenar, compartir y colaborar en proyectos de software, con funciones como ramas, issues, pull requests y control de acceso.

---

## ¿Cómo crear un repositorio en GitHub?

1. Iniciar sesión en [GitHub](https://github.com).
2. Hacer clic en el botón verde **New repository**.
3. Ingresar el nombre del repositorio, una descripción opcional, y elegir si será público o privado.
4. (Opcional) Marcar la opción para inicializar con un README.
5. Hacer clic en **Create repository**.

---

## ¿Cómo crear una rama en Git?

Para crear una nueva rama:

```bash
git branch nombre-de-la-rama
```

Esto crea una rama sin cambiar a ella. Para crearla y cambiar directamente:

```bash
git checkout -b nombre-de-la-rama
```

---

## ¿Cómo cambiar a una rama en Git?

Para cambiar de rama se usa:

```bash
git checkout nombre-de-la-rama
```

---

## ¿Cómo fusionar ramas en Git?

1. Cambiar a la rama donde se desea aplicar la fusión (por lo general `main`):

```bash
git checkout main
```

2. Fusionar la otra rama:

```bash
git merge nombre-de-la-rama
```

Esto une los cambios de la rama especificada en la rama actual.

---

## ¿Cómo crear un commit en Git?

Un commit guarda los cambios en el historial del proyecto. Los pasos son:

```bash
git add .
git commit -m "Mensaje que describe los cambios"
```

`git add .` agrega todos los cambios al área de preparación y `git commit` los guarda con un mensaje.

---

## ¿Cómo enviar un commit a GitHub?

Primero se necesita un repositorio remoto (por ejemplo, en GitHub). Luego se usa:

```bash
git push origin nombre-de-la-rama
```

Esto envía los commits locales al repositorio remoto.

---

## ¿Qué es un repositorio remoto?

Es una versión del repositorio que se encuentra alojada en un servidor externo, como GitHub. Permite compartir el código y colaborar con otros desarrolladores.

---

## ¿Cómo agregar un repositorio remoto a Git?

Se usa el comando:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

`origin` es el nombre por defecto del repositorio remoto.

---

## ¿Cómo empujar cambios a un repositorio remoto?

Para subir los cambios al repositorio remoto:

```bash
git push origin nombre-de-la-rama
```

---

## ¿Cómo tirar de cambios de un repositorio remoto?

Para obtener actualizaciones del repositorio remoto:

```bash
git pull origin nombre-de-la-rama
```

Esto descarga y fusiona los cambios con la rama actual.

---

## ¿Qué es un fork de repositorio?

Un fork es una copia de un repositorio que se crea en tu cuenta de GitHub. Te permite modificar el código sin afectar el repositorio original. Es útil para contribuir a proyectos open source.

---

## ¿Cómo crear un fork de un repositorio?

1. Ingresar al repositorio que se desea copiar.
2. Hacer clic en el botón **Fork** (arriba a la derecha).
3. GitHub creará una copia del repositorio en tu cuenta.

---

## ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?

1. Subir tus cambios a tu fork.
2. Hacer clic en **Pull Request** en la página del repositorio original.
3. Comparar ramas y escribir un mensaje que explique los cambios.
4. Hacer clic en **Create Pull Request**.

---

## ¿Cómo aceptar una solicitud de extracción?

1. Ir a la pestaña **Pull Requests** del repositorio.
2. Elegir la solicitud y revisarla.
3. Hacer clic en **Merge pull request**.
4. Confirmar con **Confirm merge**.

---

## ¿Qué es una etiqueta en Git?

Una etiqueta (tag) es una referencia a un punto específico en el historial de commits, normalmente utilizada para marcar versiones importantes (por ejemplo, `v1.0`).

---

## ¿Cómo crear una etiqueta en Git?

Para crear una etiqueta simple:

```bash
git tag v1.0
```

Para una etiqueta con mensaje anotado:

```bash
git tag -a v1.0 -m "Versión 1.0"
```

---

## ¿Cómo enviar una etiqueta a GitHub?

Después de crear la etiqueta, se envía con:

```bash
git push origin v1.0
```

Para enviar todas las etiquetas:

```bash
git push --tags
```

---

## ¿Qué es un historial de Git?

Es el registro completo de todos los commits que se han realizado en el repositorio. Permite ver cómo ha evolucionado el proyecto.

---

## ¿Cómo ver el historial de Git?

```bash
git log
```

Muestra una lista de commits con el autor, fecha y mensaje.

---

## ¿Cómo buscar en el historial de Git?

Para buscar por palabra clave en los mensajes:

```bash
git log --grep="palabra"
```

Para buscar archivos modificados:

```bash
git log -- nombre-del-archivo
```

---

## ¿Cómo borrar el historial de Git?

**Advertencia:** esto elimina todo el historial anterior.

```bash
rm -rf .git
git init
```

Esto reinicia el repositorio. Se debe usar con mucha precaución.

---

## ¿Qué es un repositorio privado en GitHub?

Es un repositorio al que solo pueden acceder personas con permiso. No aparece en los resultados de búsqueda públicos.

---

## ¿Cómo crear un repositorio privado en GitHub?

1. Hacer clic en **New repository**.
2. Ingresar nombre y descripción.
3. Seleccionar la opción **Private**.
4. Crear el repositorio.

---

## ¿Cómo invitar a alguien a un repositorio privado en GitHub?

1. Entrar al repositorio.
2. Ir a **Settings > Collaborators**.
3. Escribir el nombre de usuario de GitHub y hacer clic en **Add**.
4. El usuario debe aceptar la invitación.

---

## ¿Qué es un repositorio público en GitHub?

Es un repositorio visible para cualquier persona en GitHub. Cualquiera puede clonar el código y ver el contenido.

---

## ¿Cómo crear un repositorio público en GitHub?

1. Hacer clic en **New repository**.
2. Ingresar nombre y descripción.
3. Seleccionar la opción **Public**.
4. Crear el repositorio.

---

## ¿Cómo compartir un repositorio público en GitHub?

1. Ir al repositorio.
2. Copiar la URL del navegador o del botón **Code**.
3. Enviar el enlace por mail, chat, redes, etc.

---


