import csv
import os
from github import Github

# Path to the nginx log file
log_file_path = "nginx.log"

# Path to the CSV file
csv_file_path = "csv/nginx.csv"

# Parse the log file and convert it to CSV
with open(log_file_path, "r") as log_file, open(csv_file_path, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["IP Address", "Timestamp", "HTTP Method", "HTTP Path", "HTTP Version", "HTTP Status Code", "HTTP Response Size", "HTTP Referrer", "User Agent"])
    for line in log_file:
        parts = line.split()
        ip_address = parts[0]
        timestamp = parts[3][1:]
        http_method = parts[5][1:]
        http_path = parts[6]
        http_version = parts[7][:-1]
        http_status_code = parts[8]
        http_response_size = parts[9]
        http_referrer = parts[10][1:-1]
        user_agent = " ".join(parts[11:])[1:-2]
        csv_writer.writerow([ip_address, timestamp, http_method, http_path, http_version, http_status_code, http_response_size, http_referrer, user_agent])


# Push the CSV file to GitHub
#access_token = os.environ.get('GITHUB_TOKEN')
access_token = "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"
#github_repo_name = "parce_nginx_log_and_send_to_github"
github_username = "ihoraryku"
github_repo_name = "parce_nginx_log_and_send_to_github"
github_file_path = "csv/nginx.csv"
github_commit_message = "Added changes"
github_branch_name = "main"

g = Github(access_token)
user = g.get_user(github_username)
repo = user.get_repo(github_repo_name)
contents = repo.get_contents("")
with open(csv_file_path, "r") as csv_file:
    file = csv_file.read()
repo.create_file(github_file_path, github_commit_message, file, branch=github_branch_name)
print("CSV file uploaded to GitHub successfully.")