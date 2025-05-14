import subprocess 

eww_d = ["eww", "daemon"]
trigger = ["eww", "open", "trigger", "--arg", "arg1=0"]
clock = ["eww", "open", "clock"]

def Launch():
    subprocess.run(eww_d)
    subprocess.run(trigger)
    subprocess.run(clock)

if __name__ == "__main__":
    Launch()