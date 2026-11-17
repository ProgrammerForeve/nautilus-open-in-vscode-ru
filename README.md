# 🔷 Открыть в VS Code (Расширение для Nautilus)

Простое и оптимизированное расширение на Python для файлового менеджера **Nautilus** (Ubuntu 22.04 / 24.04+). Добавляет пункт **«🔷 Открыть в VS Code»** в контекстное меню папок и файлов.

*Форк оригинального проекта [harry-cpp/code-nautilus](https://github.com) с русской локализацией, безопасным запуском процессов и визуальным акцентом для GTK4.*

## ✨ Особенности
* **Визуальный акцент**: Использует синий ромб (`🔷`) в названии пункта, чтобы легко находить его в меню новых версий Nautilus (GTK4), где системные иконки отключены.
* **Безопасный запуск**: Корректно обрабатывает пути с пробелами, кириллицей и спецсимволами (без использования `shell=True`).
* **Умное открытие окон**: Автоматически открывает новое окно VS Code при выборе директории.

## 🚀 Быстрая установка

Выполните в терминале одну команду:

```bash
wget -qO- https://github.com/ProgrammerForeve/nautilus-open-in-vscode-ru/blob/master/install.sh | bash
```

## 🛠️ Ручная установка

1. Установите зависимость:
   ```bash
   sudo apt install python3-nautilus
   ```
2. Склонируйте репозиторий и запустите установщик:
   ```bash
   git clone https://github.com/ProgrammerForeve/nautilus-open-in-vscode-ru.git
   cd nautilus-open-in-vscode-ru
   bash install.sh
   ```

## 🗑️ Удаление

```bash
wget -qO- https://github.com/ProgrammerForeve/nautilus-open-in-vscode-ru/blob/master/uninstall.sh.sh | bash
```
