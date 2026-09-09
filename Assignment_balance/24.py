#Calculate number of days between two given dates
from datetime import date
d1 = date(2026, 8, 1)
d2 = date(2026, 8, 15)
print("Number of days:", (d2 - d1).days)