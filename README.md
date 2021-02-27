# Keylogger
Simple keylogger made with pynput module

# Setup
By default the server ip is localhost (127.0.0.1), it will only work on local. If you want to use another computer to record keypresses, change the ip in `src/client.py` to the host IPv4 address.

# Usage
Run `run.bat` to build the .EXE file. Send that file to the computer you want to keylog. Run `src/server.py` to start the socket server and receive keypresses from client. You can run the `killswitch.bat` if you want to kill the .EXE process.


    ██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗     ██╗   ██╗  ██╗
    ██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗    ██║   ██║ ███║
    █████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝    ██║   ██║ ╚██║
    ██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝  ██║
    ██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║     ╚████╔╝██╗██║
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝ ╚═╝╚═╝                                                                                          

---
Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.

