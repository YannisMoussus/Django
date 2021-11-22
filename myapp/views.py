from typing import AsyncContextManager
import requests
from django.http import HttpResponse, response
from django.shortcuts import render
from django.core.paginator import Paginator
import math
import logging
import json


# Create your views here

def index(request):
    return render(request, 'myapp/index.html')

def pokemon(request):
    
    pokeApi = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
    
    result = pokeApi.json()
    
    #RECUPERER LE(S) TYPE(S) DU POKEMON
    pokemon_type = []
    url_types = []
    for i in result["types"]:
        pokemon_type.append(i["type"]["name"])
        url_types.append(i["type"]["url"])  
        
    # #RECUPERER LE(S) TYPE(S) DU POKEMON EN FRANCAIS
    type_francais = []
    
    pokeApiType1 = requests.get(url_types[0])
    pokeApiType2 = requests.get(url_types[1])
    
    resultType1 = pokeApiType1.json()
    resultType2 = pokeApiType2.json()
    
    for i in resultType1["names"]:
        if i["language"]["name"] == "fr":
            type_francais.append(i["name"])
    
    for i in resultType2["names"]:
        if i["language"]["name"] == "fr":
            type_francais.append(i["name"])
    
    # #RECUPERER LA COULEUR DU TYPE DU POKEMON
    type_couleur = []
    colors = {
        'fire': '#de3700',
        'grass': '#21c400',
        'electric': '#fa9a00',
        'water': '#087fc4',
        'ground': '#8f4300',
        'rock': '#3b3a39',
        'fairy': '#ab18ad',
        'poison': '#175900',
        'bug': '#f07605',
        'dragon': '#c43800',
        'psychic': '#819605',
        'flying': '#c93838',
        'fighting': '#996909',
        'normal': '#996909',
        'ghost':'#240342',
        'dark': '#0f0f0f',
        'ice': '#0388a6',
        'steel': '#696B6F'
    }
    type_couleur.append(colors[pokemon_type[0]])
    type_couleur.append(colors[pokemon_type[1]])

    
    # #RECUPERER LES ABILITES DU POKEMON
    abilities = []
    url_abilities = []
    for l in result["abilities"]:
        abilities.append(l["ability"]["name"])
        url_abilities.append(l["ability"]["url"])
    
    #RECUPERER LES ABILITES DU POKEMON (FRANCAIS)
    abilities_francais = []
    description_abilities1 = []
    description_abilities2 = []
    
    pokeApiAbility1 = requests.get(url_abilities[0])
    pokeApiAbility2 = requests.get(url_abilities[1])
    
    resultAbility1 = pokeApiAbility1.json()
    resultAbility2 = pokeApiAbility2.json() 
    
    for i in resultAbility1["names"]:
        if i["language"]["name"] == "fr":
            abilities_francais.append(i["name"])
    for i in resultAbility1["flavor_text_entries"]:
        if i["language"]["name"] == "fr":
            description_abilities1.append(i["flavor_text"])
    
    for i in resultAbility2["names"]:
        if i["language"]["name"] == "fr":
            abilities_francais.append(i["name"])
    for i in resultAbility2["flavor_text_entries"]:
        if i["language"]["name"] == "fr":
            description_abilities2.append(i["flavor_text"])
      
    
    # #RECUPERER LE(S) FAIBLESSE(S) ET LE(S) POINT(S) FORT(S) DU POKEMON
    weak = []
    strong = []
    
    pokeApiType = requests.get(url_types[0])
    resultType = pokeApiType.json()
    for j in resultType["damage_relations"]["double_damage_from"]:
        weak.append(j["name"])
    for j in resultType["damage_relations"]["double_damage_to"]:    
        strong.append(j["name"])
    
    #RECUPERER LE SEXE DU POKEMON (FEMALE / MALE / NO GENDER)
    pokeApiFemale = requests.get("https://pokeapi.co/api/v2/gender/1")
    resultFemale = pokeApiFemale.json()
    pokeApiMale = requests.get("https://pokeapi.co/api/v2/gender/1")
    resultMale = pokeApiMale.json()    
    pokeApiNoGender = requests.get("https://pokeapi.co/api/v2/gender/1")
    resultNoGender = pokeApiNoGender.json()
    
    for i in resultFemale["pokemon_species_details"]:
        if(i["pokemon_species"]["name"] == result["name"]):
            female = "Femelle"
    
    for i in resultMale["pokemon_species_details"]:
        if(i["pokemon_species"]["name"] == result["name"]):
            male = "Male"
    
    for i in resultNoGender["pokemon_species_details"]:
        if(i["pokemon_species"]["name"] == result["name"]):
            no_gender = "Pas de genre"
    
    # #RECUPERER LA DESCRIPTION DU POKEMON (FRANCAIS)
    pokeApiDesc = requests.get("https://pokeapi.co/api/v2/pokemon-species/charizard")
    resultDesc = pokeApiDesc.json()
    
    for j in resultDesc["flavor_text_entries"]:
        if(j["language"]["name"]=="fr"):
            desc = j["flavor_text"]
            break
    
    # #RECUPERER LE NOM FRANCAIS DU POKEMON
    for l in resultDesc["names"]:
        if(l["language"]["name"]=="fr"):
            namefr = l["name"]
    
    # #RECUPERER LES STATS DU POKEMON
    stats = []
    for k in result["stats"]:
        stats.append(k["base_stat"])
    
    # #RECUPERER TAUX DE CAPTURE
    tauxDeCapture = resultDesc["capture_rate"]
    
    #RECUPERER HABITAT DU POKEMON ANGLAIS ET FRANCAIS
    habitat = resultDesc["habitat"]["name"]
    habitatUrl = resultDesc["habitat"]["url"]
    
    habitatApi = requests.get(habitatUrl)
    resultHabitat = habitatApi.json()
    
    for i in resultHabitat["names"]:
        if i["language"]["name"] == "fr":
            habitatFr = i["name"]
    
    # #RECUPERER LES EVOLUTIONS DU POKEMON
    evoUrl = resultDesc["evolution_chain"]["url"]
    evoUrlApi = requests.get(evoUrl)
    resultEvo = evoUrlApi.json()
    
    evoList = []
    
    try:
        evoPhaseUne = resultEvo["chain"]["species"]["name"]
    except:
        evoPhaseUne = "None"    
    try:
        evoPhaseDeux = resultEvo["chain"]["evolves_to"][0]["species"]["name"]
    except:
        evoPhaseDeux = "None"    
    try: 
        evoPhaseTrois = resultEvo["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
    except:
        evoPhaseTrois = "None"
     
    # #RECUPERER IMAGES ET ID DES EVOLUTIONS   
    evoList = [evoPhaseUne, evoPhaseDeux, evoPhaseTrois]
    evoListImage = []
    evoListId = []
    
    
    if (evoList[0] != "None"):
        pokeApiEvoUn = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(evoList[0]))
        resultEvoUn = pokeApiEvoUn.json()
        evoListImage.append(resultEvoUn["sprites"]["front_default"])
        evoListId.append(resultEvoUn["id"])
    if (evoList[1] != "None"):
        pokeApiEvoDeux = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(evoList[1]))
        resultEvoDeux = pokeApiEvoDeux.json()
        evoListImage.append(resultEvoDeux["sprites"]["front_default"])
        evoListId.append(resultEvoDeux["id"])
    if (evoList[2] != "None"):
        pokeApiEvoTrois = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(evoList[2]))
        resultEvoTrois = pokeApiEvoTrois.json()
        evoListImage.append(resultEvoTrois["sprites"]["front_default"])
        evoListId.append(resultEvoTrois["id"])
    
    #RECUPERER LES DIFFERENTES ATTAQUES DU POKEMON
    attaquesUrl = []
    attaquesFr = []
    description_attaquesFr = []
    
    for x in result["moves"]:
        attaquesUrl.append(x["move"]["url"])

    for x in attaquesUrl:
        pokeApiAttaques = requests.get(x)
        resultAttaques = pokeApiAttaques.json()
        for y in resultAttaques["flavor_text_entries"]:
            if y["language"]["name"] == "fr":
                description_attaquesFr.append(y["flavor_text"])            
        for z in resultAttaques["names"]:
            if z["language"]["name"] == "fr":
                attaquesFr.append(z["name"])
        
    context = {
        'id': result["id"],
        'name' : result["name"],
        'namefr': namefr,
        'image' : result["sprites"]["front_default"], 
        'type' : pokemon_type,
        'typeFr' : type_francais,
        'color' : type_couleur,
        'male' : male,
        'female' : female,
        'no_gender' : no_gender,
        'weak' : weak,
        'strong' : strong, 
        'weight' : result["weight"]/10,
        'height' : result["height"]/10,
        'abilites' : abilities,
        'abilites_francais' : abilities_francais,
        'desc_abilites_1' : description_abilities1,
        'desc_abilites_2' : description_abilities2,
        'desc' : desc,
        'shape' : resultDesc["shape"]["name"],
        'egg' : resultDesc["egg_groups"][0]["name"],
        'tauxDeCapture' : tauxDeCapture,
        'habitat' : habitat,
        'habitatFr' : habitatFr,
        'evolution' : evoList,
        'evolImage' : evoListImage,
        'evolId' : evoListId,
        'data' : stats,
        'attaque_desc' : description_attaquesFr,
        'attaque_fr' : attaquesFr,
    }
    
    
    return render(request, 'myapp/pokemon.html', context)