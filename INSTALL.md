# 📥 INSTALLATION — PwnedPasswordsDownloader

Diese Anleitung richtet sich an alle, die das Projekt auf einem Raspberry Pi (oder Linux-System) lokal betreiben wollen – vollständig offline und datenschutzfreundlich.

---

## 🧰 Voraussetzungen

- Docker & Docker Compose installiert (z. B. via `apt`)
- Raspberry Pi mit Internetzugang für den Erst-Download
- Python-Kenntnisse **nicht notwendig**

---

## 📦 Installation in 3 Schritten

```bash
git clone https://github.com/HalloWelt42/PwnedPasswordsDownloader.git
cd PwnedPasswordsDownloader
./install.sh
```

---

## ⚙️ Was passiert beim Installieren?

1. Docker-Container werden gebaut
2. Die Passwort-Hashes (1 Mio. Dateien) werden heruntergeladen
3. Der Webservice zur Passwortprüfung wird dauerhaft gestartet

📍 Die heruntergeladenen Dateien landen im Ordner:

```
./hashes/
```

(automatisch erstellt, lokal sichtbar)

---

## 🌐 Zugriff

Öffne im Browser:

```
http://<deine-pi-ip>:5001
```

Dort kannst du ein Passwort testen — **lokal, anonym und sicher.**

---

## 🔍 Nützliche Befehle

| Aktion              | Befehl                                 |
|---------------------|----------------------------------------|
| Webservice-Log      | `docker compose logs -f web`           |
| Neu starten         | `docker compose up -d`                 |
| Alles stoppen       | `docker compose down`                  |
| Hashdateien zählen  | `ls hashes | wc -l`                    |

---

## 🧼 Optional: `.gitignore` ergänzen

Damit du nicht versehentlich 1 Mio. Dateien pusht:

```
hashes/
```

---

## 🧠 Hinweis

Der erste Download dauert **lange** (>1 Stunde). Danach bleiben alle Daten lokal erhalten – kein erneuter Download nötig.
