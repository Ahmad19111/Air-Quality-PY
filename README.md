# Luftqualitätsvorhersage mit Machine Learning

Dieses Projekt ist eine End-to-End-Anwendung für maschinelles Lernen, die die Luftqualität basierend auf Sensordaten vorhersagt. Das Modell wurde mit realen Umweltdaten trainiert und verwendet einen Random Forest Klassifikator, um die Schadstoffbelastung in verschiedene Kategorien einzuteilen.

## Verwendete Technologien
- Python
- Pandas für die Datenbereinigung und -manipulation
- Scikit-Learn für das Training des Machine-Learning-Modells (Random Forest)
- Streamlit für die interaktive Web-Benutzeroberfläche
- Joblib für die Serialisierung des Modells

## Projektstruktur
- data/: Enthält die historischen Rohdaten für das Training.
- models/: Speichert das fertig trainierte Modell (air_quality_model_v1.pkl).
- train.py: Das Skript zur Datenvorbereitung, Behandlung fehlender Werte und zum Modelltraining.
- app.py: Die Hauptdatei für die Webanwendung.
- requirements.txt: Liste der benötigten Python-Bibliotheken.

## Installation und Nutzung

Um dieses Projekt lokal auf Ihrem Rechner auszuführen, folgen Sie diesen Schritten:

1. Klonen Sie dieses Repository auf Ihren lokalen Rechner.
2. Installieren Sie die erforderlichen Abhängigkeiten über das Terminal:
   pip install -r requirements.txt
3. Starten Sie die Streamlit-Anwendung:
   streamlit run app.py

## Über das Modell
Das Modell analysiert fünf Hauptschadstoffe: PM2.5, NO2, CO, SO2 und O3. Bei der Datenaufbereitung wurden fehlende Sensorwerte mit dem Median interpoliert, um die Robustheit des Modells gegenüber extremen Ausreißern zu gewährleisten. Durch die Wahl eines Random Forest Algorithmus wird eine hohe Genauigkeit bei der Klassifizierung der Luftqualität erreicht, selbst bei komplexen und unvollständigen realen Daten.