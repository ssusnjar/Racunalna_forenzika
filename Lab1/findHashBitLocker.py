import socket
import subprocess

image_path = 'C:\\Users\\Sanja\\Desktop\\Forenzika\\lab1\\imageFESB.001'

bitlocker2john_cmd = f'cd C:\\Users\\Sanja\\Desktop\\Forenzika\\lab1\\john-1.9.0-jumbo-1-win64\\run && bitlocker2john -i {image_path}'
process = subprocess.Popen(bitlocker2john_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

# Print the extracted recovery key
keys = output.decode().strip().split('\n')
recovery_key = [s for s in keys if "$bitlocker$1$" in s]
print(f'BitLocker recovery key: {recovery_key[0]}')

hashcat_cmd = f'cd C:\\Users\\Sanja\\Desktop\\Forenzika\\lab1\\hashcat-6.2.6 && hashcat -m 22100 -a 3 {recovery_key[0]} "218?d?d?d?d?d"'
process = subprocess.call(hashcat_cmd, shell=True)

cracked_password = subprocess.check_output([hashcat_cmd + " --show"], shell=True).decode()
cracked_password = cracked_password.split(':')[-1]
print(f"Password : {cracked_password}")