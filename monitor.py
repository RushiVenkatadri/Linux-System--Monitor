import psutil
import os
import time

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"Memory Usage: {mem.percent}% (Total: {mem.total // (1024**3)}GB, Available: {mem.available // (1024**3)}GB)"

def get_disk_usage():
    disk = psutil.disk_usage("/")
    return f"Disk Usage: {disk.percent}% (Total: {disk.total // (1024**3)}GB, Free: {disk.free // (1024**3)}GB)"

def get_running_processes():
    processes = [p.info for p in psutil.process_iter(["pid", "name", "cpu_percent"])]
    sorted_processes = sorted(processes, key=lambda p: p["cpu_percent"], reverse=True)[:5]
    
    result = "\nTop 5 CPU-Consuming Processes:\n"
    result += "-" * 40 + "\n"
    for p in sorted_processes:
        result += f"PID: {p['pid']}, Name: {p['name']}, CPU: {p['cpu_percent']}%\n"
    
    return result

def main():
    while True:
        clear_screen()
        print(get_cpu_usage())
        print(get_memory_usage())
        print(get_disk_usage())
        print(get_running_processes())
        print("\nPress Ctrl+C to exit.")
        time.sleep(2)

if __name__ == "__main__":
    main()
