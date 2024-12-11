# media.csv Dataset Analysis

## Overview
This dataset contains information about media entries, specifically movies, collected over a range of years. The dataset includes various attributes such as the publication date, language, media type, title, contributors, and several numeric ratings related to the media.

### Dataset Summary
- **Filename**: media.csv
- **Shape**: (2652, 8)
- **Columns**: 
  - `date`: Release date of the media
  - `language`: Language of the media
  - `type`: Type of the media (e.g., movie)
  - `title`: Title of the media
  - `by`: Contributors to the media
  - `overall`: Overall rating (1-5 scale)
  - `quality`: Quality rating (1-5 scale)
  - `repeatability`: Repeatability rating (1-3 scale)

## Key Insights

### General Characteristics
- **Total Entries**: 2652 rows which indicate a comprehensive collection of media entries.
- **Missing Values**:
  - `date` has 99 missing values.
  - `by` has 262 missing values, suggesting that contributor information is not consistently documented.
  
### Unique Characteristics
- **Date Range**: The dataset has 2055 unique dates, showcasing a wide range of releases across years.
- **Languages**: There are 11 unique languages represented within the dataset, with English as the predominant language.
- **Types of Media**: There are 8 unique types, with `movie` being the most frequent (2211 occurrences).
- **Titles**: A total of 2312 unique titles indicates diversity in media offerings.

### Rating Analysis
- **Overall Ratings**:
  - Average rating is approximately **3.05** with a standard deviation of **0.76**; most ratings cluster around the middle of the scale.
  - The minimum overall rating is **1** and the maximum is **5**, suggesting a rating system that allows for a full range of responses.
  
- **Quality Ratings**:
  - Average quality rating is approximately **3.21** with a standard deviation of **0.80**; similar distribution patterns as overall ratings.
  
- **Repeatability Ratings**:
  - The average repeatability is **1.49**, suggesting that most media is not considered highly rewatchable with a standard deviation of **0.60**. The ratings range from **1** (not repeatable) to **3** (highly repeatable).

### Top Entries
- The most frequently occurring media title is **"Kanda Naal Mudhal"**, which is noted to have appeared **9 times** in the dataset.
- **Contributors**: The most frequent contributor is **Kiefer Sutherland**, with **48 entries** linked with this name.

## Sample Rows
Here are several examples that depict the diversity of data:

| Date       | Language | Type  | Title             | By                                    | Overall | Quality | Repeatability |
|------------|----------|-------|-------------------|---------------------------------------|---------|---------|---------------|
| 15-Nov-24  | Tamil    | movie | Meiyazhagan       | Arvind Swamy, Karthi                 | 4       | 5       | 1             |
| 10-Nov-24  | Tamil    | movie | Vettaiyan        | Rajnikanth, Fahad Fazil              | 2       | 2       | 1             |
| 09-Nov-24  | Tamil    | movie | Amaran            | Siva Karthikeyan, Sai Pallavi        | 4       | 4       | 1             |
| 11-Oct-24  | Telugu   | movie | Kushi             | Vijay Devarakonda, Samantha          | 3       | 3       | 1             |
| 05-Oct-24  | Tamil    | movie | GOAT              | Vijay                                 | 3       | 3       | 1             |

### Conclusion
The `media.csv` dataset provides a rich source of insights into movie ratings, types, contributions, and language diversity. While it is relatively complete, efforts should be made to handle missing `date` and `by` entries to enhance the dataset's robustness for future analyses. Overall, the dataset reflects a varied landscape of media with satisfactory overall and quality ratings.