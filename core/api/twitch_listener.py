# AshveilBot: The Ultimate Twitch-Controlled Unity 360 Bot

import socket
import threading
import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class TwitchListener:
    def __init__(self, server, port, nickname, token, channel, callback):
        self.server = server
        self.port = port
        self.nickname = nickname
        self.token = token
        self.channel = channel
        self.callback = callback
        self.sock = socket.socket()

    def connect(self):
        self.sock.connect((self.server, self.port))
        self.sock.send(f"PASS {self.token}\r\n".encode('utf-8'))
        self.sock.send(f"NICK {self.nickname}\r\n".encode('utf-8'))
        self.sock.send(f"JOIN #{self.channel}\r\n".encode('utf-8'))
        print(f"[TwitchListener] Connected to #{self.channel}")

    def listen(self):
        def listen_loop():
            while True:
                resp = self.sock.recv(2048).decode('utf-8')
                if resp.startswith('PING'):
                    self.sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
                elif len(resp) > 0:
                    print(f"[TwitchListener] {resp.strip()}")
                    if "PRIVMSG" in resp:
                        parts = resp.split("PRIVMSG")
                        if len(parts) > 1:
                            message = parts[1].split(":", 1)[-1].strip()
                            self.callback(message)

        thread = threading.Thread(target=listen_loop)
        thread.daemon = True
        thread.start()

# Unity Interface Launcher

def launch_unity_scene():
    unity_project_path = "./unity360"
    unity_exe_path = os.path.join(unity_project_path, "Builds/Windows360/360Viewer.exe")
    print(f"[Unity] Launching Unity 360 scene: {unity_exe_path}")
    subprocess.Popen([unity_exe_path])

# Unity Command Router

def send_command_to_unity(cmd):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    commands_folder = "./commands"
    os.makedirs(commands_folder, exist_ok=True)
    file_path = os.path.join(commands_folder, f"{timestamp}.cmd")
    with open(file_path, 'w') as f:
        f.write(cmd)
    print(f"[Unity] Command written to {file_path}")

# Command Routing

def handle_command(command):
    print(f"[Command] Received: {command}")
    if command.lower() == "start360":
        launch_unity_scene()
    elif command.lower().startswith("rotate"):
        send_command_to_unity(f"{command}")
    elif command.lower().startswith("zoom"):
        send_command_to_unity(f"{command}")
    elif command.lower() == "pause":
        send_command_to_unity("pause")
    elif command.lower() == "resume":
        send_command_to_unity("resume")
    else:
        print(f"[Command] Unknown command: {command}")

# Main Entrypoint

if __name__ == "__main__":
    listener = TwitchListener(
        server="irc.chat.twitch.tv",
        port=6667,
        nickname="AshveilBot",
        token=os.getenv("TWITCH_OAUTH_TOKEN"),
        channel="ashveil",
        callback=handle_command
    )
    listener.connect()
    listener.listen()

    print("[Main] Listening for Twitch commands. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[Main] Disconnected from Twitch.")
