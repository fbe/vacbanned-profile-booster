## Features

- Proxies: Utilizes multiple proxies to make requests.
- Session Persistence: Maintains session persistence using cookies.
- User-Agent Randomization: Randomizes User-Agent headers for each request to mimic different user agents.
- Real-time Updates: Provides real-time updates on the request status, including successful and failed attempts.

## Requirements

- Python 3.x
- requests library
- fake_useragent library
- colorama library

## Usage

1. Clone the repository or download `main.py`.
2. Install the required libraries: `pip install requests fake_useragent colorama`.
3. Prepare a list of proxies in `proxies.txt` (one proxy per line, in the format `ip:port`).
3.1. Additionally choose if you don't want to delete the proxy upon request by changing `REMOVE_PROXY` to `False`
4. Run the program: `python main.py`.
5. Enter the SteamID you want to boost when prompted.
6. Enter the number of retries (the number of VAC banned check attempts) when prompted.
7. Sit back and let vbBoost work! Real-time updates on the request status will be displayed.

## Disclaimer

vbBoost is intended for educational and testing purposes only. The use of this program for any malicious activities or in violation of any terms of service is strictly prohibited. The author is not responsible for any consequences arising from the use of this program.
