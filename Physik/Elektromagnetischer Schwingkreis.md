![[Elektromagnetischer Schwingkreis 2025-03-21 13.45.34.excalidraw|130%]]
Werden ein geladener Kondensator und eine Spule in Reihe geschaltet, ensteht eine Schwingung des Stromes und der Spannung
### Schwingungsdauer
$$
\begin{align}
U_{C}&=U_{L} \\
\frac{Q(t)}{C}&=-L\cdot I(t) \\
\frac{Q(t)}{C}&=-L\cdot \ddot{Q}(t) \\ \\
\text{Ansatz: } \quad Q(t)&=\hat{Q}\cdot \sin(w\cdot t)\\
\quad\ddot{Q}(t)&=-w^{2}\cdot\hat{Q}\cdot \sin(w\cdot t) \\ \\
\implies \frac{\hat{Q}\cdot \sin(w\cdot t)}{C}&=-L\cdot(-w^{2})\cdot \hat{Q}\cdot \sin(w\cdot t) \\
\frac{1}{C}&=L\cdot w^{2} \\
w^{2}&=\frac{1}{L\cdot C} \\
w&=\sqrt{ \frac{1}{L\cdot C} } \\ \\
f&=\frac{1}{2\pi}\cdot \sqrt{ \frac{1}{L\cdot C} } \\ \\
T&=2\pi \cdot \sqrt{ L\cdot C }

\end{align}
$$

### Maximale Spannung
Die Maximale Spannung ist bestimmt durch die Gesamtenergie des Schwingkreises, da diese erreicht ist, wenn der Kondensator vollständig aufgeladen ist
$$
\begin{align}
E_{ges}&=E_{El} \\
E_{ges}&=\frac{1}{2}\cdot C\cdot U_{max}^{2} \\ \\
U_{max}^{2}&=\frac{2\cdot E_{ges}}{C} \\ \\
U_{max}&=\sqrt{ \frac{2E_{ges}}{C} }
\end{align}
$$
### Maximale Stromstärke
Die maximale Stromstärke ist bestimmt durch die Gesamtenergie des Schwingkreises, da diese Erreicht ist, wenn die gesamte Energie im Magnetfeld der Spule gespeichert ist
$$
\begin{align}
E_{ges}&=E_{mag} \\
E_{ges}&=\frac{1}{2}\cdot L\cdot I^{2} \\ \\
I^{2}&=\frac{2\cdot E_{ges}}{L} \\ \\
I&=\sqrt{ \frac{2E_{ges}}{L}}
\end{align}
$$

### Gegenüberstellung zu mechanischer Schwingung
- Der Kondensator entspricht der Feder in einem Federpendel
- Die Spule entspricht der trägen Masse
- Elektrische Feldenergie im Kondensator entspricht Spannenergie
- Magnetische Feldenergie um Spule entspricht Bewegungsenergie