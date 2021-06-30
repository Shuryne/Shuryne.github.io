---
title: "提高开发效率：正确使用Git"
author: "Shuryne"
description: ""

date: 2020-07-19
lastmod: 2020-07-19
draft: false
weight: 100
isCJKLanguage: true

tags: ["计算机", "开发", "Git"]
series: ["工具笔记"]
categories: ["杂技浅尝"]

ShowToc: true
TocOpen: false
ShowBreadCrumbs: false
searchHidden: false
---



# Git笔记

## 原理
1. <https://juejin.im/post/6844903782451511303>
1. <https://zhuanlan.zhihu.com/p/66506485>
1. <https://tonybai.com/2020/04/07/illustrated-tale-of-git-internal-key-concepts/>


## 开发
1. git fetch upstream：首先将远端分支fetch到本地，此操作不会修改本地
1. git rebase upstream/master：对本地代码rebase，此操作需要解决冲突
1. git status：查看git状态
1. git add file：添加file进暂存区
1. git rm -r --cached file：从暂存区中排除file
1. git commit -m msg：将暂存区中的修改commit，并添加msg描述信息
1. git push -u upstream branch_1 : branch_2 (-f)：将本地branch_1 中的commit push到远端branch_2上，可选-f使用强制覆盖


## 设置upstream
1. git remote set-url upstream xxx
1. git remote add upstream xxx


## 一般流程
1. github初始化repo
1. 增加.gitignore文件
	* cmd：touch .gitignore
	* pycharm：new .gitignore
1. 从本地项目上传到github
	* cd /project
	* git init
	* git add.
	* git commit
	* git remote add origin path
	* git push -u origin master-xxx:master
1. 解决冲突
	* 强烈推荐使用pycharm
1. 关于pycharm中的.gitignore颜色问题：
	* 未commit&push的文件可以直接在.gitignore修改，可以立即相应文件看到颜色变暗
	* 已经commit&push的文件则需要git rm -r —cached path之后，再加入.gitignore，若不加入，则会显示红色


## 基于rebase开发流程

### 1. 基于本地master进行rebase
1. 在feature1上进行分支开发: ``gco feature1``
1. 如果有未完成的修改
	* 未完成的修改：先``git stash``保存起来，后面push结束之后再``git stash pop``恢复回来
	* 已完成的修改：``git commit``
1. 回到master拉取最新的主干内容: ``gco master && git pull origin master --rebase``
1. 回到feature1分支将master最新内容rebase:``gco feature1 && git rebase master``
1. 有冲突的话需要先解决冲突再``git add . && git rebase --continue / git rebase --abort``
1. 推送到远端:``git push -u origin feature1``

### 2. 基于远端master进行rebase
1. 一种更好的做法是不通过更新本地``master``到最新版本再rebase本地``dev``分支，而是直接将本地``dev``分支``rebase``到远端的``origin/master``
1. 然后再解决冲突``push``到远端
