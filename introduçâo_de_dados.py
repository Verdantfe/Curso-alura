# -*- coding: utf-8 -*-
"""INTRODUÇÂO DE DADOS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13KnV30B3yyqPuuT4e38TxzhCBb8f1u7t

#Geral
"""

import pandas as pd
import seaborn as sns
notas = pd.read_csv("ratings.csv")
notas.head()

notas.shape

print(sns.__version__)

notas.columns = ["usuarioId", "filmeId", "nota", "tempo"]
notas.head()

notas ['nota']

notas.head()

notas ['nota']

notas ['rank'].unique()

notas ['rank'].value_counts()

notas ["rank"].mean()

notas ["filmeId"]

notas ["usuarioId"].value_counts()

notas ["usuarioId"].value_counts()
# notas.head()

notas ["rank"].median()

rank_filtrado = notas.query("rank > 4")
print(rank_filtrado)

notas ["filmeId"]

media_notas_mais_avaliadas = notas.groupby("filmeId")["rank"].mean()
filmes_mais_avaliados = media_notas_mais_avaliadas.idxmax()
print(filmes_mais_avaliados)

media_notas_menos_avaliadas = notas.groupby("filmeId")["rank"].mean()
filmes_menos_avaliados = media_notas_menos_avaliadas.idxmin()
print(filmes_menos_avaliados)

notas ["rank"].plot(kind = "hist")

notas ["filmeId"].describe()

import seaborn as sns

sns.boxplot(notas["rank"])

notas["rank"].describe()

notas ["filmeId"].describe()

"""# Filmes"""

filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId", "titulo", "genero"]
filmes.head()

"""# Avaliando alguams notas"""

notas.head()

notas.query("filmeId==1").nota.mean()

notas.query("filmeId==2").nota.mean()

media_de_nota_filme = notas.groupby("filmeId").mean().nota
print(media_de_nota_filme)

media_de_nota_filme.plot(kind = "hist")

sns.boxplot(x=media_de_nota_filme)

sns.displot(media_de_nota_filme, bins=50)



"""# TMDB

"""

import seaborn as sns

tmd = pd.read_csv("tmdb_5000_movies.csv")
tmd.head()

tmd.original_language.unique()

tmd.original_language.value_counts().index

filmes_por_linguagem = tmd.original_language.value_counts().to_frame().reset_index()
filmes_por_linguagem.columns = ["original_language", "valor"]
filmes_por_linguagem.head()

sns.barplot(x="original_language", y="valor", data = filmes_por_linguagem)

sns.catplot( x="original_language", kind = "count" ,data = tmd)

total_por_lingua = tmd["original_language"].value_counts()
total_ingles = total_por_lingua.loc["en"]
total_geral =  total_por_lingua.sum()
total_resto = total_ingles - total_geral
print(total_ingles, total_resto)

dados = {
    "lingua" : ["ingles", "outros"],
    "total" : [total_ingles, total_resto]
}
dados = pd.DataFrame(dados)
dados

sns.barplot(x="lingua", y="total", data = dados)

total_linguas_outros_filmes = tmd.query("original_language != 'en'" ).original_language.value_counts()
total_linguas_outros_filmes

filmes_sem_ingles = tmd.query("original_language != 'en'" )

sns.catplot( x="original_language", kind = "count" ,data = filmes_sem_ingles,
            aspect = 2,
            palette = "viridis",
            order = total_linguas_outros_filmes.index
            )

filmes_sem_ingles = tmd.query("original_language != 'en'" )

sns.catplot( x="original_language", kind = "count" ,data = filmes_sem_ingles)



"""
#Revisão
"""

import numpy as np
import matplotlib.pyplot as plt

filmes.head (2)

notas_do_toy = notas.query("filmeId == 1")
notas_do_jumanji = notas.query("filmeId ==2")
print(len(notas_do_jumanji),len(notas_do_toy) )

print(" notas do toy %.2f" % notas_do_toy.nota.mean())
print(" notas do jumanji %.2f" % notas_do_jumanji.nota.mean())
print(notas_do_toy.nota.std(), notas_do_jumanji.nota.std())

print(" notas do toy %.2f" % notas_do_toy.nota.median())
print(" notas do jumanji %.2f" % notas_do_jumanji.nota.median())
print(notas_do_toy.nota.std(), notas_do_jumanji.nota.std())

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

print(filme1.mean(), filme2.mean())    #media
print(np.std(filme1), np.std(filme2))  #std = desvio padrão
print(np.median(filme1), np.median(filme2)) #mediana

plt.hist(filme1)
plt.hist(filme2)

plt.boxplot([filme1, filme2])

plt.boxplot([notas_do_jumanji.nota , notas_do_toy.nota])

