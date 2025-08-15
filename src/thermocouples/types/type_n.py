"""
Type N Thermocouple (Ni-Cr-Si / Ni-Si) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type N Characteristics:
- Positive leg: Nickel-Chromium-Silicon (Ni-Cr-Si, Nicrosil)
- Negative leg: Nickel-Silicon (Ni-Si, Nisil)
- Temperature range: -270°C to 1300°C
- EMF range: -3.990 mV to 47.513 mV
- Accuracy: ±2.2°C or ±0.75% (whichever is greater)
- Maximum continuous temperature: 1200°C in oxidizing atmosphere
- Developed to improve stability of Type K thermocouples
- Superior drift characteristics compared to Type K
"""

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
    # Range: -270°C to 0°C
    # $ Source: NIST Monograph 175, ITS-90, Page 207, Table 8.3.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-270, 0),
        [
            0.000000000000e00,  # c₀
            2.615910596200e01,  # c₁
            1.095748422800e-02,  # c₂
            -9.384111155400e-05,  # c₃
            -4.641203975900e-06,  # c₄
            -2.630335771600e-07,  # c₅
            -2.265343800300e-09,  # c₆
            -7.608930079100e-12,  # c₇
            -9.341966783500e-15,  # c₈
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: NIST Monograph 175, ITS-90, Page 207, Table 8.3.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 1300),
        [
            0.000000000000e00,  # c₀
            2.592939460100e01,  # c₁
            1.571014188000e-02,  # c₂
            4.382562723700e-05,  # c₃
            -2.526116979400e-07,  # c₄
            6.431181933900e-10,  # c₅
            -1.006347151900e-12,  # c₆
            9.974533899200e-16,  # c₇
            -6.086324560700e-19,  # c₈
            2.084922933900e-22,  # c₉
            -3.068219615100e-26,  # c₁₀
        ],
    ),
]

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
    # Range: -3990µV to 0µV (-200°C to 0°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 307, Table A8.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-3990, 0),
        [
            0.000000000000e00,  # c₀
            3.843684700000e-02,  # c₁
            1.101048500000e-06,  # c₂
            5.222931200000e-09,  # c₃
            7.206052500000e-13,  # c₄
            5.848858600000e-15,  # c₅
            2.775491600000e-18,  # c₆
            7.707516600000e-22,  # c₇
            1.158266500000e-25,  # c₈
            7.313886800000e-30,  # c₉
        ],
    ),
    # Range: 0µV to 20613µV (0°C to 600°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 307, Table A8.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 20613),
        [
            0.000000000000e00,  # c₀
            3.868960000000e-02,  # c₁
            -1.082670000000e-06,  # c₂
            4.702050000000e-11,  # c₃
            -2.121690000000e-16,  # c₄
            -1.172720000000e-19,  # c₅
            5.392800000000e-24,  # c₆
            -7.981560000000e-29,  # c₇
        ],
    ),
    # Range: 20613µV to 47513µV (600°C to 1300°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 307, Table A8.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (20613, 47513),
        [
            1.972485000000e01,  # c₀
            3.300943000000e-02,  # c₁
            -3.915159000000e-07,  # c₂
            9.855391000000e-12,  # c₃
            -1.274371000000e-16,  # c₄
            7.767022000000e-22,  # c₅
        ],
    ),
    # Range: 0µV to 47513µV (0°C to 1300°C) - Additional range
    # $ Source: NIST Monograph 175, ITS-90, Page 307, Table A8.1, Type N thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 47513),
        [
            0.000000000000e00,  # c₀
            3.876327700000e-02,  # c₁
            -1.161234400000e-06,  # c₂
            6.952565500000e-11,  # c₃
            -3.009007700000e-15,  # c₄
            8.831158400000e-20,  # c₅
            -1.621383900000e-24,  # c₆
            1.669336200000e-29,  # c₇
            -7.311754000000e-35,  # c₈
        ],
    ),
]

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (-270, 0),
        [
            2.615910596200e01,  # c₀ (1 * c₁ 2.615910596200e01)
            2.191496845600e-02,  # c₁ (2 * c₂ 1.095748422800e-02)
            -2.815233346620e-04,  # c₂ (3 * c₃ -9.384111155400e-05)
            -1.856481590360e-05,  # c₃ (4 * c₄ -4.641203975900e-06)
            -1.315167885800e-06,  # c₄ (5 * c₅ -2.630335771600e-07)
            -1.359206280180e-08,  # c₅ (6 * c₆ -2.265343800300e-09)
            -5.326251055370e-11,  # c₆ (7 * c₇ -7.608930079100e-12)
            -7.473573426800e-14,  # c₇ (8 * c₈ -9.341966783500e-15)
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (0, 1300),
        [
            2.592939460100e01,  # c₀ (1 * c₁ 2.592939460100e01)
            3.142028376000e-02,  # c₁ (2 * c₂ 1.571014188000e-02)
            1.314768817110e-04,  # c₂ (3 * c₃ 4.382562723700e-05)
            -1.010446791760e-06,  # c₃ (4 * c₄ -2.526116979400e-07)
            3.215590966950e-09,  # c₄ (5 * c₅ 6.431181933900e-10)
            -6.038082911400e-12,  # c₅ (6 * c₆ -1.006347151900e-12)
            6.982203739440e-15,  # c₆ (7 * c₇ 9.974533899200e-16)
            -4.869059648560e-18,  # c₇ (8 * c₈ -6.086324560700e-19)
            1.876450640510e-21,  # c₈ (9 * c₉ 2.084922933900e-22)
            -3.068219615100e-25,  # c₉ (10 * c₁₀ -3.068219615100e-26)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (-270, 0),
        [
            2.191496845600e-02,  # c₀ (1 * 2.191496845600e-02)
            -5.630466693240e-04,  # c₁ (2 * -2.815233346620e-04)
            -5.569444771080e-05,  # c₂ (3 * -1.856481590360e-05)
            -5.260671543200e-06,  # c₃ (4 * -1.315167885800e-06)
            -6.796031401080e-08,  # c₄ (5 * -1.359206280180e-08)
            -3.195750633222e-10,  # c₅ (6 * -5.326251055370e-11)
            -5.231501998760e-13,  # c₆ (7 * -7.473573426800e-14)
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (0, 1300),
        [
            3.142028376000e-02,  # c₀ (1 * 3.142028376000e-02)
            2.629537634220e-04,  # c₁ (2 * 1.314768817110e-04)
            -3.031340375280e-06,  # c₂ (3 * -1.010446791760e-06)
            1.286236386780e-08,  # c₃ (4 * 3.215590966950e-09)
            -3.019041746840e-11,  # c₄ (5 * -6.038082911400e-12)
            4.187542616064e-14,  # c₅ (6 * 6.982203739440e-15)
            -3.408247718848e-17,  # c₆ (7 * -4.869059648560e-18)
            1.501060432408e-20,  # c₇ (8 * 1.876450640510e-21)
            -2.761397653590e-24,  # c₈ (9 * -3.068219615100e-25)
        ],
    ),
]

# Temperature to Thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
    # Range: -200°C to 0°C
    # $ Source: NIST Monograph 175, ITS-90, Page 234, Table 8.5.1, Type NN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-200, 0),
        [
            0.000000000000e00,  # c₀
            1.074111753200e01,  # c₁
            -1.474989822900e-02,  # c₂
            -3.653285783200e-06,  # c₃
            4.901358902900e-07,  # c₄
            7.222858260400e-10,  # c₅
            -1.538109323600e-11,  # c₆
            -7.608930079100e-14,  # c₇
            -9.341966783500e-17,  # c₈
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: NIST Monograph 175, ITS-90, Page 234, Table 8.5.1, Type NN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 1300),
        [
            0.000000000000e00,  # c₀
            1.048400865500e01,  # c₁
            -1.101219940900e-02,  # c₂
            6.942094028900e-05,  # c₃
            -2.195836005300e-07,  # c₄
            4.423649636800e-10,  # c₅
            -5.792656096400e-13,  # c₆
            4.793166547000e-16,  # c₇
            -2.397612067600e-19,  # c₈
            6.580494631800e-23,  # c₉
            -7.560893996500e-27,  # c₁₀
        ],
    ),
]

# Temperature to Thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: -200°C to 0°C
    # $ Source: NIST Monograph 175, ITS-90, Page 221, Table 8.4.1, Type NP thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-200, 0),
        [
            0.000000000000e00,  # c₀
            1.541798843000e01,  # c₁
            2.570738245700e-02,  # c₂
            -9.018782577100e-05,  # c₃
            -5.365479300500e-06,  # c₄
            -3.352621597600e-09,  # c₅
            -7.272344767000e-12,  # c₆
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: NIST Monograph 175, ITS-90, Page 221, Table 8.4.1, Type NP thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 1300),
        [
            0.000000000000e00,  # c₀
            1.544536594700e01,  # c₁
            2.672341269000e-02,  # c₂
            -2.559531305200e-05,  # c₃
            -3.302809741400e-08,  # c₄
            2.007532297100e-10,  # c₅
            -4.270815423000e-13,  # c₆
            5.181347352200e-16,  # c₇
            -3.689712493100e-19,  # c₈
            1.426973470800e-22,  # c₉
            -2.312130215400e-26,  # c₁₀
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: -200°C to 0°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (-200, 0),
        [
            1.074111753200e01,  # c₀ (1 * 1.074111753200e01)
            -2.949979645800e-02,  # c₁ (2 * -1.474989822900e-02)
            -1.095985734960e-05,  # c₂ (3 * -3.653285783200e-06)
            1.960543561160e-06,  # c₃ (4 * 4.901358902900e-07)
            2.889143304160e-09,  # c₄ (5 * 7.222858260400e-10)
            -9.228655941600e-11,  # c₅ (6 * -1.538109323600e-11)
            -5.326251055370e-13,  # c₆ (7 * -7.608930079100e-14)
            -7.473573426800e-16,  # c₇ (8 * -9.341966783500e-17)
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (0, 1300),
        [
            1.048400865500e01,  # c₀ (1 * 1.048400865500e01)
            -2.202439881800e-02,  # c₁ (2 * -1.101219940900e-02)
            2.082628208670e-04,  # c₂ (3 * 6.942094028900e-05)
            -8.783344021200e-07,  # c₃ (4 * -2.195836005300e-07)
            2.211824818400e-09,  # c₄ (5 * 4.423649636800e-10)
            -4.054859267480e-12,  # c₅ (6 * -5.792656096400e-13)
            3.834533237600e-15,  # c₆ (7 * 4.793166547000e-16)
            -1.917089654080e-18,  # c₇ (8 * -2.397612067600e-19)
            5.922445168620e-21,  # c₈ (9 * 6.580494631800e-22)
            -7.560893996500e-24,  # c₉ (10 * -7.560893996500e-25)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: -200°C to 0°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (-200, 0),
        [
            1.541798843000e01,  # c₀ (1 * 1.541798843000e01)
            5.141476491400e-02,  # c₁ (2 * 2.570738245700e-02)
            -2.705487868130e-04,  # c₂ (3 * -9.018782577100e-05)
            -2.146191720200e-05,  # c₃ (4 * -5.365479300500e-06)
            -1.341048639040e-07,  # c₄ (5 * -2.682097278000e-08)
            -4.363409860400e-10,  # c₅ (6 * -7.272344767000e-11)
        ],
    ),
    # Range: 0°C to 1300°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (0, 1300),
        [
            1.544536594700e01,  # c₀ (1 * 1.544536594700e01)
            5.344682538000e-02,  # c₁ (2 * 2.672341269000e-02)
            -7.678593915600e-05,  # c₂ (3 * -2.559531305200e-05)
            -1.321123896560e-07,  # c₃ (4 * -3.302809741400e-08)
            1.003766148550e-09,  # c₄ (5 * 2.007532297100e-10)
            -2.562489253800e-12,  # c₅ (6 * -4.270815423000e-13)
            3.627943146540e-15,  # c₆ (7 * 5.181347352200e-16)
            -2.951769994480e-18,  # c₇ (8 * -3.689712493100e-19)
            1.284276123720e-21,  # c₈ (9 * 1.426973470800e-22)
            -2.543343236940e-24,  # c₉ (10 * -2.312130215400e-25)
        ],
    ),
]
