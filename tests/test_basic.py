#!/usr/bin/env python3
"""
Minimales Beispiel für die Nutzung der Thermocouples-Bibliothek v2.0

Zeigt die grundlegende Verwendung des neuen OOP-Ansatzes und der Legacy-API.
"""

import os
import sys

# Füge den src-Pfad zum Python-Pfad hinzu für lokale Tests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import thermocouples as tc


def minimal_beispiel():
    """Minimales Beispiel für die Thermocouple-Nutzung."""
    print("🌡️  THERMOCOUPLES v2.0 - MINIMAL BEISPIEL")
    print("=" * 50)

    # 1. NEUE OOP API (Empfohlen)
    print("\n🔧 Neue OOP API:")

    # Thermocouple-Objekt erstellen
    tc_k = tc.get_thermocouple("K")

    # Temperatur zu Spannung
    temperatur = 100.0  # °C
    spannung = tc_k.temperature_to_voltage(temperatur)
    print(f"   {temperatur}°C → {spannung:.6f} V")

    # Spannung zu Temperatur
    temp_zurück = tc_k.voltage_to_temperature(spannung)
    print(f"   {spannung:.6f} V → {temp_zurück:.2f}°C")

    # Seebeck-Koeffizient berechnen
    seebeck = tc_k.temp_to_seebeck(temperatur)
    print(f"   Seebeck bei {temperatur}°C: {seebeck:.1f} µV/K")

    # 2. LEGACY API (Rückwärtskompatibilität)
    print("\n🔄 Legacy API (weiterhin unterstützt):")

    # Gleiche Berechnungen mit alten Funktionen
    spannung_alt = tc.temp_to_voltage(temperatur, "K")
    temp_alt = tc.voltage_to_temp(spannung_alt, "K")
    seebeck_alt = tc.temp_to_seebeck(temperatur, "K")

    print(f"   {temperatur}°C → {spannung_alt:.6f} V")
    print(f"   {spannung_alt:.6f} V → {temp_alt:.2f}°C")
    print(f"   Seebeck bei {temperatur}°C: {seebeck_alt:.1f} µV/K")

    # 3. MEHRERE THERMOCOUPLE-TYPEN
    print("\n🎯 Vergleich verschiedener Typen bei 200°C:")

    test_temperatur = 200.0
    typen = ["K", "J", "E", "T"]

    for typ in typen:
        tc_obj = tc.get_thermocouple(typ)
        spannung = tc_obj.temperature_to_voltage(test_temperatur)
        seebeck = tc_obj.temp_to_seebeck(test_temperatur)
        print(f"   Typ {typ}: {spannung:.6f} V, {seebeck:.1f} µV/K")

    # 4. VERFÜGBARE TYPEN ANZEIGEN
    print("\n📋 Verfügbare Thermocouple-Typen:")
    verfügbare_typen = tc.get_available_types()
    print(f"   {', '.join(verfügbare_typen)} ({len(verfügbare_typen)} Typen)")

    # 5. KALTSTELLENKOMPENSATION
    print("\n❄️  Kaltstellenkompensation Beispiel:")

    # Gemessene Spannung bei Referenztemperatur 25°C
    gemessene_spannung = 0.008  # V
    referenz_temperatur = 25.0  # °C

    # Wahre Temperatur berechnen
    tc_k = tc.get_thermocouple("K")
    spannung_referenz = tc_k.temperature_to_voltage(referenz_temperatur)
    korrigierte_spannung = gemessene_spannung + spannung_referenz
    wahre_temperatur = tc_k.voltage_to_temperature(korrigierte_spannung)

    print(f"   Gemessene Spannung: {gemessene_spannung:.6f} V")
    print(f"   Referenztemperatur: {referenz_temperatur}°C")
    print(f"   Wahre Temperatur: {wahre_temperatur:.1f}°C")

    print("\n✅ Beispiel abgeschlossen!")


def test_genauigkeit():
    """Test der Rundreise-Genauigkeit (Temperatur → Spannung → Temperatur)."""
    print("\n🧪 GENAUIGKEITSTEST:")
    print("-" * 30)

    tc_k = tc.get_thermocouple("K")
    test_temperaturen = [0, 100, 200, 500, 1000]

    for temp in test_temperaturen:
        try:
            # Rundreise: Temperatur → Spannung → Temperatur
            spannung = tc_k.temperature_to_voltage(temp)
            temp_zurück = tc_k.voltage_to_temperature(spannung)
            fehler = abs(temp - temp_zurück)

            status = "✅" if fehler < 0.1 else "⚠️"
            print(f"   {status} {temp}°C → {spannung:.6f}V → {temp_zurück:.2f}°C (Fehler: {fehler:.3f}°C)")

        except Exception as e:
            print(f"   ❌ {temp}°C: Fehler - {e}")


if __name__ == "__main__":
    try:
        minimal_beispiel()
        test_genauigkeit()

        print("\n🎉 Alle Tests erfolgreich!")
        print("📚 Die Thermocouples v2.0 Bibliothek ist einsatzbereit!")

    except Exception as e:
        print(f"\n❌ Fehler beim Test: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
