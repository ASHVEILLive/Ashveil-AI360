# render_engine.py

import os
from datetime import datetime

class RenderEngine:
    def __init__(self, command_folder="./commands"):
        self.command_folder = command_folder
        os.makedirs(self.command_folder, exist_ok=True)

    def write_command(self, command):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(self.command_folder, f"{timestamp}.cmd")
        with open(file_path, 'w') as f:
            f.write(command)
        print(f"[RenderEngine] Command written to {file_path}")
        return file_path

    def get_latest_command(self):
        files = sorted(
            [f for f in os.listdir(self.command_folder) if f.endswith(".cmd")],
            reverse=True
        )
        if files:
            latest_file = files[0]
            with open(os.path.join(self.command_folder, latest_file), 'r') as f:
                command = f.read().strip()
            return command
        return None

# Example usage (can be removed in production)
if __name__ == "__main__":
    engine = RenderEngine()
    engine.write_command("rotate left 15")
    print("Latest command:", engine.get_latest_command())
