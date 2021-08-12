---
title: 机器翻译：Seq2Seq
date: 2018-11-12
draft: false
categories:
- 孤独的程序员
tags:
- seq2seq

---

关于Seq2Seq

<!--more-->

#### 1. Sequence to Sequence Learning with Neural Networks

* `encoder`以及`decoder`都采用`LSTM`模型
* 模型很简单，就是最普通的多层`LSTM`
* 实现的不同之处：
    * 用两种不同的`LSTM`，一种处理输入序列，一种处理输出序列；以可忽略的计算成本增加参数数量，同时在多个语言对上训练`LSTM`；
    * 更深的`LSTM`会比浅的效果更好，故论文模型选择了四层；
    * 将输入的序列翻转之后作为输入效果提升；
* `decoder`应用了beam search来提升效果（每次生成词是取使得整个概率最高的前k个词作为候选）；beam size越大，效果越好，同时计算代价增大；
* 关于倒序输入效果提升：`rnn`是有偏模型，顺序越靠后的单词在最终占据的信息量越大，正序时最后一个词对应的state作为`decoder`的输入来预测第一个词，在`alignment`上来看显然这两个词并不是对齐的；倒序的话，`first word`成了`last word`，在`last state`中占据了主导，来预测`decoder`的第一个词，从某种意义上说实现了`alignment`，故效果提升；
* `decoder`本质上是一个`rnn`语言模型，不同的是在生成词的时候依赖于`encoder`的最后一个`hidden state`：

* 参考资料：
    * Sequence to Sequence Learning with Neural Networks
    * https://zhuanlan.zhihu.com/p/26985192