---
last modified: 24/10/2025 14:02
tags:
  - intelligenza-artificiale
  - scienze-cognitive
  - abductive-reasoning
---
Per definire una **spiegazione abduttiva**, si parte da un effetto osservato e si cerca una causa o un insieme di ipotesi che lo giustifichino. Questa forma di ragionamento è l'inverso della deduzione, che invece parte da una causa per arrivare a un effetto. L'abduzione è particolarmente utile in contesti come la diagnosi, dove i sintomi portano a possibili malattie.

Una formula $\alpha$ è considerata una spiegazione abduttiva di una formula $\beta$ rispetto a una base di conoscenza (KB) se soddisfa quattro criteri fondamentali:

1. **Sufficienza**: Aggiungendo $\alpha$ alla KB, deve essere possibile dedurre $\beta$ (formalmente, $KB \cup {\alpha} \models \beta$).
2. **Compatibilità**: $\alpha$ non deve contraddire la KB; $KB \cup {\alpha}$ deve essere consistente.
3. **Semplicità ed Essenzialità**: La spiegazione $\alpha$ non deve includere elementi superflui o irrilevanti. Idealmente, $\alpha$ dovrebbe utilizzare il numero minimo di termini necessari. Ad esempio, spiegare un "gomito dolorante" con "gomito del tennista e varicella" violerebbe questo criterio se la varicella non fosse necessaria alla spiegazione.
4. **Uso di Vocabolario Specifico (Abducibili)**: La spiegazione $\alpha$ deve essere espressa utilizzando un insieme predefinito di ipotesi plausibili (chiamate _abducibili_). Questo evita spiegazioni banali o non informative, come spiegare "gomito dolorante" con "gomito dolorante" stesso. Nel contesto medico, le malattie sono tipici abducibili.

**Esempio di Applicazione dei Criteri (da "Lo Studente Assente all’Esame")**: Si vuole spiegare $\beta$ = StudenteAssenteEsame(MarioRossi). La KB include regole come: StudenteMalato(x) → StudenteAssenteEsame(x) e StudenteAllEstero(x) → StudenteAssenteEsame(x). Il vocabolario degli abducibili ammette: StudenteMalato(x), StudenteAllEstero(x), StudenteInSciopero(x).

- **Spiegazione valida**: $\alpha$ = StudenteMalato(MarioRossi).
    
    - **Sufficienza**: $KB \cup {\text{StudenteMalato(MarioRossi)}} \models \text{StudenteAssenteEsame(MarioRossi)}$ (per la regola data).
    - **Compatibilità**: Non ci sono contraddizioni note nella KB (es. non si sa che Mario Rossi non è malato o che ha inviato un'email che implica il contrario).
    - **Semplicità**: È un singolo termine rilevante, senza condizioni superflue.
    - **Vocabolario corretto**: StudenteMalato(x) è un termine ammesso nel vocabolario degli abducibili.
- **Esempi di Spiegazioni non valide**:
    
    - $\alpha$ = StudenteMalato(MarioRossi) $\land$ StudenteAllEstero(MarioRossi): Viola la **semplicità**, essendo "troppo complessa" se entrambe le condizioni non sono strettamente necessarie.
    - $\alpha$ = EmailRicevuta(MarioRossi): Viola la **compatibilità**, poiché si assume che "EmailRicevuta(x) $\rightarrow \neg$StudenteAssenteEsame(x)" sia nella KB, rendendola contraddittoria con l'osservazione.
    - $\alpha$ = StudenteAssenteEsame(MarioRossi): Viola il criterio del **vocabolario specifico**, in quanto è una spiegazione banale che non utilizza un termine abducibile differente dall'osservazione stessa.

Per semplificare il calcolo delle spiegazioni abduttive nel caso proposizionale, è sufficiente spiegare un singolo letterale (o anche un atomo) e concentrarsi su congiunzioni di letterali. Questo può essere ricondotto alla ricerca di "prime implicates" della KB.