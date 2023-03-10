# Charger le fichier csv
library(stringr)
getwd()
setwd("/home/faye/Sonatel_Academy")
file='Donnees.csv'
donnees <- read.csv(file, header = TRUE, sep = ",")
is.data.frame(donnees)
# Initialiser les tableaux pour les données valides et invalides
invalides <- data.frame(CODE=character(),
                        Numero=character(),
                        Nom=character(),
                        Prenom=character(),
                        Date.de.naissance=character(),
                        Classe=character(),
                        Note=character()
                        )
valides <- data.frame(CODE=character(),
                        Numero=character(),
                        Nom=character(),
                        Prenom=character(),
                        Date.de.naissance=character(),
                        Classe=character(),
                        Note=character()
                        )
attach(donnees)
library(stringr)
donnees$Date.de.naissance= str_replace_all(donnees$Date.de.naissance,c(':'= '/', '\\.' = '/',',' = '/', ' '= '/', '\\|'= '/', ';'= '/','_'= '/', '-'= '/'))
# Vérifier la validité de chaque ligne
for (i in 1:nrow(donnees)) {
  # Vérifier la validité du numéro d'étudiant
  if (nchar(donnees$Numero [i])== 7 & grepl("^[A-Z0-9]*$", donnees$Numero [i])) {
    if (nchar(donnees$Nom [i]) >= 2 & nchar(donnees$Prénom [i]) >= 3) {
      valides[nrow(valides)+1,]<- donnees[i,]
      # Vérifier la validité de la classe
          library(stringr)
          donnees$Classe <-str_replace_all(donnees$Classe,c(' ' = '' ))
          if (grepl("^[3,4,5,6][A-B]*$", donnees$Classe [i]) && substring(donnees$Classe [i],nchar(donnees$Classe [i]), nchar(donnees$Classe [i]) %in% c('B','A'))) {
            #valides[nrow(valides)+1,]<- donnees[i,]
#             #valides[nrow(valides)+1,]<- donnees[i,]
              donnees$Date.de.naissance<- trimws(donnees$Date.de.naissance)
              if (grepl("^\\d{2}/\\d{2}/\\d{4}$", donnees$Date.de.naissance [i])) {
                  donnees$Date.de.naissance<- trimws(donnees$Date.de.naissance)
                #donnees$Date.de.naissance
                  date_parts <- strsplit(donnees$Date.de.naissance, "/")
                  jour <- as.numeric(date_parts[1])
                  mois <- as.numeric(date_parts[2])
                  annee <- as.numeric(date_parts[3])
                  # Vérifier que le jour, mois et année sont valides
                    if (mois == 2 & (annee %% 4 == 0 & (annee %% 100 != 0 | annee %% 400 == 0)) & jour <= 29 | mois == 2 & jour <= 28 | mois %in% c(4,6,9,11) & jour <= 30 | mois %in% c(1,3,5,7,8,10,12) & jour <= 31) {
                      valides[nrow(valides)+1,]<- donnees[i,]
                    }
              }
          }
    }
  }else{
    invalides[nrow(invalides)+1,] <- donnees[i,]
  }
}

write.csv(valides,"donnees_valides.csv")
write.csv(invalides,"donnees_invalides.csv")
library(jsonlite)
json_donnees <- toJSON(df)
write(json_donnees,"data.json")
