# Multiple Linear Regression — House Price Prediction (Pakistan)

## Files in this folder
- `2_Multiple_Linear_Regression.ipynb` — notebook
- `pakistan_house_prices.csv` — dataset (3000 rows)

## Dataset
Synthetic Pakistan real-estate data:
| Column | Description |
|---|---|
| `city` | Islamabad, Lahore, Karachi, Rawalpindi, Peshawar, Faisalabad, Multan, Bannu |
| `property_type` | House, Flat, Upper Portion, Lower Portion |
| `area_marla` | Plot/house area in Marla |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `age_years` | Age of the house |
| `distance_from_city_center_km` | Distance from city center |
| `has_parking`, `has_gas`, `is_furnished` | Amenity flags (0/1) |
| `price_lakh_pkr` | Target — price in lakh PKR |

## What this notebook covers
1. Loading and exploring the dataset
2. Encoding categorical features (`city`, `property_type`) with One-Hot Encoding
3. Train/test split and training a Multiple Linear Regression model (10 features → price)
4. Evaluating the model (R², MAE, RMSE)
5. Feature importance (coefficients) — which factors raise/lower price the most
6. Actual vs Predicted scatter plot
7. Predicting price for a new house, and comparing the same house across different cities

## Why this dataset
Price here genuinely depends on many factors at once (location, size, condition, amenities) — a realistic case for Multiple Linear Regression, unlike a single-feature setup.

## Result summary
- R² Score: ~0.85
- Strongest positive factors: Islamabad/Karachi/Lahore location, House type
- Strongest negative factors: Bannu location, Lower Portion type

## Requirements
```
pandas
numpy
matplotlib
scikit-learn
```
