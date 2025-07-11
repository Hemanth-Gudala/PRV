### *Problem 1 : Buffon's Matches Problem: Mathematical Theory*

<small>

Let $x$ be the distance from the center of the match to the closest parallel line, and let $\theta$ be the acute angle between the match and one of the parallel lines.

##### Probability Density Functions

##### PDF for Distance (x)
The uniform probability density function (PDF) of $x$ between 0 and $\frac{d}{2}$ is:

$$f_X(x) = \begin{cases} 
\frac{2}{d} & \text{for } 0 \leq x \leq \frac{d}{2} \\
0 & \text{elsewhere}
\end{cases}$$

Where:
- $x = 0$ represents a match centered directly on a line
- $x = \frac{d}{2}$ represents a match centered between two lines

##### PDF for Angle (θ)
The uniform probability density function of $\theta$ between 0 and $\frac{\pi}{2}$ is:

$$f_\Theta(\theta) = \begin{cases}
\frac{2}{\pi} & \text{for } 0 \leq \theta \leq \frac{\pi}{2} \\
0 & \text{elsewhere}
\end{cases}$$

Where:
- $\theta = 0$ represents a match parallel to the marked lines
- $\theta = \frac{\pi}{2}$ represents a match perpendicular to the marked lines

##### Joint PDF
Since $x$ and $\theta$ are independent, their joint probability density function is:

$$f_{X,\Theta}(x,\theta) = \begin{cases}
\frac{4}{d\pi} & \text{for } 0 \leq x \leq \frac{d}{2}, 0 \leq \theta \leq \frac{\pi}{2} \\
0 & \text{elsewhere}
\end{cases}$$

##### Crossing Condition
A match crosses a line when:

$$x \leq \frac{l}{2}\sin\theta$$

##### Case Analysis

##### Case 1: Short Match $(l \leq d)$
The probability of crossing is found by integrating the joint PDF:

$$P = \int_{\theta=0}^{\frac{\pi}{2}} \int_{x=0}^{\frac{l}{2}\sin\theta} \frac{4}{d\pi} dx d\theta = \frac{2l}{d\pi}$$

##### Case 2: Long Match $(l > d)$
For a long match, the integration becomes:

$$\int_{\theta=0}^{\frac{\pi}{2}} \int_{x=0}^{m(\theta)} \frac{4}{d\pi} dx d\theta$$

Where $m(\theta) = \min(\frac{l}{2}\sin\theta, \frac{d}{2})$

The probability resolves to:

$$P = \frac{2l}{d\pi} - \frac{2}{d\pi}\left(\sqrt{l^2-d^2} + d\arcsin\frac{d}{l}\right) + 1$$

Or alternatively:

$$P = \frac{2}{\pi}\arccos\frac{d}{l} + \frac{2}{\pi}\cdot\frac{l}{d}\left(1-\sqrt{1-\left(\frac{d}{l}\right)^2}\right)$$

##### Alternative Formulation
For angles where $l\sin\theta \leq d$ (i.e., $0 \leq \theta \leq \arcsin\frac{d}{l}$), the probability follows the short match case. For $\arcsin\frac{d}{l} < \theta \leq \frac{\pi}{2}$, the probability is 1.

This gives us:

$$P = \left(\int_{\theta=0}^{\arcsin\frac{d}{l}} \int_{x=0}^{\frac{l}{2}\sin\theta} \frac{4}{d\pi} dx d\theta\right) + \left(\int_{\arcsin\frac{d}{l}}^{\frac{\pi}{2}} \frac{2}{\pi} d\theta\right)$$

$$= \frac{2l}{d\pi} - \frac{2}{d\pi}\left(\sqrt{l^2-d^2} + d\arcsin\frac{d}{l}\right) + 1$$

Where:
- $l$ is the length of the match
- $d$ is the distance between parallel lines
- $x$ is the distance from match center to nearest line
- $\theta$ is the angle between match and lines

</small>
