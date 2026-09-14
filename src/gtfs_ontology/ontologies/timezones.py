#%%
import re
import requests

url = "https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry"

registry = requests.get(url, timeout=30).text

subtags = re.findall(r"^Subtag:\s*([A-Za-z0-9]+)$", registry, re.MULTILINE)