# Sites Monitoring Utility

A script enabling you to check sites health. Site is healthy if it responses HTTP status 200 and its domain name expires in more than 1 month.

# How to install

Python 3 should be already installed. Then use pip to install dependencies:
```bash
pip install -r requirements.txt # alternatively try pip3
```
It's recommended to use [virtual environment](https://docs.python.org/3/tutorial/venv.html) for better isolation.

# How to use

A launching on Linux:
```bash
python check_sites_health.py urls.txt # alternatively try python3
http://google.com is healthy
http://vk.com is healthy
http://yandex.ru is healthy
http://rtthtrhrhfhgfhd.org: unable to fetch expiration date
http://rambler.ru is healthy
localhost: unable to fetch expiration date
127.0.0.1: unable to fetch expiration date
http://qwerty.com is healthy
http://127.0.0.1: unable to fetch expiration date
```
The launching on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
