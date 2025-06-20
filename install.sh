#!/bin/bash

set -e  # Script bei Fehlern sofort abbrechen

echo "🔧 [1/4] Baue Docker-Container (kann beim ersten Mal etwas dauern)..."
docker compose build

echo ""
echo "⬇️ [2/4] Starte einmaligen Download der Passwort-Hashes..."
docker compose run --rm downloader

echo ""
echo "🚀 [3/4] Starte lokalen Passwortcheck-Service im Hintergrund..."
docker compose up -d web

echo ""
echo "✅ [4/4] Installation abgeschlossen!"

# IP-Adresse ermitteln
IP=$(hostname -I | awk '{print $1}')

echo ""
echo "🌐 Der Webservice ist jetzt erreichbar unter:"
echo "   http://$IP:5001"
echo ""
echo "📁 Die Hash-Dateien liegen im Verzeichnis: ./hashes"
echo "   Aktuelle Dateianzahl: $(ls hashes | wc -l) / 1048576"
echo ""
echo "📡 Logs live ansehen mit:"
echo "   docker compose logs -f web"
echo ""
echo "🛑 Service beenden:"
echo "   docker compose down"
echo ""
echo "💡 Weitere Informationen findest du in der README.md"