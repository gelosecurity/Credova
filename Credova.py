import os
import re
import jsbeautifier
import sys

print('\033[32m\n▄▀▀ █▀▄ ██▀ █▀▄ ▄▀▄ █ █ ▄▀▄\033[0m')
print('\033[32m▀▄▄ █▀▄ █▄▄ █▄▀ ▀▄▀ ▀▄▀ █▀█\033[0m')

search = ["admin", "api_key", "api-key", "api_secret", "api-secret", "access_token", "access-token", "username", "password", "secret_key", "auth_token", "private_key", "public_key", "master_key", "encryption_key", "decryption_key", "client_id", "client-id", "client_secret", "client-secret", "aws_access_key", "aws-access-key", "aws_secret_key", "aws-secret-key", "s3_key", "s3-key", "s3_secret", "s3-secret", "app_id", "app-id", "app_secret", "app-secret", "AKIA"]
print ('\nSearching for ' + str(search) +'\n')

def scan_for_secrets(path):
    secrets = []
    file_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".js"):
                file_count += 1
                with open(os.path.join(root, file), "r") as f:
                    contents = f.read()
                    beautified_contents = jsbeautifier.beautify(contents)
                    contents_lines = beautified_contents.split("\n")
                    for line in contents_lines:
                        matches = re.findall(f"({'|'.join(search)})\\s*:?\\s*['\"][^'\"]+['\"]", line, re.IGNORECASE)
                        cred_pairs = re.findall(r"{\"username\":\"[^\"]+\",\"password\":\"[^\"]+\"}", line)
                        secrets += matches + cred_pairs
                        if matches + cred_pairs:
                            print(f"[SECRETS] {os.path.join(root, file)}")
                            print(f"\033[32m- {line.strip()}\033[0m")
    if file_count == 0:
        sys.exit ("[ERROR] No javascript files are found. Are you in the correct directory with a www subdirectory?")
    return secrets

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    secrets = scan_for_secrets(os.path.join(current_directory, "www"))
    if secrets:
        print("[INFO] Scan complete.")
    else:
        print("[INFO] No hardcoded secrets found.")
