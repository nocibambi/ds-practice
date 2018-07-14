# The Stanford Open Policing Datasets(https://openpolicing.stanford.edu/data/) provide information on traffic stops in different states. Please download the csv files for Montana and Vermont. You may also find the README(https://github.com/5harad/openpolicing/blob/master/DATA-README.md) file helpful as you work through the challenge questions. It contains useful information about the dataset, including column descriptions.

import pandas as pd

mon = pd.read_csv("MT_cleaned.csv")

def round_10d(number):
    return round(number, 10 - len(str(round(number))) + 2)

# What proportion of traffic stops in Montana involved male drivers? In other words, divide the number of traffic stops involving male drivers by the total number of stops.
maleprop = mon.driver_gender.value_counts(normalize=True, dropna=False).loc["M"]

print("\nThe proportion of traffic stops involving male drivers in Montana is {}.\n".format(round_10d(maleprop)))
# 0.6749749733

# How many more times likely are you to be arrested in Montana during a traffic stop if you have out of state plates?
plate_arr = mon.loc[:,["is_arrested", "out_of_state"]]

oos_arr = pd.crosstab(plate_arr.out_of_state, plate_arr.is_arrested, normalize='index', margins=True)
out_state_arr = oos_arr.loc[True, True] / oos_arr.loc[False, True] - 1

print("\nIn Montana, with an out of state plate, it is {} more likely to be arrested during a traffic stop than with an instate one.\n".format(round_10d(out_state_arr)))
# 0.2095129351

# Perform a ($\Khi^2 $) test to determine whether the proportions of arrests in these two populations are equal. What is the value of the test statistic?
freqs = pd.crosstab(plate_arr.out_of_state, plate_arr.is_arrested, margins=True)

def chi2_compare(table):
    """Conducts a chi-square homogeneity test on the features of a dataframe. Takes the dataframe and returns the chi-square value.
    """
    colsum = table.sum(axis=1)
    rowsum = table.sum()
    grandsum = colsum.sum()

    expected =  colsum.apply(lambda x: x * rowsum / grandsum)

    chi2 = ((table - expected) ** 2 / expected).sum().sum()

    #dfree = (table.shape[0] - 1) * (table.shape[1] - 1)
    return chi2

chi2 = chi2_compare(freqs.iloc[:-1,:-1])

print("\nThe proportion of arrests for cars with and without out of state plates are not equal. The chi-square homogeneity test value is {}, which (with df=2, p=0,05) is bigger than the 5.99 critical value.\n".format(round_10d(chi2)))
# 128.9324677151

# What proportion of traffic stops in Montana resulted in speeding violations? In other words, find the number of violations that include "Speeding" in the violation description and divide that number by the total number of stops (or rows in the Montana dataset).
speedfreq = mon.violation.str.count("Speeding").value_counts(dropna=False, normalize=True)[1.0]

print("\nThe proportion of traffic stops resulting in speeding violation in Montana is {}.\n".format(round_10d(speedfreq)))
# 0.6580998112

#How much more likely does a traffic stop in Montana result in a DUI than a traffic stop in Vermont? To compute the proportion of traffic stops that result in a DUI, divide the number of stops with "DUI" in the violation description by the total number of stops.
ver = pd.read_csv("VT_cleaned.csv")
mondui = mon.violation.str.count("DUI").value_counts(normalize=True)[1.0]
verdui = ver.violation.str.count("DUI").value_counts(normalize=True)[1.0]

print("\nIn Montana, a traffic stop is {} more likely to result in a DUI, than in Vermont.\n".format(round_10d(mondui / verdui)))

#What is the extrapolated, average manufacture year of vehicles involved in traffic stops in Montana in 2020? To answer this question, calculate the average vehicle manufacture year for each year's traffic stops. Extrapolate using a linear regression.
from numpy import array, nan
import statsmodels.formula.api as smf

vehyear = mon.loc[:,['stop_date', 'vehicle_year']]
vehyear.stop_date = vehyear.stop_date.str.slice(0, 4)

vehyear.vehicle_year.replace(to_replace=['NON-', 'UNK'], value=nan, inplace=True)
vehyear.vehicle_year = vehyear.vehicle_year[vehyear.vehicle_year.apply(lambda x: type(x) == str)].apply(lambda x: float(x))

stop_veh_yr = vehyear.groupby(by="stop_date").mean()

y = array(stop_veh_yr.vehicle_year)
X = array(stop_veh_yr.index, dtype=int)

model = smf.OLS(y, X).fit()
prediction = model.predict(2020)[0]

print("\nBased on the annual traffic stop averages, the extrapolated vechicle manufacture year for 2020 is {}.\n".format(round_10d(prediction)))
# 2010.885346


#What is the p-value of this linear regression?
print("\nThe p-value of the linear regression is {}.\n".format(round_10d(model.pvalues[0])))
#0.0

#Combining both the Vermont and Montana datasets, find the hours when the most and least number of traffic stops occurred. What is the difference in the total number of stops that occurred in these two hours? Hours range from 00 to 23. Round stop times down to compute this difference.
hours = pd.concat([ver.stop_time, mon.stop_time])
hours = hours.str.slice(0,2).value_counts()

diff = hours.max() - hours.min()

print("\nThe difference between the number of stops occurred in the hours with the least and most stops in Montana and Vermont combined is {}.\n".format(diff))
# 95344

#We can use the traffic stop locations to estimate the areas of the counties in Montana. Represent each county as an ellipse with semi-axes given by a single standard deviation of the longitude and latitude of stops within that county. What is the area, in square kilometers, of the largest county measured in this manner? Please ignore unrealistic latitude and longitude coordinates.
import math as m
from geopy.distance import vincenty

def ellipse(min_sax, maj_sax):
    area = min_sax * maj_sax * m.pi
    return area

def saxes(m_lat, m_lon, s_lat, s_lon):
    minsax = vincenty(((m_lat - 1/2 * s_lat), (m_lon)),
                     ((m_lat + 1/2 * s_lat), (m_lon))).km
    majsax = vincenty(((m_lat), (m_lon - 1/2 * s_lon)),
                     ((m_lat), (m_lon + 1/2 * s_lon))).km
    return minsax, majsax

def calc_area(*arg):
    area = ellipse(*saxes(*arg))
    return area

cords = mon[['lat', 'lon', 'county_name']].copy()

poslonidx = cords[(cords['lon'] >= 104) & (cords['lon'] <= 116)].index
cords.loc[poslonidx,'lon'] *= -1

latcrit = (cords['lat'] >= 43.76929) & (cords['lat'] <= 49.80593)
loncrit = (cords['lon'] <= -(104 + 2/60)) & (cords['lon'] >= -(116 + 3/60))

monidx = cords[latcrit & loncrit].index
cords = cords.loc[monidx, :]

county_cords = cords.groupby('county_name').agg(['mean','std']).stack(level = 0).unstack(level = 1)

maxarea = county_cords.apply(lambda x: ellipse(*saxes(*x)), axis = 1).sort_values(ascending=False)[0]
maxarea_name = county_cords.apply(lambda x: ellipse(*saxes(*x)), axis = 1).sort_values(ascending=False).index[0]

print("\nWhen estimating county area size by traffic stop coordinates, the biggest county in Montana is {} with an area of {} sq mi.\n".format(maxarea_name, round_10d(maxarea)))
# 2201.719112
