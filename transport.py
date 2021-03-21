import pandas as pd

import solution.factory

solutions = solution.factory.all_solutions_scenarios()

trucks = solutions["trucks"][0]()
trains = solutions["trains"][0]()
ships = solutions["ships"][0]()
telepresence = solutions["telepresence"][0]()
electricvehicles = solutions["electricvehicles"][0]()
airplanes = solutions["airplanes"][0]()
hybridcars = solutions["hybridcars"][0]()

baseline_values = [[111304101],   
[114809282],   
[119293206],   
[121312310],   
[125320334],   
[130995519],   
[135887669],   
[139263493],   
[143439617],   
[149227058],   
[154566203],   
[160166726],   
[166046016],   
[172231911],   
[178710364],   
[185530068],   
[192697916],   
[200231267],   
[206140575],   
[216463901],   
[225197889],   
[234366816],   
[243988062],   
[254040124],   
[264657000],   
[275739405],   
[287343597],   
[299486959],   
[313232199],   
[325460675],   
[339325731],   
[353799349],   
[368898825],   
[384653303],   
[401044573],   
[418125492],   
[435901525],   
[454389978],   
[473476431],   
[493573367],   
[514302927],   
[535814049],   
[558123920],   
[581249753],   
[605208827],   
[630018479],   
[655696059],   
[682258946],   
[709724529]]

baseline_df = pd.DataFrame(baseline_values, columns=['Average of Baseline TAMs'], index=range(2012, 2061))

ship_vals = ships.ht.pds_adoption_data_per_region['World']
truck_vals = trucks.ht.pds_adoption_data_per_region['World']
train_vals = trains.ht.pds_adoption_data_per_region['World']
telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
electricvehicles_vals = electricvehicles.ht.pds_adoption_data_per_region['World']
telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
airplanes_vals = airplanes.ht.pds_adoption_data_per_region['World']
fuel_efficiency_vals = hybridcars.ht.pds_adoption_data_per_region['World']

def freight_adoption(baseline, truck, ship, train):
    
    df = pd.concat([baseline, ship, truck, train], axis=1)
    df.columns = ['Average of Baseline TAMs', 'Trucks', 'Ships', 'Trains']
    df['Trucks %'] = df['Trucks']/df['Average of Baseline TAMs']
    df['Ships %'] = df['Ships']/df['Average of Baseline TAMs']
    df['Trains %'] = df['Trains']/df['Average of Baseline TAMs']

    df['Remaining mtonne-kms'] = df['Average of Baseline TAMs'] - df['Trucks'] - df['Ships'] - df['Trains']
    df['Remaining %'] = df['Remaining mtonne-kms']/df['Average of Baseline TAMs']

    df = df[['Average of Baseline TAMs', 'Remaining mtonne-kms', 'Remaining %', 'Trucks', 'Trucks %', 'Ships', 'Ships %', 'Trains', 'Trains %']]
    return df

# Input Data needs to be confirmed by Ryan
freight_results = freight_adoption(baseline_df, ship_vals, truck_vals, train_vals)
    
print(freight_results.tail())



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

nonurban_pass_adoption_results = nonurban_pass_adoption(baseline_df, telepresence_vals, train_vals, airplanes_vals, electricvehicles_vals, fuel_efficiency_vals)
    
print(nonurban_pass_adoption_results.tail())






