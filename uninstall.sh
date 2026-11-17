#!/usr/bin/env bash

# Скрипт удаления расширения VS Code для Nautilus

EXT_FILE="$HOME/.local/share/nautilus-python/extensions/code-nautilus.py"

echo "🗑️ Удаление расширения VS Code для Nautilus..."

if [ -f "$EXT_FILE" ]; then
    rm -f "$EXT_FILE"
    echo "🔄 Перезапускаем Nautilus..."
    nautilus -q || true
    echo "✅ Расширение успешно удалено."
else
    echo "ℹ️ Расширение не найдено (уже удалено)."
fi
