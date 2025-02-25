#     # Example dataframe
# import pandas as pd
# df = pd.read_csv("E:\projects\house-prices-predictor-system\extracted_data\AmesHousing.csv")
# df_numeric = df.select_dtypes(include=[np.number]).dropna()

# # Initialize the OutlierDetector with the Z-Score based Outlier Detection Strategy
# outlier_detector = OutlierDetector(ZScoreOutlierDetection(threshold=3))

# # Detect and handle outliers
# outliers = outlier_detector.detect_outliers(df_numeric)
# df_cleaned = outlier_detector.handle_outliers(df_numeric, method="remove")

# print(df_cleaned.shape)
# Visualize outliers in specific features
# outlier_detector.visualize_outliers(df_cleaned, features=["SalePrice", "Gr Liv Area"])