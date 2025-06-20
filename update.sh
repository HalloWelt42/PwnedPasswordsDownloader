#!/bin/bash
set -e

echo "🔄 Update läuft..."

cd "$(dirname "$0")"
git pull

echo "🔧 Baue aktualisierte Container..."
docker compose build

echo "🚀 Starte Webservice neu..."
docker compose up -d web

echo "✅ Update abgeschlossen!"
