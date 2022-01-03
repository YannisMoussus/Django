PokéGo

PokéGo qu’est-ce que c’est ? Et bien c’est notre pokédex fait à partir de Django. Vous vous demandez sûrement pourquoi Django ? 
Le framework Django nous a été présenté en cours et nous avons aussi pu lire ceci :
« Django est un framework python open-source consacré au développement web 2.0. Les concepteurs Django lui ont attribué le slogan suivant : ‘Le framework web pour les perfectionnistes sous pression’. Il est donc clairement orienté pour les développeurs ayant comme besoin de produire un projet solide rapidement et sans surprise… c’est à dire à tous les développeurs !
Cette phrase d’accroche nous a laissé sur notre faim et nous avons donc décidé de nous lancer dans le projet à l’aide de ce framework. 

La suite de cette magnifique documentation, va vous aider à installer notre pokédex et de le lancer par la suite. Pour cela suivez bien ces étapes et amusez-vous bien sur PokéGo.😉


Étape 1 : Ouvrez le dossier soit dans PyCharm ou alors sur Visual Studio Code.

Étape 2 : Vérifiez bien que le projet se présente ainsi au niveau du dossier Django et également au niveau du dossier myapp :

Étape 3 : Ouvrez le terminal de PyCharm ou de Visual Studio Code

Étape 4 : Placez-vous dans le dossier DjangoProject avec cette commande :


Étape 5 : Une fois dans le dossier DjangoProject, commencer par créer votre environnement avec la commande suivante :


Étape 6 : Une fois dans l’environnement, activez le. C’est facile, pour cela faites la commande suivante toujours en restant dans le dossier DjangoProject :


Une fois créer, cela s’affichera : (le venv que vous voyez est le nom de mon environnement, si vous l’avez nommé pokédex, il affichera pokédex)


Étape 7 : Une fois dans votre environnement, vous allez devoir installer des librairies. Toujours dans le terminal, vous allez installer ces librairies suivantes :
```
pip install sqlparse
pip install requests
pip install urllib3
```
Si vous avez cette erreur, vous devez juste importer Django avec cette commande :
```
pip install Django
```
Étape 8 : Vous allez maintenant lancer le serveur, pour cela voici la commande à faire en restant toujours dans votre environnement :
```
python manage.py runserver
````
Étape 9 : Ensuite copier le lien de votre serveur et ouvrez une page Google et vous allez rechercher le lien de votre serveur :

N’oubliez pas d’ajouter /myapp/pokemon comme ci-contre :

http://127.0.0.1:8000/myapp/pokemon/

Et voilà, vous avez réussi à démarrer notre PokéGo ! Vous pouvez utiliser la barre de recherche pour chercher vos pokémons !
Amusez-vous bien !
