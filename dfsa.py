import os
import platform
import time
import psutil
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")
start_time = time.time()


def get_cpu_load():
    return f"📊 Загрузка CPU: {psutil.cpu_percent()}%"


def get_ram_usage():
    ram = psutil.virtual_memory()
    return f"🧠 Использование RAM: {ram.percent}%"


def get_disk_space():
    disk = psutil.disk_usage("/")
    return f"💽 Свободно на диске: {disk.free // (2**30)} ГБ"


def get_server_uptime():
    uptime = int(time.time() - start_time)
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"⏱ Время работы бота: {hours}ч {minutes}м {seconds}с"


def get_process_count():
    return f"🔢 Активных процессов: {len(psutil.pids())}"


def get_network_traffic():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent // (2**20)
    recv = counters.bytes_recv // (2**20)
    return f"🌐 Трафик (Отправлено/Принято): {sent} МБ / {recv} МБ"


def get_os_info():
    return f"💻 ОС: {platform.system()} {platform.release()}"


def get_boot_time():
    boot_timestamp = psutil.boot_time()
    boot_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_timestamp))
    return f"🚀 Время запуска системы: {boot_date}"


def get_system_status():
    metrics = [
        get_cpu_load(),
        get_ram_usage(),
        get_disk_space(),
        get_server_uptime(),
        get_process_count(),
        get_network_traffic(),
        get_os_info(),
        get_boot_time(),
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

