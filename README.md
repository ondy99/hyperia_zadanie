# hyperia_zadanie
Script dokáže rozparsovať stránku https://www.prospektmaschine.de/hypermarkte/ a stiahnuť zoznam aktuálne platných letákov pre všetky reťazce v danej kategórií. Výstup sa uloží do súboru v JSON formáte.

Pozn.: Nevedel som určiť, čo má byť hodnota parsed_time, tak som do nej uložil rovnaký dátum ako valid_from, s časom 00\:00:00.

---

Pre nainštalovanie potrebných package-ov spustite v konzole command:
```
pip install requests beautifulsoup4
```

Spustenie scriptu:
```
python brochure_parser.py
```
