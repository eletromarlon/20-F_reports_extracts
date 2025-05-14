import json
import pandas as pd

# Carrega o JSON
with open('JSON_taxation-teste.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

linhas = []

for analise in data["analises"]:
    base = {
        "empresa": analise["empresa"],
        "ano": analise["ano"],
        "cik": analise["cik"],
        "resumo_da_analise": analise.get("Resumo da Análise"),
        "recomendacao_geral": analise.get("Recomendação Geral"),
    }

    criterios = [
        "Narrativa_Tributação",
        "Planejamento_Tributário",
        "Impactos_Financeiros"
    ]

    for criterio in criterios:
        item = analise.get(criterio, [{}])[0]
        base[f"{criterio}_pontuacao"] = item.get("pontuação")
        base[f"{criterio}_analise"] = item.get("análise") or item.get("Análise")
        base[f"{criterio}_justificativa"] = item.get("justificativa") or item.get("Justificativa")

    linhas.append(base)


df = pd.DataFrame(linhas)
df.to_excel("JSON_taxation.xlsx", index=False)
df.to_csv("JSON_taxation.csv", index=False)
