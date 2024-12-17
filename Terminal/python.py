print ("Hello skbablualam, This is your MAC information")

import os
import platform
import psutil

def get_system_info():
    info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": os.cpu_count(),
        "Architecture": platform.architecture()[0],
        "RAM Size (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
    }
    return info

def display_system_info(info):
    print("System Information:")
    print("=" * 30)
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        system_info = get_system_info()
        display_system_info(system_info)
    except Exception as e:
        print(f"An error occurred while retrieving system information: {e}")