# ipaddress
Python 3 script to change a Windows 10 machine ip address 
How to run:
- In an elevated Command Prompt: python path-to-script.../AddressChanger.py

Known Limitations: 
- in an attempt to avoid external libraries and hardcoded variables, the script relies heavily on the cmd prompt returns(ipconfig, netsh...) 
(using of a better library or package could have provided these values? more research needed, time constraint)
- parsing the cmd outputs (network adapter name, subnet mask, default gateway) might be OS and version dependant (might not work on a WIN7/8 machine).
- absence of user input validation for the new ip address. (time constraint)

