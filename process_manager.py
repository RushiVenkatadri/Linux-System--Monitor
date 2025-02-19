import os
import psutil

def list_processes():
    """Lists all running processes"""
    print("\n🔹 Running Processes:")
    print(f"{'PID':<10}{'Name':<25}{'CPU%':<10}{'Memory%':<10}")
    print("-" * 60)
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        print(f"{proc.info['pid']:<10}{proc.info['name']:<25}{proc.info['cpu_percent']:<10}{proc.info['memory_percent']:<10.2f}")

def kill_process():
    """Kills a process by PID"""
    pid = int(input("Enter Process ID to kill: "))
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"✅ Successfully terminated process {pid} ({process.name()})")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        print("\n🔹 Linux Process Manager")
        print("1️⃣ List Running Processes")
        print("2️⃣ Kill a Process")
        print("3️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_processes()
        elif choice == "2":
            kill_process()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

