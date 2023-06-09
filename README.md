# Portier-ADPS

<p align="center">
   <img src="https://github.com/fromgodd/portier-adps/assets/97128346/3e400d10-1247-45a3-ac31-fc56f8aa1073">
</p>

Portier-ADPS is an asynchronous port scanner built using Python. It allows you to scan for open, closed, and blocked ports on a target system.

## Features

- Asynchronous scanning: Portier-ADPS utilizes asyncio and aiohttp to perform concurrent port scanning, making the scanning process faster and more efficient.
- Customizable port range: You can specify the range of ports to scan, allowing you to target specific ports or a range of ports.
- Interactive user input: Portier-ADPS prompts the user to input the target host and port range, providing an interactive and user-friendly experience.
- Colorful output: The scan results are displayed in a colorful manner, with open ports highlighted in green and closed or blocked ports in red.
- ASCII banner: Portier-ADPS presents a stylish ASCII banner at the start, adding visual appeal to the program.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/fromgodd/portier-adps.git
   ```

2. Navigate to the project directory:

   ```
   cd portier-adps
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the port scanner:

   ```
   python portier-adps.py
   ```

2. Follow the prompts to enter the target host and port range.

3. Sit back and wait for the scan to complete. The results will be displayed on the console.

## Example

Here is an example usage of Portier-ADPS:

```
$ python portier-adps.py

    _    ____  ____  ____  
   / \  |  _ \|  _ \/ ___| 
  / _ \ | | | | |_) \___ \ 
 / ___ \| |_| |  __/ ___) |
/_/   \_\____/|_|   |____/ 

Welcome to the Async Port Scanner!
Please provide the following details:

Enter the target host: 192.168.0.1
Enter the starting port: 1
Enter the ending port: 100

Scanning ports...

Port 22 is closed
Port 80 is open
Port 443 is open

Scan completed!

```

In this example, we scanned the IP address `192.168.0.1` within the port range of `1` to `100`. The scan results showed that port `22` was closed, while ports `80` and `443` were open.

## Contributing

Contributions to Portier-ADPS are welcome! If you encounter any issues, have suggestions, or want to contribute enhancements, please open an issue or submit a pull request on the [Portier-ADPS GitHub repository](https://github.com/fromgodd/portier-adps).

## License

Portier-ADPS is licensed under the [MIT License](LICENSE).
