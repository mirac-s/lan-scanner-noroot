# LAN Scanner (No Root Required)

👍 **NO ROOT**

A lightweight Python script for scanning devices on a local network (LAN) using multi-threading. No root or administrative privileges are required.

## Setup
```
git clone https://github.com/mirac-s/lan-scanner-noroot
```
## Features
- Fast, concurrent scanning using threads
- Detects devices by attempting TCP connection (port 80)
- Shows connection status: Accepted, Refused, Timeout, or Unreachable
- No need for `nmap` or root access
- Works and Coded with Python 

## Usage

```
python scanner.py <CIDR Notation>
```
Example:

`python scanner.py 192.168.1.0/24`

License

This project is licensed under the MIT License.

---

## **5. LICENSE (MIT License)**

```text
MIT License

Copyright (C) 2025 mirac-s

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
