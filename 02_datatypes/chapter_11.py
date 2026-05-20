from datetime import datetime, timezone
from zoneinfo import ZoneInfo

brewing_time = datetime.now(timezone.utc)
print(f"Brewing time: {brewing_time}")

brewing_time_rome = brewing_time.astimezone(ZoneInfo("Europe/Rome"))
print(f"Brewing time in Rome: {brewing_time_rome}")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
print(f"Chai profile: {chaiProfile(flavor='spicy', aroma='fragrant')}")