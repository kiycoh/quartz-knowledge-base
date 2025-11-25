---
tags: [algebra-relazionale, calcolo-infinitesimale, derivata-parziale]
last modified: 2025, 11, 24 22:11:17
---
# Esercizi derivate

1. $f(x) = \frac{1}{2}x^2 -3x+7$ 
    - $f'(x) = x-3$ 


2. $f(x)=x^{2019}-4\cdot\frac{1}{x}+2\sqrt x$ 
    - $f'(x) = 2019x^{2018}-4\cdot x^{-1}+\frac{1}{2}\cdot 2 x^{\frac{1}{2}-1}$
    - $f'(x) = 2019x^{2018}-4\cdot (-1)\cdot x^{-2} +x^{-\frac{1}{2}}$
    - $f'(x) = 2019x^{2018}+4\cdot \frac{1}{x^2}+\frac{1}{\sqrt x}$ 
    - $f'(x) = 2019x^{2018} + \frac{4}{x^2}+\frac{1}{\sqrt x}$ 


3. $f(x) = \sin x(1-2\cos x)$
    - $f'(x)=\cos x(1-2\cos x)+\sin x\cdot[0-2\cdot(-\sin x)]$ 
    - $f'(x) = \cos x-2\cos^2 x + \sin x \cdot (2 \sin x)$ 
    - $f'(x) = \cos x - 2\cos^2 x +2\sin^2 x$ 


4. $f(x) = (4x-1)^3 - 6$
    - $f'(x)=3(4x-1)^2\cdot 4$
    - $f'(x)= (12x-3)^2\cdot 4$
    - $f'(x) = (48x-12)^2$
    - $f'(x)=2304x^2-1152x+144$
    - $f'(x)=\frac{2304x^2-1152x+144}{144}$  
    - $f'(x)=16x^2-8x+1$ 


5. $f(x)= \ln(\frac{1-x}{1+x})$
    - $f'(x)= \frac{1}{\frac{1-x}{1+x}}\cdot \frac{-1(1+x)-(1-x)\cdot 1}{(1+x)^2}$ 
    - $f'(x)=\frac{1+x}{1-x}\cdot \frac{-1-x-1+x}{(1+x)^2}$ 
    - $f'(x)=\frac{1}{1-x}\cdot \frac{-2}{1+x}$
    - $f'(x)=\frac{-2}{1+x-x-x^2}$
    - $f'(x)=\frac{-2}{1-x^2}$ 


  6. $f(x) = x^3 + 3^x +3^3+\log_3 (x) + \sqrt[3]3$ 
    - $f'(x)=3x^2+3^x\cdot \ln 3+\frac{1}{x\ln3}$


7. $f(x)=\sqrt{\ln(\sin x)}+x^{\cos x}+\sqrt{\pi}$ 
    - $f'(x)=[\ln(\sin x)]^{\frac{1}{2}}+e^{\ln x^{\cos x}}$ 
      - $f'(x)=\frac{1}{2}[\ln(\sin x)]^{-\frac{1}{2}}+e^{\cos x\cdot \ln x}[\cos x \cdot \frac{1}{x}+(-\sin x)\ln x]$ 
      - $f'(x) = \frac{1}{2\sqrt{\ln(\sin x)}}\cdot \frac{1}{\sin x} \cdot \cos x +e^{\cos x\cdot \ln x}[\cos x \cdot \frac{1}{x}+(-\sin x)\ln x]$ 
      - $f'(x)=\frac{1}{2\sqrt{\ln(\sin x)}}\cdot \frac{\cos x}{\sin x}+x^{\cos x} (\frac{\cos x}{x}-\sin x\cdot \ln x)$ 
      - $f'(x)=\frac{1}{2\sqrt{\ln(\sin x)}}\cdot \cot x+x^{\cos x} (\frac{\cos x}{x}-\sin x\cdot \ln x)$ 
      - $f'(x)=\frac{\cot x}{2\sqrt{\ln(\sin x)}}+x^{\cos x} (\frac{\cos x}{x}-\sin x\cdot \ln x)$

