from abc import ABC, abstractmethod
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Abstract Base Class for Multivariate Analysis
class Multivariate_analysisMultivariate_analysis(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Perform a comprehensive multivariate analysis by generating a correlation heatmap and pair plot.
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self, df):
        pass

    @abstractmethod
    def generate_pairplot(self, df):
        pass

# Concrete Class for Multivariate Analysis with Correlation Heatmap and Pair Plot
class simple_analysis(Multivariate_analysis):
    def __init__(self):
        super().__init__()

    def generate_correlation_heatmap(self, df):
        """ Generates a correlation heatmap """
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        """ Generates and displays a pair plot """
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()

# Main execution
if __name__ == "__main__":  
    # Load dataset
    df = pd.read_csv(r'E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv')

    # Ensure selected features exist in the dataset
    selected_features = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]

    # Perform multivariate analysis
    analyzer1 = simple_analysis()
    analyzer1.analyze(selected_features)
