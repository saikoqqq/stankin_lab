import re
log_data = """2026-09-26 08:00:12 INFO  Connected to database at 10.0.0.5:5432
2026-09-26 08:01:33 WARN  Connection pool usage at 85 percent
2026-09-26 08:02:47 INFO  User 'admin' logged in from 192.168.1.10
2026-09-26 08:05:19 ERROR Failed to parse request body: invalid JSON
2026-09-26 08:05:20 INFO  Retrying request id=4423 in 500ms
2026-09-26 08:07:55 DEBUG Cache hit ratio: 0.92
2026-09-26 08:10:00 INFO  Scheduled job 'cleanup' started
2026-09-26 08:10:41 WARN  Disk usage on /var/log reached 90 percent
2026-09-26 08:12:03 ERROR Timeout while calling payment-service after 5000ms
2026-09-26 08:12:04 INFO  Fallback provider activated
2026-09-26 08:15:37 DEBUG GC pause: 42ms
2026-09-26 08:18:22 INFO  User 'maria' uploaded file report.pdf
2026-09-26 08:20:11 WARN  Deprecated API endpoint /v1/old called
2026-09-26 08:22:50 ERROR Unhandled exception in worker-3: NullPointerException
2026-09-26 08:22:51 INFO  Worker-3 restarted by supervisor
2026-09-26 08:25:14 DEBUG Heartbeat sent to cluster node 10.0.0.7
2026-09-26 08:30:00 INFO  Daily backup completed in 128 seconds
2026-09-26 08:31:45 ERROR Backup verification failed: checksum mismatch"""


r"""
ЗАДАНИЕ 1
Регулярка: r"\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+(ERROR|WARN)\s+(.*)"

Разбор:
1. \d{4}-\d{2}-\d{2}\s+  -> Игнорируем дату (4 цифры - 2 цифры - 2 цифры) и пробелы.
2. (\d{2}:\d{2}:\d{2})  -> Группа 1: Запоминаем ВРЕМЯ (чч:мм:сс).
3. (ERROR|WARN)         -> Группа 2: Ищем строго ERROR или WARN.
4. (.*)                 -> Группа 3: Запоминаем ВСЁ сообщение до конца строки.
"""

print("Задание 1: Строки ERROR и WARN")
pattern1 = r"\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+(ERROR|WARN)\s+(.*)"
for match in re.finditer(pattern1, log_data):
    time, level, msg = match.groups()
    print(f"{time} {level} {msg}")

r"""
ЗАДАНИЕ 2
Регулярка: r"\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.*\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b.*)"

Разбор:
1. \d{4}-\d{2}-\d{2}\s+                     -> Игнорируем дату и пробелы.
2. (\d{2}:\d{2}:\d{2})                     -> Группа 1: Запоминаем ВРЕМЯ.
3. ([A-Z]+)                                -> Группа 2: Запоминаем ЛЮБОЙ уровень (INFO, DEBUG и т.д.).
4. (.*\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b.*) -> Группа 3: Запоминаем сообщение, в котором есть IP-адрес 
                                               (4 числа от 1 до 3 цифр через точку).
"""
print("\nЗадание 2: Строки с IP-адресами")
pattern2 = r"\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.*\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b.*)"
for match in re.finditer(pattern2, log_data):
    time, level, msg = match.groups()
    print(f"{time} {level} {msg}")