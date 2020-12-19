import pandas as pd
import matplotlib.pyplot as plt


def plot_count_data(variables, data):
    for v in variables:
        plt.clf()
        plt.bar([0, 1], [data.loc[data[variables[v]] == 0]["COUNT"].sum(),
                         data.loc[data[variables[v]] == 1]["COUNT"].sum()])
        plt.gcf().canvas.set_window_title('Count for ' + v)
        plt.show()


def plot_correlation_matrix(variables, data):
    correlation_data = data.drop(["COUNT", "PERCENT"], axis=1).corr()

    for v in variables:
        temp = correlation_data[variables[v]].sort_values(ascending=False)
        temp = temp.iloc[1:]
        temp = temp.sort_index()
        plt.clf()
        plt.bar(temp.keys(), temp)
        plt.show()


file = "./data.csv"
data = pd.read_csv(file, delimiter=";")
variables = {
    # Activities of daily living
    "EATING": "Y1",
    "OUT_IN_BED": "Y2",
    "AROUND_INSIDE": "Y3",
    "DRESSING": "Y4",
    "BATHING": "Y5",
    "BATHROOM_TOILET": "Y6",
    # Now instrument ADL
    "HEAVY_HOUSE_WORK": "Y7",
    "LIGHT_HOUSE_WORK": "Y8",
    "LAUNDRY": "Y9",
    "COOKING": "Y10",
    "GROCERY_SHOPPING": "Y11",
    "GO_OUTSIDE": "Y12",
    "TRAVELING": "Y13",
    "MANAGING_MONEY": "Y14",
    "TAKING_MEDICINE": "Y15",
    "TELEPHONING": "Y16"
}
# On trie par nombre d'occurence descendant
data = data.sort_values("COUNT", axis=0, ascending=False)
number_of_samples = data["COUNT"].sum()
print("Nombre d'échantillons: " + str(number_of_samples))
# Ne sert à rien je pense vvv
sum_percent = data["PERCENT"].sum()
print("Somme des pourcentages: " + str(sum_percent))
print("Nombre de personnes qui ne sortent pas ou ne vont pas au lit: "
      + str(data.loc[data[variables["OUT_IN_BED"]] == 0]["COUNT"].sum()))

# Voir les graphiques pour chaque colonne la proportion de 1 et 0
# plot_count_data(variables, data)

# Voir la matrice de corrélation en graphique
# plot_correlation_matrix(variables, data)

# print(correlation_data["Y1"].sort_values(ascending=False))
print("Taille du dataframe: " + str(data.shape))


