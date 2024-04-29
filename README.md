# Nono
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](README.es.md)

It is a customizable offline voice assistant. 
The goal of this project is to automate some processes using the voice without sending my data to an external server and 
not consume a lot of resources.

For speech recognition, we use [Vosk](https://alphacephei.com/vosk/).

## Install 
### Installing dependencies
```shell
sudo apt install espeak # To use pyttsx3
pip install -r requirements. txt 
```

### Descargar modelo 
1. download the [model from vosk page](https://alphacephei.com/vosk/models).
The small ones consume about 180 of RAM and the big ones about 4 of RAM.

2. Unzip the model in the `~/.config/nono/model` folder, without subfolders, as follows.
```bash
├── ~/.config/nono/model
│   ├── am
│   ├── conf
│   ├── graph
│   ├── ivector
```

3. If you want to move it to another location, see [Configure](## Configure).

## Configure
Create a json file in `~/.config/nono/config.json` with the following content.
```json
{
    "model_dir": "~/.config/nono/model",
    "key_world": "wendy",
    "commands": [
        {
            "name": "brave",
            "need_confirmation": true,
            "run": "brave-browser",
            "phrases": [
                "run browser",
                "open browser"
            ]
        }
    ]
}
```
**model_dir:** Absolute address of vosk model
**key_world:** Keyword to trigger the commands
**phrases:** These are the phrases that must be said after the word specified in *key_world* and is the one that will trigger the command, the clearer and different from the others the better.
**Needed_confirmation:** It is for the commands that must be verified for its execution with yes or no.

There are some words that the models do not have and ignore them. 
There is still work to be done to show these words to the user and/or add them if possible.

## Add as Linux service
1. Change the directory where the script is located in the `configs/nono.service` file to the `WorkingDirectory` line.
2. Copy file to `systemd` folder.

```shell
mkdir -p ~/.config/systemd/user/
cp configs/nono.service ~/.config/systemd/user/nono.service
```

3. Load the new configuration
```shell
systemctl --user daemon-reload
```

4. Activate and start the service 
```shell
systemctl --user enable nono
systemctl --user start nono
```

5. Restart the service
```shell
systemctl --user restart nono
```

See service status
```shell
systemctl --user status nono
```

How to delete the service
```shell
systemctl --user stop nono
systemctl --user disable nono
rm ~/.config/systemd/user/nono.service
```

## How to contribute
To contribute, upload a [Merger Request](https://gitlab.com/ruby232/nono/-/merge_requests) or add an [issue](https://gitlab.com/ruby232/nono/-/issues).


## Todo
- Add speaker recognition - See what this example is about https://github.com/alphacep/vosk-api/blob/master/python/example/test_speaker.py
- Get the list of available commands

- Pass the logs to another folder
- Get list of ignored words
- Add commands with arguments
- Add words to the model
- Show words ignored by the model
- Train model with my voice
- Make a graphical interface



