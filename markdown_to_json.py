import markdown
import json
import re


def extract_tables_from_markdown(file_path):
    # Lire le contenu du fichier Markdown
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convertir le contenu Markdown en HTML
    html_content = markdown.markdown(markdown_content, extensions=['markdown.extensions.tables'])

    # Rechercher les balises de tableau dans le HTML
    table_pattern = re.compile(r'<table.*?>.*?</table>', re.DOTALL)
    table_matches = table_pattern.findall(html_content)

    # Créer une liste pour stocker les tables extraites
    extracted_tables = []

    # Ajouter les tables extraites à la liste
    for table_match in table_matches:
        extracted_tables.append(table_match)

    return extracted_tables


def tables_from_markdown_to_json(file_path:str,json_path:str="tables.json"): 
    extracted_tables = extract_tables_from_markdown(file_path)
    
    tables_json = []
    for table in extracted_tables : 
        # Extraire les lignes du tableau HTML
        table_rows = table.split('<tr>')[1:]
        table_rows = [row.split('</td>')[:-1] for row in table_rows]

        # Supprimer les balises HTML et les espaces vides
        table_data = [[cell.replace('\n<td>', "") for cell in row] for row in table_rows]
        # Créer une liste de dictionnaires avec les données du tableau
        table_json = []
        for row in table_data:
            row_dict = {}
            for i, cell in enumerate(row):
                if i == 0 : 
                    row_dict[f"Paper"] = cell
                else : 
                    row_dict[f"Code"] = cell
            table_json.append(row_dict)
        tables_json.append(table_json[1:])
    with open(json_path, "w") as file_write : 
        json.dump(tables_json, file_write)
    return tables_json

if __name__ == "__main__" : 
    path_to_readme = "old_repo_readme.md"
    path_to_readme_en = "old_repo_readme_en.md"
    
    tables_from_markdown_to_json(path_to_readme, "tables_readme.json")
    tables_from_markdown_to_json(path_to_readme_en, "tables_readme_en.json")