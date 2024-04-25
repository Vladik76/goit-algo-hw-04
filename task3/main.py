from colorama import Fore
from pathlib import Path
import sys

def scan_directory(path:Path,level:int):
    """
    This function scans all object in the passed directory and show them.
    GREEN color - directory
    BLUE color - file
    
    """
    for e in path.iterdir():
        
        if e.is_dir():
            print (f"{" "*(level*3)+Fore.GREEN+e.name+Fore.RESET}") #show directory + spaces before depends on the level
            scan_directory(e.absolute(),level+1) # continuing scanning recursively
        else:
            print (f"{" "*(level*3+1)+Fore.BLUE+e.name+Fore.RESET}") #show file + spaces before depends on the level+ 1 more


def main():
    """
    Entry point. Recures 1 parameter - path to scan
    """
    passed_arguments=sys.argv
    if len(passed_arguments) > 1:
        directory_to_scan = passed_arguments[1]
        path_to_scan=Path(directory_to_scan)

        if path_to_scan.is_dir():
            scan_directory(path_to_scan,0)
        else:
            if path_to_scan.exists():
                print("Only Directory can be scanned.")
            else:
                print("The directory does not exist.")
    else:
        print("The valid path to the directory should be passed as a parameter.")
    

if __name__ == '__main__':
    main()