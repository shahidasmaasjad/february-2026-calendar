import requests
import xml.etree.ElementTree as ET
import json

SITEMAP_URL = "https://february2026calendarideas.online/sitemap.xml"
INDEXNOW_API = "https://api.indexnow.org/indexnow"

HOST = "february2026calendarideas.online"
API_KEY = "3f83cbba186547b3891f197aa59652fd"
KEY_LOCATION = f"https://{HOST}/{API_KEY}.txt"

print("Fetching sitemap...")
resp = requests.get(SITEMAP_URL, timeout=30)
resp.raise_for_status()

root = ET.fromstring(resp.text)
ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

urls = []
for url in root.findall("ns:url", ns):
    loc = url.find("ns:loc", ns)
    if loc is not None:
        urls.append(loc.text.strip())

print(f"Found {len(urls)} URLs")

payload = {
    "host": HOST,
    "key": API_KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": urls
}

response = requests.post(
    INDEXNOW_API,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload),
    timeout=30
)

print("IndexNow status:", response.status_code)
print("IndexNow response:", response.text)
