# 🔐 PwnedPasswordsDownloader

Ein datenschutzfreundlicher Offline-Dienst zum Prüfen, ob Passwörter in bekannten Datenlecks auftauchen – **vollständig lokal, ohne das Passwort zu übertragen.**

## 🚀 Funktionen

- Lädt die vollständige PwnedPasswords-Datenbank herunter
- Lokaler Webservice zur sicheren Passwortprüfung (Flask)
- Kein Cloud-Zugriff oder API-Versand von Passwörtern
- Raspberry-Pi-kompatibel, optimiert für Selfhosting
- Komplett via Docker betreibbar

## 📦 Projektüberblick

```text
main.py          # Downloader-Skript (lädt Hashdaten)
server.py        # Flask-Service für Passwortprüfung
Dockerfile       # Multi-Stage Build für Downloader und Webservice
docker-compose.yml
install.sh       # Einfache Installation mit Fortschrittsanzeige
hashes/          # (wird automatisch erzeugt, enthält die Datenbank)
```

## 📥 Installation

➡️ Siehe [INSTALL.md](INSTALL.md) für eine vollständige Schritt-für-Schritt-Anleitung zur Einrichtung.

## 🌐 Nutzung

Nach der Installation erreichst du den Passwortprüf-Service über:

```
http://<dein-pi-ip>:5001
```

## 🛡 Datenschutz

Das eingegebene Passwort wird **nicht übertragen** und **ausschließlich lokal** geprüft.

## 📜 Lizenz

MIT License — nutzbar, aber beachte die Datenquelle [haveibeenpwned.com](https://haveibeenpwned.com/Passwords)
