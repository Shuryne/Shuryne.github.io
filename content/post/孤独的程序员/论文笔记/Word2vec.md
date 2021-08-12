---
title: Word2vec
date: 2021-06-27
draft: true
categories:
- 孤独的程序员
tags:
- word2vec
---

## Word2vec

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



参考资料



[1]:https://spaces.ac.cn/usr/uploads/2017/04/146269300.pdf "Deep Learning 实战之 word2vec"
[2]:https://arxiv.org/pdf/1310.4546.pdf "Distributed Representations of Words and Phrases and their Compositionality"
[3]:https://arxiv.org/pdf/1301.3781.pdf "Efficient Estimation of Word Representations in Vector Space"
[4]:https://github.com/renpengcheng-github/nlp/blob/master/3.word2vec/word2vec_中的数学原理详解.pdf "word2vec中的数学"



