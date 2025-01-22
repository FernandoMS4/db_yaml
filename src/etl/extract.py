import requests
import json

def get_map_monsters(lista:list) ->list:
    """
    Captura os monstros dos mapas disponibilizados em uma lista

    necessário: ["mapa_01","mapa_02"]
    """
    lista_monstros: list = []
    for mapas in lista:
        try:
            response = requests.get(f"https://www.divine-pride.net/api/database/Map/{mapas}?apiKey=c89e47a2956e1cca82a1f18afcfe81c0")
            file = json.loads(response.text)
            for i in file["spawn"]:
                lista_monstros.append(i["monsterId"])
        except KeyError as e:
            print(e)
    return lista_monstros

def get_monster_status(lista_mob:list) ->list:
    """
    Captura o database dos id's passados em lista

    necessário: ["1234","1235"]
    """
    lista_monstros: list = []
    for mobs in lista_mob:
        try:
            response = requests.get(f"https://www.divine-pride.net/api/database/Monster/{mobs}?apiKey=c89e47a2956e1cca82a1f18afcfe81c0")
            file = json.loads(response.text)
            lista_monstros.append(file)
        except KeyError as e:
            print(e)
    with open("src/data/monster_db.jsonl","w",encoding="utf-8") as archive:
        for i in lista_monstros:
            archive.write(f"{i}\n")

def get_item_db(lista_itens: list) -> list:
    """
    Captura os database dos itens listados 
    lista a ser passada: ["728","1001424","1001087","1001076","etc.."]
    Retorno exemplo: ['Golden_Jewel', 'Hot_Water_Drop_Gem', 'Shining_Crystal', 'Small_Sewing_Box']
    """
    lista_item: list = []
    for itens in lista_itens:
        try:
            response = requests.get(f"https://www.divine-pride.net/api/database/Item/{itens}?apiKey=c89e47a2956e1cca82a1f18afcfe81c0")
            file = json.loads(response.text)
            lista_item.append(file["aegisName"])
        except KeyError as e:
            print(e)
    return lista_item


if __name__ == '__main__':
    #lista_mobs = get_map_monsters(lista=["nif_fild03","moc_akhet"])
    #get_monster_status(lista_mobs)
    print(get_item_db(["728","1001424","1001087","1001076"]))
    