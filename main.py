from src.etl.extract import *
from src.etl.transform import Mapeamento
import yaml
import ast

def main():
    lista_mobs = get_map_monsters(lista=["nif_fild03","moc_akhet"])
    get_monster_status(lista_mobs)

    with open('src/data/monster_db.jsonl','r',encoding='utf-8') as file:
        monster_dict: dict = [ast.literal_eval(i) for i in file]
        
    meu_dicionario = []

    for i in monster_dict:
        meu_teste = Mapeamento(i)
        meu_dicionario.append(meu_teste.padrao)


    with open("src/data/monster_db.yaml",'w',encoding="utf-8") as out:
        for i in meu_dicionario:
            transform = [{**i}]
            yaml.dump(transform,out,sort_keys=False,allow_unicode=True,default_flow_style=False)

if __name__ == "__main__":
    main()