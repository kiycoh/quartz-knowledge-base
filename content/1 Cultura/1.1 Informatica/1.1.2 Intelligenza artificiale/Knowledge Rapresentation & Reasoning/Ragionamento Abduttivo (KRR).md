---
last modified: 2025, 11, 10 16:11:34
tags:
  - krr
  - abduttivo
  - ragionamento-abduttivo
---
# Ragionamento Abduttivo (KRR)
- **Definizione**: Inverso della deduzione. Parte da un effetto osservato e cerca una causa o un insieme di ipotesi che lo giustifichino. È particolarmente utile nella diagnosi (es. risalire dai sintomi alle malattie).
- **Criteri per una Spiegazione Abduttiva**: Una formula $\alpha$ è una spiegazione abduttiva di $\beta$ rispetto a una KB se soddisfa:
    1. **Sufficienza**: KB $\cup$ {$\alpha$} $\models$ $\beta$.
    2. **Compatibilità**: KB $\cup$ {$\alpha$} è consistente.
    3. **Semplicità ed Essenzialità**: $\alpha$ non include elementi superflui; idealmente, usa il numero minimo di termini.
    4. **Uso di Vocabolario Specifico (Abducibili)**: $\alpha$ deve essere espressa usando un insieme predefinito di ipotesi plausibili (es. malattie in diagnosi mediche).
	    - **Prime Implicates**: Utili per trovare spiegazioni abduttive. Una clausola è un "prime implicate" della KB se è implicata dalla KB ed è minimale (nessuna sotto-clausola è implicata dalla KB).