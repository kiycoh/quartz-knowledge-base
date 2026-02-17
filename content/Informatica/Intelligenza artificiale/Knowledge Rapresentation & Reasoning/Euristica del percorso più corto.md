---
last modified: 2025, 11, 24 22:11:54
tags: [euristica-del-percorso-piu-corto, specificita, strategie-di-pre-emption]
---
# Euristica del percorso più corto
euristica del percorso più corto: si dà maggiore peso alle conclusioni che
derivano da un percorso più breve nella rete

L'idea di fondo è che, in una rete dove le proprietà possono entrare in conflitto, non
ha senso considerare tutti i percorsi allo stesso modo: alcuni "argomenti" (cioè
percorsi che portano a una certa conclusione) sono più forti o più diretti di altri, e
possono prevalere, rendendo gli altri "non ammissibili".

L'euristica del percorso più corto rientra in una categoria di strategie chiamate
[[Strategie di pre-emption]], cioè tecniche che cercano di decidere quale percorso
abbia più "diritto" di essere seguito quando nella rete ci sono conclusioni
contrastanti.
L'idea alla base è quella della specificità: l'informazione più specifica su un oggetto
dovrebbe avere più peso rispetto a quella più generica, perché è più rilevante per il
caso particolare.