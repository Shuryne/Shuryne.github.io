---
title: "提高开发效率：Tmux常用命令"
author: "Shuryne"
description: ""

date: 2019-11-16
lastmod: 2019-11-16
draft: false
weight: 100
isCJKLanguage: true

tags: ["计算机", "开发", "Pycharm"]
series: ["工具笔记"]
categories: ["杂技浅尝"]

ShowToc: true
TocOpen: false
ShowBreadCrumbs: false
searchHidden: false

---



# Tmux笔记


## 介绍
* 推荐博客：[Tmux使用手册](http://louiszhai.github.io/2017/09/30/tmux/)
* 优势：对比nohup，tmux有其独到的优势，如能够同时开多个后台运行程序等


## 使用
1. tmux new -s demo：新建一个名称为demo的会话
1. tmux kill-session -t demo：关闭demo会话
1. tmux a -t demo：进入到名称为demo的会话
1. Ctrl + b + d：断开当前会话，会话在后台运行
1. tmux内使用滚动：Ctrl + b，键入set -g mouse on
1. tmux内使用选中复制：按住alt再选中即可复制选中内容
