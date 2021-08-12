---
title: 提高开发效率（三）：好用的Pycharm
date: 2021-06-02
draft: false
categories:
- 孤独的程序员
tags:
- PyCharm
---

记录并积累自己的PyCharm使用习惯

<!--more-->

## 远端开发

### 1. SSH Configuration

1. 本地在.ssh/config中设置hosts
1.  Pycharm中设置ssh configuration（如果设置了Hostname可以直接用）

### 2. Python Interpreter

1. 最好为不同的project配置不同的python Interpreter，避免不同项目对包依赖不一致导致冲突
1. 尽量使用远端服务器Python Interpreter
1. 使用ssh方式而不是Deployment Configuration设置Python Interpreter

## 项目配置

1. 设置requirements.txt
1. 设置file template: 添加作者、时间、介绍等
1. 设置注释风格为Google
1. 设置save action: 保存时自动排版规范化并上传至远端
1. 一般习惯在项目内部创建同名文件夹放核心代码文件，CI/CD、docker以及数据文件等放在外部

## 其他

### 1. 快捷键

1. option + enter：快速点出错误提示并进行修改
1. cmd + [：回到上一个文件光标处


### 2. refactor

1. 统一更新变量名
1. 提取函数到新文件中
