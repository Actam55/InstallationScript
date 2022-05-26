from datetime import datetime
from software import *
import subprocess

#Function to execute powershell command, takes command as string
def run(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    return completed

def InstallCustom():
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
                softwareList.remove(software)
        if(gameFound == False and installationChoice != 'q'):
            print(installationChoice, "does not exist, please try again")
    print("Thank you for using InstallationScript!")
    quit()

def InstallAll():
    print("Installing...")
    installTimeStart = datetime.now()
    for software in softwareList:
        run(software.installCommand)
    installTimeTotal = datetime.now() - installTimeStart
    print("All software has been installed! Installation took:", installTimeTotal.seconds, "seconds")

#This might not work as intended
def InstallChoco():
    run("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")


if __name__ == '__main__':
    print("Welcome to the installation script!")
    print("Please select the software you wish to install, all installations will be on the C drive and executables will be placed in the temp folder.")
    userInput = 'cock'
    while userInput != 'a' or userInput != 'c' or userInput != 'q':
        userInput = input("[a] All current software -- [c] Custom selection -- [q] Quit:   ")
        if(userInput == 'a'):
            InstallAll()
        elif(userInput == 'c'):
            print("-------------------------------------------")
            print("A list of avaliable software will be displayed:")
            InstallCustom()
        elif(userInput == 'q'):
            print("Thank you for using InstallationScript!")
            quit()
        print("Incorrect input, please try again.")
