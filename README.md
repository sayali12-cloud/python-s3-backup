# Python S3 Backup Script

This project is a simple DevOps automation script written in Python that uploads a backup file from a local system to an AWS S3 bucket.

## Features

- Create AWS S3 bucket
- List existing S3 buckets
- Upload backup file to S3
- Automated backup storage in cloud

## Technologies Used

- Python
- AWS S3
- Boto3
- PowerShell

## Project Structure

python-for-devops
│
├── s3.backup.py
├── backups
│   └── backup_2026-03-06.tar.gz
└── README.md


## How It Works

1. Python script connects to AWS using Boto3.
2. It creates an S3 bucket if required.
3. It reads the backup file from local system.
4. The file is uploaded to AWS S3 with a new name.

## Example Code

```python
s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
---

## Requirements

## Install boto3 library:
pip install boto3

## Configure AWS Credentials
Run:
aws configure
Provide:
--- AWS Access Key
--- AWS Secret Key
--- Region
--- Output format
---
## Run the Script
python s3.backup.py

---

## ☁️ Output

Backup uploaded to S3:

## 📷 Screenshots

### Script Execution
![Script](screenshots/script-run.png)

### S3 Bucket
![Bucket](screenshots/s3-bucket.png)

### Uploaded Backup
![Upload](screenshots/backup-uploaded.png)

---

## 📌 DevOps Concepts

- AWS S3
- Automation
- Backup management
- Python scripting

---

## 👩‍💻 Author

Sayali Adsul  
DevOps & AWS Learner


