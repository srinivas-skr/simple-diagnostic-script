# Basic Troubleshooting Script

This project provides a simple automated troubleshooting script designed to identify and diagnose common system issues. It includes checks for disk usage, memory usage, CPU load, and network connectivity, and generates a system report with suggested solutions.

## Features

- **Disk Usage Check**: Retrieves and reports disk usage statistics.
- **Memory Usage Check**: Retrieves and reports memory usage statistics.
- **CPU Load Check**: Retrieves and reports CPU load statistics.
- **Network Connectivity Check**: Tests network connectivity to an external server.

## Technologies Used

- Python
- Shell scripting

## Usage

### Prerequisites

- Python 3.x must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Running the Script

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/basic-troubleshooting-script.git
    cd basic-troubleshooting-script
    ```

2. **Run the Script**:
    - Open your terminal (Command Prompt on Windows, terminal on macOS/Linux).
    - Navigate to the directory where the script is located.
    - Execute the script using Python:
        ```bash
        python troubleshooting_script.py
        ```

3. **View the Report**:
    - The script generates a file named `system_report.txt` in the same directory.
    - Open `system_report.txt` to view the system diagnostics and suggested solutions.

## Example Output

```plaintext
Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   27G  43% /

Memory Usage:
              total        used        free      shared  buff/cache   available
Mem:           7.8G        2.3G        3.1G        300M        2.4G        5.0G
Swap:          2.0G          0B        2.0G

CPU Load:
 14:35:01 up  1:13,  1 user,  load average: 0.44, 0.23, 0.15

Network Connectivity:
Pinging google.com [172.217.14.206] with 32 bytes of data:
Reply from 172.217.14.206: bytes=32 time=14ms TTL=54
Reply from 172.217.14.206: bytes=32 time=14ms TTL=54
Reply from 172.217.14.206: bytes=32 time=14ms TTL=54
Reply from 172.217.14.206: bytes=32 time=14ms TTL=54
