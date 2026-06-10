\# Binance Futures Testnet Trading Bot



\## Overview



This project is a Python-based Binance Futures Testnet Trading Bot.



The bot supports:



\- MARKET Orders

\- LIMIT Orders

\- BUY and SELL Operations

\- Input Validation

\- Logging

\- Error Handling



\---



\## Requirements



\- Python 3.12

\- python-binance



\---



\## Installation



Install dependencies using:



```bash

pip install -r requirements.txt

```



\## Configuration



Add your Binance Futures Testnet API credentials in client.py:



```python

API\_KEY = "YOUR\_API\_KEY"

API\_SECRET = "YOUR\_SECRET\_KEY"

```



\## Usage



\### MARKET Order



```bash

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

```



\### LIMIT Order



```bash

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

```



\## Logging



Logs are stored in:



```text

logs/bot.log

```



\## Project Structure



```text

trading\_bot/

│

├── cli.py

├── client.py

├── validators.py

├── logging\_config.py

├── requirements.txt

├── README.md

└── logs/

&#x20;   └── bot.log

```



\## Assumptions



\- User has a Binance Futures Testnet account.

\- API credentials are valid.

\- Testnet account contains sufficient virtual funds.

