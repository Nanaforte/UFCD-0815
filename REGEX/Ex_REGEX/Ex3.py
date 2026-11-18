import json
import re

with open("dados.json", "r", encoding="utf-8") as d:
    dados = json.load(d)
    
print("extracao de dominios dos sites")

# Padrão regex
dominio_regex = r"https?://(?:www\.)?([^/]+)"

for person in dados:
    site = person["site"]
    
    match_url = re.match(dominio_regex, site)
    
    if match_url:
        dominio = match_url.group(1)
        print(f"site original: {site} -> dominio: {dominio}")