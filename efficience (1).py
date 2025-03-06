import streamlit as st  # Importer Streamlit

# Titre du site
st.title("Tableau de Bord d'Efficience")

# Exemple de données (remplace ces valeurs par tes vraies données)
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

# Charger et traiter des données à partir d'un fichier Excel (exemple ici)
import pandas as pd

# Exemple de données simulées dans un DataFrame
df = pd.DataFrame({
    'FAMILLE': ['Famille A', 'Famille B', 'Famille C'],
    'Efficience (%)': [85, 65, 92]
})

# Calculer l'efficience par famille (ajusté si nécessaire)
df['Efficience (%)'] = ((40 * df['Efficience (%)']) / (df['Efficience (%)'] * 460)) * 100

# Grouper les données par famille et calculer la moyenne de l'efficience pour chaque famille
efficience_par_famille = df.groupby('FAMILLE')['Efficience (%)'].mean().reset_index()

# Afficher les résultats sous forme de tableau
st.write("Efficience par Famille :")
st.write(efficience_par_famille)

# Créer un graphique de jauge avec Plotly
import plotly.graph_objects as go

fig2 = go.Figure()

# Ajouter une jauge pour chaque famille
for i, row in efficience_par_famille.iterrows():
    fig2.add_trace(go.Indicator(
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

# Mettre en forme le tableau de bord avec plusieurs jauges
fig2.update_layout(
    title="Tableau de bord de l'efficience par famille",
    grid={'rows': len(efficience_par_famille), 'columns': 1},
    height=500 * len(efficience_par_famille),
    showlegend=False
)

# Afficher le graphique avec Plotly
st.plotly_chart(fig2)

