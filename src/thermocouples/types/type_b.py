"""
Type B Thermocouple (Pt-30%Rh / Pt-6%Rh) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type B Characteristics:
- Positive leg: Platinum-30%Rhodium (Pt-30%Rh)
- Negative leg: Platinum-6%Rhodium (Pt-6%Rh)
- Temperature range: 0°C to 1820°C
- EMF range: 0 mV to 13.820 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1700°C in oxidizing atmosphere
- Minimum temperature: 0°C (no output below this)
- Used for very high temperature measurements
"""

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
    # Range: 0°C to 630.615°C
    # $ Source: NIST Monograph 175, ITS-90, page 12, table 2.3.1, Type B thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 630.615),
        [
            0.000000000000e00,  # c₀
            -2.465081834600e-01,  # c₁
            5.904042117100e-03,  # c₂
            -1.325793163600e-06,  # c₃
            1.566829190100e-09,  # c₄
            -1.694452924000e-12,  # c₅
            6.299034709400e-16,  # c₆
        ],
    ),
    # Range: 630.615°C to 1820°C
    # $ Source: NIST Monograph 175, ITS-90, page 12, table 2.3.1, Type B thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (630.615, 1820),
        [
            -3.893816862100e03,  # c₀
            2.857174747000e-01,  # c₁
            -8.488510478500e-05,  # c₂
            1.578528016400e-04,  # c₃
            -1.683534486400e-07,  # c₄
            1.110979401300e-10,  # c₅
            -4.451543103300e-14,  # c₆
            9.897564082100e-18,  # c₇
            -9.379133028900e-22,  # c₈
        ],
    ),
]

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
    # Range: 291µV to 2431µV (250°C to 700°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 296, Table A2.1, Type B thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (291, 2431),
        [
            9.842332100e01,  # c₀
            6.997150000e-01,  # c₁
            -8.476530400e-04,  # c₂
            1.005264400e-06,  # c₃
            -8.334595200e-10,  # c₄
            4.550854200e-13,  # c₅
            -1.552303700e-16,  # c₆
            2.988675000e-20,  # c₇
            -2.474286000e-24,  # c₈
        ],
    ),
    # Range: 2431µV to 13820µV (700°C to 1820°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 296, Table A2.1, Type B thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (2431, 13820),
        [
            2.131507100e02,  # c₀
            2.851050400e-01,  # c₁
            -5.274288700e-05,  # c₂
            9.916080400e-09,  # c₃
            -1.296530300e-12,  # c₄
            1.119587000e-16,  # c₅
            -6.062519900e-21,  # c₆
            1.866169600e-25,  # c₇
            -2.487858500e-30,  # c₈
        ],
    ),
]

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: 0°C to 630.615°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (0, 630.615),
        [
            -2.465081834600e-01,  # c₀ (1 * c₁ -2.465081834600e-01)
            1.180804234200e-02,  # c₁ (2 * c₂ 5.904042117100e-03)
            -3.977379490800e-06,  # c₂ (3 * c₃ -1.325793163600e-06)
            6.267316760400e-09,  # c₃ (4 * c₄ 1.566829190100e-09)
            -8.472264620000e-12,  # c₄ (5 * c₅ -1.694452924000e-12)
            3.779420845640e-15,  # c₅ (6 * c₆ 6.299034709400e-16)
        ],
    ),
    # Range: 630.615°C to 1820°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (630.615, 1820),
        [
            2.857174747000e-01,  # c₀ (1 * c₁ 2.857174747000e-01)
            -1.697702095700e-04,  # c₁ (2 * c₂ -8.488510478500e-05)
            4.735584049200e-04,  # c₂ (3 * c₃ 1.578528016400e-04)
            -6.734137945600e-07,  # c₃ (4 * c₄ -1.683534486400e-07)
            5.554897006500e-10,  # c₄ (5 * c₅ 1.110979401300e-10)
            -2.670925859800e-13,  # c₅ (6 * c₆ -4.451543103300e-14)
            6.928304857470e-17,  # c₆ (7 * c₇ 9.897564082100e-18)
            -7.503266423120e-21,  # c₇ (8 * c₈ -9.379133028900e-22)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: 0°C to 630.615°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (0, 630.615),
        [
            1.180804234200e-02,  # c₀ (1 * 1.180804234200e-02)
            -7.954758981600e-06,  # c₁ (2 * -3.977379490800e-06)
            1.880195028120e-08,  # c₂ (3 * 6.267316760400e-09)
            -3.388905848000e-11,  # c₃ (4 * -8.472264620000e-12)
            1.889710422820e-14,  # c₄ (5 * 3.779420845640e-15)
        ],
    ),
    # Range: 630.615°C to 1820°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (630.615, 1820),
        [
            -1.697702095700e-04,  # c₀ (1 * -1.697702095700e-04)
            9.471168098400e-04,  # c₁ (2 * 4.735584049200e-04)
            -2.020241383680e-06,  # c₂ (3 * -6.734137945600e-07)
            2.221958802600e-09,  # c₃ (4 * 5.554897006500e-10)
            -1.335462929900e-12,  # c₄ (5 * -2.670925859800e-13)
            4.156982914482e-16,  # c₅ (6 * 6.928304857470e-17)
            -5.252586738384e-20,  # c₆ (7 * -7.503266423120e-21)
        ],
    ),
]

# Temperature to Thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
    # Range: 0°C to 630.615°C
    # $ Source: NIST Monograph 175, ITS-90, page 28, table 2.4.1 Type BP thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 630.615),
        [
            0.000000000000e00,  # c₀
            4.822787568700e00,  # c₁
            1.565116570900e-02,  # c₂
            -2.223379788200e-05,  # c₃
            2.833324407400e-08,  # c₄
            -2.025894044700e-11,  # c₅
            6.148870509600e-15,  # c₆
        ],
    ),
    # Range: 630.615°C to 1768.1°C
    # $ Source: NIST Monograph 175, ITS-90, page 28, table 2.4.1 Type BP thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (630.615, 1768.1),
        [
            -7.9680432282e3,  # c₀
            6.39411102130e1,  # c₁
            -1.7102421410e-1,  # c₂
            3.05557825270e-4,  # c₃
            -3.2105744492e-7,  # c₄
            2.09091027940e-10,  # c₅
            -8.2335825426e-14,  # c₆
            1.78228415150e-17,  # c₇
            -1.6187074187e-21,  # c₈
        ],
    ),
]

# Temperature to thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: 0°C to 630.615°C
    # $ Source: NIST Monograph 175, ITS-90, Table 2.5.1, Type BN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 630.615),
        [
            0.000000000000e00,  # c₀
            5.069295752200e00,  # c₁
            9.747123532000e-03,  # c₂
            -2.090906471800e-05,  # c₃
            2.676641488300e-08,  # c₄
            -1.856448752300e-11,  # c₅
            5.518967038600e-15,  # c₆
        ],
    ),
    # Range: 630.615°C to 1768.1°C
    # $ Source: NIST Monograph 175, ITS-90, Table 2.5.1, Type BN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (630.615, 1768.1),
        [
            -4.074226366200e03,  # c₀
            3.536936274300e01,  # c₁
            -8.613910931500e-02,  # c₂
            1.477050236200e-04,  # c₃
            -1.527039962900e-07,  # c₄
            9.799308790500e-11,  # c₅
            -3.782039439300e-14,  # c₆
            7.925277432800e-18,  # c₇
            -6.807941157800e-22,  # c₈
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: 0°C to 630.615°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (0, 630.615),
        [
            4.822787568700e00,  # c₀ (1 * 4.822787568700e00)
            3.130233141800e-02,  # c₁ (2 * 1.565116570900e-02)
            -6.670139364600e-05,  # c₂ (3 * -2.223379788200e-05)
            1.133329762960e-07,  # c₃ (4 * 2.833324407400e-08)
            -1.012947022350e-10,  # c₄ (5 * -2.025894044700e-11)
            3.689322305760e-14,  # c₅ (6 * 6.148870509600e-15)
        ],
    ),
    # Range: 630.615°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (630.615, 1768.1),
        [
            6.39411102130e1,  # c₀ (1 * 6.39411102130e1)
            -3.4204842820e-1,  # c₁ (2 * -1.7102421410e-1)
            9.16673475810e-4,  # c₂ (3 * 3.05557825270e-4)
            -1.28422977968e-6,  # c₃ (4 * -3.2105744492e-7)
            1.04545513970e-9,  # c₄ (5 * 2.09091027940e-10)
            -4.94014952556e-13,  # c₅ (6 * -8.2335825426e-14)
            1.42582732120e-16,  # c₆ (7 * 1.78228415150e-17)
            -1.29496593496e-20,  # c₇ (8 * -1.6187074187e-21)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: 0°C to 630.615°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (0, 630.615),
        [
            5.069295752200e00,  # c₀ (1 * 5.069295752200e00)
            1.949424706400e-02,  # c₁ (2 * 9.747123532000e-03)
            -6.272719415400e-05,  # c₂ (3 * -2.090906471800e-05)
            1.070656595320e-07,  # c₃ (4 * 2.676641488300e-08)
            -9.282243761500e-11,  # c₄ (5 * -1.856448752300e-11)
            3.311380223160e-14,  # c₅ (6 * 5.518967038600e-15)
        ],
    ),# Range: 630.615°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (630.615, 1768.1),
        [
            3.536936274300e01,  # c₀ (1 * 3.536936274300e01)
            -1.722782186300e-01,  # c₁ (2 * -8.613910931500e-02)
            4.431150708600e-04,  # c₂ (3 * 1.477050236200e-04)
            -6.108159851600e-07,  # c₃ (4 * -1.527039962900e-07)
            4.899654395250e-10,  # c₄ (5 * 9.799308790500e-11)
            -2.269223663580e-13,  # c₅ (6 * -3.782039439300e-14)
            5.547694203960e-17,  # c₆ (7 * 7.925277432800e-18)
            -5.446352926240e-21,  # c₇ (8 * -6.807941157800e-22)
        ],
    ),
]
