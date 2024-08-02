import os
import subprocess

def check_disk_usage():
    usage = subprocess.check_output(['wmic', 'logicaldisk', 'get', 'size,freespace,caption']).decode('utf-8')
    return usage

def check_memory_usage():
    usage = subprocess.check_output(['systeminfo']).decode('utf-8')
    return usage

def check_cpu_load():
    load = subprocess.check_output(['wmic', 'cpu', 'get', 'loadpercentage']).decode('utf-8')
    return load

def check_network_connectivity():
    connectivity = subprocess.check_output(['ping', '-n', '4', 'google.com']).decode('utf-8')
    return connectivity

def generate_report():
    report = ""
    report += "Disk Usage:\n" + check_disk_usage() + "\n"
    report += "Memory Usage:\n" + check_memory_usage() + "\n"
    report += "CPU Load:\n" + check_cpu_load() + "\n"
    report += "Network Connectivity:\n" + check_network_connectivity() + "\n"
    
    with open("system_report.txt", "w") as file:
        file.write(report)

if __name__ == "__main__":
    generate_report()
    print("System report generated: system_report.txt")
