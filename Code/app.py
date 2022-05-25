import subprocess

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def ScriptCommandTest():
    hello_command = "Write-Host 'Hello Wolrd!'"
    hello_info = run(hello_command)
    if hello_info.returncode != 0:
        print("An error occured: %s", hello_info.stderr)
    else:
        print("Hello command executed successfully!")


def InstallCustom():
    print()

if __name__ == '__main__':
    print("Welcome to the installation script!")
    print("Please select the software you wish to install, all installations will be on the C drive and executables will be placed in the temp folder.")
    installationChoice = input("[a] All current software -- [c] Custom selection:   ")

    if(installationChoice == 'a'):
        ScriptCommandTest()
    elif(installationChoice == 'c'):
        InstallCustom()
    



