import subprocess

class Software:
    def __init__(self, name, installCommand):
        self.name = name
        self.installCommand = installCommand

#Maybe have a seperate place for all of the software, as it will be a big list
#Check each entry to make sure they work
googleChrome = Software("Google Chrome", '(new-object System.Net.WebClient).DownloadFile("https://dl.google.com/chrome/install/latest/chrome_installer.exe", "c:/temp/chrome.exe");. c:/temp/chrome.exe /silent /install;')


#discord = Software("Discord", '(new-object System.Net.WebClient).DownloadFile("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "c:/temp/discord.exe");. c:/temp/discord.exe /silent /install;')
discord = Software("Discord", '(new-object System.Net.WebClient).DownloadFile("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "c:/temp/discord.exe");')

spotify = Software("Spotify", '(new-object System.Net.WebClient).DownloadFile("https://download.spotify.com/SpotifyFullSetup.exe", "c:/temp/spotify.exe");. c:/temp/spotify.exe /silent /install;')

steam = Software("Steam", '(new-object System.Net.WebClient).DownloadFile("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "c:/temp/steam.exe");. c:/temp/steam.exe /silent /install;')

obsidian = Software("Obsidian", '(new-object System.Net.WebClient).DownloadFile("https://github.com/obsidianmd/obsidian-releases/releases/download/v0.14.6/Obsidian.0.14.6.exe", "c:/temp/obsidian.exe");. c:/temp/obsidian.exe /silent /install;')

clipStudioPaint = Software("Clip Studio Paint", '(new-object System.Net.WebClient).DownloadFile("https://www.clipstudio.net/gd?id=csp-install-win", "c:/temp/clipStudioPaint.exe");. c:/temp/clipStudioPaint.exe /silent /install;')

oneDrive = Software("OneDrive", '(new-object System.Net.WebClient).DownloadFile("https://go.microsoft.com/fwlink/p/?LinkID=2182910&clcid=0x406&culture=da-dk&country=DK", "c:/temp/oneDrive.exe");. c:/temp/oneDrive.exe /silent /install;')

vsCode = Software("Visual Studio Code", '(new-object System.Net.WebClient).DownloadFile("https://code.visualstudio.com/Download#", "c:/temp/vsCode.exe");. c:/temp/vsCode.exe /silent /install;')

windowsTerminal = Software("Windows Terminal", "choco install microsoft-windows-terminal")


#Consider alphabetical sort
softwareList = [googleChrome, discord, spotify, steam, obsidian, clipStudioPaint, oneDrive, vsCode]

#Function to execute powershell command, takes command as string
def run(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    return completed


def InstallCustom():
    for software in softwareList:
        print(software.name)

    installationChoice = input("Please type the name of software you wish to install: ").lower()
    for software in softwareList:
        if(software.name.lower() == installationChoice):
            print(installationChoice, "exists")
            run(software.installCommand)
            softwareList.remove(software)
        else:
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
