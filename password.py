import subprocess

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    return result.stdout

def get_profiles():
    output = run_command("netsh wlan show profiles")
    profiles = []

    for line in output.splitlines():
        if "All User Profile" in line:
            profiles.append(line.split(":")[1].strip())

    return profiles

def get_password(profile):
    output = run_command(f'netsh wlan show profile name="{profile}" key=clear')

    for line in output.splitlines():
        if "Key Content" in line:
            return line.split(":")[1].strip()

    return "No password saved"

profiles = get_profiles()

if not profiles:
    print("No saved Wi-Fi profiles found.")
else:
    print("Saved Wi-Fi Passwords:\n")

    for wifi in profiles:
        password = get_password(wifi)
        print(f"Wi-Fi Name : {wifi}")
        print(f"Password  : {password}")
        print("-" * 30)
