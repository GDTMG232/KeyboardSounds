# KeyboardSounds V1.0.4
[Релизы](https://github.com/GDTMG232/KeyboardSounds/releases) , [Примечания к V1.0.4](#примечания-к-патчу-для-v104) , [Дискорд-сервер TMG](https://discord.com/invite/QtXPH9SVzV) 

[In English](https://github.com/GDTMG232/KeyboardSounds/blob/main/README.md), [Im Deutsch](https://github.com/GDTMG232/KeyboardSounds/blob/main/READMEs/LANGUAGES/README-DE.md), [В Русский](https://github.com/GDTMG232/KeyboardSounds/blob/main/READMEs/LANGUAGES/README-DE.md)

## Installation

> [!Note]
> Эта установка предназначена для Windows. Если вы не знаете, как установить эти модули/библиотеки на системе на базе UNIX, пожалуйста, перейдите к [README-UNIX.md](https://github.com/GDTMG232/KeyboardSounds/blob/main/README-UNIX.md)

Скачайте и установите Python [отсюда](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe) (Убедитесь, что добавили PIP и также добавили Python в PATH)

Откройте файл `Install Requirements.bat`, чтобы установить необходимые зависимости для правильной работы файла `__main__.py`

## Как использовать эту программу

Просто запустите файл `__main__.py` с помощью Python

Вы можете использовать папки и свои собственные звуки, если хотите, например:
```
KeyboardSounds/
└── Sounds/
    └── ВашНаборЗвуков/
        ├── default.mp3
        ├── special.mp3
        ├── space.mp3
        └── backspace.mp3
```

и в файле `Sounds.json` вы можете добавить ключ к JSON.

```json
{
    "Set": "YourSoundSet",
    "..." : [
        "...",
    ],
    "ВашНаборЗвуков" : {
        "default": "default.mp3",
        "special": "special.mp3", 
        "space": "space.mp3",
        "backspace": "backspace.mp3"
    }
}
```

Вы также можете изменить, какие клавиши считаются специальными или Backspace и так далее в файле `YourKeys.py`

и нет, я не собираюсь делать `YourKeys.py` файлом JSON, мне не хочется 😭

## Примечания к патчу для V1.0.4

Добавлена новая функция В Sounds.json вы можете иметь ключ `"all"`, чтобы не устанавливать всё на один и тот же файл.

Скачайте V1.0.4 [здесь](https://github.com/GDTMG232/KeyboardSounds/releases/tag/v1.0.4)