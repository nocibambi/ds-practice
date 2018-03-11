# Intro

This exercise is base on the following data set: (https://data.gov.uk/dataset/road-accidents-safety-data) on vehicle accidents.
* "2014 All STATS19 data (accident, casualties and vehicle tables) for 2005 to 2014."
* Information on the variables can be found at the bottom of the page under additional links. In addition, the form which is used to record data by police officers can be found here(http://docs.adrn.ac.uk/888043/mrdoc/pdf/888043_stats19-road-accident-injury- statistics-report-form.pdf).

```python
import pandas as pd
accidents = pd.read_csv('Accidents0514.csv')
vehicles = pd.read_csv('Vehicles0514.csv')
casualties = pd.read_csv("Casualties0514.csv")
```

# 1. Fractions
What fraction of accidents occur in urban areas? Report the answer in decimal form.

## Answering with value_counts()
```python
accidents.Urban_or_Rural_Area.value_counts(normalize = True).iloc[0]
```
0.64265691086842169

## Answering with len()

```python
len(accidents['Urban_or_Rural_Area'][accidents['Urban_or_Rural_Area'] == 1]) / len(accidents['Urban_or_Rural_Area'])
```
0.6426569108684217

## Answering with count()
```python
accidents['Urban_or_Rural_Area'][accidents['Urban_or_Rural_Area'] == 1].count() / accidents['Urban_or_Rural_Area'].count()
```
0.64265691086842169

## count*()
```python
accidents.Urban_or_Rural_Area.count().div(accidents.Urban_or_Rural_Area.count()).iloc[0]
```
0.64265691086842169

## Crosstab
```python
pd.crosstab(accidents.Urban_or_Rural_Area, columns='Urban_or_Rural_Area').div(accidents.Urban_or_Rural_Area.count()).iloc[0,0]
```
0.64265691086842169


## Possible enhancements
 * fraction function
 * Solving it with crosstab
 * Solving it with pivot


# 2. Frequencies
When is the most dangerous time to drive?
 - Find the hour of the day that has the highest occurance of fatal accidents normalized by the total number of accidents that occured in that hour
 - For your answer, submit the corresponding frequency of fatal accidents to all accidents in that hour.
 - Note: round accident times down. For example, if an accident occured at 23:55 it occured in hour 23.


## Solving with value_counts
```python
(accidents.Time.str[:2][accidents.Accident_Severity == 1].value_counts() / accidents.Time.str[:2].value_counts()).max()
```
0.039486673247778874

## Solving with pd.crosstabs()
```python
pd.crosstab(accidents.Time.str[:2], columns = accidents.Accident_Severity, normalize = 'index').iloc[:,0].max()
```
0.039486673247778874

## pivot_table
```python
accidents[['Time', 'Accident_Severity']].pivot_table(index = accidents.Time.str[:2], columns = 'Accident_Severity', aggfunc= 'count').apply(lambda x: x / x.sum(), axis = 1).iloc[:,0].max()
```
0.039486673247778874

## groupby
```python
accidents.Accident_Severity.groupby(by = [accidents.Time.str[:2], accidents.Accident_Severity]).count()
```

## Enhancements
  * function asking for dimension and value and giving back its most frequent hour

# 3. Linear regression
There appears to be a linear trend in the number of accidents that occur each year. What is that trend? Return the slope in units of increased number of accidents per year.



## With every year

```python
import statsmodels.formula.api as sm
years = accidents['Date'].str[-4:]
yr_fr = years.value_counts().sort_index()
data = {'Years': yr_fr.index, 'Accidents': yr_fr.values}
yearly_accidents = pd.DataFrame(data).astype(float)

result = sm.ols('Accidents ~ Years', yearly_accidents).fit()
result.params['Years']
```
-6511.7272727266127

## When taking out 2014 as an outlier
```python
yr_fr = years.value_counts().sort_index()[:-1]
```
...
-7475.4833333333354

## References

http://aimotion.blogspot.hu/2011/10/machine-learning-with-python-linear.html
"TypeError: Axis must be specified when shapes of a and weights differ."

## Enhance
 * Make shorter the dataframe transformation:
 	* create a function which transforms into pandas
 	* create a function which returns the frequency of accidents/casualties/vehicles for a dimension's values
 * Create a function which returns the slope in units of increased number of one value per another value

# 4. Pearson correlation coefficient, data binning
Do accidents in high-speed-limit areas have more casualties? Compute the Pearson correlation coefficient between the speed limit and the ratio of the number of casualties to accidents for each speed limit. Bin the data by speed limit.

```python
cas_val = casualties['Accident_Index'].value_counts()
data = {
	'Accident_Index' : cas_val.index,
	'Number_of_casualties' : cas_val.values}

num_cas = pd.DataFrame(data)
speed_l = accidents[['Accident_Index', 'Speed_limit']]

cas_spl = pd.merge(speed_l, num_cas, on = 'Accident_Index')

pivot = cas_spl.pivot_table(index = 'Speed_limit')

data2 = {'Speed_limit' : pivot.index, 'Cas_rat' : pivot['Number_of_casualties']}
cas_by_spl = pd.DataFrame(data2)

cas_by_spl['Speed_limit'].corr(cas_by_spl['Cas_rat'])

```
0.96593905551148207

## Enhance
 * do this with crosstab
 * user groupby() instead of pivot
 * Make shorter the df transf
 * make a function which joins columns of the different data

## Alternative solution
https://stackoverflow.com/questions/47000959/how-to-calculate-the-correlation-coefficient-of-grouped-quantities-in-pandas/47001197#47001197

Instead of count and sum you can use directly use `mean` of groupby data then use [`series corr`](https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.Series.corr.html) (by default method is pearson) i.e

```python
m = df.groupby('Speed_limit').mean().reset_index()
m['Speed_limit'].corr(m['Number_of_casualties'])

```
Output: 0.99926008128973687

# 5. Conditional probability
How many times more likely are you to be in an accident where you skid, jackknife, or overturn (as opposed to an accident where you don't) when it's raining or snowing compared to nice weather with no high winds? Ignore accidents where the weather is unknown or missing.


Skiddin or overturning
0	None
1	Skidded
2	Skidded and overturned
3	Jackknifed
4	Jackknifed and overturned
5	Overturned
-1	Data missing or out of range

Weather
1	Fine no high winds
2	Raining no high winds
3	Snowing no high winds
4	Fine + high winds
5	Raining + high winds
6	Snowing + high winds
7	Fog or mist
8	Other
9	Unknown
-1	Data missing or out of range

```python
import pandas as pd

accidents = pd.read_csv('Accidents0514.csv')
weather = accidents[['Accident_Index', 'Weather_Conditions']]
%reset_selective -f accidents

vehicles = pd.read_csv('Vehicles0514.csv')
skidding = vehicles[['Accident_Index', 'Skidding_and_Overturning']]
%reset_selective -f vehicles

table = pd.merge(skidding, weather, on = 'Accident_Index', how = 'outer')
table = table[['Skidding_and_Overturning', 'Weather_Conditions']]
table = table[table['Skidding_and_Overturning'] != -1]
table = table[~table['Weather_Conditions'].isin([4, 7, 8, 9, -1])]

## Might use this, but crashes the kernel
## table[(table[table['Skidding_and_Overturning'] != -1]) | (~table['Weather_Conditions'].isin([7, 8, 9, -1]))]

table['Weather_Conditions'] = table['Weather_Conditions'].replace([3, 5, 6], 2)
table['Skidding_and_Overturning'] = table['Skidding_and_Overturning'].replace([2, 3, 4, 5], 1)

crosstab = pd.crosstab(index = table['Skidding_and_Overturning'], columns = table['Weather_Conditions'], margins = True)
crosstab.columns = ['Fine', 'Rain or snow', 'Row_total']
crosstab.index = ['No skid, etc', 'Skid or overturn', 'Column_total']
freqs = crosstab / crosstab.iloc[-1,-1]

ratio = freqs.loc['Skid or overturn', 'Rain or snow'] / freqs.loc['Skid or overturn', 'Fine']
```

## Enhance
 * Review for the error
0.31196593328601846
 * Crosstab: normalize

## Alternative solution
### Question
I have a `DataFrame` in which the rows represent traffic accidents. Two of the columns are `Weather` and `Skidding`:

```python
import pandas as pd

df = pd.DataFrame({'Weather': ['rain', 'fine', 'rain', 'fine', 'snow', 'fine', 'snow'], 'Skidding': ['skid', 'skid', 'no skid', 'no skid', 'skid', 'no skid', 'jackknife']})
```
I'd like to compute how much more likely it is that either skidding or jackknifing occurs when it is raining or snowing compared to when it is not. So far I've come up with a solution using Boolean indexing and four auxiliary data frames:

```python
df_rainsnow = df[[weather in ('rain', 'snow') for weather in df.Weather]]
df_rainsnow_skid = df_rainsnow[[skid in ('skid', 'jackknife') for skid in df_rainsnow.Skidding]]
df_fine = df[df.Weather == 'fine']
df_fine_skid = df_fine[[skid in ('skid', 'jackknife') for skid in df_fine.Skidding]]
relative_probability = len(df_rainsnow_skid)/len(df_fine_skid)
```
which evaluates to a `relative_probability` of `3.0` for this example. This seems unnecessarily verbose, however, and I'd like to refactor it.

One solution I tried is

```python
counts = df.groupby('Weather')['Skidding'].value_counts()
relative_probability = (counts['rain']['skid'] + counts['snow']['skid'] + counts['rain']['jackknife'] + counts['snow']['jackknife']) / (counts['fine']['skid'] + counts['fine']['jackknife'])
```
However, this leads to a `KeyError` because `jackknife` doesn't occur in every weather situation, and anyways it is also verbose to write out all the terms. What is a better way to achieve this?

### Answer
You can use `isin` instead of `... in ... for ...` comprehension; Also no need to filter the data frame if you just need the number at the end, just build the conditions, `sum` and `divide`:

```python
rain_snow = df.Weather.isin(['rain', 'snow'])
(rain_snow & skid).sum()/(fine & skid).sum()
fine = df.Weather.eq('fine')
skid = df.Skidding.isin(['skid', 'jackknife'])
```
3

# 6. Frequencies
How many times more likely are accidents involving male car drivers to be fatal compared to accidents involving female car drivers? The answer should be the ratio of fatality rates of males to females. Ignore all accidents where the driver wasn't driving a car.

vehicle.sex_of_driver
code	label
1	Male
2	Female
3	Not known
-1	Data missing or out of range

vehicle.Vehicle_Type
code	label
1	Pedal cycle
2	Motorcycle 50cc and under
3	Motorcycle 125cc and under
4	Motorcycle over 125cc and up to 500cc
5	Motorcycle over 500cc
8	Taxi/Private hire car
9	Car
10	Minibus (8 - 16 passenger seats)
11	Bus or coach (17 or more pass seats)
16	Ridden horse
17	Agricultural vehicle
18	Tram
19	Van / Goods 3.5 tonnes mgw or under
20	Goods over 3.5t. and under 7.5t
21	Goods 7.5 tonnes mgw and over
22	Mobility scooter
23	Electric motorcycle
90	Other vehicle
97	Motorcycle - unknown cc
98	Goods vehicle - unknown weight
-1	Data missing or out of range


accidents.accident_severity
code	label
1	Fatal
2	Serious
3	Slight

```python
import pandas as pd

accidents = pd.read_csv('Accidents0514.csv')
vehicles = pd.read_csv('Vehicles0514.csv')

table = pd.merge(accidents[['Accident_Index', 'Accident_Severity']], vehicles[['Accident_Index','Sex_of_Driver', 'Vehicle_Type']], how = 'inner', on = 'Accident_Index')

table = table[table['Vehicle_Type'].isin([8, 9, 10, 11, 19, 20, 21, 98])]
table = table[table['Sex_of_Driver'].isin([1, 2])]
table = table[['Accident_Severity', 'Sex_of_Driver']]

crosstab = pd.crosstab(index = table.Sex_of_Driver, columns = table.Accident_Severity, margins = True)
crosstab.index = ['Male', 'Female', 'All']
crosstab.columns = ['Fatal', 'Serious', 'Slight', 'All']

fatality_rates = crosstab.div(crosstab.iloc[:, -1], axis = 'rows')

fatality_rates.loc['Male', 'Fatal'] / fatality_rates.loc['Female', 'Fatal']
```
1.9538711859282092

## Enhance
 * Crosstab: normalize

## Alternative answer
https://stackoverflow.com/questions/47010032/in-pandas-how-to-calculate-the-relative-probabilities-of-values-of-a-column-giv
Here they focus only on cars

```python
g = casualties.merge(vehicles, on='Accident_Index')\
        .query("Vehicle_Type == 'car' and Casualty_Severity == 'fatal'")\
        .groupby('Sex_Driver').Sex_Driver.count()

g / g.sum()
```

### Simpler
```python
vehicle = 'car'
severity = 'fatal'
query("Vehicle_Type == @vehicle and Casualty_Severity == @severity")
```

# 7. Funcitons,
We can use the accident locations to estimate the areas of the police districts. Represent each as an ellipse with semi-axes given by a single standard deviation of the longitude and latitude. What is the area, in square kilometers, of the largest district measured in this manner?


Police Force
code	label
1	Metropolitan Police
3	Cumbria
4	Lancashire
5	Merseyside
6	Greater Manchester
7	Cheshire
10	Northumbria
11	Durham
12	North Yorkshire
13	West Yorkshire
14	South Yorkshire
16	Humberside
17	Cleveland
20	West Midlands
21	Staffordshire
22	West Mercia
23	Warwickshire
30	Derbyshire
31	Nottinghamshire
32	Lincolnshire
33	Leicestershire
34	Northamptonshire
35	Cambridgeshire
36	Norfolk
37	Suffolk
40	Bedfordshire
41	Hertfordshire
42	Essex
43	Thames Valley
44	Hampshire
45	Surrey
46	Kent
47	Sussex
48	City of London
50	Devon and Cornwall
52	Avon and Somerset
53	Gloucestershire
54	Wiltshire
55	Dorset
60	North Wales
61	Gwent
62	South Wales
63	Dyfed-Powys
91	Northern
92	Grampian
93	Tayside
94	Fife
95	Lothian and Borders
96	Central
97	Strathclyde
98	Dumfries and Galloway


```python
import pandas as pd
accidents = pd.read_csv('Accidents0514.csv')
```

## Using groupby
```python
aggs = accidents[['Police_Force', 'Latitude', 'Longitude']].groupby('Police_Force').agg(['mean','std']).stack(level = 0).unstack(level = 1)
```

## Using pivot_tables
```python
polloc = accidents[['Police_Force', 'Longitude', 'Latitude']]
means = polloc.pivot_table(index = ['Police_Force'], aggfunc= 'mean')
stds = polloc.pivot_table(index = ['Police_Force'], aggfunc= 'std')

import math as m

def ellipse(min_sax, maj_sax):
    area = min_sax * maj_sax * m.pi
    return area

from geopy.distance import vincenty

def saxes(m_lat, m_lon, s_lat, s_lon):
    minsax = vincenty(((m_lat - 1/2 * s_lat), (m_lon)),((m_lat + 1/2 * s_lat), (m_lon))).km
    majsax = vincenty(((m_lat), (m_lon - 1/2 * s_lon)),((m_lat), (m_lon + 1/2 * s_lon))).km
    return minsax, majsax

def pol_area(*arg):
    area = ellipse(*saxes(*arg))
    return area

aggs.apply(lambda x: ellipse(*saxes(*x)), axis = 1).max()
```
19458.370872875956

## Enhance
 * Drop empty latitude and longitude values

# 8. exponential distribution
Find the rate at which the number of accidents exponentially decays with age.
 - Age is measured in years.
 - Only consider car drivers who are legally allowed to drive in the UK (17 years or older).
 - Assume that the number of accidents is exponentially distributed with age for driver's over the age of 17.

How fast do the number of car accidents drop off with age?

```python
import pandas as pd

vehicles = pd.read_csv('Vehicles0514.csv')

age = vehicles[vehicles.Age_of_Driver > 16][['Accident_Index', 'Age_of_Driver']]
age_freq = age.groupby(by = 'Age_of_Driver').agg('count')

from scipy.stats import expon
expon.fit(age_freq)[0]
```
-25.287191113338508
