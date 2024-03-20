#  Detecting Outliers, Attacks, and Drift

In the previous part, we discussed serving a model. In this section, we will discuss how to protect our model in the real world. We will discuss how to detect outliers, adversarial attacks, and drift using the Alibi Detect library.

## Outlier Detection

Outliers are data points that are different from other data points. They can be caused by errors in data collection or can be indicative of some new trends in the data. Outliers can significantly affect the performance of machine learning models. Therefore, it is important to detect and handle outliers.

While there are many ways to detect outliers for tabular data, we will discuss how to detect outliers in image data. For this, we will use Variational Autoencoders (VAEs). VAEs are generative models, so they learn the underlying distribution of the data. This is crucial for detecting outliers, since outliers are data points that are different from other data points - they are samples from the tails of the distribution or not even part of it.
If you have never heard of VAEs, you can read more about them [in this detailed introduction to variational autoencoders](https://arxiv.org/abs/1906.02691).

In practice, detecting outliers using VAEs amounts to checking how well the input data can be reconstructed by the model. If the input data cannot be reconstructed well, it is likely an outlier.

In [`notebooks/outlier_detection.ipynb`](notebooks/outlier_detection.ipynb), we will use the not-so-exciting MNIST dataset to detect outliers using a VAE to demonstrate the concept.

## Adversarial Attack Detection

In a previous lab, we discussed how to generate and defend against adversarial attacks. In this section, we will discuss how to detect adversarial attacks.

If you think about it, adversarial attacks are not too different from outliers. So, you might be tempted to use the same approach to detect adversarial attacks as you would to detect outliers. However, there is an issue: (Variational) autoencoders are trained to find a transformation $T$ that reconstructs the input data $x$ as well as possible. This is done by minimizing the reconstruction error $L(x, T(x)) = \|x - x'\|^2$. However, these types of loss functions suffer from a fundamental flaw for the detection of adversarial attacks: they are not sensitive to small perturbations in the input data. This is because the loss function is minimized when the input data is reconstructed as well as possible, regardless of whether the input reconstruction error is due to an adversarial attack or not.

One way to detect adversarial attacks is to use a model-dependent reconstruction error. Given a model $M$, we can optimize the weights $\theta$ of the model to minimize the following loss function:

$$\min\limits_\theta D_{KL}(M(x) \| M(AE_\theta(x)))$$

$M$ is the model we want to protect from adversarial attacks - e.g. a classifier. During training of the autoencoder, the weights of $M$ are frozen, and we use its output probabilities to compute the loss. The loss function is the Kullback-Leibler divergence between the output probabilities of the model $M$ and the output probabilities of the model $M$ when the input data is reconstructed by the autoencoder. The intuition behind this loss function is that the output probabilities of the model $M$ should be similar when the input data is reconstructed by the autoencoder and when it is not. If the output probabilities are not similar, it is likely that the input data is an adversarial attack.

### Excursion: What is the Kullback-Leibler divergence?

TODO

### Back to the main topic

In [`notebooks/adversarial_attack_detection.ipynb`](notebooks/adversarial_attack_detection.ipynb), we will again use the MNIST dataset to detect adversarial attacks using a model-dependent reconstruction error.

## Outliers, attacks, and drift detection in the wild

TODO