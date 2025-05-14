import json
import pandas as pd

# Carrega o JSON
with open('Saidas_analises_2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Lista para armazenar os dados achatados
linhas = []

# Itera pelas análises
for analise in data["analises"]:
    base = {
        "empresa": analise["empresa"],
        "ano": analise["ano"],
        "cik": analise["cik"],
        "resumo_da_analise": analise.get("resumo_da_análise") or analise.get("Resumo da Análise"),
        "recomendacao_geral": analise.get("recomendação_geral") or analise.get("Recomendação Geral"),
    }

    # Para cada critério de avaliação, extrai a pontuação, análise e justificativa
    criterios = [
        "clareza",
        "credibilidade_e_objetividade",
        "minimização_e_justificação_do_risco",
        "transparência",
        "apresentação_visual",
        "responsabilização_e_praticidade"
    ]

    for criterio in criterios:
        item = analise.get(criterio, [{}])[0]
        base[f"{criterio}_pontuacao"] = item.get("pontuação")
        base[f"{criterio}_analise"] = item.get("análise") or item.get("Análise")
        base[f"{criterio}_justificativa"] = item.get("justificativa") or item.get("Justificativa")

    linhas.append(base)

# Converte em DataFrame
df = pd.DataFrame(linhas)


df.to_excel("analises.xlsx", index=False)

df.to_csv("analises.csv", index=False)