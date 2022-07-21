from datetime import datetime
from software import *
import subprocess

#Function to execute powershell command, takes command as string
def run(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    return completed

def InstallCustomDownloader():
    installationChoice = 'cock'
    while installationChoice != 'q': 
        gameFound = False
        for software in softwareList:
            print(software.name)
        installationChoice = input("Please type the name of software you wish to install. [q] To exit: ").lower()
        for software in softwareList:
            if(software.name.lower() == installationChoice.lower()):
                gameFound = True
                print("Installing", installationChoice, "...")
                installTimeStart = datetime.now()
                run(software.installCommand)
                installTimeTotal = datetime.now() - installTimeStart
                print(installationChoice, "has been installed! Installation took:", installTimeTotal.seconds, "seconds")
                print("-------------------------------------------\n")
                softwareList.remove(software)
        if(gameFound == False and installationChoice != 'q'):
            print(installationChoice, "does not exist, please try again:\n")
            print("-------------------------------------------\n")
    print("Thank you for using InstallationScript!")
    quit()

def InstallAllDownloader():
    installTimeTotal = datetime.now()
    for software in softwareList:
        installTimeStart = datetime.now()
        print("Installing", software.name, "...")
        run(software.installCommand)
        installTimeEnd = datetime.now() - installTimeStart
        print(software.name, "has been installed! Installation took:", installTimeEnd.seconds, "seconds")
        print("-------------------------------------------\n")
    installTimeTotalEnd = datetime.now() - installTimeTotal
    print("All software has been installed! Installation took:", installTimeTotalEnd.seconds, "seconds\n")

if __name__ == '__main__':
    print("Welcome to the installation script!")
    print("Please select the software you wish to install, all installations will be on the C drive and executables will be placed in the temp folder.\n")
    userInput = 'cock'
    while userInput != 'q' or userInput != 'a' or userInput != 'c':
        userInput = input("[a] All current software -- [c] Custom selection -- [q] Quit:   ")
        if(userInput == 'a'):
            InstallAllDownloader()
            print("Thank you for using InstallationScript!")
            quit()
        elif(userInput == 'c'):
            print("-------------------------------------------")
            print("A list of avaliable software will be displayed:")
            InstallCustomDownloader()
        elif(userInput == 'q'):
            print("Thank you for using InstallationScript!")
            quit()
        print("Invalid input, please try again.")
