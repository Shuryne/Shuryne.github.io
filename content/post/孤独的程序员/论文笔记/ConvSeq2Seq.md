---
title: ConvSeq2Seq
date: 2018-11-12
draft: false
categories:
- 孤独的程序员
tags:

---

《 Convolutional Sequence to Sequence Learning》

<!--more-->

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

  
  



参考资料



[1]: https://arxiv.org/pdf/1705.03122.pdf
[2]: https://zhuanlan.zhihu.com/p/26918935
[3]: https://zhuanlan.zhihu.com/p/27464080
