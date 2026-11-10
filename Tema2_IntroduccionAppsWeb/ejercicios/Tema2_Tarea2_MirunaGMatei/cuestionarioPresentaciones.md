<h1 align="center">
——— CUESTIONARIO PRESENTACIÓN ———
</h1>

## ÍNDICE
- [Preguntas](#preguntas)
- [Recordatorio](#recordatorio)

## PREGUNTAS
### 1. Qué significa las siglas HTTP y para qué se utiliza?

**HTTP** significa HyperText Transfer Protocol, que en español sería Protocólo de Transferencia de Hipertexto. Se utiliza para la comunicación entre clientes y servidores web, permitiendo solicitar y transferir páginas HTML, imágenes, archivos y otros recursos

### 2. ¿En qué puerto funciona normalmente el protocolo HTTP?

Suele funcionar en el puerto 80


### 3. ¿Cuál es la diferencia principal entre HTTP y HTTPS?

- **HTTP:** envía todo por texto plano.
- **HTTPS:** añade una capa de cifrado mediante TLS/SSL, por lo que los datos viajan cifrados y usa el puerto 443

### 4. ¿Qué función cumple el servidor web Apache dentro de una arquitectura web?

Recibe las peticiones de los clientes y devuelve los recursos solicitados. Es la capa que sirve el contenido en la arquitectura web

### 5. ¿Cómo puedes comprobar si el servicio de Apache está activo en un sistema Ubuntu?

Lo puedes comprobar poniendo el siguiente comando:
```bash
sudo systemctl status apache2
```

### 6. Explica brevemente en qué consiste una arquitectura cliente-servidor.

El cliente le envía una petición para saber si se encuentra ahí, en caso de que el servidor responda diciendo que se encuentra ahí, el cliente le envía la petición que necesita que el servidor realice, procesando y devolviendo una respuesta.

### 7. ¿Qué diferencia hay entre una arquitectura de dos capas y una de tres capas en entornos web?

La de **_dos capas_** distribuye las tareas entre una capa de presentación (cliente) y una capa de datos (servidor). Es sencillo y asequible de implementar, pero tiene una baja escabilidad, alta carga de red y dificultadores para mantener versiones.

La de **_tres capas_** introduce una capa entre medias que ser dedica a la lógica de negocio, separándolo de la presentación y almacenamiento.

### 8. ¿Qué es el protocolo FTP y para qué se usa?

Es un estándar de red diseñado para la transferencia eficiente de archivos entre un cliente y un servidor en un red TCP/IP. Se usa para subir. descargar. gestionar archivos; mover grandes volúmenes de datos; realizar backups y ofrecer descargas públicas desde repositorios.

### 9. Menciona un ejemplo de cliente FTP y un ejemplo de servidor FTP.

- **_Ejemplo cliente FTP:_** FileZilla Cliente
- **_Ejemplo servidor FTP:_** FileZilla Server

### 10. ¿Qué diferencia existe entre FTP y SFTP?

- **_FTP:_** Transmite datos en texto plano sin cifrar
- **_SFTP:_** Cifra la comunicación mediante el protocolo **SSH**, protegiendo tanto las credenciales como los archivos.

### 11. Indica tres tipos de alojamiento web y explica brevemente en qué se diferencian.

- **_Alojamiento compartido:_** Varios sitios comparten un mismo servidor físico, siendo la opción más económica y sencilla. **Ejemplo:** Blogs o webs pequeñas
- **_Alojamiento VPS (Servidor Privado Virtual):_** Servidor físico que se divide en instancias virtuales con recursos garantizados y aislados. **Ejemplo:** Partidas privadas de Minecraft o CS:GO
- **_Alojamiento dedicado:_** Se alquila un servidor físico completo para un único cliente, proporcionando máximo rendimiento, seguridad y control total para proyectos de alto tráfico. **Ejemplo:** E-Commerce grande

### 12. ¿Qué ventajas ofrece un servidor VPS frente a un alojamiento compartido?

Un **servidor VPS** ofrece recursos dedicados que garantizan un rendimiento constante y consistente, que ha diferencia del **servidor compartido**, este proporciona mayor control mediante acceso root, permitiendo personalizar el sistema operativo, entre otras cosas.

### 13. Describe brevemente los componentes principales de una arquitectura web moderna.

Tiene 3 capas:
1. **_Capa de Presentación (Frontend):_** interactúa directamente con el usuario mediante el navegador usando HTML, CSS Y JS.
2. **_Capa de Aplicación (Backend):_** gestiona la lógica del negocio, la seguridad y el procesamietno de datos, exponiendo funcionalidad a través de APIs para ser consumida por múltiples clientes
3. **_Capa de Datos e Insfraestructura:_** incluye base de datos para el almacenamiento, balanceadores de carga para distribuir tráfica, y CDNs (red de servidores distribuidos geográficamente) para la entrega rápida de contenido estático.

### 14. ¿Qué papel cumple el servidor de aplicaciones dentro de dicha arquitectura?

En la arquitectura cliente-servidor, el **Servidor de aplicaciones** actúa como el intermediario central (o también podemos decirle que actúa como el cerebro), que gestiona la lógica del negocio y coordina la comunicación entre la capa de presentación y la capa de datos.

### 15. ¿Qué software o paquete puedes usar para instalar Apache fácilmente en Windows?

Hay varias opciones, pero la más usada es XAMP ya que es gratuito e incluye Apache, MariaDB, PHP y Perl que son diseñador para ser fáciles de instalar y usar tanto en Windows, Linux y OS X.

### 16. ¿Qué carpeta suele contener los archivos del sitio web en una instalación de Apache en Windows (por ejemplo, con XAMPP)?

La carpeta es **htdocs** que se encuentra dentro del directorio principal de la instalación teniendo como ruta predeterminada: ``` C:\xampp\htdocs\ ```

### 17. Escribe el comando para instalar Apache en Ubuntu desde la terminal.

```bash
sudo apt install apache2
```

### 18. ¿Qué comando se usa para iniciar el servicio Apache en Ubuntu?

```bash
sudo systemctl start apache2
```

### 19. ¿En qué ruta se almacena normalmente la página web por defecto de Apache en Ubuntu?

En la ruta ``` /var/www/html/ ```

### 20. ¿Qué es el protocolo SSH y cuál es su propósito principal?

El **SSH** es un protocólo de red. Su proṕosito es proporcionar un canal seguro y cifrado para que los usuarios puedas acceder, controlar y modificar servidores remotos de forma remota, garantizando la confidencialidad, autenticación e integridad de los datos transmitidos.

### 21. ¿Qué comando se usa para conectarse a un servidor remoto mediante SSH?

```bash
ssh usuario@direccionHost

```

### 22. Menciona una ventaja de usar autenticación mediante claves SSH frente a contraseña

Es más seguro, ya que las claves SSH son resistentes a los ataques de fuerza bruta y a la interceptación de contraseñas, dado que la clave privada nunca se transmite por red.


## RECORDATORIO
**¡ PASARLO A UN FICHERO DOCX !**

---

> Realizado por Miruna Georgiana Matei ~ IES Juan Bosco 🥀
