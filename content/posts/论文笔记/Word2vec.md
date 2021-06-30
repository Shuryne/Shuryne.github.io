---
title: "Word2vec"
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



### Word2vec

1. 基于局部预料&窗口上下文
1. 提出背景：采用分布式表示替代one-hot编码
1. 方法
   * CBOW：已知周围词预测中心词，小预料表现好
   * Skip-Gram：已知中心词预测周围词，大预料表现好
1. 改进
   * 输入层到隐藏层：embedding直接sum作为隐藏层
   * 隐藏层到输出层
     * 分层softmax：输出建立哈夫曼树，O(V)->O(logV)，高频词更接近树根
     * 负采样：负样本大大减少，每个训练样本只更新一部分权重参数，将原本多分类softmax变成了多个二分类

