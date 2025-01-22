import ast
import requests
import json
import yaml

class Mapeamento:
    def __init__(self,arquivo:dict)->dict:
        self.arquivo = arquivo

        self.drops = self.arquivo["drops"]
        self.list_drops = []
        for i in self.drops:
            response = requests.get(f"https://www.divine-pride.net/api/database/Item/{i["itemId"]}?apiKey=c89e47a2956e1cca82a1f18afcfe81c0")
            file = json.loads(response.text)
            self.list_drops.append({"Item": file["aegisName"],"Rate":i["chance"]},)

        self.padrao = {
            "Id" : self.arquivo["id"],
            "AegisName" : self.arquivo["dbname"],
            "Name" : self.arquivo["name"],
            "Level" : self.arquivo["stats"]["level"],
            "Hp" : self.arquivo["stats"]["health"],
            "BaseExp" : self.arquivo["stats"]["baseExperience"],
            "JobExp" :  self.arquivo["stats"]["jobExperience"],
            "Attack" : self.arquivo["stats"]["atk1"],
            "Attack2" : self.arquivo["stats"]["atk2"],
            "Defense" : self.arquivo["stats"]["defense"],
            "MagicDefense" : self.arquivo["stats"]["magicDefense"],
            "Str": self.arquivo["stats"]["str"],
            "Agi": self.arquivo["stats"]["agi"],
            "Vit": self.arquivo["stats"]["vit"],
            "Int": self.arquivo["stats"]["int"],
            "Dex": self.arquivo["stats"]["dex"],
            "Luk": self.arquivo["stats"]["luk"],
            "AttackRange" : self.arquivo["stats"]["attackRange"],
            "SkillRange" : self.arquivo["stats"]["aggroRange"],
            "ChaseRange" : self.arquivo["stats"]["escapeRange"],
            "Size" : self.arquivo["stats"]["scale"],
            "Race" : self.arquivo["stats"]["race"],
            "Element": self.arquivo["stats"]["element"]%10,
            "ElementLevel": 0 if self.arquivo["stats"]["element"]/20 is None else int(self.arquivo["stats"]["element"]/20),
            "WalkSpeed" : self.arquivo["stats"]["movementSpeed"],
            "AttackDelay": 0  if self.arquivo["stats"]["rechargeTime"] is None else int(self.arquivo["stats"]["rechargeTime"]),
            "AttackMotion": 0 if self.arquivo["stats"]["attackSpeed"] is None else int(self.arquivo["stats"]["attackSpeed"]),
            "DamageMotion": (self.arquivo["stats"]["attackedSpeed"]),
            "DamageTaken": 10 if self.arquivo["stats"]["mvp"] is None else 0,
            "Ai": 21 if self.arquivo["stats"]["ai"] =="" else self.arquivo["stats"]["ai"],
            "Modes": {"Detector": True},
            "Drops": {"Item":"apple","Rate":0} if [i for i in self.list_drops] == [] else [i for i in self.list_drops],
        }

if __name__ == "__main__": 

    with open('../data/monster_db.jsonl','r',encoding='utf-8') as file:
        monster_dict: dict = [ast.literal_eval(i) for i in file]
        
    meu_dicionario = []

    for i in monster_dict:
        meu_teste = Mapeamento(i)
        meu_dicionario.append(meu_teste.padrao)


    with open("../data/monster_db.yaml",'w',encoding="utf-8") as out:
        for i in meu_dicionario:
            transform = [{**i}]
            yaml.dump(transform,out,sort_keys=False,allow_unicode=True,default_flow_style=False)