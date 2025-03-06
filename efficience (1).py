import streamlit as st  # Importer Streamlit

# Titre du site
st.title("Tableau de Bord d'Efficience")

# Exemple de données
production = 1000  # Remplace par ta vraie valeur
wsd = 1.2  # Work Standard Data
nb_personnes = 5  # Nombre de personnes

# Calcul de l'efficience
efficience = ((production * wsd) / (nb_personnes * 460)) * 100

# Affichage de l'efficience sous forme de texte
st.metric(label="Efficience (%)", value=f"{efficience:.2f}%")

# Ajouter un graphique avec Matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(["Efficience"], [efficience], color='blue')
ax.set_ylim(0, 100)  # Limite de la jauge
st.pyplot(fig)  # Afficher le graphique

# Lecture du fichier Excel (tu devras remplacer par le chemin correct de ton fichier)
import pandas as pd

# Exemple de lecture d'un fichier Excel
# Remplace 'LIST.xlsx' par le chemin de ton fichier Excel téléchargé
df = pd.read_excel('LIST.xlsx', engine='openpyxl')

# Affiche les 5 premières lignes de tes données pour vérifier
df.head()

# Vérifie les types de données dans le DataFrame
df.dtypes

# Convertir la colonne 'NB PERSONNES' en numérique (entiers)
df['NB PERSONNES'] = pd.to_numeric(df['NB PERSONNES'], errors='coerce')

# Convertir la colonne 'TEMPS CYCLE' en numérique (entiers)
df['TEMPS CYCLE'] = pd.to_numeric(df['TEMPS CYCLE'], errors='coerce')

# Calculer l'efficience par famille
df['Efficience (%)'] = ((40 * df['WSD']) / (df['NB PERSONNES'] * 460)) * 100

# Grouper les données par famille et calculer la moyenne de l'efficience pour chaque famille
efficience_par_famille = df.groupby('FAMILLE')['Efficience (%)'].mean().reset_index()

# Afficher les résultats
efficience_par_famille.head()

# Visualiser avec Plotly pour afficher des jauges
import plotly.graph_objects as go

fig = go.Figure()

for i, row in efficience_par_famille.iterrows():
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=row['Efficience (%)'],
        title={"text": f"Famille: {row['FAMILLE']}"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkblue"},
            "steps": [
                {"range": [0, 40], "color": "red"},
                {"range": [40, 70], "color": "yellow"},
                {"range": [70, 100], "color": "green"}
            ]
        }
    ))

# Mettre en forme le tableau de bord
fig.update_layout(
    title="Tableau de bord de l'efficience par famille",
    grid={'rows': len(efficience_par_famille), 'columns': 1},
    height=500 * len(efficience_par_famille),
    showlegend=False
)

# Afficher le tableau de bord
st.plotly_chart(fig)
