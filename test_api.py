from github import Github
import os
from pprint import pprint


token_value = "7764489ab33c5e5ba17ae641b8d86dfbbd2e52a3"
repo_path = "Monish-Samuel/rest-api"

print("Open Issues :")
token = os.getenv(token_value)
g = Github(token)
repo = g.get_repo(repo_path)
open_issue = repo.get_issues(state='open')
pprint(open_issue.get_page(0))
print()

print('Closed Issues:')
token = os.getenv(token_value)
g = Github(token)
repo = g.get_repo(repo_path)
closed_issue = repo.get_issues(state='closed')
pprint(closed_issue.get_page(0))
print()


print('All Issues:')
token = os.getenv(token_value)
g = Github(token)
repo = g.get_repo(repo_path)
all_issue = repo.get_issues(state='all')
pprint(all_issue.get_page(0))

