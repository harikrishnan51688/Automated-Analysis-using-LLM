# Happiness Dataset Analysis

## Filename
- `happiness.csv`

## Dataset Overview
- **Shape**: (2363, 11)
- **Total Records**: 2363
- **Features**: 11 columns

## Columns
The dataset contains the following columns:
1. **Country name**: Name of the country.
2. **year**: Year of the data recorded.
3. **Life Ladder**: A measure of well-being or happiness (scale from 0 to 10).
4. **Log GDP per capita**: Logarithm of GDP per capita, a measure of economic performance.
5. **Social support**: A measure of perceived social support (scale from 0 to 1).
6. **Healthy life expectancy at birth**: Average expected healthy years of life at birth.
7. **Freedom to make life choices**: A measure of personal freedom (scale from 0 to 1).
8. **Generosity**: A measure of generosity where negative values indicate less generosity (scale from -0.34 to +0.70).
9. **Perceptions of corruption**: Measure of perceived corruption (scale from 0 to 1).
10. **Positive affect**: Measure of positive emotions (scale from 0 to 1).
11. **Negative affect**: Measure of negative emotions (scale from 0 to 1).

## Summary Statistics
- **Count of Records**: Most variables have complete data, while a few have missing values:
  - `Life Ladder`: 28 missing values
  - `Log GDP per capita`: 28 missing values
  - `Social support`: 13 missing values
  - `Healthy life expectancy at birth`: 63 missing values
  - `Freedom to make life choices`: 36 missing values
  - `Generosity`: 81 missing values
  - `Perceptions of corruption`: 125 missing values
  - `Positive affect`: 24 missing values
  - `Negative affect`: 16 missing values

- **Unique Countries**: 165 unique countries are represented in the dataset.
- **Year Range**: Data spans from 2005 to 2023.

### Descriptive Statistics
| Metric                   | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy | Freedom to make choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|--------------------------|-------------|---------------------|----------------|-------------------------|-------------------------|------------|---------------------------|-----------------|-----------------|
| Mean                     | 5.48        | 9.40                | 0.81           | 63.40                   | 0.75                    | 0.00       | 0.74                      | 0.65            | 0.27            |
| Standard Deviation       | 1.13        | 1.15                | 0.12           | 6.84                    | 0.14                    | 0.16       | 0.18                      | 0.10            | 0.09            |
| Minimum                  | 1.28        | 5.53                | 0.23           | 6.72                    | 0.23                    | -0.34      | 0.03                      | 0.18            | 0.08            |
| 25th Percentile          | 4.65        | 8.51                | 0.74           | 59.20                   | 0.66                    | -0.11      | 0.69                      | 0.57            | 0.21            |
| Median                   | 5.45        | 9.50                | 0.83           | 65.10                   | 0.77                    | -0.02      | 0.80                      | 0.66            | 0.26            |
| 75th Percentile          | 6.32        | 10.39               | 0.90           | 68.55                   | 0.86                    | 0.09       | 0.87                      | 0.74            | 0.33            |
| Maximum                  | 8.02        | 11.68               | 0.99           | 74.60                   | 0.99                    | 0.70       | 0.98                      | 0.88            | 0.71            |

## Key Insights
- **Average Happiness**: The average `Life Ladder` score is approximately 5.48, indicating a moderate level of happiness among surveyed countries.
- **Economic Influence**: The mean `Log GDP per capita` is 9.40 (approximately $12,143), suggesting a strong correlation between economic performance and happiness levels.
- **Social Support**: The average social support score of 0.81 indicates that most individuals perceive a high level of social backing.
- **Health and Longevity**: The average `Healthy life expectancy at birth` is 63.40 years, with considerable variation suggested by the standard deviation.
- **Perceptions of Freedom**: The mean freedom score (0.75) reflects that most individuals feel they have a considerable ability to make life choices.
- **Generosity**: Interestingly, the average `Generosity` score is close to zero, indicating a potential trend where many countries exhibit low levels of generosity, or the data might be influenced by the number of missing values.
- **Emotional Metrics**: The average `Positive affect` is 0.65, indicating a generally positive emotional outlook, whereas `Negative affect` is considerably lower at 0.27, allowing room for optimism.

## Unique Characteristics
- The dataset covers multiple years and various countries, allowing for dynamic analysis such as trends over time and comparisons across regions.
- The presence of numerous socioeconomic factors suggests potential multivariate analyses to explore correlations among happiness, economic indicators, and social metrics.
- Missing value patterns can indicate data quality issues in certain variables, emphasizing the need for careful pre-processing when performing analyses.

## Future Analysis
- Conducting correlations between different factors such as GDP, social support, and life expectancy with happiness levels.
- Exploring time series analyses to assess how happiness scores have changed across years, particularly post significant global events (e.g., economic crises, pandemics).
- Investigating geographical patterns or clusters of happiness based on region, and exploring inter-country comparisons for a more in-depth understanding of societal well-being.