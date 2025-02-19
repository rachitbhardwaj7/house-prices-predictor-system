from abc import ABC, abstractmethod
import pandas as pd

# Abstract base class for inspection strategies
class datainspectstrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """Abstract method for data inspection"""
        pass

# Strategy: Inspect data types and non-null counts
class datatypeinspectionstrategy(datainspectstrategy):
    def inspect(self, df: pd.DataFrame):
        """Prints the data types and non-null counts"""
        print("\nData Types and Non-null Counts:")
        df.info()  # Avoid extra print()

# Strategy: Inspect summary statistics
class summaryinspectionstrategy(datainspectstrategy):
    def inspect(self, df: pd.DataFrame):
        """Prints summary statistics for numerical and categorical features"""
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))

# Context class for executing strategies
class DataInspector:
    def __init__(self, strategy: datainspectstrategy):
        """Initialize with a strategy"""
        self._strategy = strategy

    def set_strategy(self, strategy: datainspectstrategy):
        """Change the strategy"""
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """Run the current inspection strategy"""
        self._strategy.inspect(df)

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv(r'E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv')

    # Initialize inspector with datatype inspection
    inspector = DataInspector(datatypeinspectionstrategy())
    inspector.execute_inspection(df)

    # Switch to summary statistics inspection
    inspector.set_strategy(summaryinspectionstrategy())
    inspector.execute_inspection(df)
