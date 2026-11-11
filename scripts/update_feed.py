import gzip
import os
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCE = 'https://storage.googleapis.com/adnabu-feeds/google/39d43722-358c-41c1-93ce-7a920853b5d9.xml.gz'
TARGET = Path('docs/catalogo.xml')
LIMIT = 150 * 1024 * 1024
req = urllib.request.Request(SOURCE, headers={'User-Agent': 'ABMedicalFeedSync/1.0'})
with urllib.request.urlopen(req, timeout=90) as response:
    data = response.read(LIMIT + 1)
if len(data) > LIMIT:
    raise RuntimeError('Feed compresso troppo grande')
xml = gzip.decompress(data)
if len(xml) > 400 * 1024 * 1024:
    raise RuntimeError('Feed XML troppo grande')
ET.fromstring(xml)
TARGET.parent.mkdir(parents=True, exist_ok=True)
fd, tmp = tempfile.mkstemp(dir=TARGET.parent, suffix='.tmp')
try:
    with os.fdopen(fd, 'wb') as f:
        f.write(xml)
    os.replace(tmp, TARGET)
finally:
    if os.path.exists(tmp):
        os.unlink(tmp)
print(f'XML valido: {len(xml)} byte')
