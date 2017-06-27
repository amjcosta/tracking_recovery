# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import subprocess
from datetime import datetime

# This method outlined in 'Web Development with Django Cookbook' by 
# Aidas Bendoraitis contains 'shell=True', which could
# cause security issues. I'll come back to it after research.
# def get_git_changeset(absolute_path):
#     repo_dir = absolute_path
#     git_show = subprocess.Popen(
#         'git show --pretty=format:%ct --quiet HEAD',
#         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#         shell=True, cwd=repo_dir, universal_newlines=True,
#     )
#     timestamp = git_show.communicate()[0].partition('\n')[0]
#     try:
#         timestamp = datetime.utcfromtimestamp(int(timestamp))
#     except ValueError:
#         return ""
#     changeset = timestamp.strftime('%Y%m%d%H%M%S')
#     return changeset
