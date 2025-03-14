# CVE_HUNTER

CVE Hunter is a tool designed to detect security vulnerabilities by either inputting the software version or scanning the operating system and version via an IP address, providing a list of potential vulnerabilities.

# Key Features
Detect vulnerabilities based on the input software version.
Scan the operating system and version via an IP address.
Provide detailed reports on detected vulnerabilities.

# Installation
`git clone https://github.com/RedStrike0/CVE_HUNTER.git`                                                                                                                                                                                                    


`cd CVE_HUNTER`  



`pip install -r requirements.txt`

                                                                                          
┌──(root㉿kali)-[/home/kali/Desktop/CVE_HUNTER-main]
└─# python redstrike.py

              __ _     _ ___   _  _ _   ___  _  _____ ___ __
             / __\ \ / /| __| | || | | | | \| ||_   _| __| _ \  
            | (__ \ V / | _|  | __ | |_| | .` |  | | | _||   /  
             \___| \_/  |___| |_||_|\___/|_|\_|  |_| |___|_|_\        
                                           
                     [+] Developed by RedStrike0                      

1. Search Vulnrabiltice                  (example scan device if you enter os and version)
2. Search Vulnrabilitice For IP          (example scan device if you enter IP)                           
                                                                                                         
Enter your Choice: 2                                                                                     
                                                                                                         
Enter IP: 192.185.52.104                                                                                 
===============================================================                                          
[+] Scanning : 192.185.52.104                                                                            
===============================================================                                          
                                                                                                         
Detected OS candidates for 192.185.52.104:                                           
OS: Linux 3.4 - Accuracy: 96%
OS: Linux 2.6.32 - Accuracy: 91%
OS: Linux 3.5 - Accuracy: 91%
OS: Linux 4.2 - Accuracy: 91%
OS: Synology DiskStation Manager 5.1 - Accuracy: 91%
OS: Linux 3.10 - Accuracy: 90%
OS: Linux 2.6.32 or 3.10 - Accuracy: 90%
OS: Linux 2.6.39 - Accuracy: 90%
OS: Linux 3.10 - 3.12 - Accuracy: 90%
OS: Linux 4.4 - Accuracy: 90%

Cleaned OS Name: linux 3.4

Most likely OS: linux 3.4 with 96% accuracy
Port: 21 | State: open | Product: Pure-FTPd | Version: 
Port: 22 | State: open | Product: OpenSSH | Version: 7.4
Port: 25 | State: filtered | Product:  | Version: 
Port: 26 | State: open | Product: Exim smtpd | Version: 4.98.1
Port: 53 | State: open | Product: Unbound | Version: 
Port: 80 | State: open | Product: Apache httpd | Version: 
Port: 110 | State: open | Product: Dovecot pop3d | Version: 
Port: 135 | State: filtered | Product:  | Version: 
Port: 143 | State: open | Product: Dovecot imapd | Version: 
Port: 161 | State: filtered | Product:  | Version: 
Port: 443 | State: open | Product: Apache httpd | Version: 
Port: 445 | State: filtered | Product:  | Version: 
Port: 465 | State: open | Product: Exim smtpd | Version: 4.98.1
Port: 587 | State: open | Product: Exim smtpd | Version: 4.98.1
Port: 993 | State: open | Product: Dovecot imapd | Version: 
Port: 995 | State: open | Product: Dovecot pop3d | Version: 
Port: 999 | State: filtered | Product:  | Version: 
Port: 1080 | State: filtered | Product:  | Version: 
Port: 1300 | State: filtered | Product:  | Version: 
Port: 2222 | State: open | Product: OpenSSH | Version: 7.4
Port: 3306 | State: open | Product: MySQL | Version: 5.7.23-23
Port: 4444 | State: filtered | Product:  | Version: 
Port: 4662 | State: filtered | Product:  | Version: 
Port: 6346 | State: filtered | Product:  | Version: 
Port: 6699 | State: filtered | Product:  | Version: 

Service version distribution:
Product: OpenSSH, Version: 7.4 - 2 occurrences (33.33%)
Product: Exim smtpd, Version: 4.98.1 - 3 occurrences (50.00%)
Product: MySQL, Version: 5.7.23-23 - 1 occurrences (16.67%)




# Usage
`python redstrike.py`



select 1 and input OS and Version



Select the specific CPE version and it will show you the vulnerabilities in it.

`python redstrike.py`



select 2 and input IP 



It will show you the ports, their versions, the system and its version, then choose the CPE you want and it will show you the vulnerabilities in it.'''
