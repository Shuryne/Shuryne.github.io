---
title: XLNet
date: 2021-06-27
draft: true
categories:
- 孤独的程序员
tags:
- transformer
---

## XLNet

1. 提出背景：
   * 自回归LM只能利用上文，不能利用上下文
   * 自编码DAE能利用上下文，但是[mask]会导致训练应用过程不一致
     方法：
   * 排列语言模型
   * 双流自注意力机制：query流、content流