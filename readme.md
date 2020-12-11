# ECE143: Understanding factors attributing to accidents in California
## Team members:  John O’Boyle, Derek Yang, Isaias Larios, Kaixin Lin
## Problem:
The state of California accounts for 11% of the nation's auto deaths. Visualizing the factors that lead to accidents can help understand motor vehicle safety.
## Dataset:
US-Accidents open dataset ( https://smoosavi.org/datasets/us_accidents )
The entire dataset contains data on 3.5 million traffic accidents collected from February 2016 to June 2020 for the Contiguous United States. The data also includes attributes pertaining to environmental factors, locations, times, and other reported details of the accident. 
## Proposed Solution:
Our proposed solution is to use this dataset to visualize correlations between car accidents and various factors and try to answer the following questions:
- How much do the following factors affect accident severity and rates? Including but not limited to:
  - Traffic signs
  - Weather
  - Speed and acceleration
  - Time of day and traffic patterns
  - Traffic hotspots and high risk locations
- What measure is most effective in decreasing traffic accidents?


## File Structure
```
root
├── data
│   └── CA_County_Pop_Miles.csv
│
├── scripts
│   ├── __init__.py
│   ├── pie_charts.py
│   ├── plot_for_capita.py
│   ├── plot_for_sign.py
│   ├── plot_for_time.py
│   └── plot_for_weather.py
│
├── pics
│
├── Analysis-Overview.ipynb
│
└── Team_6_Presentation.pdf

```
## Third Party Modules
- pandas==1.1.3
- matplotlib==3.1.2
- numpy==1.18.1
- seaborn==0.11.0
- altair==4.1.0
- folium==0.11.0

## How to Run the Code
The `requirements.txt` file has listed all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```
Then, you need to download the US-Accidents open dataset ( https://smoosavi.org/datasets/us_accidents ) and put the `US_Accidents_June20.csv` into data folder.

All visualizations were produced in `Analysis-Overview.ipynb`. You can run the following command to see the result.

```
jupyter notebook Analysis-Overview.ipynb 
```
