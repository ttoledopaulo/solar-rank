import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.paths import PROCESSED_DIR

try:
    df = pd.read_csv(PROCESSED_DIR / "energia_solar_processed.csv")

    top3 = df.nlargest(3, 'eficiencia')
    sns.set_theme(style="whitegrid")

    fig = plt.figure(figsize=(8, 5))
    fig.canvas.manager.set_window_title("Solar Rank - Dashboard de Eficiência")

    sns.barplot(
        data=top3,
        x="cidade",
        y="eficiencia",
        hue="cidade",
        palette="viridis",
        legend=False
    )

    plt.title("Top 3 cidades com maior eficiência solar", fontsize=14)
    plt.xlabel("Cidade")
    plt.ylabel("Eficiência")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    raise FileNotFoundError("Arquivo processado nao encontrado, rode a pipeline primeiro")
