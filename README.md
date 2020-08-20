# Simple http get/post hooks server

This server can hook all headers and post/get data, also in can specify response data for sharing payloads.
This server is written in pure python3, so it doesn't have any dependencies.

## Usage

`python3 hook.py` [-i IP] [-p PORT] [-d TEXT | -f PATH]

```text
  -i IP, --ip IP        set server ip (default: 0.0.0.0)
  -p PORT, --port PORT  set server port (default: 80)
  -d TEXT, --data TEXT  specify response data (default: "Hello from D00Movenok")
  -f PATH, --file PATH  specify response data from file
```

Remember! By default it listens 0.0.0.0 on port 80
