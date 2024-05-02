# Nono
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Es un asistente de voz offline personalizable. 
El objetivo de este proyecto es automatizar algunos procesos usando la voz sin enviar mis datos a un servidor externo y 
que no consuma muchos recursos.

Para el reconocimiento de voz se utiliza [Vosk](https://alphacephei.com/vosk/).

## Instalar 
### Instalar dependencias
```shell
sudo apt install espeak # Solo se se va a usar pyttsx3
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

3. Sí desea moverlo para otra localización ver [Configurar](## Configurar)

## Configurar
Crear un fichero json en `~/.config/nono/config.json` con el siguiente contenido.
```json
{
    "model_dir": "~/.config/nono/model",
    "key_world": "pedro",
    "commands": [
        {
            "name": "brave",
            "need_confirmation": true,
            "run": "brave-browser",
            "phrases": [
                "ejecutar navegador",
                "abrir navegador"
            ]
        }
    ]
}
```
**model_dir:** Dirección absoluta del modelo vosk
**key_world:** Palabra clave para disparar los comandos
**phrases:** Son las frases que se debe decir después de la palabra especificada en *key_world* y es la que va a disparar el comando, entre más clara y diferente de los demás mejor.
**need_confirmation:** Es para los comandos que deben ser verificados para su ejecución con si o no.

Existen algunas palabras que los modelos no tienen y las ignoran. 
Falta trabajar en mostrar estas palabras al usuario y/o agregarlas si es posible.

## Agregar como servicio de Linux
1. Cambiar el directorio donde se encuentra el script en el fichero `configs/nono.service` linea `WorkingDirectory`.
2. Copiar fichero a la carpeta de `systemd`
```shell
mkdir -p ~/.config/systemd/user/
cp configs/nono.service ~/.config/systemd/user/nono.service
```

3. Cargar la nueva configuración
```shell
systemctl --user daemon-reload
```

4. Activar e iniciar el servicio 
```shell
systemctl --user enable nono
systemctl --user start nono
```

5. Reiniciar el servicio
```shell
systemctl --user restart nono
```

Ver estado del servicio y logs
```shell
systemctl --user status nono
journalctl -u nono
```

Como eliminarlo el servicio
```shell
systemctl --user stop nono
systemctl --user disable nono
rm ~/.config/systemd/user/nono.service
```

## Como contribuir
Para contribuir subir un [Merger Request](https://gitlab.com/ruby232/nono/-/merge_requests) o agregar una [issue](https://gitlab.com/ruby232/nono/-/issues).


## Todo
- Agregar reconocimiento de speaker - Ver que va este ejemplo https://github.com/alphacep/vosk-api/blob/master/python/example/test_speaker.py
- Usar otra tecnologia para el reconocimiento de voz y que sea configurable
- Probarlo en wondows (yo no )
- Obtener el listado de comando disponible
- Pasar los logs para otra carpeta
- Obtener listado de palabras ignoradas
- Agregar comandos con argumentos
- Agregar palabras al modelo
- Entrenar modelo con mi voz
- Hacer una interfaz gráfica

## Done
- Escribir documentación
- Hacer que los comandos sean independientes
- Mejorar el sistema para comprar la comparación de frases
- Agregar como servicio de Linux
- Agregar comandos con confirmación
- Escribir artículo