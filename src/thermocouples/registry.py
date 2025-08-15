"""
Registry and utility functions for thermocouples.
"""

from .core import ThermocoupleType
from .types.type_b import (
    MICROVOLT_TO_TEMP as B_MICROVOLT_TO_TEMP,
)
from .types.type_b import (
    TEMP_TO_DSDT as B_TEMP_TO_DSDT,
)
from .types.type_b import (
    TEMP_TO_MICROVOLT as B_TEMP_TO_MICROVOLT,
)
from .types.type_b import (
    TEMP_TO_MICROVOLT_NEG_LEG as B_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_b import (
    TEMP_TO_MICROVOLT_POS_LEG as B_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_b import (
    TEMP_TO_SEEBECK as B_TEMP_TO_SEEBECK,
)
from .types.type_b import (
    TEMP_TO_SEEBECK_NEG_LEG as B_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_b import (
    TEMP_TO_SEEBECK_POS_LEG as B_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_e import (
    MICROVOLT_TO_TEMP as E_MICROVOLT_TO_TEMP,
)
from .types.type_e import (
    TEMP_TO_DSDT as E_TEMP_TO_DSDT,
)
from .types.type_e import (
    TEMP_TO_MICROVOLT as E_TEMP_TO_MICROVOLT,
)
from .types.type_e import (
    TEMP_TO_MICROVOLT_NEG_LEG as E_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_e import (
    TEMP_TO_MICROVOLT_POS_LEG as E_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_e import (
    TEMP_TO_SEEBECK as E_TEMP_TO_SEEBECK,
)
from .types.type_e import (
    TEMP_TO_SEEBECK_NEG_LEG as E_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_e import (
    TEMP_TO_SEEBECK_POS_LEG as E_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_j import (
    MICROVOLT_TO_TEMP as J_MICROVOLT_TO_TEMP,
)
from .types.type_j import (
    TEMP_TO_DSDT as J_TEMP_TO_DSDT,
)
from .types.type_j import (
    TEMP_TO_MICROVOLT as J_TEMP_TO_MICROVOLT,
)
from .types.type_j import (
    TEMP_TO_MICROVOLT_NEG_LEG as J_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_j import (
    TEMP_TO_MICROVOLT_POS_LEG as J_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_j import (
    TEMP_TO_SEEBECK as J_TEMP_TO_SEEBECK,
)
from .types.type_j import (
    TEMP_TO_SEEBECK_NEG_LEG as J_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_j import (
    TEMP_TO_SEEBECK_POS_LEG as J_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_k import (
    MICROVOLT_TO_TEMP as K_MICROVOLT_TO_TEMP,
)
from .types.type_k import (
    TEMP_TO_DSDT as K_TEMP_TO_DSDT,
)
from .types.type_k import (
    TEMP_TO_MICROVOLT as K_TEMP_TO_MICROVOLT,
)
from .types.type_k import (
    TEMP_TO_MICROVOLT_NEG_LEG as K_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_k import (
    TEMP_TO_MICROVOLT_POS_LEG as K_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_k import (
    TEMP_TO_SEEBECK as K_TEMP_TO_SEEBECK,
)
from .types.type_k import (
    TEMP_TO_SEEBECK_NEG_LEG as K_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_k import (
    TEMP_TO_SEEBECK_POS_LEG as K_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_k import (
    _type_k_dsdt_expo_function,
    _type_k_kn_expo_function,
    _type_k_seebeck_expo_function,
    _type_k_voltage_expo_function,
)
from .types.type_n import (
    MICROVOLT_TO_TEMP as N_MICROVOLT_TO_TEMP,
)
from .types.type_n import (
    TEMP_TO_DSDT as N_TEMP_TO_DSDT,
)
from .types.type_n import (
    TEMP_TO_MICROVOLT as N_TEMP_TO_MICROVOLT,
)
from .types.type_n import (
    TEMP_TO_MICROVOLT_NEG_LEG as N_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_n import (
    TEMP_TO_MICROVOLT_POS_LEG as N_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_n import (
    TEMP_TO_SEEBECK as N_TEMP_TO_SEEBECK,
)
from .types.type_n import (
    TEMP_TO_SEEBECK_NEG_LEG as N_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_n import (
    TEMP_TO_SEEBECK_POS_LEG as N_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_r import (
    MICROVOLT_TO_TEMP as R_MICROVOLT_TO_TEMP,
)
from .types.type_r import (
    TEMP_TO_DSDT as R_TEMP_TO_DSDT,
)
from .types.type_r import (
    TEMP_TO_MICROVOLT as R_TEMP_TO_MICROVOLT,
)
from .types.type_r import (
    TEMP_TO_MICROVOLT_NEG_LEG as R_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_r import (
    TEMP_TO_MICROVOLT_POS_LEG as R_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_r import (
    TEMP_TO_SEEBECK as R_TEMP_TO_SEEBECK,
)
from .types.type_r import (
    TEMP_TO_SEEBECK_NEG_LEG as R_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_r import (
    TEMP_TO_SEEBECK_POS_LEG as R_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_s import (
    MICROVOLT_TO_TEMP as S_MICROVOLT_TO_TEMP,
)
from .types.type_s import (
    TEMP_TO_DSDT as S_TEMP_TO_DSDT,
)
from .types.type_s import (
    TEMP_TO_MICROVOLT as S_TEMP_TO_MICROVOLT,
)
from .types.type_s import (
    TEMP_TO_MICROVOLT_NEG_LEG as S_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_s import (
    TEMP_TO_MICROVOLT_POS_LEG as S_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_s import (
    TEMP_TO_SEEBECK as S_TEMP_TO_SEEBECK,
)
from .types.type_s import (
    TEMP_TO_SEEBECK_NEG_LEG as S_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_s import (
    TEMP_TO_SEEBECK_POS_LEG as S_TEMP_TO_SEEBECK_POS_LEG,
)
from .types.type_t import (
    MICROVOLT_TO_TEMP as T_MICROVOLT_TO_TEMP,
)
from .types.type_t import (
    TEMP_TO_DSDT as T_TEMP_TO_DSDT,
)
from .types.type_t import (
    TEMP_TO_MICROVOLT as T_TEMP_TO_MICROVOLT,
)
from .types.type_t import (
    TEMP_TO_MICROVOLT_NEG_LEG as T_TEMP_TO_MICROVOLT_NEG_LEG,
)
from .types.type_t import (
    TEMP_TO_MICROVOLT_POS_LEG as T_TEMP_TO_MICROVOLT_POS_LEG,
)
from .types.type_t import (
    TEMP_TO_SEEBECK as T_TEMP_TO_SEEBECK,
)
from .types.type_t import (
    TEMP_TO_SEEBECK_NEG_LEG as T_TEMP_TO_SEEBECK_NEG_LEG,
)
from .types.type_t import (
    TEMP_TO_SEEBECK_POS_LEG as T_TEMP_TO_SEEBECK_POS_LEG,
)

# Create thermocouple instances
TYPE_K = ThermocoupleType(
    name="K",
    temp_to_microvolt=K_TEMP_TO_MICROVOLT,
    microvolt_to_temp=K_MICROVOLT_TO_TEMP,
    temp_to_seebeck=K_TEMP_TO_SEEBECK,
    temp_to_dsdt=K_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=K_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=K_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=K_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=K_TEMP_TO_SEEBECK_NEG_LEG,
    microvolt_expo_function=_type_k_voltage_expo_function,
    seebeck_expo_function=_type_k_seebeck_expo_function,
    dsdt_expo_function=_type_k_dsdt_expo_function,
    microvolt_neg_leg_expo_function=_type_k_kn_expo_function,
)

TYPE_J = ThermocoupleType(
    name="J",
    temp_to_microvolt=J_TEMP_TO_MICROVOLT,
    microvolt_to_temp=J_MICROVOLT_TO_TEMP,
    temp_to_seebeck=J_TEMP_TO_SEEBECK,
    temp_to_dsdt=J_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=J_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=J_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=J_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=J_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_T = ThermocoupleType(
    name="T",
    temp_to_microvolt=T_TEMP_TO_MICROVOLT,
    microvolt_to_temp=T_MICROVOLT_TO_TEMP,
    temp_to_seebeck=T_TEMP_TO_SEEBECK,
    temp_to_dsdt=T_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=T_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=T_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=T_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=T_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_E = ThermocoupleType(
    name="E",
    temp_to_microvolt=E_TEMP_TO_MICROVOLT,
    microvolt_to_temp=E_MICROVOLT_TO_TEMP,
    temp_to_seebeck=E_TEMP_TO_SEEBECK,
    temp_to_dsdt=E_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=E_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=E_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=E_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=E_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_N = ThermocoupleType(
    name="N",
    temp_to_microvolt=N_TEMP_TO_MICROVOLT,
    microvolt_to_temp=N_MICROVOLT_TO_TEMP,
    temp_to_seebeck=N_TEMP_TO_SEEBECK,
    temp_to_dsdt=N_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=N_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=N_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=N_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=N_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_B = ThermocoupleType(
    name="B",
    temp_to_microvolt=B_TEMP_TO_MICROVOLT,
    microvolt_to_temp=B_MICROVOLT_TO_TEMP,
    temp_to_seebeck=B_TEMP_TO_SEEBECK,
    temp_to_dsdt=B_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=B_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=B_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=B_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=B_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_R = ThermocoupleType(
    name="R",
    temp_to_microvolt=R_TEMP_TO_MICROVOLT,
    microvolt_to_temp=R_MICROVOLT_TO_TEMP,
    temp_to_seebeck=R_TEMP_TO_SEEBECK,
    temp_to_dsdt=R_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=R_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=R_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=R_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=R_TEMP_TO_SEEBECK_NEG_LEG,
)

TYPE_S = ThermocoupleType(
    name="S",
    temp_to_microvolt=S_TEMP_TO_MICROVOLT,
    microvolt_to_temp=S_MICROVOLT_TO_TEMP,
    temp_to_seebeck=S_TEMP_TO_SEEBECK,
    temp_to_dsdt=S_TEMP_TO_DSDT,
    temp_to_microvolt_pos_leg=S_TEMP_TO_MICROVOLT_POS_LEG,
    temp_to_microvolt_neg_leg=S_TEMP_TO_MICROVOLT_NEG_LEG,
    temp_to_seebeck_pos_leg=S_TEMP_TO_SEEBECK_POS_LEG,
    temp_to_seebeck_neg_leg=S_TEMP_TO_SEEBECK_NEG_LEG,
)

# Registry of all available thermocouple types
THERMOCOUPLE_TYPES = {
    "B": TYPE_B,
    "E": TYPE_E,
    "J": TYPE_J,
    "K": TYPE_K,
    "N": TYPE_N,
    "R": TYPE_R,
    "S": TYPE_S,
    "T": TYPE_T,
}


def get_thermocouple(tc_type: str) -> ThermocoupleType:
    """
    Get a thermocouple instance by type.

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)

    Returns:
        ThermocoupleType instance

    Raises:
        ValueError: If the thermocouple type is not supported
    """
    tc_type = tc_type.upper()
    if tc_type not in THERMOCOUPLE_TYPES:
        available = ", ".join(sorted(THERMOCOUPLE_TYPES.keys()))
        raise ValueError(f"Thermocouple type '{tc_type}' not supported. Available types: {available}")

    return THERMOCOUPLE_TYPES[tc_type]


def temperature_to_voltage(tc_type: str, temp_c: float) -> float:
    """
    Convenience function: Convert temperature (°C) to voltage (V).

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)
        temp_c: Temperature in degrees Celsius

    Returns:
        Thermoelectric voltage in volts
    """
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_voltage(temp_c)


def voltage_to_temperature(tc_type: str, voltage: float) -> float:
    """
    Convenience function: Convert voltage (V) to temperature (°C).

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)
        voltage: Thermoelectric voltage in volts

    Returns:
        Temperature in degrees Celsius
    """
    tc = get_thermocouple(tc_type)
    return tc.voltage_to_temperature(voltage)


def voltage_to_temperature_with_reference(tc_type: str, v_measured: float, t_ref: float) -> float:
    """
    Convenience function: Convert measured voltage and reference temperature to actual temperature.

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)
        v_measured: Measured thermoelectric voltage in volts
        t_ref: Reference junction temperature in degrees Celsius

    Returns:
        Actual temperature in degrees Celsius
    """
    tc = get_thermocouple(tc_type)
    return tc.voltage_to_temperature_with_reference(v_measured, t_ref)


def temp_to_seebeck(tc_type: str, temp_c: float) -> float:
    """
    Convenience function: Calculate Seebeck coefficient at temperature.

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)
        temp_c: Temperature in degrees Celsius

    Returns:
        Seebeck coefficient in µV/K
    """
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_seebeck(temp_c)


def temp_to_dsdt(tc_type: str, temp_c: float) -> float:
    """
    Convenience function: Calculate dSeebeck/dT at temperature.

    Args:
        tc_type: Thermocouple type ('K', 'J', 'T', etc.)
        temp_c: Temperature in degrees Celsius

    Returns:
        dSeebeck/dT in nV/K²
    """
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_dsdt(temp_c)
