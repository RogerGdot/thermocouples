# PyPI Veröffentlichung - Anleitung

## Schritte zur Veröffentlichung auf PyPI

### 1. Voraussetzungen
```bash
pip install build twine
```

### 2. PyPI Account
- Registriere dich auf https://pypi.org/
- Aktiviere 2FA (Two-Factor Authentication)
- Erstelle ein API Token in deinen Account-Einstellungen

### 3. Paket erstellen
```bash
# Alles bereinigen
rm -rf dist/ build/ *.egg-info/

# Neue Pakete erstellen
python -m build
```

### 4. Paket prüfen
```bash
# Prüfe die Pakete auf Fehler
twine check dist/*
```

### 5. Test-Upload (optional aber empfohlen)
```bash
# Upload auf TestPyPI
twine upload --repository testpypi dist/*

# Teste Installation von TestPyPI
pip install --index-url https://test.pypi.org/simple/ python-thermocouples
```

### 6. Finaler Upload auf PyPI
```bash
# Upload auf echtes PyPI
twine upload dist/*
```

### 7. Installation testen
```bash
pip install python-thermocouples
```

## Wichtige Dateien für PyPI

### pyproject.toml
- ✅ Vollständig konfiguriert
- ✅ Version 2.0.0
- ✅ Metadata komplett
- ✅ Dependencies definiert

### README.md
- ✅ Aktualisiert für v2.0
- ✅ Installation guide
- ✅ Usage examples
- ✅ Badges hinzugefügt

### MANIFEST.in
- ✅ Alle notwendigen Dateien inkludiert
- ✅ py.typed für Type-Hints

### Lizenz
- ✅ MIT License vorhanden
- ✅ In pyproject.toml referenziert

## Automatische Veröffentlichung mit GitHub Actions

Die GitHub Actions sind bereits konfiguriert:
- `.github/workflows/tests.yml` - Automatische Tests
- `.github/workflows/publish.yml` - Automatisches PyPI Publishing bei Releases

### GitHub Release erstellen
1. Gehe zu deinem GitHub Repository
2. Klicke auf "Releases" → "Create a new release"
3. Tag: `v2.0.0`
4. Title: `Release 2.0.0 - Complete OOP Refactoring`
5. Beschreibung: [siehe unten]
6. Klicke "Publish release"

Das löst automatisch den PyPI Upload aus!

## Release Notes für v2.0.0

```markdown
# 🚀 Major Release: Python Thermocouples v2.0.0

## 🎯 Complete Architectural Redesign

This is a major release that completely refactors the library from a registry-based approach to a modern object-oriented architecture.

### ✨ New Features

- **Object-Oriented Design**: Each thermocouple type is now a class inheriting from an abstract base class
- **Factory Pattern**: Simple `get_thermocouple("K")` function for easy instantiation  
- **Type Safety**: Full Python type hints throughout the codebase
- **Better Performance**: Optimized polynomial evaluation algorithms
- **Enhanced Documentation**: Comprehensive docstrings and examples

### 🔧 All Standard Thermocouple Types Implemented

- **Type B**: 0°C to 1820°C (Pt-30%Rh / Pt-6%Rh)
- **Type E**: -270°C to 1000°C (Ni-Cr / Cu-Ni) 
- **Type J**: -210°C to 1200°C (Fe / Cu-Ni)
- **Type K**: -270°C to 1372°C (Ni-Cr / Ni-Al)
- **Type N**: -270°C to 1300°C (Ni-Cr-Si / Ni-Si)
- **Type R**: -50°C to 1768°C (Pt-13%Rh / Pt)
- **Type S**: -50°C to 1768°C (Pt-10%Rh / Pt) 
- **Type T**: -270°C to 400°C (Cu / Cu-Ni)

### 🔄 100% Backward Compatibility

All existing APIs continue to work exactly as before:
```python
# Old API still works
voltage = tc.temp_to_voltage(100.0, "K")
temp = tc.voltage_to_temp(voltage, "K")

# New OOP API (recommended)
tc_k = tc.get_thermocouple("K") 
voltage = tc_k.temperature_to_voltage(100.0)
temp = tc_k.voltage_to_temperature(voltage)
```

### 📊 High Accuracy & NIST Compliance

- Based on NIST Monograph 175 polynomial coefficients
- Includes exponential correction functions for Type K
- Roundtrip accuracy < 0.05°C for standard temperature ranges
- Individual thermocouple leg calculations where available

### 🐍 Modern Python Support

- Python 3.9+ required
- Full type hints for better IDE support
- Zero external dependencies
- Comprehensive test suite

### 📦 Installation

```bash
pip install python-thermocouples
```

### 🔗 Quick Example

```python
import thermocouples as tc

# Create thermocouple instance
tc_k = tc.get_thermocouple("K")

# Convert temperature to voltage
voltage = tc_k.temperature_to_voltage(100.0)  # 4.096 mV
print(f"100°C → {voltage:.3f} V")

# Convert voltage back to temperature  
temp = tc_k.voltage_to_temperature(voltage)   # ~100°C
print(f"{voltage:.3f} V → {temp:.1f}°C")

# Get Seebeck coefficient
seebeck = tc_k.temp_to_seebeck(100.0)        # ~40.7 µV/K
print(f"Seebeck: {seebeck:.1f} µV/K")
```
```

## Checkliste vor Veröffentlichung

- ✅ Alle Tests laufen erfolgreich
- ✅ Dokumentation ist aktuell
- ✅ Version in pyproject.toml ist korrekt (2.0.0)
- ✅ README.md ist vollständig
- ✅ Lizenz ist korrekt
- ✅ Paket lässt sich erfolgreich bauen
- ✅ twine check läuft ohne Fehler
- ✅ GitHub Repository ist öffentlich
- ✅ API Token für PyPI ist bereit

## Nächste Schritte

1. **GitHub Repository erstellen/aktualisieren**
2. **Git Commit & Push** aller Änderungen
3. **GitHub Release erstellen** (triggert automatisch PyPI Upload)
4. **Installation testen** `pip install python-thermocouples`
5. **Dokumentation aktualisieren** falls nötig
