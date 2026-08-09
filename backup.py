import os
import subprocess
from dotenv import load_dotenv

def backup(self):

    load_dotenv()

    backup_name = input("Enter Backup file name: ")

    result = subprocess.run(
        [
            "mysqldump",
            f"-u{os.getenv('db_user')}",
            f"-p{os.getenv('db_password')}",
            "--all-databases"
        ],
        stdout=open(f"{backup_name}.sql", "w"),
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode == 0:
        print("Backup Created Successfully.")
    else:
        print("Backup Failed.")
        print(result.stderr)