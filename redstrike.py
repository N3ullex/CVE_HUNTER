from banner import display_banner
from cpe_search import search_cpe
from cve_search import search_cve
from colorama import Style , Fore
from nmap1 import scan_cpe

def display1_vulnrabilities(cpes):   
    for idx, cpew in enumerate(cpes, start=1):
        
        print(f"{idx}.{cpew.cpeName}{Style.RESET_ALL}")
        
    try:
        print ("===============================================================")
        choice = int(input("\nSelect Number To Scan (Or Select 0 to Exit): "))
        if choice == 0:
            return False , None
        if 1 <= choice <= len(cpes):
            selected_cpe =  cpes[choice - 1].cpeName
            print("==========================================================================================================")
            print (f"[+] Scanning   :  [{selected_cpe}]")
            print("==========================================================================================================")
    except (ValueError, IndexError):
        print(" Command Error !")
        return display1_vulnrabilities(cpes)
              
        
    cves = search_cve(selected_cpe)
    if not cves:
        print("[-] Not Found Vulnrability.")
        return 
   
    
def cve_run(cpes):
    global selected_cpe
    for idx, cpew in enumerate(cpes, start=1):
        
        print(f"{idx}. {cpew} ")
        
    try:
        print ("===============================================================")
        choice = int(input("\nSelect Number To Scan (Or Select 0 to Exit): "))
        if choice == 0:
            return False , None
        if 1 <= choice <= len(cpes):
            selected_cpe =  cpes[choice - 1]
            print("================================================================================================")
            print (f"[+] Scanning   :  [{selected_cpe}]")
            print("================================================================================================")
    except (ValueError, IndexError):
        print(" Command Error !")
        return cve_run(cpes)

    cve = search_cve(selected_cpe)
    if not cve:
       print("[-] Not Found Vulnrability")
       return
    print("found cve")

def main():
    

    while True:
        display_banner()
        print  (     f"\n{Fore.WHITE}{Style.DIM}"        "1. Search Vulnrabiltice " f"                 (example scan device if you enter os and version)")
        print (    f"{Fore.WHITE}{Style.DIM}"          "2. Search Vulnrabilitice For IP         " ,   "(example scan device if you enter IP)"   )
        choice = input("\nEnter your Choice: ").strip()

        if choice == "1":
            print("===============================================================")
            os_name = input("Enter name of the OS (example: Microsoft Windows, Linux): ").strip().lower()
            version = input("Enter Version (example: 10 , 2.4.3): ").strip().lower()
            
            while True:
                print("")
                print("===============================================================")
                print ("Searching CPEs... ")
                print ("===============================================================")
                cpes = search_cpe(os_name, version)
                    
                if not cpes:
                       print(f"{Fore.RED}Not Found CPEs:{Style.RESET_ALL}")
                       choice2 = input("Click 1 To Back and 2 to Exit: ").strip()
                       if choice2 == '1':
                          return main()
                       elif choice2 == '2':
                            print("Good Bye :)")
                            return None
                     
                continue_searching = display1_vulnrabilities(cpes)
                if not continue_searching:
                   break

            action = input("\nEnter 'back' to go back or exit to quite: ")
            if action == 'exit':
               print("Exiting the tool...")
               break
            elif action != 'back':
               print("Invalid input, please enter 'back' or 'exit' to quit: ").strip().lower()
               continue 
        
        elif choice == "2":
             ip = input("\nEnter IP: ").strip()
             print("===============================================================")
             print (f"[+] Scanning : {ip}")
             print("===============================================================")
             cpes = scan_cpe(ip)
             print("===============================================================")
             print (cpes)
             print("===============================================================")
             print("Please Wait...")
             if not cpes:
                 print(f"{Fore.RED}Sorry Not Found CPEs{Style.RESET_ALL}")
                 choice1 = input("If you want to check the service versions, type back and choose number 1. ").strip()
                 if choice1 == 'back':
                    return main()
                 else:
                     return None
             cve = search_cve(cpes)
             if not cve:
                print("[-] Not Found Vulnrability")
                return
             print("found cve")

if __name__ == "__main__":
    main()
