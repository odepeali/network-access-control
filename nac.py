class Device:
    def __init__(self, username, password, os_patched):
        self.username = username
        self.password = password
        self.os_patched = os_patched


AUTHORIZED_USERS = {
    "admin": "secure123",
    "analyst": "cyber456"
}


def authenticate(device):
    if device.username in AUTHORIZED_USERS:
        if AUTHORIZED_USERS[device.username] == device.password:
            return True
    return False


def posture_check(device):
    if not device.os_patched:
        return False
    return True


def nac_decision(device):
    print("\n--- NAC Evaluation Started ---")

    if not authenticate(device):
        print("ACCESS DENIED: Unauthorized user")
        return

    if not posture_check(device):
        print("DEVICE QUARANTINED: System not compliant")
        return

    print("ACCESS GRANTED: Full network access")


print("=== Network Access Control Simulation ===")

username = input("Username: ")
password = input("Password: ")
patched = input("Is OS patched? (yes/no): ").lower() == "yes"

device = Device(username, password, patched)

nac_decision(device)
