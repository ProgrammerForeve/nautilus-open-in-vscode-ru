# Расширение VS Code для файлового менеджера Nautilus
#
# Поместите этот файл в ~/.local/share/nautilus-python/extensions/,
# убедитесь, что установлен пакет python3-nautilus, и перезапустите Nautilus.

import os
import subprocess
from gi.repository import GObject, Nautilus

# Команда запуска VS Code
VSCODE_CMD = 'code'

# Название приложения в контекстном меню
VSCODE_NAME = 'VS Code'

# Всегда открывать в новом окне (True / False)
ALWAYS_NEW_WINDOW = False


class VSCodeExtension(GObject.GObject, Nautilus.MenuProvider):
    """Добавляет пункт открытия файлов и папок через VS Code в меню Nautilus."""

    def launch_vscode(self, menu, files):
        paths = []
        open_new_window = ALWAYS_NEW_WINDOW

        for file in files:
            location = file.get_location()
            if not location:
                continue

            filepath = location.get_path()
            if not filepath:
                continue

            paths.append(filepath)

            # Если среди выбранных элементов есть папка, открываем новое окно
            if os.path.isdir(filepath):
                open_new_window = True

        if not paths:
            return

        cmd = [VSCODE_CMD]
        if open_new_window:
            cmd.append('--new-window')
        cmd.extend(paths)

        # Безопасный фоновый запуск без использования shell=True
        subprocess.Popen(cmd, start_new_session=True)

    def get_file_items(self, *args):
        """Пункт меню при клике правой кнопкой по файлу или папке."""
        files = args[-1]
        if not files:
            return []

        item = Nautilus.MenuItem(
            name='VSCodeOpen',
            label=f'🔷 Открыть в {VSCODE_NAME}',
            tip=f'Открыть выбранные элементы в {VSCODE_NAME}'
        )
        item.connect('activate', self.launch_vscode, files)
        return [item]

    def get_background_items(self, *args):
        """Пункт меню при клике по пустому месту внутри открытой папки."""
        current_folder = args[-1]
        if not current_folder:
            return []

        item = Nautilus.MenuItem(
            name='VSCodeOpenBackground',
            label=f'🔷 Открыть в {VSCODE_NAME}',
            tip=f'Открыть текущую директорию в {VSCODE_NAME}'
        )
        item.connect('activate', self.launch_vscode, [current_folder])
        return [item]
