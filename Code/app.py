from datetime import datetime
from software import *
import subprocess

#Function to execute powershell command, takes command as string
def run(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    return completed


def InstallCustom():
    gameFound = False
    

    for software in softwareList:
        print(software.name)
    installationChoice = input("Please type the name of software you wish to install: ")
    if(installationChoice == 'q'):
        print("Thank you for using InstallationScript!")
        quit()
    for software in softwareList:
        if(software.name.lower() == installationChoice.lower()):
            gameFound = True
            print("Installing", installationChoice, "...")
            installTimeStart = datetime.now()
            run(software.installCommand)
            installTimeTotal = datetime.now() - installTimeStart
            print(installationChoice, "has been installed! Installation took:", installTimeTotal.seconds, "seconds")
            print("###############")
            softwareList.remove(software)
            InstallCustom()
    if(gameFound == False):
        print(installationChoice, "does not exist, please try again")
        InstallCustom()


#This might not work as intended
def InstallChoco():
    run("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")


if __name__ == '__main__':
    print("Welcome to the installation script!")
    print("Please select the software you wish to install, all installations will be on the C drive and executables will be placed in the temp folder.")
    installationChoice = input(
        "[a] All current software -- [c] Custom selection:   ")

    if(installationChoice == 'a'):
        print("Not ready yet")
    elif(installationChoice == 'c'):
        print("-------------------------------------------")
        print("A list of avaliable software will be displayed:")
        InstallCustom()
