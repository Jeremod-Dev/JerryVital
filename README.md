# JerryVital
Cette application de bureau permettant de déchiffrer un numéro de sécurité sociale.

## Contexte
J'ai développé cette application de bureau avant de commencer ma formation à l'Institut Universitaire de Technologie du Limousin. Plus récement, j'ai repris le code afin d'effectuer un peu de `refactoring`.

Le but au début du developpement était de me mieux comprendre le système de base de données, de requete sur une base de données et approfondir les bases de IHM en python. Pour ce dernier point, j'ai, d'abord, réalisé une maquette.

![Maquette de l'application JerryVital](https://github.com/Jeremod-Dev/JerryVital/blob/main/MaquetteHomePage.png)

Durant le développement j'ai apporté quelques modifications à ma maquette, comme l'ajout d'une `checkbox` pour valider ou non si la personne est à la retraite. Cette information permet de differentié les personnes nés en 1902 et 2002 par exemple.

L'application peut-être amélioré en proposant par exemple une version en `POO` ou en gérant les cas exceptionnels, comme un numéro commençant par 3, 4, 7 ou 8 (numéro provisoir).