# KI-Luftqualitaetsvorhersage (Echtzeit-API Integration)

Dieses Projekt ist eine End-to-End-Anwendung fuer maschinelles Lernen, die die Luftqualitaet fuer jede Stadt weltweit in Echtzeit vorhersagt. Das Modell wurde mit realen Umweltdaten trainiert (Random Forest) und in Version 2.0 mit der OpenWeatherMap-API verknuepft, um Live-Schadstoffdaten abzurufen und zu analysieren.

## Neue Features in Version 2.0
- Globale Echtzeit-Daten: Direkte Integration der OpenWeatherMap API (Geocoding und Air Pollution).
- Automatisierte Datenpipeline: Der Benutzer gibt nur den Stadtnamen ein. Die App konvertiert diesen automatisch in Koordinaten und ruft die Live-Sensordaten (PM2.5, NO2, CO, SO2, O3) ab.
- Data Transformation und Preprocessing: Automatische Einheitenumrechnung (z. B. CO von µg/m³ in mg/m³), um die API-Live-Daten exakt an die Trainingsstruktur des KI-Modells anzupassen.
- Robustes Error Handling: Abfangen von Fehlern bei ungueltigen Stadtnamen oder leeren Eingaben zur Vermeidung von App-Abstuerzen.
- Security: Sichere Verwaltung des API-Keys durch Streamlit Secrets (secrets.toml).

## Verwendete Technologien
- Python (Kernsprache)
- Pandas (Datenmanipulation und -strukturierung)
- Scikit-Learn (Machine-Learning-Modell: Random Forest Classifier)
- Requests (API-Kommunikation und JSON-Parsing)
- Streamlit (Interaktive Web-Benutzeroberflaeche und Secrets Management)
- Joblib (Serialisierung des trainierten Modells)

## Projektstruktur
- data/: Enthaelt die historischen Rohdaten fuer das Training.
- models/: Speichert das fertig trainierte Modell (air_quality_model_v1.pkl).
- train.py: Das Skript zur Datenvorbereitung und zum Modelltraining.
- app.py: Die Hauptdatei fuer die Webanwendung (beinhaltet die API-Pipeline und UI).
- requirements.txt: Liste der benoetigten Python-Bibliotheken.

## Installation und lokale Nutzung

Um dieses Projekt lokal auf Ihrem Rechner auszufuehren, folgen Sie diesen Schritten:

1. Repository klonen:
   git clone https://github.com/IhrBenutzername/Air-Quality-PY.git
   cd Air-Quality-PY

2. Abhaengigkeiten installieren:
   pip install -r requirements.txt

3. API-Key konfigurieren (Secrets Management):
   - Erstellen Sie einen versteckten Ordner namens .streamlit im Hauptverzeichnis.
   - Erstellen Sie darin eine Datei namens secrets.toml.
   - Fuegen Sie Ihren OpenWeatherMap API-Key wie folgt hinzu:
     API_KEY = "Ihr_eigener_API_Schluessel_hier"

4. App starten:
   streamlit run app.py

## Ueber das Modell und die Architektur
Das System analysiert fuenf Hauptschadstoffe: PM2.5, NO2, CO, SO2 und O3. Waehrend Version 1.0 manuelle Sensoreingaben erforderte, agiert Version 2.0 als vollstaendige Pipeline. Der Random Forest Algorithmus wurde gewaehlt, da er eine hohe Genauigkeit und Robustheit gegenueber komplexen und nicht-linearen Umweltdaten bietet. Das Modell klassifiziert die aktuelle Schadstoffbelastung direkt in verstaendliche Gesundheitskategorien (z. B. Good, Satisfactory, Moderate, Poor).