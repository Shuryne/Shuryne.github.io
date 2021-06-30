---
title: "XLNet"
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



## XLNet

1. 提出背景：
   * 自回归LM只能利用上文，不能利用上下文
   * 自编码DAE能利用上下文，但是[mask]会导致训练应用过程不一致
     方法：
   * 排列语言模型
   * 双流自注意力机制：query流、content流

