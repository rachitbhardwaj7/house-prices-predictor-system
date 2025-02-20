import matplotlib.pyplot as plt
import seaborn as sns
from  abc import ABC ,abstractmethod
import pandas as pd

class Missing_value_template(ABC):
    def analyze(self, df: pd.DataFrame):
        # Performs a complete missing values analysis by identifying and visualizing missing values.
        self.identify_missing_values(df)
        self.visualize_missing_values(df)
    @abstractmethod
    def identify_missing_values(self,df):
        # Identifies missing values in the dataframe.
        pass
    @abstractmethod
    def visualize_missing_values(self,df):
        # Visualizes missing values in the dataframe.
        pass

class SimpleMissingValuesAnalysis(Missing_value_template):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Prints the count of missing values for each column in the dataframe.
        Parameters:
        """
        print("\nMissing Values Count by Column:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Creates a heatmap to visualize the missing values in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to be visualized.

        Returns:
        None: Displays a heatmap of missing values.
        """
        print("\nVisualizing Missing Values...")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

if __name__ == "__main__":
    # Example usage of the SimpleMissingValuesAnalysis class.

    # Load the data
    df = pd.read_csv(r'E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv')

    # Perform Missing Values Analysis
    missing_values_analyzer = SimpleMissingValuesAnalysis()
    missing_values_analyzer.analyze(df)
    pass

