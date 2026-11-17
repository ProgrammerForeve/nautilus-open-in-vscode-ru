#!/usr/bin/env bash

# Скрипт установки расширения VS Code для Nautilus

set -e

EXT_DIR="$HOME/.local/share/nautilus-python/extensions"
EXT_FILE="$EXT_DIR/code-nautilus.py"
RAW_URL="https://github.com/ProgrammerForeve/nautilus-open-in-vscode-ru/blob/master/code-nautilus.py"

echo "🔷 Установка расширения VS Code для Nautilus..."

# Проверка и установка пакета python3-nautilus
if ! dpkg -s python3-nautilus >/dev/null 2>&1; then
    echo "📦 Устанавливаем пакет python3-nautilus (потребуется пароль sudo)..."
    sudo apt-get update -qq
    sudo apt-get install -y python3-nautilus
fi

# Создание директории для расширений
mkdir -p "$EXT_DIR"

# Скачивание скрипта или копирование локального файла
if [ -f "./code-nautilus.py" ]; then
    echo "📂 Копируем локальный файл расширения..."
    cp "./code-nautilus.py" "$EXT_FILE"
else
    echo "🌐 Загружаем расширение с GitHub..."
    wget -qO "$EXT_FILE" "$RAW_URL"
fi

# Перезапуск Nautilus
echo "🔄 Перезапускаем файловый менеджер Nautilus..."
nautilus -q || true

echo "✅ Установка завершена! Нажмите правой кнопкой по любой папке для проверки."
