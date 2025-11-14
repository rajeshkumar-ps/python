from datetime import datetime, timezone, timedelta
print(datetime.now(timezone.utc).strftime('%d-%m-%Y %H:%M:%S')) # UTC time
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) # Local time
print((datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)).strftime('%d-%m-%Y %H:%M:%S')) # UTC+5:30 time