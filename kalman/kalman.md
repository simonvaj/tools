
## Kalman vectors and matrices with dimensions

| Name                          | Symbol                         | Dimensions    | Notes |
| ----------------------------- |:------------------------------:|:-------------:|-------|
| state                         | $$\mathbf{x}$$                 | $$n\times 1$$ | |
| input                         | $$\mathbf{u}$$                 | $$p\times 1$$ | control input |
| output                        | $$\mathbf{z}$$                 | $$m\times 1$$ | measurements, observation |
| state gain                    | $$\mathbf{A}$$, $$\mathbf{F}$$ | $$n\times n$$ | state-transition model |
| input gain                    | $$\mathbf{B}$$                 | $$n\times p$$ | control-input model |
| output gain                   | $$\mathbf{H}$$                 | $$m\times n$$ | observation model |
| process noise                 | $$\mathbf{w}$$                 | $$n\times 1$$ | dynamic noise |
| process noise covariance      | $$\mathbf{Q}$$                 | $$n\times n$$ | |
| measurement noise             | $$\mathbf{v}$$                 | $$m\times 1$$ | |
| measurement noise covariance  | $$\mathbf{R}$$                 | $$m\times m$$ | |
| _a priori_ covariance         | $$\mathbf{P}^-$$               | $$n\times n$$ | state estimation error covariance |
| _a posteriori_ covariance     | $$\mathbf{P}$$                 | $$n\times n$$ | |
| Kalman filter gain            | $$\mathbf{K}$$                 | $$n\times m$$ | |
| innovation process            | $$\mathbf{\tilde{y}}$$, $$\alpha$$ | $$m\times 1$$ | |
| innovation process covariance | $$\mathbf{S}$$                 | $$m\times m$$ | |

## Kalman filter equations

$$\begin{align}
\mathbf{x}_j &= \mathbf{A}\mathbf{x}_{j - 1} +
    \mathbf{B} \mathbf{u}_j + \mathbf{w}_j,\nonumber\\
\mathbf{z}_j &=
\mathbf{H}_j\mathbf{x}_{j} + \mathbf{v}_j\nonumber\\
\mathbf{P}_j &=
\mathrm{E}\big[\big(\mathbf{x}_j - \mathbf{\hat{x}}_j\big)
    \big(\mathbf{x}_j - \mathbf{\hat{x}}_j\big)^{\mathrm{T}}\big]\nonumber
\end{align}$$

### Prediction step

$$\begin{align}
\mathbf{\hat{x}}_j^- &=
    \mathbf{A} \mathbf{\hat{x}}_{j-1} + \mathbf{B} \mathbf{u}_j\nonumber\\
\mathbf{P}_j^- &=
    \mathbf{A}\mathbf{P}_{j-1}\mathbf{A}^\mathrm{T} + \mathbf{Q}\nonumber
\end{align}$$

### Update step

$$\begin{align}
\mathbf{\tilde{y}}_j &=
    \mathbf{z}_j- \mathbf{H}\mathbf{\hat{x}}_j^-=
    \mathbf{z}_j- \mathbf{\hat{z}}_j^-\nonumber\\
\mathbf{S}_j &= {\rm cov}(\mathbf{\tilde{y}}_j) =
    \mathrm{E}[\mathbf{\tilde{y}}_j\mathbf{\tilde{y}}_j^{\rm T}]\nonumber\\
\mathbf{K}_j &= \mathbf{P}_j\mathbf{H}_j^{\rm T}
    \big(\mathbf{H}\mathbf{P}_j\mathbf{H}_j^{\rm T} + \mathbf{R}\big)^{-1}=
    \mathbf{P}_j^-\mathbf{H}_j^{\rm T}\mathbf{S}_j^{-1}\nonumber\\
\mathbf{\hat{x}}_j &= \mathbf{\hat{x}}_j^- +
    \mathbf{K}_j \mathbf{\tilde{y}}_j\nonumber\\
\mathbf{P}_j &=
    \big(\mathbf{1} - \mathbf{K}_j\mathbf{H}_j\big)\mathbf{P}_j^-\nonumber
\end{align}$$
