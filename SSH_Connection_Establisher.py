import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="cryptography")

import paramiko  # SSH library

def ssh_connect(target_ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target_ip, username=username, password=password, timeout=5)
        print(f"Success! Connected to {target_ip} with Username: {username}, Password: {password}")
    except paramiko.AuthenticationException:
        print(f"Authentication failed for Username: {username}, Password: {password}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

# Main
target = input("Enter target IP: ").strip()
user = input("Enter SSH username: ").strip()
password = input("Enter the known password: ").strip()

ssh_connect(target, user, password)
