# KeyboardSounds V1.0.4
[Releases](https://github.com/GDTMG232/KeyboardSounds/releases) , [V1.0.4 Notizen](#patch-notizen-für-v104) , [TMG's Discord-Server](https://discord.com/invite/QtXPH9SVzV)

[In English](https://github.com/GDTMG232/KeyboardSounds/blob/main/README.md), [Im Deutsch](https://github.com/GDTMG232/KeyboardSounds/blob/main/READMEs/LANGUAGES/README-DE.md), [В Русский](https://github.com/GDTMG232/KeyboardSounds/blob/main/READMEs/LANGUAGES/README-DE.md)

## Installation

> [!Note]
> Diese Installation ist für Windows. Wenn Sie nicht wissen, wie Sie diese Module/Bibliotheken auf einem UNIX-basierten System installieren, gehen Sie bitte zu [README-UNIX.md](https://github.com/GDTMG232/KeyboardSounds/blob/main/READMEs/README-UNIX.md)

Laden Sie Python [hier herunter](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe) (Stellen Sie sicher, dass Sie PIP hinzufügen und Python auch zum PATH hinzufügen)

Öffnen Sie die Datei `Install Requirements.bat`, um die erforderlichen Abhängigkeiten zu installieren, damit die Datei `__main__.py` ordnungsgemäß funktioniert

## So verwenden Sie dieses Programm

Führen Sie einfach die Datei `__main__.py` mit Python aus

Sie können Ordner und Ihre eigenen Sounds verwenden, wenn Sie möchten, zum Beispiel:
```
KeyboardSounds/
└── Sounds/
    └── IhrSoundsSet/
        ├── default.mp3
        ├── special.mp3
        ├── space.mp3
        └── backspace.mp3
```

und in der Datei `Sounds.json` können Sie einen Schlüssel zum JSON hinzufügen.

```json
{
    "Set": "YourSoundSet",
    "..." : [
        "...",
    ],
    "IhrSoundsSet" : {
        "default": "default.mp3",
        "special": "special.mp3", 
        "space": "space.mp3",
        "backspace": "backspace.mp3"
    }
}
```

Sie können auch ändern, welche Tasten als besonders oder Backspace betrachtet werden und so weiter in der Datei `YourKeys.py`

und nein, ich mache `YourKeys.py` nicht zu einer JSON-Datei, ich kann nicht gefragt werden 😭

## Patch-Notizen für V1.0.4

Eine neue Funktion hinzugefügt In Sounds.json können Sie einen `"all"`-Schlüssel haben, sodass Sie nicht alles auf dieselbe Datei setzen müssen.

Laden Sie V1.0.4 [hier herunter](https://github.com/GDTMG232/KeyboardSounds/releases/tag/v1.0.4)
