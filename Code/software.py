import subprocess

class Software:
    def __init__(self, name, installCommand):
        self.name = name
        self.installCommand = installCommand

#Check each entry to make sure they work
googleChrome = Software("Google Chrome", '(new-object System.Net.WebClient).DownloadFile("https://dl.google.com/chrome/install/latest/chrome_installer.exe", "c:/temp/chrome.exe");. c:/temp/chrome.exe;')
discord = Software("Discord", '(new-object System.Net.WebClient).DownloadFile("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "c:/temp/discord.exe");')
spotify = Software("Spotify", '(new-object System.Net.WebClient).DownloadFile("https://download.spotify.com/SpotifyFullSetup.exe", "c:/temp/spotify.exe");. c:/temp/spotify.exe;')
steam = Software("Steam", '(new-object System.Net.WebClient).DownloadFile("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "c:/temp/steam.exe");. c:/temp/steam.exe;')
obsidian = Software("Obsidian", '(new-object System.Net.WebClient).DownloadFile("https://github.com/obsidianmd/obsidian-releases/releases/download/v0.14.6/Obsidian.0.14.6.exe", "c:/temp/obsidian.exe");. c:/temp/obsidian.exe;')
clipStudioPaint = Software("Clip Studio Paint", '(new-object System.Net.WebClient).DownloadFile("https://www.clipstudio.net/gd?id=csp-install-win", "c:/temp/clipStudioPaint.exe");. c:/temp/clipStudioPaint.exe;')
oneDrive = Software("OneDrive", '(new-object System.Net.WebClient).DownloadFile("https://go.microsoft.com/fwlink/p/?LinkID=2182910&clcid=0x406&culture=da-dk&country=DK", "c:/temp/oneDrive.exe");. c:/temp/oneDrive.exe;')
vsCode = Software("Visual Studio Code", '(new-object System.Net.WebClient).DownloadFile("https://code.visualstudio.com/Download#", "c:/temp/vsCode.exe");. c:/temp/vsCode.exe;')
zip = Software("7-zip", '(new-object System.Net.WebClient).DownloadFile("https://www.7-zip.org/a/7z2200-x64.exe", "c:/temp/7zip.exe");. c:/temp/7zip.exe;')

#softwareList = [googleChrome, discord, spotify, steam, obsidian, clipStudioPaint, oneDrive, vsCode, zip]
softwareList = [googleChrome, zip]
softwareList.sort(key=lambda x: x.name)