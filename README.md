# 🔐 PwnedPasswordsDownloader

Ein datenschutzfreundlicher Offline-Dienst zum Prüfen, ob Passwörter in bekannten Datenlecks auftauchen – **vollständig lokal, ohne das Passwort zu übertragen.**

## 🚀 Funktionen

* Lädt die vollständige PwnedPasswords-Datenbank herunter
* Lokaler Webservice zur sicheren Passwortprüfung (Flask)
* Kein Cloud-Zugriff oder API-Versand von Passwörtern
* Raspberry-Pi-kompatibel, optimiert für Selfhosting
* Swagger-Dokumentation automatisch integriert
* Moderne Benutzeroberfläche mit Darkmode und JavaScript (keine Drittanbieter)
* Komplett via Docker betreibbar

## 📆 Projektstruktur

```text
main.py          # Downloader-Skript (lädt Hashdaten)
server.py        # Flask-Service für Passwortprüfung + Swagger
Dockerfile       # Multi-Stage Build für Downloader und Webservice
docker-compose.yml
install.sh       # Einfache Installation mit Fortschrittsanzeige
templates/
  └─ index.html   # Moderne UI für Passwortprüfung
hashes/          # (wird automatisch erzeugt, enthält die Datenbank)
```

## 📅 Installation

➡️ Siehe [INSTALL.md](INSTALL.md) für eine vollständige Schritt-für-Schritt-Anleitung zur Einrichtung mit Docker.

## 🌐 Nutzung

Nach der Installation erreichst du den Passwortprüf-Service über:

```
http://<dein-pi-ip>:5001
```

Zusätzlich erreichst du die Swagger-API-Dokumentation hier:

```
http://<dein-pi-ip>:5001/apidocs
```

## 🛡 Datenschutz

Das eingegebene Passwort wird **nicht übertragen** und **ausschließlich lokal** gegen die Hash-Datenbank geprüft. Kein API-Call verlässt dein Netzwerk.

## 👍 Hinweise

* Die Passwortdatenbank besteht aus ca. **1 Million Dateien**
* Diese werden einmalig geladen (Download via `/range`-API von HIBP)
* Die Anwendung funktioniert **offline**, sobald die Daten vorliegen

## 📚 Quellen

* Daten: [haveibeenpwned.com](https://haveibeenpwned.com/Passwords)
* Swagger: [flasgger](https://github.com/flasgger/flasgger)

## 🔠 Lizenz

MIT License — frei nutzbar, bitte beachte die Herkunft der Hashdaten von HIBP.

---

⭐ Projekt auf GitHub:
[github.com/HalloWelt42/PwnedPasswordsDownloader](https://github.com/HalloWelt42/PwnedPasswordsDownloader)
