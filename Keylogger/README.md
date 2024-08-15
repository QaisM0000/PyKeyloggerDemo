# Keylogger Project

## Overview
This project implements a basic keylogger in Python. It captures keyboard inputs and logs them to a file. The project also includes (currently commented out) functionality to send the log file via email.

**Note: This tool is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical.**

## Features
- Captures keyboard inputs
- Logs keystrokes to a local file
- (Commented out) Email functionality to send log files

## Requirements
- Python 3.x
- pynput library
- smtplib (for email functionality, currently disabled)

## How It Works
1. The script listens for keyboard events using pynput.
2. It records keystrokes and writes them to a log file.
3. The log file is saved in a specified directory.
4. (Optional Add-on) Email functionality to send log files to a specified email address.

## Configuration
- `fxl`: Name of the log file
- `file_path`: Directory where the log file will be saved
- `count`: Number of keystrokes before writing to file

## Usage
1. Ensure all required libraries are installed.
2. Run the script.
3. The script will start logging keystrokes to the specified file.
4. Press 'Esc' to stop the keylogger.

## Ethical Considerations
This project is intended for educational purposes to understand system vulnerabilities and security concepts. Always obtain explicit permission before running this or any similar tool on systems you do not own or have authorization to test.

## Author
Qaisar Shaikh

## Disclaimer
The use of this software to collect data without consent is illegal and unethical. The author is not responsible for any misuse of this software.
