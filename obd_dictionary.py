obd_library = {
    # --- ENGINE SYNCHRONIZATION & LOAD ---
    "0104": {
        "name": "calculated_engine_load",
        "formula": lambda b: (100 / 255) * b[0],
        "unit": "%"
    },
    "010C": {
        "name": "engine_rpm",
        "formula": lambda b: ((b[0] * 256) + b[1]) / 4,
        "unit": "RPM"
    },
    
    # --- DRIVER INPUTS & PERFORMANCE ---
    "010D": {
        "name": "vehicle_speed",
        "formula": lambda b: b[0],
        "unit": "km/h"
    },
    "0111": {
        "name": "throttle_position",
        "formula": lambda b: (100 / 255) * b[0],
        "unit": "%"
    },
    
    # --- THERMAL CRITICAL BOUNDARIES (Poll these slowly) ---
    "0105": {
        "name": "coolant_temp",
        "formula": lambda b: b[0] - 40,
        "unit": "°C"
    },
    "010F": {
        "name": "intake_air_temperature",
        "formula": lambda b: b[0] - 40,
        "unit": "°C"
    }
}
