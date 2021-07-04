---
ShowBreadCrumbs: false
TocOpen: false
author: Shuryne
categories:
- 孤独的程序员
date: 2021-06-27
description: ''
draft: true
isCJKLanguage: true
searchHidden: false
showToc: false
tags:
- 论文笔记
title: Transformer-XL：更长？更强！
weight: 100
---

## Transformer-XL

1. 解决长距离依赖问题
   * 片段级递归机制：解决编码长距离依赖和上下文碎片化
   * 相对位置编码机制：实现片段级递归机制，解决可能出现的时序混淆问题