from abc import ABC , abstractmethod
import seaborn  as sns
import matplotlib.pyplot as plt
import pandas as pd

class univarient_analyzer(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        # Perform univariate analysis on a specific feature of the dataframe.
        pass

class NumericalUnivariateAnalysis(univarient_analyzer):

    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots the distribution of a numerical feature using a histogram and KDE.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

class CategoricalUnivariateAnalysis(univarient_analyzer):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots the distribution of a categorical feature using a bar plot.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

# Context Class that uses a univarient_analyzer
class UnivariateAnalyzer:
    def __init__(self, strategy: univarient_analyzer):
        """
        Initializes the UnivariateAnalyzer with a specific analysis strategy.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: univarient_analyzer):
        """
        Sets a new strategy for the UnivariateAnalyzer.
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes the univariate analysis using the current strategy.
        """
        self._strategy.analyze(df, feature)

if __name__ == "__main__":
    # Example usage of the UnivariateAnalyzer with different strategies.

   # Load dataset
    df = pd.read_csv(r'E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv')

    # Analyzing a numerical feature
    analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    analyzer.execute_analysis(df, 'SalePrice')

    # Analyzing a categorical feature
    analyzer.set_strategy(CategoricalUnivariateAnalysis())
    analyzer.execute_analysis(df, 'Neighborhood')
    pass





