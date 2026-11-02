# -*- coding:Latin-1 -*-
# ******************************************************************************
# @project yqtVlm
# @file    yqtVlm.py
# @author  yJPO92 sur github / jpo92 sur Virtualregatta
# @brief   A partir du JSON listant les zones interdites de VirtualRegatta
#          créer autant de fichiers '.qbar' représentant
#          les barrières à installer ds qtVlm
#
# @version 1.0
# ******************************************************************************
# Modified :
# Created  : nov 2026
# ******************************************************************************
# @note Le JSON importé depuis ITYC VR Dashboard doit d'abord être débarrassé
#       des caractères ANSI (éèçà...) via Notepad2
# ******************************************************************************

from os import path
import subprocess
import json
import jsonpath_ng as jp


# ****
# C'est le point de départ!!
# ****
if __name__ == '__main__':
    # clear terminal
    subprocess.run("cls", shell=True)
    # Msg de bienvenue
    print('\n**  salut Maître Jean  **')
    print("Prog: " + path.basename(__file__))

    # ---------------- charger JSON file to dict
    # try not necessary, I known the file!!!
    # try:
    # except FileNotFoundError as e:
    #     print(f"Erreur lors de la lecture du fichier JSON : {e}")
    #     exit(1)
    with open("restrictedZones_IMOCA.json", "r") as fic:
        zones = json.load(fic)
        print(zones)
        fic.close()

    print("\n")


    # ----- combien de barrieres?
    features_query = jp.parse("$.features[*]")
    barrieres = features_query.find(zones)
    print("nb de barrieres: ", len(barrieres))

    # ne fonctionne pas
    # for feat in barrieres:
    #     print("\n",feat.value)
    #     file_name_query = jp.parse("$..name")
    #     file_name = file_name_query.find(feat)
    #     print("\tfichier: ",file_name)
    # input('\nPress the Enter key to exit...')

    # ----- recuperer noms de fichiers qbar
    file_name_query = jp.parse("$..name")
    files_name =file_name_query.find(zones)
    print("\tfichiers qbar")
    for result in files_name:
        print(result.value)

    # ----- recupere coordonees barriere
    bar_coord_query = jp.parse("$..coordinates")
    bars_coordinates = bar_coord_query.find(zones)
    print("\tcoordonees")
    for result in bars_coordinates:
        print(result.value)

    # ----- on sait qu'i y a x barrieres
    for i in range(len(barrieres)):
        # check/debug
        print("\nidx: ", i)
        print("file: ", files_name[i].value)
        print("coord: ", bars_coordinates[i].value)
        # ---- multiplier les coordonnées par 1000 (be carefull 3 [, we take indice 0)
        coord1000 = [[x * 1000 for x in sous_liste] for sous_liste in bars_coordinates[i].value[0]]
        print("coordx1000: ", coord1000)
        # ---- transformer liste en chaine comme attendu par qtVlm
        coord_chaine = ""
        for a in coord1000:
            # for b in a:
            coord_chaine = coord_chaine + str(a[0]) + "/" + str(a[1]) + ";"
        # - may be remove the last ';'
        print("coord_chaine: ", coord_chaine)
        # ---- creer chaine complete correspondant a la barriere
        qbarriere = "{\"color\":\"#550000\",\"name\":\"" \
                    + files_name[i].value \
                    + "\",\"points\":[[\"\",\"1\",\"#550000\",\"" \
                    + coord_chaine + "\"]]}"
        print("file content: " + qbarriere)
        # ---- écrire tout cela dans un fichier
        with open("zones/" + files_name[i].value + ".qbar", "w", encoding="utf-8") as f:
            f.write(qbarriere)
        f.close()

# ------- It is the end
print("\nc'est fini!")

# Pause de l'interface textuelle pour voir ce qui s'est passé!!
# input('\nPress the Enter key to exit...')

# That's all folks!
