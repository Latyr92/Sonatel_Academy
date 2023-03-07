# Chargement du fichier CSV
donnees <- read.csv("/home/faye/Sonatel_Academy/donnée_projet.csv", header = TRUE, sep = ",")

# Initialisation des tableaux pour les données valides et invalides
donnees_valides <- data.frame()
donnees_invalides <- data.frame()

# Boucle à travers les lignes du fichier
for (i in 1:nrow(donnees)) {
  # Extraction des données de la ligne
  code <- donnees[i, "code"]
  numero <- donnees[i, "numero"]
  nom <- donnees[i, "nom"]
  prenom <- donnees[i, "prenom"]
  date_naissance <- donnees[i, "date_naissance"]
  classe <- donnees[i, "classe"]
  notes <- donnees[i, "notes"]
  
  # Vérification de la validité des données
  if (nchar(numero) == 7 && grepl("^[A-Z0-9]*$", numero)) {
    if (nchar(nom) >= 2 && nchar(prenom) >= 3) {
      if (grepl("^\\d{2}-\\d{2}-\\d{4}$", date_naissance)) {
        if (grepl("^\\d{6,5,4,3}eme[AB]$", classe)) {
          #Extraction des notes pour chaque matière
          notes_matieres <- strsplit(notes, "#")[[1]]
          notes_devoirs <- list()
          notes_examens <- list()
          for (note_matiere in notes_matieres) {
            notes_matiere <- strsplit(note_matiere, "\\s*:\\s*")[[1]]
            matiere <- trimws(notes_matiere[1])
            notes_devoir <- unlist(strsplit(trimws(notes_matiere[2]), "\\s*\\|\\s*"))
            notes_examen <- as.numeric(trimws(notes_matiere[3]))
            notes_devoirs[[matiere]] <- as.numeric(notes_devoir)
            notes_examens[[matiere]] <- notes_examen
          }
          
          # Calcul de la moyenne des devoirs pour chaque matière
          moyennes_devoirs <- sapply(notes_devoirs, mean, na.rm = TRUE)
          
          # Calcul de la moyenne générale pour l'étudiant
          moyennes_generales <- sapply(seq_along(notes_devoirs), function(i) {
            (mean(notes_devoirs[[i]], na.rm = TRUE) + 2 * notes_examens[[i]]) / 3
          })
          
          # Création d'une ligne pour les données valides
          ligne_valide <- data.frame(
            code = code,
            numero = numero,
            nom = nom,
            prenom = prenom,
            date_naissance = date_naissance,
            classe = classe,
            moyennes_devoirs,
            moyenne_generale = moyennes_generales
          )
          
          # Ajout de la ligne au tableau des données valides
          donnees_valides <- rbind(donnees_valides, ligne_valide)
        } else {
          # Ajout de la ligne au tableau des données invalides
          donnees_invalides <- rbind(donnees_invalides, donnees[i, ])
        }
      } else {
        #Ajout de la ligne au tableau des données invalides
        donnees_invalides <- rbind(donnees_invalides, donnees
                                   
                                   