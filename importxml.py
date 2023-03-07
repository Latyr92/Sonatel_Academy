import csv
import xml.etree.ElementTree as ET

# Définir les noms de fichiers pour le CSV et le XML
csv_filename = 'monlecteur.csv'
xml_filename = 'monlecteur.xml'

# Définir les noms de balises pour les données valides et invalides
valid_tag = 'valid_data'
invalid_tag = 'invalid_data'

# Créer les balises racine du document XML
root = ET.Element('monlecteur_xml')

# Créer les balises pour les données valides et invalides
valid_data = ET.SubElement(root, valid_tag)
invalid_data = ET.SubElement(root, invalid_tag)

# Lire le fichier CSV
with open(csv_filename, 'r') as monlecteur:
    reader = csv.DictReader(monlecteur)

    # Parcourir chaque ligne dans le fichier CSV
    for row in reader:
        # Vérifier si toutes les colonnes requises sont présentes dans la ligne
        if all(key in row for key in ('code', 'numero', 'nom', 'prenom', 'date_de_naissance', 'classe' ,'notes')):
            # Créer un élément pour les données valides
            valid_row = ET.SubElement(valid_data, 'row')

            # Ajouter les valeurs des colonnes à l'élément valide
            for key, value in row.items():
                ET.SubElement(valid_row, key).text = value
        else:
            # Créer un élément pour les données invalides
            invalid_row = ET.SubElement(invalid_data, 'row')

            # Ajouter les valeurs des colonnes à l'élément invalide
            for key, value in row.items():
                ET.SubElement(invalid_row, key).text = value

# Créer un objet ElementTree à partir de l'élément racine
tree = ET.ElementTree(root)

# Écrire l'arbre XML dans un fichier
tree.write(xml_filename)

print(f"Les données valides ont été écrites dans {valid_tag}")
print(f"Les données invalides ont été écrites dans {invalid_tag}")