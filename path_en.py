# Define the file options and their year-to-fieldname mappings for various prosperity indicators
indicator_options = {
    'Average debt per household': {
        'path': 'AverageDebt.geojson',  # Path to the GeoJSON file for this indicator
        'year_columns': {  # Mapping of years to column names in the data
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Average debt per household',  # Title of the indicator
    },
    'Built up area': {
        'path': 'BuiltUpArea.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Built up area',
    },
    'Contact with family, friends or neighbors': {
        'path': 'ContactWithFamilyEtc.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        'title': 'Contact with family, friends or neighbors',
    },
    'Distance to café etc.': {
        'path': 'DistanceToCafe.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        'title': 'Distance to café etc.',
    },
    'Distance to primary school': {
        'path': 'DistanceToPrimarySchool.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Distance to primary school',
    },
    'Distance to public green areas': {
        'path': 'DistanceToPublicGreenAreas.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Distance to public green areas',
    },
    'Distance to public transportation': {
        'path': 'DistanceToPublicTransportation.geojson',
        'year_columns': {
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Distance to public transportation',
    },
    'Distance to sports field': {
        'path': 'DistanceToSportsField.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Distance to sports field',
    },
    'Emissions of particulate matter to air': {
        'path': 'EmissionsParticulateMatter.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        'title': 'Emissions of particulate matter to air',
    },
    'Experienced health': {
        'path': 'ExperiencedHealth.geojson',
        'year_columns': {
            '2016': 'Year2016',
            '2020': 'Year2020',
            '2022': 'Year2022',
        },
        'title': 'Experienced health',
    },
    'Greenhouse gas emissions per capita': {
        'path': 'GreenhouseEmissions.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        'title': 'Greenhouse gas emissions per capita - No Spillover',
    },
    'Life expectancy of the population': {
        'path': 'LifeExpectancyOfThePopulation.geojson',
        'year_columns': {
            '2022': 'Year2022',
        },
        'title': 'Life expectancy of the population',
    },
    'Median disposable income': {
        'path': 'MedianDisposableIncome.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Median disposable income',
    },
    'Median household wealth': {
        'path': 'MedianHouseholdWealth.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Median household wealth',
    },
    'Nature area per inhabitant': {
        'path': 'NatureAreaPerInhabitant.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Nature area per inhabitant',
    },
    'Nature and forest areas': {
        'path': 'NatureForestAreas.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Nature and forest areas',
    },
    'Net labor participation': {
        'path': 'NetLaborParticipation.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Net labor participation',
    },
    'Number of crimes encountered': {
        'path': 'NumberCrimes.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        'title': 'Number of crimes encountered',
    },
    'Often feeling unsafe in the neighborhood': {
        'path': 'OftenFeelingUnsafe.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        'title': 'Often feeling unsafe in the neighborhood',
    },
    'Overweight': {
        'path': 'Overweight.geojson',
        'year_columns': {
            '2016': 'Year2016',
            '2020': 'Year2020',
            '2022': 'Year2022',
        },
        'title': 'Overweight',
    },
    'Population with a starting qualification': {
        'path': 'PopulationWithStartingQualification.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Population with a starting qualification',
    },
    'Private solar energy': {
        'path': 'SolarEnergy.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        'title': 'Private solar energy',
    },
    'Quality of bathing water coastal waters': {
        'path': 'QualityOfBathingWaterCoastalWaters.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Quality of bathing water coastal waters',
    },
    'Quality of inland bathing water': {
        'path': 'QualityOfInlandBathingWater.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Quality of inland bathing water',
    },
    'Recorded crimes': {
        'path': 'RecordedCrimes.geojson',    
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Recorded crimes',
    },
    'Registered problematic debt': {
        'path': 'RegisteredProblematicDebt.geojson',
        'year_columns': {
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Registered problematic debt',
    },
    'Satisfaction with free time': {
        'path': 'SatisfactionFreeTime.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Satisfaction with free time',
    },
    'Satisfaction with housing': {
        'path': 'SatisfactionHousing.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2018': 'Year2018',
            '2021': 'Year2021',
        },
        'title': 'Satisfaction with housing',
    },
    'Satisfaction with life': {
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'path': 'SatisfactionLife.geojson',
        'title': 'Satisfaction with life',
    },
    'Satisfaction with living environment': {
        'path': 'SatisfactionLivingEnvironment.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2018': 'Year2018',
            '2021': 'Year2021',
        },
        'title': 'Satisfaction with living environment',
    },
    'Satisfaction with social life': {
        'path': 'SatisfactionWithSocialLife.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Satisfaction with social life',
   },
    'Social cohesion': {
        'path': 'SocialCohesion.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        'title': 'Social cohesion',
    },
    'Trust in institutions': {
        'path': 'TrustInstitutions.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Trust in institutions',
    },
    'Trust in others': {
        'path': 'TrustOthers.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Trust in others',
    },
    'Unemployment': {
        'path': 'Unemployment.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Unemployment',
    },
    'Volunteer work': {
        'path': 'VolunteerWork.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Volunteer work',
    }
}

# Define the file options for themes of prosperity indicators and their year-to-fieldname mappings
theme_options = {
    'Air quality': {
        'path': 'Theme_Air_Quality.geojson',  # Path to the GeoJSON file for this theme
        'year_columns': {  # Mapping of years to column names in the data
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
        },
        'title': 'Air quality',  # Title of the theme
    },
    'Distance to living facilities': {
        'path': 'Theme_Distance_to_Living_Facilities.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Distance to living facilities',
    },
    'Environment': {
        'path': 'Theme_Environment.geojson',
        'year_columns': {
            '2015': 'Year2015',
        },
        'title': 'Environment',
    },
    'Health': {
        'path': 'Theme_Health.geojson',
        'year_columns': {
            '2016': 'Year2016',
            '2020': 'Year2020',
            '2022': 'Year2022',
        },
        'title': 'Health',
    },
    'Labor and free time': {
        'path': 'Theme_Labor_and_Free_Time.geojson',
        'year_columns': {
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Labor and free time',
    },
    'Material welfare and economic capital': {
        'path': 'Theme_Material_Welfare_and_Economic_Capital.geojson',
        'year_columns': {
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Material welfare and economic capital',
    },
    'Natural capital': {
        'path': 'Theme_Natural_Capital.geojson',
        'year_columns': {
            '2015': 'Year2015',
        },
        'title': 'Natural capital',
    },
    'Nature': {
        'path': 'Theme_Nature.geojson',
        'year_columns': {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        'title': 'Nature',
    },
    'Society': {
        'path': 'Theme_Society.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Society',
    },
    'Well-being': {
        'path': 'Theme_Wellbeing.geojson',
        'year_columns': {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        'title': 'Well-being',
    }
}

# Define color schemes for different quantile ranges in prosperity data visualization
color_schemes = {
    # Blues color scheme for representing quantile ranges
    "Blues": [
        [255, 255, 255],  # White for missing values (no data)
        [228, 239, 209],  # Lightest blue for 0-25% quantile range (low values)
        [152, 197, 194],  # Medium light blue for 25-50% quantile range (mid-low values)
        [73, 127, 153],   # Darker blue for 50-75% quantile range (mid-high values)
        [44, 86, 124]     # Deep blue for 75-100% quantile range (high values)
    ],
    
    # Reds color scheme for representing quantile ranges
    "Reds": [
        [255, 255, 255],  # White for missing values (no data)
        [255, 194, 179],  # Lightest red for 0-25% quantile range (low values)
        [255, 112, 77],   # Medium red for 25-50% quantile range (mid-low values)
        [230, 46, 0],     # Strong red for 50-75% quantile range (mid-high values)
        [153, 31, 0]      # Dark red for 75-100% quantile range (high values)
    ],
    
    # Purples color scheme for representing quantile ranges
    "Purples": [
        [255, 255, 255],  # White for missing values (no data)
        [255, 204, 255],  # Light purple for 0-25% quantile range (low values)
        [255, 128, 255],  # Medium purple for 25-50% quantile range (mid-low values)
        [255, 51, 255],   # Vivid purple for 50-75% quantile range (mid-high values)
        [204, 0, 204]     # Deep purple for 75-100% quantile range (high values)
    ],
    
    # Greens color scheme for representing quantile ranges
    "Greens": [
        [255, 255, 255],  # White for missing values (no data)
        [204, 255, 204],  # Lightest green for 0-25% quantile range (low values)
        [128, 255, 128],  # Medium green for 25-50% quantile range (mid-low values)
        [51, 255, 51],    # Bright green for 50-75% quantile range (mid-high values)
        [0, 153, 0]       # Dark green for 75-100% quantile range (high values)
    ]
}

        
