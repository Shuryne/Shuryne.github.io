#!/usr/bin/env bash

# 自动化 front matter
python scripts/front_matter_set.py

# 删除已有的部署文件
rm -r docs/*

# 文章部署
hugo

# git update
git add .
git commit -m "add new file"
git push -u origin master