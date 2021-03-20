---
title: "从seq2seq到Transformer"
author: "Shuryne"
description: ""

date: 2018-11-12
lastmod: 2021-03-20
draft: false
weight: 100

tags: ["计算机", "NLP", 'Transformer']
series: ["论文笔记"]
categories: ["杂技浅尝"]

ShowToc: true
TocOpen: true
ShowBreadCrumbs: false
searchHidden: false

---

关于Seq2Seq和Transformer

<!--more-->

#### 1. Sequence to Sequence Learning with Neural Networks

* `encoder`以及`decoder`都采用`LSTM`模型
* 模型很简单，就是最普通的多层`LSTM`
* 实现的不同之处：
  * 用两种不同的`LSTM`，一种处理输入序列，一种处理输出序列；以可忽略的计算成本增加参数数量，同时在多个语言对上训练`LSTM`；
  * 更深的`LSTM`会比浅的效果更好，故论文模型选择了四层；
  * 将输入的序列翻转之后作为输入效果提升；<!-- more -->
* `decoder`应用了beam search来提升效果（每次生成词是取使得整个概率最高的前k个词作为候选）；beam size越大，效果越好，同时计算代价增大；
* 关于倒序输入效果提升：`rnn`是有偏模型，顺序越靠后的单词在最终占据的信息量越大，正序时最后一个词对应的state作为`decoder`的输入来预测第一个词，在`alignment`上来看显然这两个词并不是对齐的；倒序的话，`first word`成了`last word`，在`last state`中占据了主导，来预测`decoder`的第一个词，从某种意义上说实现了`alignment`，故效果提升；
* `decoder`本质上是一个`rnn`语言模型，不同的是在生成词的时候依赖于`encoder`的最后一个`hidden state`：

* 参考资料：
  * Sequence to Sequence Learning with Neural Networks
  * https://zhuanlan.zhihu.com/p/26985192

---

#### 2. Convolutional Sequence to Sequence Learning

* Seq2Seq 先把语句转换为一组词向量，通过对词向量的剪辑，提炼出语义向量。但对于如何剪辑有争议。有人提议使用`LSTM`等循环模型（RNN），来实现语义剪辑。RNN 模型的剪辑手段是：记忆门、遗忘门、和输出门。
* RNN 模型的突出优势，是很好地解决了长距离依赖的难题；
* 作者使用`CNN`取代`RNN`循环模型，训练速度提高9倍，精度超越`RNN`；
* **为什么更快？**
  * 卷积并行处理，而循环只能顺序处理，多个机器同时并行训练卷积模型，速度比串行训练循环模型快很多；
  * 可用`GPU`芯片来加速卷积模型的训练，而暂时还没有硬件能够加速`RNN`的训练；
* **为什么更准？**
  * `CNN`的层层抽象，与`RNN`的三重门，其实异曲同工。虽手段不同，但目的都是忽略次要内容，传承重要内容。所以在精度方面二者差距不大； 
  * 但是层级结构与循环网络链结构相比，提供了一种较短的路径来捕获词之间远程的依赖关系，因此也可以更好地捕捉更复杂的关系；
  * `Facebook translate` 与`Google translate`的精度差异，应该是由于`attention`的改进引起的；
    * `Google Translate`的解码器使用单层`LSTM`模型，故`attention`也是单层的；`Facebook`的解码器使用`CNN`模型，是多层的，`attention` 是多跳的（multi-hop）；越是底层的`attention`越聚焦，细节越丰富；越是高层的`attention`，视野越开阔，抽象程度越高，越能抓住文章主旨；
    * `Google Translate`使用的`attention`，依赖于编码器生成的语义向量，而不依赖于输入的原生态的词向量。而`Facebook`的`attention`，对语义向量和原生态词向量兼收并取；语义向量负责把握主旨，保证解码器的输出不偏题；原生态词向量关注措辞，保障解码器的输出用词得当；
* 将来`attention`的机制，还得融入规则。论文里只理解字面意思的`attention`的计算方式，无法理解“画外音”、“引经据典”、“含沙射影”的联想型语句。要正确理解“引经据典”和“含沙射影”，将来`attention`机制，还得融入知识图谱（张俊的猜想）；
* 模型结构：`encoder-decoder` +`attention`模块
  * encoder 和 decoder采用了相同的卷积结构
  * 非线性部分采用门控结构`GLM`；
  * `attention`采用多跳注意`multi-hop attention`，即在`decoder`的每一个卷积层都会进行`attention`操作，并将结果输入到下一层；

* 参考资料
  * Convolutional Sequence to Sequence Learning
  * https://zhuanlan.zhihu.com/p/26918935
  * https://zhuanlan.zhihu.com/p/27464080

---

#### 3. Attention Is All You Need

* 优点：

  * 靠`attention`机制，不使用`RNN`和`CNN`，并行度高；

  * 提出`self-attention`，自己和自己做`attention`，使得每个词都有全局的语义信息（长依赖）：由于`Self-Attention`是每个词和所有词都要计算`Attention`，所以不管他们中间有多长距离，最大的路径长度也都只是1，可以捕获长距离依赖关系；

  * 提出`multi-head attention`，可以看成`attention`的`ensemble`版本，不同`head`学习不同的子空间语义；


* 参考资料

  * Attention Is All You Need
  * https://jalammar.github.io/illustrated-transformer/
  * https://zhuanlan.zhihu.com/p/39034683



