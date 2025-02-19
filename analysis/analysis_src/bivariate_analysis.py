from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Abstract class for bivariate analysis
class BivariateAnalysis(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform bivariate analysis on two features."""
        pass

# Numerical vs Numerical analysis (scatter plot)
class NumericalVsNumericalAnalysis(BivariateAnalysis):
    def analyze(self, df, feature1, feature2):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

# Categorical vs Numerical analysis (box plot)
class CategoricalVsNumericalAnalysis(BivariateAnalysis):
    def analyze(self, df, feature1, feature2):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()

# Strategy pattern to switch between analyses
class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysis):
        """Initialize with a specific analysis strategy."""
        self._strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysis):
        """Change the strategy."""
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Execute the bivariate analysis strategy."""
        self._strategy.analyze(df, feature1, feature2)

# Main execution
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv(r'E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv')

    # Remove extra spaces in column names
    df.rename(columns=lambda x: x.strip(), inplace=True)

    # Analyze numerical vs numerical features
    analyzer = BivariateAnalyzer(NumericalVsNumericalAnalysis())
    analyzer.execute_analysis(df, "Gr Liv Area", "SalePrice")

    # Analyze categorical vs numerical features
    analyzer.set_strategy(CategoricalVsNumericalAnalysis())
    analyzer.execute_analysis(df, "Overall Qual", "SalePrice")
