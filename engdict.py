# Define the themes and their corresponding markdown content

Themes = {
    "Average debt per household": """
        **Welcome to the Average Household Debt indicator**
        - This indicator is part of the Material Welfare and Economic Capital theme. This 
        indicator tracks the average household debt, considering spillover effects from 
        neighboring municipalities. Using ArcGIS Pro, neighboring municipalities are identified,
        and their total household debt and number of households are combined to calculate a 
        collective score. The final value is then recalculated back to average debt per 
        household, considering the spillover effect from neighboring areas.
        - 2022 figures are preliminary, and the adjustment for price changes 
        in 2021 and 2022 is based on the consumer price research series, which 
        uses actual energy prices paid. This aligns more closely with the price 
        developments experienced by the population than the consumer price index.
        - Measuring unit: Euro average debt per household
    """,
    "Built up area": """
        **Welcome to the Built-up Area indicator**
        - This indicator is part of the Natural Capital theme. This indicator measures the 
        percentage of surface area that is built-up within municipalities. First order 
        contiguity is used, assuming that built-up areas spill over across shared borders. 
        Using ArcGIS Pro, neighboring municipalities are identified, and the data is combined 
        to account for spillovers. The final score is recalculated back into a percentage 
        for each municipality.
        - Measuring unit: Percentage of land area that is built-up.
    """,
    "Contact with family, friends or neighbors": """
        **Welcome to the Contact with Family, Friends, or Neighbors indicator**
        - This indicator is part of the Society theme, focusing on social relationships and 
        support. It measures the percentage of individuals aged 15 and older who have regular
        contact (at least once a week) with family, friends, or neighbors.
        Municipal spillover effects are considered based on shared borders between 
        municipalities. Using spatial analysis in ArcGIS Pro, values are adjusted by combining
        data from neighboring municipalities. The final score reflects the broader social 
        network dynamics, with the value recalculated back to the percentage of individuals 
        with regular contact.
        - Measuring unit: Percentage of population aged 15+ has contact at least once a week on average
    """,
    "Distance to café etc.": """
        **Welcome to the Distance to Café, etc. indicator**
        - This indicator is part of the Distance and Living Facilities theme. It measures the average distance residents 
        travel to access cafés and similar establishments, assuming a 4.184 km travel distance. Using 
        municipal data and spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring 
        municipalities. If spillover effects suggest a greater distance than the original municipal value, 
        the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to primary school": """
        **Welcome to the Distance to Primary School indicator**
        - This indicator is part of the Distance to Living Facilities theme. It measures the average distance 
        residents travel to access a primary school, assuming a 4.023 km travel distance. Using municipal data 
        and spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring municipalities. 
        If spillover effects suggest a greater distance than the original municipal value, the original value 
        is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to public green areas": """
        **Welcome to the Distance to Public Green Areas indicator**
        - This indicator is part of the Environment theme, in the Nature sub-theme. It measures the average 
        distance residents travel to access public green spaces, assuming a 1.65 km travel distance. 
        Using municipal data and spatial analysis in ArcGIS Pro, distances are adjusted to account for 
        neighboring municipalities. If spillover effects suggest a greater distance than the original 
        municipal value, the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to public transportation": """
        **Welcome to the Distance to Public Transport indicator**
        - This indicator is part of the Labor and Free Time theme.
        -It measures the average distance residents travel to access public transportation, 
        considering a 791-meter assumed travel distance. Using municipal data and
        spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring
        municipalities. If spillover effects suggest a greater distance than the original
        municipal value, the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to sports field": """
        **Welcome to the Distance to Sports Field indicator**
        - This indicator is part of the Labor and Free Time theme.
        - It measures the average distance residents travel to access sports fields, 
        assuming a 1 km travel distance. Using municipal data and spatial analysis in ArcGIS Pro, 
        distances are adjusted to account for neighboring municipalities. 
        If spillover effects suggest a greater distance than the original municipal value, 
        the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Emissions of particulate matter to air": """
        **Welcome to the Emissions of Particulate Matter to Air indicator**
        - This indicator is part of the Environment theme, in the Air Quality and Natural Capital sub-themes. 
        It measures the emissions of particulate matter (PM₂.₅) to air, assuming a 500-meter spillover distance
        to reflect regional dispersion. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest
        a greater emission value than the original municipal value, the original value is retained.
        - Measuring unit: kg PM₂.₅ per km²
    """,
    "Experienced health": """
        **Welcome to the Experienced Health indicator**
        - This indicator is part of the Health theme. It measures the percentage of individuals
        who rate their health as (very) good, assuming spillover effects occur between 
        neighboring municipalities based on shared borders. Using municipal data and spatial 
        analysis in ArcGIS Pro, values are adjusted to account for neighboring municipalities.
        If spillover effects suggest a greater percentage than the original municipal value, 
        the original value is retained.
        - Measuring unit: Percentage of the population aged 18+ consider their own health to be (very) good
    """,
    "Greenhouse gas emissions per capita": """
        **Welcome to the Greenhouse Gas Emissions per Inhabitant indicator**
        - This indicator is part of the Environment theme and Air-Quality sub-theme. This indicator 
        tracks the greenhouse gas emissions per capita for each municipality, adjusted for 
        neighboring municipalities' emissions based on shared borders. Using ArcGIS Pro, the 
        neighborhood summary statistics tool is applied, combining data from neighboring municipalities
        to calculate an average. The value is then recalculated per capita by dividing the total
        emissions by the population size of the municipality.
        - The entire series has been adjusted due to new IPCC guidelines.
        - Measuring unit: Kilograms of CO2 equivalent per inahbitant
    """,
    "Life expectancy of the population": """
        **Welcome to the Life Expectancy of the Population indicator**
        - This indicator is part of the Health theme. It measures the life expectancy of the population, 
        assuming spillover effects occur between neighboring municipalities based on shared borders.
        Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to account for 
        neighboring municipalities. If spillover effects suggest a greater value than the original municipal 
        value, the original value is retained.
        - Measuring unit: The life expentancy in years at birth
    """,
    "Median disposable income": """
        **Welcome to the Median Disposable Income indicator**
        - This indicator is part of the Material Welfare and Economics Capital theme. 
        This indicator tracks the median disposable income per household, with spillover 
        effects considered for neighboring municipalities. Using ArcGIS Pro, neighboring 
        municipalities are identified, and their total disposable income and number of
        households are combined to calculate a collective score. The final value is then 
        recalculated back to median disposable income, considering the spillover from 
        neighboring areas.
        - 2021 figures are preliminary, and the adjustment for price changes in 
        2021 is based on the consumer price research series, which uses actual 
        energy prices paid. This aligns more closely with the price developments 
        experienced by the population than the consumer price index.
        - Measuring unit: Euro per household corrected for inflation, in constant 2021 prices
    """,
    "Median household wealth": """
        **Welcome to the Median Household Wealth indicator**
        - This indicator is part of the Material Welfare and Economic Capital theme. This indicator 
        measures median household wealth, incorporating spillover effects from neighboring municipalities.
        Using ArcGIS Pro, neighboring municipalities are identified, and their total household wealth 
        and number of households are combined to calculate a collective score. The final value is 
        recalculated back to median household wealth, considering the spillover effect from neighboring areas.
        - 2021 figures are preliminary, and the adjustment for price changes 
        in 2021 is based on the consumer price research series, which uses 
        actual energy prices paid. This aligns more closely with the price 
        developments experienced by the population than the consumer price index.
        - Measuring unit: Euro
    """,
    "Nature and forest areas": """
        **Welcome to the Nature and Forest Areas indicator**
        - This indicator is part of the Environment theme, in the Nature and Natural Capital sub-themes.
        It measures the percentage of municipal surface area covered by nature and forests, assuming a 1.65 km
        spillover distance. Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to
        account for neighboring municipalities. If spillover effects suggest a greater percentage than
        the original municipal value, the original value is retained.
        - Measuring unit: Percentage of surface area
    """,
    "Nature area per inhabitant": """
        **Welcome to the Nature Area per Inhabitant indicator**
        - This indicator is part of the Environment theme, in the Nature sub-theme. It measures the amount 
        of nature area per 1,000 inhabitants, assuming a 1.65 km spillover distance to reflect regional 
        accessibility. Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to account
        for neighboring municipalities. If spillover effects suggest a greater value than the original 
        municipal value, the original value is retained.
        - Measuring unit: Square meters per 1000 inhabitants
    """,
    "Net labor participation" : """
        **Welcome to the Net Labor Participation indicator**
        - This indicator is part of Labor and Free Time theme. It measures the percentage of individuals participating in the labor force,
        assuming a 25 km spillover distance to reflect regional influence. Due to data limitations,
        calculations use the working population aged 15 to 64. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest a greater percentage 
        than the original municipal value, the original value is retained.
        - Measuring unit: Percentage of the working population
    """,
    "Number of crimes encountered": """
        **Welcome to the Number of Crimes Encountered indicator**
        - This indicator measures the number of crimes encountered per 100 inhabitants, 
        with spillover effects considered for neighboring municipalities. Using ArcGIS Pro, 
        the neighborhood summary statistics tool calculates the mean of crimes encountered 
        across neighboring municipalities, adjusting for shared borders. The final value is 
        then recalculated per 100 inhabitants, considering the population size.
        - Measuring unit: Number of crimes experienced per 100 inhabitants
    """,
    "Overweight": """
        **Welcome to the Overweight indicator**
        - This indicator is part of the Health theme. It measures the percentage of overweight 
        individuals, assuming spillover effects occur between neighboring municipalities based 
        on shared borders. Using municipal data and spatial analysis in ArcGIS Pro, values are 
        adjusted to account for neighboring municipalities. If spillover effects suggest 
        a greater percentage than the original municipal value, the original value is retained.
        - Measuring unit: Percentage of the population aged 18+ is overweight
    """,
    "Population with a starting qualification": """
        **Welcome to the Population with a Starting Qualification indicator**
        - This indicator is part of the Labor and Free Time theme. It measures the percentage of individuals 
        aged 15 to 74 with a starting qualification, using a 25 km spillover distance to reflect regional 
        influence. Due to data limitations, calculations are based on the working population (aged 15 to 64). 
        Spatial analysis in ArcGIS Pro accounts for municipal spillovers and adjusts the values accordingly.
        - Measuring unit: Percentage of the population with a starting qualification
    """,
    "Private solar energy": """
        **Welcome to the Private Solar Energy indicator**
        - This indicator is part of the Natural Capital sub-theme. 
        It measures private solar energy production per household, assuming a 1 km spillover distance to
        reflect regional influence. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest
        a greater value than the original municipal value, the original value is retained.
        - Measuring unit: Watts per home
    """,
    "Recorded crimes": """
        **Welcome to the Recorded Crimes indicator**
        - This indicator tracks the recorded crimes per 1,000 inhabitants, adjusted for 
        neighboring municipalities based on shared borders. Using ArcGIS Pro, the neighborhood
        summary statistics tool calculates the average of recorded crimes across neighboring 
        municipalities. The final value is then recalculated per 1,000 inhabitants by adjusting
        for the population size.
        - 2021 and 2022 figures are preliminary.
        - Measuring unit: Registered crimes per 1000 inhabitants
    """,
    "Registered problematic debt": """
        **Welcome to the Registered Problematic Debt indicator**
        - This indicator is part of the Material Welfare and Economic Capital theme. First order
        contiguity is applied, assuming debt issues spill over across shared municipal borders.
        Using ArcGIS Pro, neighboring municipalities are identified and their data combined. 
        The final score is recalculated back into a percentage for each municipality, 
        factoring in the spillover effect.
        - Measuring unit: Percentage of registered problematic debts
    """,
    "Satisfaction with free time": """
        **Welcome to the Satisfaction with free time indicator**
        - This indicator is part of the Well-being sub-theme. It measures satisfaction with free 
        time, assuming spillover effects occur between neighboring municipalities based on shared
        borders. Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to 
        account for neighboring municipalities. If spillover effects suggest a greater percentage
        than the original municipal value, the original value is retained.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of the population aged 18+ is (very) satisfied
    """,
    "Satisfaction with housing": """
        **Welcome to the Satisfaction with Housing indicator**
        - This indicator is part of the Distance to Living Facilities theme. Due to the lack of
        specific spillover literature, first order contiguity is applied, assuming satisfaction
        with housing spills over across shared municipal borders. ArcGIS Pro is used to identify
        neighboring municipalities, and their satisfaction data is combined. The final score is
        recalculated back into a percentage for each municipality, considering the spillover effects.
        - Measuring unit: Percentage of private households are (very) satisfied
    """,
    "Satisfaction with life": """
        **Welcome to the Life Satisfaction indicator**
        - This indicator is part of the Well-being theme. It measures satisfaction with life, assuming 
        spillover effects occur between neighboring municipalities based on shared borders. Using municipal 
        data and spatial analysis in ArcGIS Pro, values are adjusted to account for neighboring municipalities. If spillover effects suggest a greater percentage than the original municipal value, the original value is retained.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of Dutch people give life a 7 or higher
    """,
    "Satisfaction with living environment": """
        **Welcome to the Satisfaction with Living Environment indicator**
        - This indicator is part of the Distance to Living Facilities theme. Since no specific 
        spatial spillover literature is available, first order contiguity is used, 
        assuming that satisfaction with the living environment spills over across shared 
        municipal borders. Using ArcGIS Pro, neighboring municipalities are identified,
        and their household satisfaction data is combined. The final score is recalculated 
        back into a percentage for each municipality, considering the spillover effects.
        - Measuring unit: Percentage of private households are (very) satisfied
    """,
    "Satisfaction with social life": """
        **Welcome to the Satisfaction with Social Life indicator**
        - This indicator is part of the Society theme. Due to the lack of specific spatial 
        spillover literature, first order contiguity is applied, assuming that satisfaction 
        with social life spills over across shared municipal borders. Using ArcGIS Pro, 
        neighboring municipalities are identified, and their populations reporting satisfaction
        are combined. The final score is recalculated back into a percentage for each municipality, 
        accounting for spillover effects from neighboring areas.
        - Measuring unit: Percentage of the population(15+) satisfied with their social life
    """,
    "Social cohesion": """
        **Welcome to the Social Cohesion indicator**
        - This indicator measures social cohesion, assuming spillover effects occur between neighboring 
        municipalities based on shared borders. Using municipal data and spatial analysis in ArcGIS Pro, 
        values are adjusted to account for neighboring municipalities. If spillover effects suggest a greater 
        value than the original municipal value, the original value is retained.
        - Measuring unit: Scale score (0-10)
    """,
    "Trust in institutions": """
        **Welcome to the Trust in Institutions indicator**
        - This indicator is part of the Society theme. It measures the percentage of the population aged 15 
        and older who have sufficient trust in institutions, with a 41.05 km spillover distance reflecting 
        regional influence. Using municipal data and spatial analysis in ArcGIS Pro, trust levels are adjusted 
        to account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of the population aged 15+ has sufficient confidence in institutions.
    """,
    "Trust in others": """
        **Welcome to the Trust in Others indicator**
        - This indicator is part of the Society theme. It measures the percentage of the population aged 15 
        and older who have sufficient trust in others, with a 41.05 km spillover distance reflecting regional 
        influence. Using municipal data and spatial analysis in ArcGIS Pro, trust levels are adjusted to
        account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of population aged 15+ find most people trustworthy
    """,
    "Unemployment": """
        **Welcome to the Unemployment indicator**
        - This indicator is part of the Labor and Free Time theme. It measures the percentage of 
        the working population who are unemployed, with a 25 km spillover distance reflecting regional
        influence. Using municipal data and spatial analysis in ArcGIS Pro, unemployment levels are adjusted to
        account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of the working population
    """,
    "Volunteer work": """
        **Welcome to the Volunteering indicator**
        - This indicator is part of the Society theme. Due to the lack of a specific spatial 
        spillover distance, first order contiguity is applied, assuming that volunteer activity
        spills over across shared borders. Using ArcGIS Pro, neighboring municipalities are 
        identified, and their populations engaged in volunteer work are combined to calculate 
        a collective score. This value is then recalculated back to a percentage of individuals
        involved in volunteer work for each municipality, considering the influence of nearby municipalities.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of population aged 15 and over doing organised volunteer work in the current year
    """,
    "Often feeling unsafe in the neighborhood": """
        **Welcome to the Often Feeling Unsafe in the Neighborhood indicator**
        - Due to the absence of specific spatial spillover literature, first order contiguity 
        is applied, assuming that the feeling of insecurity spills over across shared municipal
        borders. Using ArcGIS Pro, neighboring municipalities are identified, and their 
        populations reporting insecurity are combined to calculate a collective score. 
        This score is then recalculated back into a percentage for each municipality, 
        considering the spillover effect from neighboring areas.
        - Measuring unit: Percentage of the population aged 15+ that often feels unsafe in the neighborhood
    """,
    "People with one or more longterm illnesses or conditions": """
        **Welcome to the People with one or more long-term illnesses or conditions indicator**
        - This indicator is part of the Health theme. It measures the percentage of individuals
        aged 15 and older who have one or more long-term illnesses or conditions, assuming 
        spillover effects occur between neighboring municipalities based on shared borders. 
        Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to account
        for neighboring municipalities. If spillover effects suggest a greater percentage than
        the original municipal value, the original value is retained.
        - Measuring unit: Percentage of population aged 18 years or older with long-term illnesses or conditions
    """,
    "Quality of bathing water coastal waters": """
        **Welcome to the Quality of Swimming Water in Coastal Waters indicator**
        - This indicator is part of the Environment theme. It measures the average quality of 
        coastal bathing water, assuming a 1.65 km spillover distance. Using municipal data and 
        spatial analysis in ArcGIS Pro, quality values are adjusted to account for neighboring municipalities.
        This ensures that the indicator reflects regional influences on water quality beyond municipal borders.
        - Measuring unit: Quality score (1=poor to 4=excellent)
    """,
    "Quality of inland bathing water": """
        **Welcome to the Quality of Swimming Water in Inland Waters indicator**
        - This indicator is part of the Environment theme. It measures the average quality of inland 
        bathing water, assuming a 1.65 km spillover distance. Using municipal data and spatial analysis
        in ArcGIS Pro, quality values are adjusted to account for neighboring municipalities. 
        This ensures that the indicator reflects regional influences on water quality beyond municipal borders.
        - Measuring unit: Quality score (1=poor to 4=excellent)
    """,
    "Air quality": """
        **Welcome to the Air Quality theme**
        - The sub-theme air quality includes two indicators: emissions of particulate matter to air and greenhouse gas emissions per capita.
        - Emissions of particulate matter to air tracks the annual average emission of fine particulate matter (less than 2.5 micrometers in diameter).
        - Greenhouse gas emissions per capita measures the total greenhouse gas emissions (in CO2 equivalents) per inhabitant, following IPCC guidelines. It includes emissions in the Netherlands, regardless of the residency of the emitter, but excludes emissions by Dutch residents abroad.
        - Data for particulate matter emissions is available for 2015 and 2019-2022, while data for greenhouse gas emissions per capita spans 2015-2021. The sub-theme is constructed for the years 2019-2021.
    """,
    "Distance to living facilities": """
        **Welcome to the Distance to Living Facilities theme**
        - The theme Distance to Living Facilities includes three indicators: Distance to Sports Field, Distance to Primary School, and Distance to Café, etc.
        - Distance to sports field tracks the average distance, by road, from all residents to a terrain used for sports activities (e.g., sports field, sports hall, swimming pool), with a minimum area of 0.5 hectares. 
        - Distance to primary school measures the average distance from residents to the nearest primary school, based on road distance. It includes only primary schools recognized by the Education Executive Agency (DUO). 
        - Distance to café, etc. tracks the average distance to the nearest café, coffee house, coffee shop, discotheque, sex/night club, or party center, calculated by road. 
        - Data for distance to sports field is available for 2015 and 2017. Data for distance to primary school and distance to café, etc. spans 2013-2023. The theme is constructed for the years 2015 and 2017.

    """,
    "Environment": """
        **Welcome to the Environment theme**
        - The theme Environment includes five indicators: Nature Area per Inhabitant, Emissions of Particulate Matter to Air, Nature and Forest Areas, Distance to Public Green Areas, and Greenhouse Gas Emissions per Capita.
        - Nature area per inhabitant tracks the amount of hectares of forest and open natural terrain per 1000 inhabitants. 
        - Emissions of particulate matter to air measures the annual average particulate matter emissions to air, specifically particles with a diameter of less than 2.5 micrometers. 
        - Nature and forest areas measures the percentage of total land area consisting of forest and open natural terrain. 
        - Distance to public green areas tracks the average distance from residents to the nearest public green space, such as parks, gardens, or forests. 
        - Greenhouse gas emissions per capita measures total greenhouse gas emissions (in CO2 equivalents) per inhabitant, including emissions from within the Netherlands, regardless of the residency of the emitter. 
        - Data for nature area per inhabitant, nature and forest areas, and distance to public green areas is available for 2015 and 2017. Emissions of particulate matter to air has data from 2015 and 2019-2022, while greenhouse gas emissions per capita is available for 2015-2021. - The theme is constructed for the year 2015.

    """,
    "Health": """
        **Welcome to the Health theme**
        - The theme Health includes three indicators: Overweight, Experienced Health, and People with one or more long-term illnesses or conditions. 
        - Overweight tracks the percentage of individuals aged 18 and older with a BMI of 25.0 kg/m² or higher, based on self-reported values. 
        - Experienced health measures the percentage of individuals aged 18 and older who rate their general health as 'good' or 'very good'. 
        - People with one or more long-term illnesses or conditions tracks the percentage of individuals aged 18 and older with one or more long-term illnesses or conditions, defined as lasting 6 months or more. 
        - Data for overweight, experienced health, and people with one or more long-term illnesses or conditions is available for the years 2016, 2020, and 2022. The theme is constructed using data from these years.

    """,
    "Labor and free time": """
        **Welcome to the Labor and Free Time theme**
        - The theme Labour and Free Time includes four indicators: Net Labour Force Participation, Highly Educated Population, Unemployment, and Distance to Public Transportation.
        - Net labour force participation measures the share of the working population (aged 15-74) in the total population of the same age group (working and non-working). 
        - Highly educated population tracks the percentage of individuals aged 15-74 with a diploma at MBO 2, 3, or 4, HAVO, VWO, HBO, or WO level. 
        - Unemployment measures the percentage of the labour force (employed and unemployed) that is unemployed, defined as those without paid work, actively seeking employment, and available for work. 
        - Distance to public transportation tracks the average distance from residents to the nearest public transport stop, covering train, tram, bus, metro, and ferry, based on the 2023 cycle network. 
        - Data for net labour force participation, highly educated population, and unemployment is available for the years 2013-2023. Data for distance to public transportation spans 2017-2023. The theme is constructed for the years 2017-2023.

    """,
    "Material welfare and economic capital": """
        **Welcome to the Material Welfare and Economic Capital theme**
        - The sub-theme material welfare and economic prosperity includes four indicators: median disposable income, average debt per household, median household wealth, and average problematic debt. 
        - Median disposable income tracks the median standardized disposable income per household in euros, adjusted for household size and composition. 
        - Average debt per household measures the average debt of private households, including mortgages, study debt, consumer debt, and other liabilities, corrected for price developments. 
        - Median household wealth reflects the balance of assets and liabilities (adjusted for inflation), including bank deposits, real estate, and debts, in 2023 prices. 
        - Average problematic debt measures the percentage of households with registered problematic debts, based on the Personal Records Database (BRP) as of January 1st of the reference year. 
        - Data for median disposable income, average debt per household, and median household wealth spans from 2013 to 2023, while data for average problematic debt is available from 2021 to 2023. The theme is constructed for the years 2021-2023. 
    """,
    "Natural capital": """
        **Welcome to the Natural Capital theme**
        - The sub-theme Natural Capital includes four indicators: private solar energy, nature and forest areas, built environment, and emissions of particulate matter to air. 
        - Private solar energy measures the installed capacity of solar power installations per home at the end of the reference year. 
        - Nature and forest areas tracks the percentage of total land area that consists of forest and open natural terrain. 
        - Built environment measures the land used for living, working, shopping, entertainment, culture, and public facilities as a percentage of total land area. 
        - Emissions of particulate matter to air measures the annual average particulate matter emissions to air, focusing on particles with a diameter of less than 2.5 micrometers. 
        - Data for private solar energy is available for 2013-2022, while nature and forest areas and built environment have data for 2015 and 2017. Emissions of particulate matter to air has data for 2015 and 2019-2022. - The theme is constructed for the year 2015.
 """,
    "Nature": """
        **Welcome to the Nature theme**
        - The sub-theme nature includes three indicators: nature area per inhabitant, nature and forest areas, and distance to public green areas.
        - Nature area per inhabitant measures the amount of hectares of forest and open natural terrain per 1000 inhabitants. Forest includes terrain planted with trees for timber production and/or nature management, while natural terrain refers to land in its natural dry or wet state.
        - Nature and forest areas tracks the percentage of total land area that consists of forest and open natural terrain.
        - Distance to public green areas calculates the average distance from residents to the nearest public green area, such as parks, gardens, or forests, measured over the road. Public green areas are at least one hectare in size and can be both privately and publicly accessible.
        - Data for all three indicators is available for the years 2015 and 2017. The sub-theme is constructed for the years 2015 and 2017.
    """,
    "Society": """
        **Welcome to the Society theme**
        - The theme Society includes five indicators: Contact with Family, Friends or Neighbours, Trust in Institutions, Trust in Others, Volunteer Work, and Satisfaction with Social Life.
        - Contact with family, friends or neighbours tracks the percentage of people aged 15 and over who have contact with family, friends, or neighbours at least once a week on average. It averages three indicators: weekly contact with family, friends, and neighbours. 
        - Trust in institutions measures the percentage of people aged 15 and over who have confidence in three institutions: the House of Representatives, the police, and judges. The score is the average of the three. 
        - Trust in others tracks the percentage of people aged 15 and over who agree that most people can generally be trusted (generalized trust). 
        - Volunteer work tracks the percentage of people aged 15 and over who have done voluntary work for organizations or associations in the past 12 months. 
        - Satisfaction with social life measures the percentage of people aged 18 and over who score between 7 and 10 on a scale of 1 to 10 in response to their satisfaction with social life. 
        - Data for all five indicators is available from 2013 through 2023. The theme is constructed for the years 2013 through 2023.

    """,
    "Well-being": """
        **Welcome to the Well-being theme**
        - The sub-theme well-being includes two indicators: satisfaction with free time and satisfaction with life.
        - Satisfaction with free time measures the percentage of individuals aged 18 and older who give a score between 7 and 10 on their satisfaction with the amount of free time they have, based on a scale from 1 to 10. 
        - Satisfaction with life measures the percentage of individuals aged 18 and older who give a score between 7 and 10 on their overall life satisfaction, based on the same scale. 
        - Data for both indicators spans the years 2013-2023, and both indicators have been fully incorporated into the well-being score for the theme.
    """,
}

Sources = {
    "Population with a starting qualification": """ 
    - Source for spillover calculation: https://www.sciencedirect.com/science/article/pii/S0166046222000163 
    """,
    "Unemployment": """
    - Source for spillover calculation: https://www.sciencedirect.com/science/article/pii/S0166046222000163 
    """,
    "Distance to public transport": """ 
    - Source for spillover calculation: https://www.researchgate.net/figure/Reported-values-for-willingness-to-walk-to-public-transport-in-meters-and-for-the_tbl1_358628261 
    """,
    "Distance to sports field": """ 
    - Source for spillover calculation: https://www.sciencedirect.com/science/article/abs/pii/S1353829219304861?via%3Dihub
    """,
    "Distance to primary school": """ 
    - Source for spillover calculation: https://ijbnpa.biomedcentral.com/articles/10.1186/1479-5868-5-1
    """,
    "Distance to café etc.": """
    - Source for spillover calculation: https://www.cdc.gov/pcd/issues/2015/15_0065.htm#:~:text=The%20median%20distance%20to%20sit,0.4%20miles%20to%20grocery%2Fsupermarkets.
    """,
    "Trust in institutions": """
    - Source for spillover calculation: https://ifh.wiwi.uni-goettingen.de/site/assets/files/8720/ifh_wp-41_2023.pdf
    """,
    "Trust in others": """ 
    - Source for spillover calculation: https://ifh.wiwi.uni-goettingen.de/site/assets/files/8720/ifh_wp-41_2023.pdf
    """,
    "Distance to public green space": """ 
    - Source for spillover calculation: https://pdf.sciencedirectassets.com/271856/1-s2.0-S0143622821X00161/1-s2.0-S0143622822000443/main.pdf
    """,
    "Nature and forest areas": """ 
    - Source for spillover calculation: https://ijbnpa.biomedcentral.com/articles/10.1186/1479-5868-5-1
    """,
    "Private solar energy": """
    - Source for spillover calculation: https://www.cdc.gov/pcd/issues/2015/15_0065.htm#:~:text=The%20median%20distance%20to%20sit,0.4%20miles%20to%20grocery%2Fsupermarkets.
    """,
    "Emissions of particulate matter to air": """ 
    - Source for spillover calculation: https://www.rivm.nl/ggd-richtlijn-medische-milieukunde-luchtkwaliteit-en-gezondheid/gezondheidseffecten-luchtverontreiniging/luchtkwaliteit-invloed-drukke-wegen
    """,
}
