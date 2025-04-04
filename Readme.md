# Comandos dispobles
<img src="/img/como-usar.png" />
# Guia para desplegar el bot
* **requisitos**
* python 3.X (Ultima versión)
* pip
* git
* Conocimiento basico de como manejarse por consola/terminal (hay muchos videos en Youtube que enseñan eso)
## Clonar repositorio
* (Estos pasos se hacen por consola)
* git clone https://github.com/LuisAnng/HelmoWikiBot
* cd HelmoWikiBot
## Crear la aplicacion en Discord Developer Portal
* Ve a [Discord Developer Portal](https://discordapp.com/developers/applications/)
* Crea una nueva aplicacion.
* Vaya a la pestaña bot marca estas casillas "Server Members Intent" , "Message Content Intent".
* Agrega estos permisos "Send Messages", "Manage Messages" o simplemente agrege "administrator" y ya se asignan todos los permisos
* mas abajo hay un campo "Permissions Integer" debe de haber un numero en ese campo copielo y guardelo en un block de notas
* Luego se va a la pestaña de "Installation"  copias el link que aparece que seria algo asi "https://discord.com/oauth2/authorize?client_id= (el id de su bot)"  luego agrege "&permissions=(el numero que guardo hace un momento) y luego escriba "&scope=bot" le deberia quedar algo asi "https://discord.com/oauth2/authorize?client_id=( el id de su bot)&permissions=(el numero de permisos que le asignaron)&scope=bot(eso es para que discord lo reconozca como un bot)"
## Obtener el Token
* Tu token es lo que usas para iniciar sesión en el bot
* En la pestaña del Bot, haga clic en "Reset Token" o "Generar Token"
* Una vez que haya copiado el token, ahora puede pegarlo en el archivo de .env
* **ASEGÚRESE DE PEGARLO ENTRE LAS COMILLAS " "**  
<img src="/img/Token-ejemplo.png" />

## Desplegar el bot en su pc
* Añadan al bot con el enlance que generaron hace un momento que seria algo asi https://discord.com/oauth2/authorize?client_id=0101&permissions=01001&scope=bot entre y seleccionen el servidor que quieran agregar el bot 
- **Activar el bot**
** PD: Si ya clonaron el repositorio no lo vuelvan a clonar -_-
<img src="/img/ejecutarbot.png" />

**Los comandos para activar el entorno virtual pueden ser diferentes en windows si no les funciona el de la imagen investiguen como activarlo en su sistema operativo**
* De esta manera el bot lo podran usar los usuarios en el servidor que este agregado siempre y cuando su pc  este ejecutando el codigo
# Desplegar el bot mediante la nube
* Existe varios metodos para hacer esto y todos o casi todos son de paga,  hay varios videos de youtube para hacer esto les dejo 2 aqui en diferentes idomas si ninguno de estos les funcionan busquen "como desplegar bot de discord en python" 
- **ES** [tutorial](https://youtu.be/2zf1hjGFCgU?si=wxXFhpuimSL6VQ1f) 

- **BR** [tutorial](https://youtu.be/WdlJi5j4pps?si=IonkN3WIRGoJ7paO&t=284) 

**ADVERTENCIA HAY POSIBILIDAD DE QUE ESOS METODOS YA NO FUNCIONE**

# Contacto
* Dudas o sugerencias me pueden hablar por ahí
* **Discord:sleepingg01** 
