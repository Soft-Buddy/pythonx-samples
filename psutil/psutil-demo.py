import psutil
import platform

# On Android, access to some system information is restricted, so some functions of psutil may give permission denied errors to users.
def display_system_info():
    # Display basic system information
    print("System Information:")
    print(f"Platform: {platform.system()} {platform.version()}")
    print(f"Architecture: {platform.architecture()}")

def display_cpu_info():
    # Display CPU information
    print("\nCPU Information:")
    print(f"CPU Count: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
    print(f"CPU Frequency: {psutil.cpu_freq()}")

def display_memory_info():
    # Display memory information
    print("\nMemory Information:")
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024 ** 3):.2f} GB")

def display_process_info():
    # Display information about running processes
    print("\nRunning Processes:")
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, CPU %: {process.info['cpu_percent']:.2f}, Memory: {process.info['memory_info'].rss / (1024 ** 2):.2f} MB")

def display_battery_info():
    # Display battery information
    try:
        battery = psutil.sensors_battery()
        print("\nBattery Information:")
        print(f"  Percentage: {battery.percent}%")
        print(f"  Power Plugged: {battery.power_plugged}")
        print(f"  Time Left: {battery.secsleft / 3600:.2f} hours")
    except AttributeError:
        print("\nBattery Information: No battery available or information not supported.")

if __name__ == "__main__":
    display_system_info()
    display_cpu_info()
    display_memory_info()
    display_process_info()
