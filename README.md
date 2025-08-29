<h1 align="center" style="color:red; font-family:Arial, sans-serif; text-shadow: 1px 1px #000;">Vulnex</h1>

---
<div align="center">
<img src="cve.png" alt="CVE Hunter" width="300"/>
</div>

---

CVE Hunter is a tool designed to detect security vulnerabilities by either inputting the software version or scanning the operating system and version via an IP address, providing a list of potential vulnerabilities.

# Key Features
Detect vulnerabilities based on the input software version.
Scan the operating system and version via an IP address.
Provide detailed reports on detected vulnerabilities.

# Installation
`git clone https://github.com/N3ullex/Vulnex.git`                                                                                                                                                                                                    


`cd Vulnex`  



`pip install -r requirements.txt`

[If you encounter an error use:]

`python -m pip install -r requiments.txt --break-system-packages`

                                                                                          



# Usage
`python redstrike.py`



```
┌──(root㉿kali)-[/home/kali/Desktop/CVE_HUNTER-main]
└─# python redstrike.py

              __ _     _ ___   _  _ _   ___  _  _____ ___ __
             / __\ \ / /| __| | || | | | | \| ||_   _| __| _ \  
            | (__ \ V / | _|  | __ | |_| | .` |  | | | _||   /  
             \___| \_/  |___| |_||_|\___/|_|\_|  |_| |___|_|_\        
                                           
                     [+] Developed by RedStrike0                      

1. Search Vulnrabiltice                  (example scan device if you enter os and version)
2. Search Vulnrabilitice For IP          (example scan device if you enter IP)                           
                                                                                                         
Enter your Choice: 1                                                                 
===============================================================                      
Enter name of the OS (example: Microsoft Windows, Linux): windows                    
Enter Version (example: 10 , 2.4.3): 10                                              
                                                           
===============================================================                      
Searching CPEs...                                                                    
===============================================================     
```


Select the specific CPE version and it will show you the vulnerabilities in it.


`python redstrike.py`


select 2 and input IP 

















```
Available CPEs found:
[1] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:x64:*
[2] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:*:*
[3] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:arm64:*
[4] cpe:2.3:o:microsoft:windows_10:1709:*:*:*:*:*:x86:*
[5] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2166:*:*:*:*:*:arm64:*
[6] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2107:*:*:*:*:*:arm64:*
[7] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.2045:*:*:*:*:*:arm64:*
[8] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1992:*:*:*:*:*:arm64:*
[9] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1937:*:*:*:*:*:arm64:*
[10] cpe:2.3:o:microsoft:windows_10_1709:10.0.16299.1932:*:*:*:*:*:arm64:*
===============================================================
Select a CPE number from the list: 227
===============================================================
cpe:2.3:o:microsoft:windows_10_1709:-:*:*:*:*:*:*:*
===============================================================
Please Wait...

CVE ID: CVE-2018-0824
Descriptions: A remote code execution vulnerability exists in "Microsoft COM for Windows" when it fails to properly handle serialized objects, aka "Microsoft COM for Windows Remote Code Execution Vulnerability." This affects Windows 7, Windows Server 2012 R2, Windows RT 8.1, Windows Server 2008, Windows Server 2012, Windows 8.1, Windows Server 2016, Windows Server 2008 R2, Windows 10, Windows 10 Servers.
Severity: HIGH
CVSS_ScoreV40: None
CVSS_ScoreV31: 8.8
CVSS_ScoreV30: None
===============================================================
```


It will show you the ports, their versions, the system and its version, then choose the CPE you want and it will show you the vulnerabilities in it.'''


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
