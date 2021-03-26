import sys

import pandas as pd

sys.path.append('../..')
import solution.factory

# initial: scenario_PDS1 = ['PDS1-7p2050-Using ICCT/RMI', 'PDS1-58p2050-Avg EEOI', 'PDS1-5p2050-with UIC Electrification Rate']  
scenario_PDS1 = ['PDS1-6p2050-using ICCT/RMI', 'PDS1-57p2050-Avg_EEOI', 'PDS1-5p2050-with UIC Electrification Rate']  

# initial: scenario_PDS2 = ['PDS2-8p2050-Using ICCT Regional Data', 'PDS2-78p2050-1 St Dev bel. Mean EEOI', 'PDS2-8p2050-with IEA 2DS']  
scenario_PDS2 = ['PDS2-7p2050_based on ICCT', 'PDS2-78p2050-1StDev_below_Mean_EEOI', 'PDS2-8p2050-with IEA 2DS']  

# initial: scenario_PDS3 = ['PDS3-8p2050-Using IEA (Maximum)', 'PDS3-98p2050-Lowest EEOi', 'PDS3-11p2050-Complete Electrification']  
scenario_PDS3 = ['PDS3-7p2050_based on IEA (Maximum)', 'PDS3-97p2050-Lowest_EEOI', 'PDS3-9p2050-Complete Electrification']  



solutions_list = ["trucks", "trains", "ships"] #, "telepresence", "electricvehicles", "airplanes", "hybridcars"]
solutions_dict = {}
for s in solutions_list:
  solutions_dict[s] = solution.factory.one_solution_scenarios(s)

PDS_scenarios = [scenario_PDS1, scenario_PDS2, scenario_PDS3]

for s, i in zip(PDS_scenarios, range(1, 4)):
  trucks = solutions_dict["trucks"][0](s[0])
  ships = solutions_dict["ships"][0](s[1])
  trains = solutions_dict["trains"][0](s[2])

  ship_vals = ships.ht.pds_adoption_data_per_region['World']
  truck_vals = trucks.ht.pds_adoption_data_per_region['World']
  train_vals = trains.ht.pds_adoption_data_per_region['World']

  df = pd.concat([truck_vals, ship_vals, train_vals], axis=1)
  df.to_csv(f'PDS_{i}.csv')

  # print(truck_vals)
  # print(ship_vals)
  # print(train_vals)

# telepresence = solutions_dict["telepresence"][0]()
# electricvehicles = solutions_dict["electricvehicles"][0]()
# airplanes = solutions_dict["airplanes"][0]()
# hybridcars = solutions_dict["hybridcars"][0]()

# print(solutions_dict["trucks"])
# print(solutions_dict["trains"])
# print(solutions_dict["ships"])

baseline_values = [[111304101], [114809282], [119293206], [121312310], [125320334], [130995519], [135887669], [139263493], [143439617], [149227058], [154566203], [160166726], [166046016], [172231911], [178710364], [185530068], [192697916], [200231267], [206140575], [216463901], [225197889], [234366816], [243988062], [254040124], [264657000], [275739405], [287343597], [299486959], [313232199], [325460675], [339325731], [353799349], [368898825], [384653303], [401044573], [418125492], [435901525], [454389978], [473476431], [493573367], [514302927], [535814049], [558123920], [581249753], [605208827], [630018479], [655696059], [682258946], [709724529]]

baseline_df = pd.DataFrame(baseline_values, columns=['Average of Baseline TAMs'], index=range(2012, 2061))

ship_vals = ships.ht.pds_adoption_data_per_region['World']
truck_vals = trucks.ht.pds_adoption_data_per_region['World']
train_vals = trains.ht.pds_adoption_data_per_region['World']
# telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
# electricvehicles_vals = electricvehicles.ht.pds_adoption_data_per_region['World']
# telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
# airplanes_vals = airplanes.ht.pds_adoption_data_per_region['World']
# fuel_efficiency_vals = hybridcars.ht.pds_adoption_data_per_region['World']

def freight_adoption(scenarios):

  trucks = solutions_dict["trucks"][0](scenarios[0])
  ships = solutions_dict["ships"][0](scenarios[1])
  trains = solutions_dict["trains"][0](scenarios[2])

  ship_vals = ships.ht.pds_adoption_data_per_region['World']
  truck_vals = trucks.ht.pds_adoption_data_per_region['World']
  train_vals = trains.ht.pds_adoption_data_per_region['World']

  df = pd.concat([baseline_df, truck_vals, ship_vals, train_vals], axis=1)

  df.columns = ['Average of Baseline TAMs', 'Trucks', 'Ships', 'Trains']
  df['Trucks %'] = df['Trucks']/df['Average of Baseline TAMs']
  df['Ships %'] = df['Ships']/df['Average of Baseline TAMs']
  df['Trains %'] = df['Trains']/df['Average of Baseline TAMs']

  df['Remaining mtonne-kms'] = df['Average of Baseline TAMs'] - df['Trucks'] - df['Ships'] - df['Trains']
  df['Remaining %'] = df['Remaining mtonne-kms']/df['Average of Baseline TAMs']

  df = df[['Average of Baseline TAMs', 'Remaining mtonne-kms', 'Remaining %', 'Trucks', 'Trucks %', 'Ships', 'Ships %', 'Trains', 'Trains %']]
  return df

# Input Data needs to be confirmed by Ryan
# freight_results = freight_adoption(baseline_df, ship_vals, truck_vals, train_vals)
  
# print(freight_results.tail())



def nonurban_pass_adoption(baseline, telepresence, trains, aviation, electricvehicles, fuel_efficiency):
  
  df = pd.concat([baseline, telepresence, trains, aviation, electricvehicles, fuel_efficiency], axis=1)
  df.columns = ['Average of Baseline TAMs', 'Telepresence', 'High Speed Rail', 'Efficient Aviation', 'Electric Vehicles', 'Car Fuel Efficiency']
  df['Telepresence %'] = df['Telepresence']/df['Average of Baseline TAMs']
  df['High Speed Rail %'] = df['High Speed Rail']/df['Average of Baseline TAMs']
  df['Efficient Aviation %'] = df['Efficient Aviation']/df['Average of Baseline TAMs']
  df['Electric Vehicles %'] = df['Electric Vehicles']/df['Average of Baseline TAMs']
  df['Car Fuel Efficiency %'] = df['Car Fuel Efficiency']/df['Average of Baseline TAMs']

  df['Remaining mtonne-kms'] = df['Average of Baseline TAMs'] - df['Telepresence'] - df['High Speed Rail'] - df['Efficient Aviation'] - df['Electric Vehicles'] - df['Car Fuel Efficiency']
  df['Remaining %'] = df['Remaining mtonne-kms']/df['Average of Baseline TAMs']

  df = df[['Average of Baseline TAMs', 'Remaining mtonne-kms', 'Remaining %', 'Telepresence', 'Telepresence %', 'High Speed Rail', 'High Speed Rail %', 
    'Efficient Aviation', 'Efficient Aviation %', 'Electric Vehicles', 'Electric Vehicles %', 'Car Fuel Efficiency', 'Car Fuel Efficiency %']]
  return df

# nonurban_pass_adoption_results = nonurban_pass_adoption(baseline_df, telepresence_vals, train_vals, airplanes_vals, electricvehicles_vals, fuel_efficiency_vals)
  
# print(nonurban_pass_adoption_results.tail())






