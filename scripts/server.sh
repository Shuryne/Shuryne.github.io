#!/usr/bin/env bash

# 自动化 front matter
python /Users/gungnir/Google/hugo-blog/scripts/front_matter_set.py

# 文章部署
hugo

# git update
git add .
git commit
git push -u origin master