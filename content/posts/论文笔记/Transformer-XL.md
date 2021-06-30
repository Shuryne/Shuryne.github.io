---
title: "Transformer-XL"
author: "Shuryne"
description: ""

date: 2021-06-27
lastmod: 2021-06-27
draft: true
weight: 100
isCJKLanguage: true

tags: ["计算机", "NLP"]
series: ["论文笔记"]
categories: ["杂技浅尝"]

ShowToc: true
TocOpen: false
ShowBreadCrumbs: false
searchHidden: false
---



## Transformer-XL

1. 解决长距离依赖问题
   * 片段级递归机制：解决编码长距离依赖和上下文碎片化
   * 相对位置编码机制：实现片段级递归机制，解决可能出现的时序混淆问题