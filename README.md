# CertUtil - encode & decode
An automation for multiple encode \ decode

## Prerequisites: ##
* python 2.7
  
## Installing ##
```sh
git clone https://github.com/ronbenbenishti/CertUtil-encode-decode.git
```

## How to use ##
```sh
Syntax: python cert.py <MODE> <PATH> <PARAM1>

MODES:  -en <PATH> <LOOPS_COUNT>
        -de <PATH> <ORIGINAL_EXTENSION> (optional)

Example: 'python cert.py -en C:\users\Ron\Desktop\nc.exe 20'
         'python cert.py -de C:\users\Ron\Desktop\nc.cert20 exe'
```
#### or
```sh
python cert.py
```
