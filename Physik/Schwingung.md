### Charakteristische Größen
- **Ruhezustand:** Zustand des schwingenden Systems ohne Anregung
- **Elongation:** Momentane Auslenkung vom Ruhezustand
- **Amplitude:** Maximale Elongation
- **Periode:** Sich wiederholende Einheit der Schwingung
- **Schwingungsdauer/Periodendauer:** Dauer einer Periode $(T)$
- **Frequenz:** Anzahl Perioden pro Zeit $(f)$
- **Phasenwinkel:** Position im Schwingungsverlauf
- **Rückstellkraft:** Kraft in Richtung Ruhelage


### Harmonische Schwingung
Schwingung, bei der die Rückstellkraft proportional zur Auslenkung ist

#### Federpendel
![[Schwingungen 2025-03-14 14.30.34.excalidraw]]

- Rückstellkraft ist eine Kombination aus Federkraft und Gewichtskraft$$\begin{aligned}F_r&=F_F - F_G \\  &= D \cdot s -m\cdot g \\ &= D\cdot s-D\cdot s_{0}\\ &=D\cdot (s-s_{0}) \\ \\ F_{r}&=(-)D\cdot y\end{aligned}$$
- Ruhelage ist die Auslenkung der Feder, in der die Gewichtskraft gleich der Federkraft ist $(s_{0})$
- Aus der Rückstellkraft lässt sich die DGL der Schwingung aufstellen: $$
\begin{align}
F_{r}(t)&= -D\cdot y(t) \\
a_{r}(t)\cdot m&=-D\cdot y(t) \\
a_{r}(t)&=-\frac{D}{m}\cdot y(t) \\
\ddot{y}(t)&=-\frac{D}{m}\cdot y(t) \\ \\ 
\implies y(t)&= \hat{y}\cdot \sin(w\cdot t)
\end{align}
$$
- Für die Schwingungsdauer folgt:$$
\begin{align}
y(t)&=\hat{y}\cdot \sin(w\cdot t)&&&&&&&&\\ 
\dot{y}(t)&=w \cdot \hat{y}\cdot \sin(w\cdot t) \\
\ddot{y}(t) &=w^{2}\cdot \hat{y}\cdot \sin (w\cdot t) \\ \\
a(t) &=w^{2}\cdot \hat{y}\cdot \sin (w\cdot t) \\
m\cdot a(t) &=m \cdot w^{2}\cdot \hat{y}\cdot \sin (w\cdot t) \\
F(t) &=m \cdot w^{2}\cdot y(t) \\ \\
\text{f\"ur das Federpendel gilt:} \quad F(t)&=D\cdot y(t) \\ \\
\implies D\cdot y(t)&=m\cdot w^{2}\cdot y(t) \\
D&=m\cdot w^{2} \\
w^{2}&=\frac{D}{m} \\
w&=\sqrt{ \frac{D}{m} } \\ \\
f&=\frac{1}{2\pi}\sqrt{ \frac{D}{m} } \\
T&=2\pi \cdot \sqrt{ \frac{m}{D} }
\end{align}
$$
- Die Schwingungsbewegung ist deckungsgleich mit der Projektion einer Kreisbewegung
	- ==> Die Schwingung kann durch eine Sinuskurve beschrieben werden![[Pasted image 20250320191739.png]]

#### Fadenpendel bei kleinen Auslenkungen
![[Schwingungen 2025-03-20 17.28.12.excalidraw|30%]]
- Betrachtet man beim Fadenpendel die Auslenkung nur in x-Richtung so gilt:$$
\begin{align}
\sin(\alpha)&=\frac{F_{R}}{F_{G}}  &  &  &  &  &  &\\ \\
\tan(\alpha)&=\frac{x}{l} \\ \\
\text{Kleinwinkeln\"aherung:}\quad\sin (\alpha)&=\tan(\alpha) \\ \\
\implies \frac{F_{R}}{F_{G}}&=\frac{x}{l} \\ \\
F_{R}&=F_{G}\cdot \frac{x}{l}
\end{align}
$$ 

- Die Rückstellende Kraft ist proportional zur Auslenkung 
	- ==> Harmonische Schwingung bei kleiner Auslenkung
- Für die Schwingungsdauer gilt wie beim [[Schwingung#Federpendel|Federpendel]]: $$
\begin{align}
\ddot{x}(t)&=w^{2}\cdot x(t) \\
a(t)&=w^{2}\cdot x(t) \\
F(t)&=m\cdot w^{2}\cdot x(t) \\ \\
F_R&=F_{G}\cdot \frac{x}{l} \\
F_{R}&=m\cdot g\cdot \frac{x}{l} \\ \\
F(t)&=F_{R} \\
m\cdot w^{2}\cdot x(t)&=m\cdot g\cdot \frac{x}{l} \\ \\
w^{2}&=\frac{g}{l} \\
w&=\sqrt{ \frac{g}{l} } \\
T&=2\pi \cdot\sqrt{ \frac{g}{l} }

\end{align}
$$

### Anharmonische Schwingung
![[Schwingungen 2025-03-19 23.21.53.excalidraw|30%]]
- Rückstellende Kraft ist nicht proportional zur Auslenkung
	- Bsp: Hemmungspendel
	- Länge bei einer Halbschwingung verändert
		- ==> Schwingungsdauer für Halbschwingung verändert
- Kann nicht durch eine Sinuskurver beschrieben werden

### Energieerhaltung
- Bei einer Schwingung wird immer Abwechselnd:
	1. Kinetische Energie in Potenzielle Energie umgewandelt
	2. Potenzielle Energie in Kinetische Energie umgewandelt
- Die Gesamtenergie des Systems verändert sich dabei nicht
- 




