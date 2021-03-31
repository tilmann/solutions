import pandas as pd
from solution import factory

solutions_list = ["trucks", "trains", "ships", "telepresence",
    "electricvehicles", "airplanes", "hybridcars"]
solutions_dict = {}
for s in solutions_list:
    solutions_dict[s] = factory.one_solution_scenarios(s)

# copied from excel
baseline_values_freight = [[111304101], [114809282], [119293206], [121312310], [125320334], [130995519], [135887669], [139263493], [143439617], [149227058], [154566203], [160166726], [166046016], [172231911], [178710364], [185530068], [192697916], [200231267], [206140575], [216463901], [225197889], [234366816], [243988062], [254040124], [
    264657000], [275739405], [287343597], [299486959], [313232199], [325460675], [339325731], [353799349], [368898825], [384653303], [401044573], [418125492], [435901525], [454389978], [473476431], [493573367], [514302927], [535814049], [558123920], [581249753], [605208827], [630018479], [655696059], [682258946], [709724529]]

baseline_freight_df = pd.DataFrame(baseline_values_freight, columns=[
                           'Average of Baseline TAMs'], index=range(2012, 2061))

# copied from excel
baseline_values_nonurban = [
    [23.944e+11], [24.731e+11], [25.633e+11], [26.368e+11], [27.348e+11], [28.227e+11], [29.121e+11], [30.029e+11], [31.242e+11], [31.891e+11], [32.844e+11], [33.814e+11], [34.800e+11], [35.904e+11], [36.821e+11], [37.858e+11], [38.912e+11], [39.984e+11], [41.071e+11], [42.183e+11], [43.311e+11], [44.458e+11], [45.626e+11], [46.661e+11], [48.021e+11], [49.250e+11], [50.500e+11], [51.772e+11], [52.996e+11], [54.382e+11], [55.722e+11], [57.084e+11], [58.470e+11], [59.970e+11], [61.314e+11], [62.772e+11], [64.255e+11], [65.762e+11], [67.293e+11], [68.854e+11], [70.439e+11], [72.050e+11], [73.687e+11], [75.350e+11], [77.040e+11], [78.757e+11], [80.501e+11], [82.273e+11], [84.073e+11]]

baseline_nonurban_df = pd.DataFrame(baseline_values_nonurban, columns=[
                           'Average of Baseline TAMs'], index=range(2012, 2061))


def freight_adoption(scenario):

    scenarios_dict = {
            # plausible
            'pds1': {
                'trucks': 'PDS1-6p2050-using ICCT/RMI',
                'ships': 'PDS1-57p2050-Avg_EEOI',
                'trains': 'PDS1-5p2050-with UIC Electrification Rate'
            },
            # drawdown
            'pds2': {
                'trucks': 'PDS2-7p2050_based on ICCT',
                'ships': 'PDS2-78p2050-1StDev_below_Mean_EEOI',
                'trains': 'PDS2-8p2050-with IEA 2DS'
            },
            # optimum
            'pds3': {
                'trucks': 'PDS3-7p2050_based on IEA (Maximum)',
                'ships': 'PDS3-97p2050-Lowest_EEOI',
                'trains': 'PDS3-9p2050-Complete Electrification'
            }
    }

    trucks = solutions_dict["trucks"][0](scenarios_dict[scenario]['trucks'])
    ships = solutions_dict["ships"][0](scenarios_dict[scenario]['ships'])
    trains = solutions_dict["trains"][0](scenarios_dict[scenario]['trains'])

    ships_vals = ships.ht.pds_adoption_data_per_region['World']
    trucks_vals = trucks.ht.pds_adoption_data_per_region['World']
    trains_vals = trains.ht.pds_adoption_data_per_region['World']

    df = pd.concat(
            [baseline_freight_df, trucks_vals, ships_vals, trains_vals], axis=1)

    df.columns = ['Average of Baseline TAMs', 'Trucks', 'Ships', 'Trains']
    df['Trucks %'] = df['Trucks'] / df['Average of Baseline TAMs']
    df['Ships %'] = df['Ships'] / df['Average of Baseline TAMs']
    df['Trains %'] = df['Trains'] / df['Average of Baseline TAMs']

    df['Remaining mtonne-kms'] = df['Average of Baseline TAMs'] - \
        df['Trucks'] - df['Ships'] - df['Trains']
    df['Remaining %'] = df['Remaining mtonne-kms'] / \
        df['Average of Baseline TAMs']

    df = df[['Average of Baseline TAMs', 'Remaining mtonne-kms', 'Remaining %',
             'Trucks', 'Trucks %', 'Ships', 'Ships %', 'Trains', 'Trains %']]
    return df


# PDS_scenarios = [scenario_PDS1, scenario_PDS2, scenario_PDS3]

# for s, i in zip(PDS_scenarios, range(1, 4)):
#     trucks = solutions_dict["trucks"][0](s[0])
#     ships = solutions_dict["ships"][0](s[1])
#     trains = solutions_dict["trains"][0](s[2])

#     ship_vals = ships.ht.pds_adoption_data_per_region['World']
#     truck_vals = trucks.ht.pds_adoption_data_per_region['World']
#     train_vals = trains.ht.pds_adoption_data_per_region['World']

#     df = pd.concat([truck_vals, ship_vals, train_vals], axis=1)
#     df.to_csv(f'PDS_{i}.csv')

# telepresence = solutions_dict["telepresence"][0]()
# electricvehicles = solutions_dict["electricvehicles"][0]()
# airplanes = solutions_dict["airplanes"][0]()
# hybridcars = solutions_dict["hybridcars"][0]()

# ship_vals = ships.ht.pds_adoption_data_per_region['World']
# truck_vals = trucks.ht.pds_adoption_data_per_region['World']
# train_vals = trains.ht.pds_adoption_data_per_region['World']
# telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
# electricvehicles_vals = electricvehicles.ht.pds_adoption_data_per_region['World']
# telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
# airplanes_vals = airplanes.ht.pds_adoption_data_per_region['World']
# hybridcars_vals = hybridcars.ht.pds_adoption_data_per_region['World']


# Intercity Rail Share: 10.51%
# Intercity Bus Share: 28.15%
# Total Aviation Share: 21.38%
# modeshare = [10.51, 28.15, 21.38]
def nonurban_pass_adoption(scenario="pds1", include_telepresence=True, include_trains=True, include_electricvehicles=True, include_hybridcars=True, modeshare=[0.1051, 0.2815, 0.2138]):

    scenarios_dict = {
            # plausible
            'pds1': {
                'telepresence': 'PDS1-20p2050-Bass Curve Fit',
                'trains': 'PDS1-5p2050-with UIC Electrification Rate',
                'airplanes': 'PDS1-80p2050-13.2%Efficiency',
                'electricvehicles': 'PDS1-16p2050-using IEA 2DS (Pre-Integration)',
                'hybridcars': 'PDS1-11p2050-using IEA 2DS (Pre-Integration)',
            },
            # drawdown
            'pds2': {
                'telepresence': 'PDS2-28p2050-Bass Curve Fit',
                # TODO trains key "PDS2-5p2050-based on on IEA 2DS (Book Ed.1)" did NOT work
                'trains': 'PDS2-8p2050-with IEA 2DS',
                'airplanes': 'PDS2-85p2050-18%Efficiency',
                'electricvehicles': 'PDS2-23p2050-using IEA B2DS (Pre-Integration)',
                'hybridcars': 'PDS2-4p2050-Transition to EVs (Pre-Integration)',
            },
            # optimum
            'pds3': {
                'telepresence': 'PDS3-46p2050-Bass Curve Fit',
                'trains': 'PDS3-9p2050-Complete Electrification',
                'airplanes': 'PDS3-100p2050-20%Efficiency',
                # TODO electricvehicles: Key 'PDS3-18p2050-Car Survival Analysis (Pre-Integration)' did NOT work
                'electricvehicles': 'PDS3-18p2050-Car Survival Analysis',
                # TODO hybridcars: Key 'PPDS3-1p2050-Transition to EVs (Pre-Integration)' did NOT work
                'hybridcars': 'PDS3-0p2050-Transition to EV\'s',
            }
    }

    telepresence = solutions_dict["telepresence"][0](
        scenarios_dict[scenario]['telepresence'])
    trains = solutions_dict["trains"][0](scenarios_dict[scenario]['trains'])
    airplanes = solutions_dict["airplanes"][0](
        scenarios_dict[scenario]['airplanes'])
    electricvehicles = solutions_dict["electricvehicles"][0](
        scenarios_dict[scenario]['electricvehicles'])
    hybridcars = solutions_dict["hybridcars"][0](
        scenarios_dict[scenario]['hybridcars'])

    telepresence_vals = telepresence.ht.pds_adoption_data_per_region['World']
    trains_vals = trains.ht.pds_adoption_data_per_region['World']
    # TODO Figure out why the solutions output need a factor
    trains_vals = trains_vals * 100000
    airplanes_vals = airplanes.ht.pds_adoption_data_per_region['World']
    # TODO see above
    airplanes_vals = airplanes_vals * 1000000000
    electricvehicles_vals = electricvehicles.ht.pds_adoption_data_per_region['World']
    # TODO see above
    electricvehicles_vals = electricvehicles_vals * 100000000
    hybridcars_vals = hybridcars.ht.pds_adoption_data_per_region['World']

    df = pd.concat([baseline_nonurban_df, telepresence_vals, trains_vals, airplanes_vals,
                   electricvehicles_vals, hybridcars_vals], axis=1)
    df.columns = ['Average of Baseline TAMs', 'Telepresence', 'High Speed Rail',
        'Efficient Airplanes', 'Electric Vehicles', 'Car Fuel Efficiency']
    df['Telepresence %'] = df['Telepresence'] / df['Average of Baseline TAMs']
    df['High Speed Rail %'] = df['High Speed Rail'] / \
        df['Average of Baseline TAMs']
    df['Efficient Airplanes %'] = df['Efficient Airplanes'] / \
        df['Average of Baseline TAMs']
    df['Electric Vehicles %'] = df['Electric Vehicles'] / \
        df['Average of Baseline TAMs']
    df['Car Fuel Efficiency %'] = df['Car Fuel Efficiency'] / \
        df['Average of Baseline TAMs']

    if not include_telepresence:
        df['Telepresence'] = 0

    if not include_trains:
        df['High Speed Rail'] = 0

    if not include_electricvehicles:
        df['Electric Vehicles'] = 0

    if not include_hybridcars:
        df['Car Fuel Efficiency'] = 0

    # TODO the MAX in C8 (=B8-SUM($AA$3:$AA$4;MAX($AA$5;$N8))*B8-...)) is missing
    df['Remaining mtonne-kms'] = df['Average of Baseline TAMs'] - \
        df['Telepresence'] - df['High Speed Rail'] - \
        df['Electric Vehicles'] - df['Car Fuel Efficiency'] - \
        (df['Average of Baseline TAMs'] * (modeshare[0] +
         modeshare[1] + df['Efficient Airplanes %']))

    df['Remaining %'] = df['Remaining mtonne-kms'] / \
        df['Average of Baseline TAMs']

    df = df[['Average of Baseline TAMs', 'Remaining mtonne-kms', 'Remaining %', 'Telepresence', 'Telepresence %', 'High Speed Rail', 'High Speed Rail %',
      'Efficient Airplanes', 'Efficient Airplanes %', 'Electric Vehicles', 'Electric Vehicles %', 'Car Fuel Efficiency', 'Car Fuel Efficiency %']]

    #print(df.iloc[0:5, 0:3])

    return df
