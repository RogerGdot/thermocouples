"""
Type S Thermocouple (Pt-10%Rh / Pt) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type S Characteristics:
- Positive leg: Platinum-10%Rhodium (Pt-10%Rh)
- Negative leg: Pure Platinum (Pt)
- Temperature range: -50°C to 1768.1°C
- EMF range: -0.235 mV to 18.693 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1600°C in oxidizing atmosphere
- Reference standard for platinum resistance thermometers
"""

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
    # Range: -50°C to 1064.18°C
    # $ Source: NIST Monograph 175, ITS-90, Page 83, Table 4.3.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-50, 1064.18),
        [
            0.000000000000e00,  # c₀
            5.403133086310e00,  # c₁
            1.259342897400e-02,  # c₂
            -2.324779686890e-05,  # c₃
            3.220288230360e-08,  # c₄
            -3.314651963890e-11,  # c₅
            2.557442517860e-14,  # c₆
            -1.250688713930e-17,  # c₇
            2.714431761450e-21,  # c₈
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: NIST Monograph 175, ITS-90, Page 83, Table 4.3.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1064.18, 1664.5),
        [
            1.329004440850e03,  # c₀
            3.345093113440e00,  # c₁
            6.548051928180e-03,  # c₂
            -1.648562592090e-06,  # c₃
            1.299896051740e-11,  # c₄
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: NIST Monograph 175, ITS-90, Page 83, Table 4.3.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1664.5, 1768.1),
        [
            1.466282326360e05,  # c₀
            -2.584305167520e02,  # c₁
            1.636935746410e-01,  # c₂
            -3.304390469870e-05,  # c₃
            -9.432236906120e-12,  # c₄
        ],
    ),
]

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
    # Range: -235µV to 1874µV (-50°C to 250°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 299, Table A4.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-235, 1874),
        [
            0.000000000000e00,  # c₀
            1.849494600000e-01,  # c₁
            -8.005040620000e-05,  # c₂
            1.022374300000e-07,  # c₃
            -1.522485920000e-10,  # c₄
            1.888213430000e-13,  # c₅
            -1.590859410000e-16,  # c₆
            8.230278800000e-20,  # c₇
            -2.341819440000e-23,  # c₈
            2.797862600000e-27,  # c₉
        ],
    ),
    # Range: 1874µV to 11950µV (250°C to 1200°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 299, Table A4.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1874, 11950),
        [
            1.291507177000e01,  # c₀
            1.466298863000e-01,  # c₁
            -1.534713402000e-05,  # c₂
            3.145945973000e-09,  # c₃
            -4.163257839000e-13,  # c₄
            3.187963771000e-17,  # c₅
            -1.291637500000e-21,  # c₆
            2.183475087000e-26,  # c₇
            -1.447379511000e-31,  # c₈
            8.211272125000e-36,  # c₉
        ],
    ),
    # Range: 10332µV to 17536µV (1064°C to 1664.5°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 299, Table A4.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (10332, 17536),
        [
            -8.087801117000e01,  # c₀
            1.621573104000e-01,  # c₁
            -8.536869453000e-06,  # c₂
            4.719686976000e-10,  # c₃
            -1.441693666000e-14,  # c₄
            2.081618890000e-19,  # c₅
        ],
    ),
    # Range: 17536µV to 18693µV (1664.5°C to 1768.1°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 299, Table A4.1, Type S thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (17536, 18693),
        [
            5.333875126000e01,  # c₀
            -1.235892298000e-02,  # c₁
            1.092657613000e-06,  # c₂
            -4.265693686000e-09,  # c₃
            6.247205420000e-13,  # c₄
        ],
    ),
]

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (-50, 1064.18),
        [
            5.403133086310e00,  # c₀ (1 * c₁ 5.403133086310e00)
            2.518685794800e-02,  # c₁ (2 * c₂ 1.259342897400e-02)
            -6.974339060670e-05,  # c₂ (3 * c₃ -2.324779686890e-05)
            1.288115292144e-07,  # c₃ (4 * c₄ 3.220288230360e-08)
            -1.657325963945e-10,  # c₄ (5 * c₅ -3.314651963890e-11)
            1.534465510716e-13,  # c₅ (6 * c₆ 2.557442517860e-14)
            -8.754820751100e-17,  # c₆ (7 * c₇ -1.250688713930e-17)
            2.171545409160e-20,  # c₇ (8 * c₈ 2.714431761450e-21)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (1064.18, 1664.5),
        [
            3.345093113440e00,  # c₀ (1 * c₁ 3.345093113440e00)
            1.309610385636e-02,  # c₁ (2 * c₂ 6.548051928180e-03)
            -4.945637776270e-06,  # c₂ (3 * c₃ -1.648562592090e-06)
            5.199584069600e-11,  # c₃ (4 * c₄ 1.299896051740e-11)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (1664.5, 1768.1),
        [
            -2.584305167520e02,  # c₀ (1 * c₁ -2.584305167520e02)
            3.273871492820e-01,  # c₁ (2 * c₂ 1.636935746410e-01)
            -9.913171409610e-05,  # c₂ (3 * c₃ -3.304390469870e-05)
            -3.772894762448e-11,  # c₃ (4 * c₄ -9.432236906120e-12)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (-50, 1064.18),
        [
            2.518685794800e-02,  # c₀ (1 * 2.518685794800e-02)
            -1.394867812134e-04,  # c₁ (2 * -6.974339060670e-05)
            3.864345876432e-07,  # c₂ (3 * 1.288115292144e-07)
            -6.629303855780e-10,  # c₃ (4 * -1.657325963945e-10)
            7.672327553580e-13,  # c₄ (5 * 1.534465510716e-13)
            -5.252874525770e-16,  # c₅ (6 * -8.754820751100e-17)
            1.520081486312e-19,  # c₆ (7 * 2.171545409160e-20)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (1064.18, 1664.5),
        [
            1.309610385636e-02,  # c₀ (1 * 1.309610385636e-02)
            -9.891275552540e-06,  # c₁ (2 * -4.945637776270e-06)
            1.559875220880e-10,  # c₂ (3 * 5.199584069600e-11)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (1664.5, 1768.1),
        [
            3.273871492820e-01,  # c₀ (1 * 3.273871492820e-01)
            -1.982634281922e-04,  # c₁ (2 * -9.913171409610e-05)
            -1.131868428734e-10,  # c₂ (3 * -3.772894762448e-11)
        ],
    ),
]

# Temperature to thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
    # Range: -50°C to 1064.18°C
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-50, 1064.18),
        [
            0.000000000000e00,  # c₀
            5.403133086310e00,  # c₁
            1.259342897400e-02,  # c₂
            -2.324779686890e-05,  # c₃
            3.220288230360e-08,  # c₄
            -3.314651963890e-11,  # c₅
            2.557442517860e-14,  # c₆
            -1.250688713930e-17,  # c₇
            2.714431761450e-21,  # c₈
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1064.18, 1664.5),
        [
            1.329004440850e03,  # c₀
            3.345093113440e00,  # c₁
            6.548051928180e-03,  # c₂
            -1.648562592090e-06,  # c₃
            1.299896051740e-11,  # c₄
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1664.5, 1768.1),
        [
            1.466282326360e05,  # c₀
            -2.584305167520e02,  # c₁
            1.636935746410e-01,  # c₂
            -3.304390469870e-05,  # c₃
            -9.432236906120e-12,  # c₄
        ],
    ),
]

# Temperature to thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: 0°C to 630.615°C
    # $ RN high-purity platinum, Pt vs. Pt = 0µV
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-50, 1768.1),
        [
            0.000000000000e00,  # (c₀)
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (-50, 1064.18),
        [
            5.403133086310e00,  # c₀ (1 * 5.403133086310e00)
            2.518685794800e-02,  # c₁ (2 * 1.259342897400e-02)
            -6.974339060670e-05,  # c₂ (3 * -2.324779686890e-05)
            1.288115292144e-07,  # c₃ (4 * 3.220288230360e-08)
            -1.657325963945e-10,  # c₄ (5 * -3.314651963890e-11)
            1.534465510716e-13,  # c₅ (6 * 2.557442517860e-14)
            -8.754820751100e-17,  # c₆ (7 * -1.250688713930e-17)
            2.171545409160e-20,  # c₇ (8 * 2.714431761450e-21)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (1064.18, 1664.5),
        [
            3.345093113440e00,  # c₀ (1 * 3.345093113440e00)
            1.309610385636e-02,  # c₁ (2 * 6.548051928180e-03)
            -4.945637776270e-06,  # c₂ (3 * -1.648562592090e-06)
            5.199584069600e-11,  # c₃ (4 * 1.299896051740e-11)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (1664.5, 1768.1),
        [
            -2.584305167520e02,  # c₀ (1 * -2.584305167520e02)
            3.273871492820e-01,  # c₁ (2 * 1.636935746410e-01)
            -9.913171409610e-05,  # c₂ (3 * -3.304390469870e-05)
            -3.772894762448e-11,  # c₃ (4 * -9.432236906120e-12)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: -50°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (-50, 1768.1),
        [
            0.0,  # c₀ (Platin-Referenz, Ableitung = 0)
        ],
    ),
]
