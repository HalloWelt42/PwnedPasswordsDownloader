# 🔐 PwnedPasswordsDownloader & Checker

Dieses Projekt lädt die vollständige Datenbank geleakter Passwörter von [haveibeenpwned.com](https://haveibeenpwned.com) herunter – lokal, sicher und offline nutzbar. Anschließend kannst du deine Passwörter gegen die Hashes prüfen – **ohne sie ins Internet zu senden**.

---

## 📦 Funktionen

✅ Vollständiger Download der HIBP-Passwort-Hashes  
✅ Speicherung im Format `<PREFIX>.txt` (nach SHA-1-Prefix)  
✅ Lokaler Webservice zur Passwortprüfung  
✅ Kein Passwort verlässt deinen Rechner  
✅ Ideal für Raspberry Pi, Server oder Desktop

---

## 🛠️ Installation

### 🔁 1. Repository klonen

```bash
git clone https://github.com/HalloWelt42/PwnedPasswordsDownloader.git
cd PwnedPasswordsDownloader
```
🐍 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```
(z.B. Flask, tqdm, requests)

⬇️ Hash-Datenbank herunterladen
Lade die SHA‑1‑Präfix-Listen (k-Anonymitäts-Prinzip) herunter:

```bash
python3 main.py
```

💡 Das erzeugt über 1 Mio. Textdateien (je 5-stelliger Hash-Prefix) im Verzeichnis hashes/.

🚀 Lokaler Web-Service starten
Starte den Passwort-Check-Service:

```bash
python3 server.py
```
Besuche danach http://localhost:5001 in deinem Browser.

## 🔐 Gib ein Passwort ein → Du bekommst zurück:

```json
{
  "found": true,
  "count": 9812
}
```

## 🖥️ Beispiel (API-Endpunkt)
Request
```http
POST /check HTTP/1.1
Content-Type: application/json

{
  "password": "123456"
}
```

Response
```json
{
  "found": true,
  "count": 2309812
}
```

## 📁 Projektstruktur
```text
.
├── hashes/                  # Hier landen die heruntergeladenen Hash-Präfix-Dateien
├── main.py                  # Downloader für alle k-Anonymitäts-Präfixe
├── server.py                # Flask-Webservice zur lokalen Passwortprüfung
├── requirements.txt         # Python-Abhängigkeiten
└── README.md                # Diese Anleitung
```

## 💡 Hinweise
Alle Daten stammen von Troy Hunt (HIBP): https://haveibeenpwned.com/Passwords
Dieses Projekt ist nicht kommerziell und dient der lokalen, datenschutzfreundlichen Nutzung
Unterstützt Offline-Validierung ohne Risiko für dein Passwort


## 📜 Lizenz
MIT License – frei nutzbar, aber bitte respektiere die Bedingungen von haveibeenpwned.com


