Spannung, die in einem Leiter aufgrund einer Veränderung des magnetischen Feldes entsteht

### Leiterschleife
- Induktion in der Leiterschleife wird duch eine Veränderung des [[Magnetischer Fluss|Magnetischen Flusses]] verursacht, der durch die Fläche der Leiterschleife fließt
	- Veränderung des Flusses durch die Fläche korrespondiert mit Veränderung an allen Seiten der Leiterschleife
	- Ursache: Lorentzkraft
- Magnetischer Fluss durch die Fläche verändert sich mit:
	1. Veränderung der [[Magnetisches Feld#Magnetische Flussdichte|magnetischen Flussdichte]]
	2. Veränderung der Fläche des Leiters

$$U_{ind}=\frac{\Delta(\lvert \vec B\rvert \cdot \lvert \vec A \rvert \cdot \cos(\varphi)) }{\Delta t}$$
$$U_{ind}=\frac{\Delta(\vec B \cdot\vec A)}{\Delta t} $$


### Induktionsgesetz
- Eine Spule mit n Windungen kann als n Leiterschleifen modelliert werden
- Daraus folgt:
$$\begin{aligned}U_{ind}&=-n\cdot\frac{\Delta(\vec B \cdot\vec A)}{\Delta t}\\\\U_{ind}&=-n\cdot\frac{\Delta\Phi}{\Delta t}\end{aligned}$$
- Daraus folgt für $B\perp A:$ $$U_{ind}=-n\cdot\frac{\Delta(B \cdot A)}{\Delta t}$$
#### Differenzen- und Differenzialquotient
- Bei linearen Veränderungen von $\Phi$ gilt die zuvor aufgestellte Formel $$U_{ind}=-n\cdot\frac{\Delta\Phi}{\Delta t}$$
- Bei nichtlinearen Veränderungen von $\Phi$ lässt sich der Differenzenquotient in einen Differenzialquotienten überführen $$\begin{aligned}U_{ind}&=-n\cdot \frac{d\Phi}{dt}\\\\U_{ind}&=-n\cdot\dot\Phi\end{aligned}$$
- Bei konstanter Fläche A $(\dot A = 0)$ gilt:$$U_{ind}=-n\cdot A\cdot \dot B$$
- Bei konstanter Fläche B $(\dot B = 0)$ gilt:$$U_{ind}=-n\cdot \dot A\cdot B$$

### Lentz'sche Regel
- Der Induktionsstrom ist so gerichtet, dass er seiner Ursache entgegenwirkt
- Das entstehende [[Magnetisches Feld|Magnetfeld]] wirkt der bewegenden Kraft entgegen
- Die Arbeit, um die [[Elektrische Ladung|Elektronen]] im Leiter zu bewegen, also den [[Elektrische Stromstärke|Strom]] zu verursachen muss zusätzlich aufgewendet werden (Energieerhaltung)
- Beispiele:
	- Wirbelstrombremse

### Selbstinduktion
- Leiter besitzen ein Magnetfeld, welches Proportional zum Strom durch den Leiter ist
- Das Magnetfeld verändert sich bei veränderder Stromstärke
- Das sich verändernde Magnetfeld induziert wiederum eine Spannung im Leiter
- Eine sich verändernde [[Elektrische Stromstärke|Stromstärke]] hemmt also ihre eigene Veränderung
- Für eine lange Spule gilt daher:$$\begin{aligned} U_{ind}&=-n\cdot\frac{\Delta(\vec B \cdot\vec A)}{\Delta t} \\\\ U_{ind}&=-n\cdot\frac{\Delta(B \cdot A)}{\Delta t} \qquad \text{(B und A senkrecht)}\\\\ U_{ind}&=-n\cdot\frac{\Delta(\mu_0\cdot\mu_r \cdot\frac{n\cdot I}{l} \cdot A)}{\Delta t} \\\\ U_{ind}&=-n\cdot\frac{\mu_0\cdot\mu_r \cdot\frac{n}{l} \cdot A\cdot \Delta I}{\Delta t} \\\\ U_{ind}&=-n\cdot \mu_0\cdot\mu_r \cdot\frac{n}{l} \cdot A\cdot \frac{\Delta I}{\Delta t} \\\\\\ U_{ind}&=-\frac{\mu_0\cdot\mu_r \cdot n^2\cdot A}{l} \cdot \frac{dI}{d t} \\\\ U_{ind}&=-L \cdot \frac{dI}{dt} \end{aligned}$$

### Induktivität
- Proportionalitätsfaktor für den Strom der Selbstinduktion $L$
- Bei einer langen Spule: $$L=\frac{\mu_0\cdot\mu_r \cdot n^2\cdot A}{l}$$

### Energie des Magnetfeldes einer langen Spule
$$\begin{aligned}  dW&=P\cdot dt \\ &= U_{ind} \cdot I \cdot dt \\ &= -L \cdot \frac{dI}{dt}\cdot I \cdot dt &|\int \\ W&=-\frac 1 2 L \cdot I^2 &|\;\lvert\cdot\rvert \\\\ W&=\frac 1 2 L \cdot I^2 \end{aligned}$$

### Phasenverschiebung
Beim Elektrischen Schwingkreis  

