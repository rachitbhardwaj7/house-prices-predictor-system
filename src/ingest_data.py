import os 
import zipfile
from abc import ABC , abstractmethod
import pandas as pd
#data ingestion  abstract  class
class Data_ingest(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass

class zip_data_ingestor(Data_ingest):
    def ingest(self, file_path)-> pd.DataFrame:
        """ extracts the data from the zip file present on the data"""
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")
        # Find the extracted CSV file (assuming there is one CSV file inside the zip)
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")
        # Read the CSV into a DataFrame
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        # Return the DataFrame
        return df
    
    # Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> Data_ingest:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return zip_data_ingestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")
        
if __name__ == "__main__":
    # # get  the file path  from running file_path.py in   data directory
    # file_path = r"E:\projects\house-prices-predictor-system\data\archive.zip"
    # # geting the file extension by spiliting the ;path from "."
    # file_extension = os.path.splitext(file_path)[1]

    # data_ingest1 = DataIngestorFactory.get_data_ingestor(file_extension)

    # # Ingest the data and load it into a DataFrame
    # df = data_ingest1.ingest(file_path)
    # # Now df contains the DataFrame from the extracted CSV
    # print(df.head())  # Display the first few rows of the DataFrame
    pass


