# Nono
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Es un asistente de voz offline personalizable. 
El objetivo de este projecto es automatizar algunos procesos usando la voz sin enviar mis datos a un servidro externo y 
que no consuma muchos recursos.

Para el reconocimiento de voz se utiliza [Vosk](https://alphacephei.com/vosk/).

## Instalar 
### Instalar dependencias
```shell
sudo apt install espeak # Para poder usar pyttsx3
pip install -r requirements. txt 
```

### Descargar modelo 
1. Descargar el [modelo de la paguina de vosk](https://alphacephei.com/vosk/models).
Los pequeños consumen serca de XX de RAM los grande cerca de 4 de RAM.

2. Descomprimir el modelo en la carpeta `~/.config/nono/model`, sin subcarpetas, quedando de la siguiente manera.
```bash
├── ~/.config/nono/model
│   ├── am
│   ├── conf
│   ├── graph
│   ├── ivector
```

4. Si desea moverlo para otra localizacion ver [Configurar](## Configurar)

## Configurar
Crear un fichero json en `~/.config/nono/config.json` con el siguiente contenido.
```json
{
    "model_dir": "~/.config/nono/model",
    "key_world": "pedro",
    "commands": [
        {
            "name": "brave",
            "run": "brave-browser",
            "phrases": [
                "ejecutar navegador",
                "abrir navegador"
            ]
        }
    ]
}
```
**model_dir:** Direccion absoluta del modelo vosk
**key_world:** Palabra clave para disparar los comandos
**phrases:** Frases despues de *key_world* que va a disparar el comando, entre mas clara y diferente de los demas mejor.

Existen algunas palabras que los modelos no tienen y las ignoran. 
Falta trabajar en mostrar estas palabras al usuario y/o agregarlas si es posible.

## Agregar como servicio de Linux
1. Cambiar el directorio donde se encuentra el script en el fichero `configs/nono.service` linea `WorkingDirectory`.
2. Copiar fichero a la carpeta de `systemd`
```shell
mkdir -p ~/.config/systemd/user/
cp configs/nono.service ~/.config/systemd/user/nono.service
```
3. Cargar la nueva congiguracion
```shell
systemctl --user daemon-reload
```
4. Activar y iniciar el servicio 
```shell
systemctl --user enable nono
systemctl --user start nono
```

5. Reiniciar
```shell
systemctl --user restart nono
```

Ver estado 
```shell
systemctl --user status nono
```

Como eliminarlo
```shell
systemctl --user stop nono
systemctl --user disable nono
rm ~/.config/systemd/user/nono.service
```

## Como contribuir
Para contribuir subir un [Merger Request](https://gitlab.com/ruby232/nono/-/merge_requests) o agregar una [issue](https://gitlab.com/ruby232/nono/-/issues).


## Todo
- Agregar comandos con confirmacion
- Agregar comandos con argumentos
- Escribir documentacion
- Escribir articulo

- Agregar palabras al modelo
- Mostrar palabras ignoradas por el modelo
- Entrenar modelo con mi voz
- Hacer una interfza grafica

## Done
- Hacer que los comandos sean independientes
- Mejorar el sistema para comprar la comparaciond e frases
- Agregar como servicio de linux
