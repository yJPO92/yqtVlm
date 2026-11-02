\page page_readme5 G431RB_Air_Quality

# Project yqtVlm

A partir du JSON listant les zones interdites de VirtualRegatta créer autant de fichiers '.qbar' représentant les barrières à installer dans qtVlm.  

## Hardware
 N/A  

## Software
Python  
pyCharm
plugin jsonpath-ng  

## Fonctionnalities
Parser le fichier JSON à l'aide du plugin 'jsonpath-ng',  
en extraire les noms des zones ainsi que les coordonnées délimitant la zone,  
celles-ci deviendront les coordonnées des points de la barrière au sens qtVlm.  
Le résultat sera écrit dans un fichier dont le format se trouve dans 'Z0-jaune.qbar'.  

##### Inputs
Fichier 'restrictedZones_IMOCA.json' a placer dans le répertoire de qtVlm.py   
Récupéré depuis l'onglet 'config' de I.T.Y.C. Dashboard extension pour Virtual Regatta  

##### Outputs
Autant de fichiers .qbar qu'il y a de zones déclarées.  
Veuillez créer un dossier "zones" dans le répertoire de yqtVlm.py

## Version
##### v1.0: creation avec pyCharm

## Author
**yJPO92 (Jean92)** - nov. 2026  
**jpo92** sur Virtual Regatta  

## License
This project is licensed under the [CC0 1.0 Universal](LICENSE.md) 
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for details.  
