# 6. Kernel Methods

Created: July 13, 2021 6:05 PM

## **6.1. Dual Representations**

kernel functions: $k(x,x^{'})=\phi(x)^T\phi(x^{'})$

Basis function/ feature vector:  $\phi(x)$

## **6.2. Constructing Kernels**

给出任意一个f(x, z)，如果能写成的形式$\phi(x)^T\phi(z)$，说明可以作为一个kernel function。

1. 检验方法，充要条件：Gram Matrix $K_{m,n}=\phi(x_m)\phi(x_n)$是一个**半正定矩阵**。
2. kernel 的有一些性质使得kernel function进行变换后还是kernel function。(e.g., $exp(k(x,x^{}))$)。从而可以根据具体任务构建更加复杂的kernel。(为什么要构建更加复杂的kernel？如何知道什么任务下需要怎样的kernel？）
3. Gaussian Kernel:  $k(x,x^{'})=exp(-||x-x^{'}||^2/2\sigma^2)$。对应的feature vector $\phi(x)$ 有无穷维。

> 用generative model 来construct kernel，再将这个kernel应用到discriminative model 中。

> 判别式模型举例：要确定一个羊是山羊还是绵羊，用判别模型的方法是从历史数据中学习到模型，然后通过提取这只羊的特征来预测出这只羊是山羊的概率，是绵羊的概率。

> 生成式模型举例：利用生成模型是根据山羊的特征首先学习出一个山羊的模型，然后根据绵羊的特征学习出一个绵羊的模型，然后从这只羊中提取特征，放到山羊模型中看概率是多少，在放到绵羊模型中看概率是多少，哪个大就是哪个。

1. Hidden Markov Model based kernel

    $k(x,x^{'})=\int p(x|z)p(x^{'}|z)p(z)dz$，其中z是latent variable。

2. Fisher Kernel

    generative model $p(x|\theta)$ ，$​$$​\theta$ 表示vector of parameters。现在目的是找到一个kernel来measure similarity between $x$ and $x'$。

> in the limit of an infinite number of basis functions, a Bayesian neural network with an appropriate prior reduces to a Gaussian process, thereby providing a deeper link between neural networks and kernel methods.

## 6.3. Radial Basis Function Networks

## 6.4. Gaussian Process

extend the role of kernels to probabilistic discriminiative models

在parametric model中，我们首先有一个关于parameters的prior distribution，然后有了training data之后，获得一个parameteres的posterior distribution。

在GP model中，我们是首先直接定义一个关于function的prior distribution。

> 有许多GP model的变形。For instance, in the geostatistics literature Gaussian process regression is known as *kriging* (Cressie, 1993). Similarly, ARMA (autoregressive moving aver- age) models, Kalman filters, and radial basis function networks can all be viewed as forms of Gaussian process models.

### 6.4.5. Gaussian Process for Classification

在GP regression基础上，加上了sigmoid function $f(x)=\sigma(a(x))$。

$p(t_{N+1}=1|a_N)=\int p(t_{N+1}=1|a_{N+1})p(a_{N+1}|t_N)da_{N+1}$，

其中$p(t_{N+1}=1|a_{N+1})=\sigma(a_{N+1})$

这个积分没有解析解，所以用Gaussian Approximation (1. variational inference 2. expectation propagation 3. laplace approximation)

![6%20Kernel%20Methods%2099ddb06ac61c4f3988afa16351993c33/Untitled.png](6%20Kernel%20Methods%2099ddb06ac61c4f3988afa16351993c33/Untitled.png)

### 6.4.6. Laplace Approximation

### 6.4.7. Connection to Neural Networks

## Note

$p(x;\theta)$表示是参数$\theta$，$\theta$决定了  $x$ 的值，这是频率学派的观点，即参数是固定的，是上帝视角看到的。贝叶斯中的MAP的思想则是 $\theta$  同样是随机变量，因此会写成$p(x|\theta)$ 。

mode 是概率分布中最大值点。