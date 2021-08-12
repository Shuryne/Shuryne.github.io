---
title: PRML笔记
date: 2021-08-02
draft: true
categories:
- 孤独的程序员
tags:
- PRML

---

PRML读书笔记

<!--more-->

## 绪论

### 信息论

观察到一个变量的值时，我们到底获得了多少信息？怎么度量信息？香侬通过事件/变量的概率构造信息量

#### 自信息

该概率事件发生时，获得的信息量为其概率的负对数，概率越小，事件也不可能发生，一旦发生带来的信息量就越大
$$
\color{blue}
{
s(x) = -logp(x)
}
$$

#### 熵（Entropy）

当观测到变量的值时，减小的不确定性
$$
\color{blue}
{
\begin{align}
H(X) &= -\sum_{x} p(x)logp(x) \\
H(X,Y) &= H(X) + H(Y|X) = H(Y) + H(Y|X)
\end{align}
}
$$

#### 相对熵（KL散度）

真实分布p(x)和建模分布q(x)之间不相似程度的度量。知道真实分布之后一定能得到最佳压缩，若使用非真实分布进行压缩，必定会损失编码效率，在传输时增加额外信息量，KL散度就等于建模分布离真实分布之间的平均额外信息量
$$
\color{blue}
{
\begin{align}
KL(p||q) &= (-\int p(x)lnq(x)dx) - (-\int p(x)lnp(x)dx) \\
&= -\int p(x)ln(\frac{q(x)}{p(x)})dx >=0
\end{align}
}
$$


#### 互信息

视角一：由于知道Y的值而导致X的不确定性的减小（反之亦然）可以想象成两个有交集的圆之间的交集部分
$$
\color{blue}
{
I(X,Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)
}
$$
视角二：KL散度度量下XY联合分布和相互独立之间的差异程度
$$
\color{blue}
{
I(X,Y)=KL(p(X,Y)||p(X)p(Y)) = -\int\int p(x,y)ln(\frac{p(x)p(y)}{p(x,y)})dxdy
}
$$

