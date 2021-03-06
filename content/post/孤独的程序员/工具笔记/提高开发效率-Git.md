---
title: 提高开发效率（一）：正确使用Git
date: 2020-07-19
draft: false
categories:
- 孤独的程序员
tags:
- Git
---

使用Git开发过程中踩过的坑

<!--more-->

## 原理

掌握工具的核心最重要的是掌握其原理，要知其然，更知其所以然。

1. <https://juejin.im/post/6844903782451511303>
1. <https://zhuanlan.zhihu.com/p/66506485>
1. <https://tonybai.com/2020/04/07/illustrated-tale-of-git-internal-key-concepts/>

## 常用工具

工具无所谓好坏之分，基于适用场景来具体选择更加切实。以下两个工具均使用过，作为开发人员，目前偏好第二种。

### 1. SourceTree

说明：一款支持图形界面的git客户端工具

评价：适合项目管理者（<span style="color:red;">需要经常Merge别人的MR</span>），时刻保证开发分支主干清晰，提高项目开发稳定性

### 2. PyCharm

说明：将git功能集成到IDE中

评价：功能完善，也支持图形界面，适合项目开发人员（时常提交MR），方便版本控制，提高开发效率

## 基本流程

从一个新项目开始，使用git进行协同开发和版本控制的基本流程。其他具体命令（若删除暂存区文件等）可以等用到的时候再去查。

```bash
# 初始化project
git init

# 设置远端
git remote add upstream xxx

# 修改远端（若有需要）
git remote set-url upstream xxx

# 添加.gitignore文件
git add .gitignore

# 创建feature分支进行开发
git checkout -b feature

# 本地提交修改到远端 -f强制覆盖
git add .
git commit -m "message"
git push -u origin feature:feature (-f)
```

## 细说rebase

项目开发过程中经常需要协同开发，所以会经常使用rebase。目前工业界大量项目都是需要协同开发的（学术界使用场景不多），如何深刻地理解以及使用好rebase，就显得尤为重要。

rebase的意义在于，项目开发很多时候，<span style="color:red;">**保持一条清晰的主干**</span>比其他优先级更高，因为清晰的主干开发能够保证很多

笔者在开发过程中使用过以下两种rebase方式

### 1. 基于本地master进行rebase

通过保持local master是origin master的最新版本，然后通过local master对local feature进行rebase

```bash
# 切换feature进行开发
gco feature

# 暂存未完成的修改
git stash

# 提交已完成的修改
git add .
git commit -m "xxx"

# 回到master分支 以rebase模式拉取最新版本
gco master && git pull origin master --rebase

# 回到feature分支 将master最新内容rebase到当前分支
gco feature1 && git rebase master

# 若有冲突需要先解决冲突 
git rebase --continue / git rebase --abort

# 推送到远端feature分支
git push -u origin feature
```

### 2. 基于远端master进行rebase

第一种的问题在于必须经过local master，但是实际上，local master是否是最新并不是我们所需要的，因此直接绕过local master一样能达到目的，且简洁高效。

具体做法是在PyCharm中点击希望进行rebase的目标远端分支（可能不是master），点击rebase，按提示一步步解决冲突即可。这样就能够将当前local feature分支直接rebase到目标远端分支。