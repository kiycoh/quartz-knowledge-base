import os

def trova_file_md(cartella_selezionata):
  """
  Questa funzione estrae tutti i nomi dei file .md da una cartella specificata.

  Args:
    cartella_selezionata: Il percorso della cartella in cui cercare.

  Returns:
    Una lista contenente i nomi di tutti i file .md trovati.
  """
  lista_file_md = []
  try:
    # Scansiona tutti i file e le directory nella cartella specificata
    for nome_file in os.listdir(cartella_selezionata):
      # Controlla se il nome del file termina con .md
      if nome_file.endswith(".md"):
        lista_file_md.append(nome_file)
  except FileNotFoundError:
    return f"Errore: La cartella '{cartella_selezionata}' non è stata trovata."
  except Exception as e:
    return f"Si è verificato un errore: {e}"
  
  return lista_file_md

def mostra_risultati(nomi_dei_file, percorso):
  """
  Mostra i risultati della ricerca dei file .md
  
  Args:
    nomi_dei_file: La lista dei file o il messaggio di errore
    percorso: Il percorso della cartella analizzata
  """
  print(f"\nRisultati per la cartella: {percorso}")
  if isinstance(nomi_dei_file, list):
    if nomi_dei_file:
      print("File .md trovati:")
      for nome in nomi_dei_file:
        print(f"- {nome}")
    else:
      print("Nessun file .md trovato nella cartella specificata.")
  else:
    print(nomi_dei_file)  # Stampa il messaggio di errore

# --- Esempio di utilizzo ---

# Caso 1: cartella corrente
percorso_cartella_1 = "."  # "." indica la cartella corrente in cui si esegue lo script
nomi_dei_file_1 = trova_file_md(percorso_cartella_1)
mostra_risultati(nomi_dei_file_1, percorso_cartella_1)

# Caso 2: cartella Statistica
percorso_cartella_2 = "C:\\Users\\Alessandro\\Documents\\Obsidian\\Alex's Second Brain\\1 Cultura\\1.2 Matematica\\1.2.3 Statistica"
nomi_dei_file_2 = trova_file_md(percorso_cartella_2)
mostra_risultati(nomi_dei_file_2, percorso_cartella_2)
