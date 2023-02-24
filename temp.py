import os
from github import Github

access_token = os.environ.get('GITHUB_TOKEN')
# print(access_token)



#access_token = "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"
github_username = "ihoraryku"
github_repo_name = "parce_nginx_log_and_send_to_github"

g = Github(access_token)
user = g.get_user(github_username)
repo = user.get_repo(github_repo_name)

# create a new file
file_path = "example.txt"
file_contents = "Hello, world!"
commit_message = "Add example file"
branch_name = "main"

repo.create_file(file_path, commit_message, file_contents, branch=branch_name)
