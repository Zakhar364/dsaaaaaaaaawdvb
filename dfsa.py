# Telegram-бот для мониторинга системы 🖥️

Простой Telegram-бот на Python, который позволяет удаленно отслеживать состояние сервера или персонального компьютера в реальном времени.

## Описание

Бот собирает основные системные метрики (загрузка процессора, оперативной памяти, свободное место на диске и т.д.) с помощью библиотеки `psutil` и отправляет их пользователю по команде `/status`.

## Исходный код

```python
import os
import platform
import time
import psutil
import telebot

# Инициализация бота
bot = telebot.TeleBot("YOUR_BOT_TOKEN")
start_time = time.time()

def get_cpu_load():
    return f"📊 Загрузка CPU: {psutil.cpu_percent()}%"

def get_ram_usage():
    ram = psutil.virtual_memory()
    return f"💾 Использование RAM: {ram.percent}%"

def get_disk_space():
    disk = psutil.disk_usage("/")
    return f"💽 Свободно на диске: {disk.free // (2**30)} ГБ"

def get_server_uptime():
    uptime = int(time.time() - start_time)
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"⏱️ Время работы бота: {hours}ч {minutes}м {seconds}с"

def get_process_count():
    return f"⚙️ Активных процессов: {len(psutil.pids())}"

def get_network_traffic():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent // (2**20)
    recv = counters.bytes_recv // (2**20)
    return f"🌐 Трафик (Отправлено/Принято): {sent} МБ / {recv} МБ"

def get_os_info():
    return f"🐧 ОС: {platform.system()} {platform.release()}"

def get_system_status():
    metrics = [
        get_os_info(),
        get_cpu_load(),
        get_ram_usage(),
        get_disk_space(),
        get_process_count(),
        get_network_traffic(),
        get_server_uptime(),
    ]
    return "\n".join(metrics)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чтобы проверить параметры системы, отправь команду /status")

@bot.message_handler(commands=["status"])
def send_status(message):
    bot.reply_to(message, get_system_status())

if __name__ == "__main__":
    print("Бот успешно запущен и готов к работе...")
    bot.infinity_polling()
```

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd имя_репозитория
   ```

2. **Установите зависимости:**
   ```bash
   pip install pyTelegramBotAPI psutil
   ```

3. **Настройка:**
   * Замените `"YOUR_BOT_TOKEN"` в коде на токен вашего бота, полученный от [@BotFather](https://t.me).

4. **Запуск:**
   ```bash
   python main.py
   ```

## Доступные команды

* `/start` — Приветственное сообщение и инструкция.
* `/status` — Получить текущую сводку о состоянии системы.



