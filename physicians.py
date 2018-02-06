# cd C:\Users\andras\Dropbox\Learn\Data Incubator\Challenge\Project proposal\Physician Compare datasets\

# Prerequisites
import pandas as pd
ind = pd.read_csv("Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv")
perf = pd.read_csv("Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv")
pat = pd.read_csv("Physician_Compare_2015_Group_Public_Reporting_-_Patient_Experience.csv")
nat = pd.read_csv("Physician_Compare_National_Downloadable_File.csv")

# Number of clinicians
## nat table idenfier numbers
natpac = len(nat['PAC ID'].value_counts())
natnpi = len(nat['NPI'].value_counts())
max(natpac, natnpi)

## There are more clinicians with 'PAC ID', so we are going to use that instead of NPI.

## ind table identifier numbers
indnpi = len(ind['NPI'].value_counts())
indpac = len(ind['PAC ID'].value_counts())

## diffs between the tables
indnat_npi = len(ind['NPI'].value_counts().index[ind['NPI'].value_counts().index.isin(nat['NPI'].value_counts().index) == False])
indnat_pac = len(ind['PAC ID'].value_counts().index[ind['PAC ID'].value_counts().index.isin(nat['PAC ID'].value_counts().index) == False])
indnat_npi == indnat_pac

natind_npi = len(nat['PAC ID'].value_counts().index[nat['PAC ID'].value_counts().index.isin(ind['PAC ID'].value_counts().index) == False])
natind_pac = len(nat['NPI'].value_counts().index[nat['NPI'].value_counts().index.isin(ind['NPI'].value_counts().index) == False])
natind_pac == natind_npi

## Number of clinicians
nucli = indnpi + max(natind_npi, natind_pac) + indnat_npi
print("The number of clinicians is: ")
nucli # The number of clients

# Male to female clinicians ratio
nat.Gender.value_counts()[0] / nat.Gender.value_counts()[1]
## The male to female ratio is 1.3073393456791762.

# The highest ratio of female clinicians to male clinicians with a given type of credential.
nat.Gender.groupby(by = [nat.Credential, nat.Gender]).count()
## Only one female clinicians has an SCW credential, therefor it is 1

## with groupby
nat.Gender.value_counts()[0] / nat.Gender.value_counts()[1]
grgencret = nat.Gender.groupby(by = [nat.Credential, nat.Gender]).count()
grgencret.loc[:,'F'] / grgencret.loc[:,'M']

## with crosstab
gencred = pd.crosstab(nat.Gender, nat.Credential)
malcred = pd.crosstab(nat.Gender, nat.Credential).loc['M']
credrat = gencred / malcred
femcredrat = credrat.loc['F']
femcredrat.max()

# States with less than 10 healthcare facilities
## How many states have fewer than 10 healthcare facilities in this dataset?
## Include Washington D.C. and and U.S.territories in this calculation.

statorg = nat.loc[:,['State','Organization legal name','Group Practice PAC ID']]

## Checking the reason behind the difference between the name and id counts
statorg[(statorg['Organization legal name'].isnull() == False) & (statorg['Group Practice PAC ID'].isnull() == True)].count()
statorg[(statorg['Organization legal name'].isnull() == True) & (statorg['Group Practice PAC ID'].isnull() == False)].count()
## There is 2609 organizations without a name but being registered with an id, therefore, we will use that id from now on.
statorg = statorg.iloc[:,[0,2]]
## There is no state with less than 10 facilities

# Standard deviation of measure averages
## All measure performance rates are on a 0 to 100 scale. Compute the average measure performance rate for each clinician (across all measures). Consider the distribution of these average rates for individuals who have at least 10. What is the standard deviation of that distribution?

## Concatenating the two performance tables
permen = pd.concat([ind, perf], join = 'inner')
permen.rename(columns = {"PAC ID" : "PACID", "Measure Identifier": "MesId", "Inverse Measure": "InvMe", "Measure Performance Rate" : "MPR"}, inplace = True)

## Finding the inverse measures and turning them into negative values
permen['MPR'] = permen['MPR'].where(permen['InvMe'] == 'N', -permen['MPR'])

## Filtering the data
sample = permen.groupby(by = 'PACID').mean()[(permen.groupby(by = 'PACID').count()['MPR'] >= 10)]
sample.describe()['MPR']['std']
## The is standard deviation is 21.59552465837087

# Performance difference between MDs and NPs
## What is the absolute difference in the average performance rates between doctors (MD) and nurse practitioners (NP)? For each clinician, use his or her average performance rates across all measures. Furthermore, only consider individuals who have at least 10 rates.
nat.rename(columns = {'PAC ID' : 'PACID'}, inplace = True)
credper = pd.merge(sample, nat[['PACID', 'Credential']], how = 'left', left_index = True, right_on = 'PACID')

credperme = credper.groupby(by= 'Credential').mean()
abs(credperme['MPR']['MD'] - credperme['MPR']['NP'])
## The absolute difference between MD and NP performance means is 7.3000968904461132

# Performance rates vs. graduation year
## What is the p-value of the linear regression of performance rates vs. graduation year? Consider the average performance rates (across all measures) of every doctor (MD) who graduated between 1973 and 2003 (inclusive). Only consider doctors who have at least 10 rates. For each graduation year, compute the mean of these rates. Assuming the relationship between graduation year and performance rates is linear, find the slope and determine if the relationship is significant. Return the p-value of the linear regression.
nat.rename(columns = {"Graduation Year": "GradYr"}, inplace = True)
mdper = pd.merge(permen, nat[['PACID', 'Credential', 'GradYr']]), on = 'PACID', how = 'left')
