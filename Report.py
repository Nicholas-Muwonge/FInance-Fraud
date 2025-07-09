#Task 1: Total number of rows in the dataset = 1050
#       Total number of columns in the dataset = 15
#      Missing Values and their Percentage:
#                   Missing Values  Percentage
#TransactionID                  10    0.952381
#TransactionDate                10    0.952381
#CustomerID                    712   67.809524
#Amount                        780   74.285714
#Currency                      176   16.761905
#PaymentMethod                 165   15.714286
#MerchantName                  190   18.095238
#MerchantCategory              160   15.238095
#Location                      155   14.761905
#DeviceType                    147   14.000000
#CardType                      184   17.523810
#TransactionStatus             202   19.238095
#IsFraud                       252   24.000000
#CustomerAge                   789   75.142857
#CustomerGender                200   19.047619

#Task 2:
#Appropriate methods to handle missing values:
#a. CustomerAge: Since this feature has a high percentage of missing values (75.14%), we can consider dropping this feature as it may not provide significant insights. Also may not be critical for fraud detection.   
#b. Amount: This feature has a high percentage of missing values (74.29%). We can consider investigating it first whether formatting or encoding issues caused miissing values then consider dropping this feature.
#c. CustomerID: This feature has a high percentage of missing values (67.81%). We can consider dropping this feature as it may not be likely to be informative without user profile. Many missing values make it unsuitable for analysis.
#d. IsFraud: This feature has a moderate percentage of missing values (24.00%). We can consider imputing the missing values with the mode (most common value) since it is a categorical feature.
#e. TransactionStatus, CustomerGender, MerchantCategory, MerchantName, DeviceType, Currency, PaymentMethod, Location: These features have moderate percentages of missing values (15.24% to 19.24%). We can consider imputing the missing values with the mode for categorical features or using a placeholder value like "Unknown" for better analysis.
#f. TransactionID, TransactionDate: These features have a low percentage of missing values (0.95%). We can consider dropping these features as they may not provide significant insights.
#Tree based models like Random forest can handle missing values effectively, so we can consider using them for fraud detection. However, we should still preprocess the data to ensure that the model can learn effectively.

