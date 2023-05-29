def demographic_data():
    """
    :param df: Dataframe including locality information for deriving demographic data
    :return: Dataframe with columns for demographic data including longitude, latitude, median home value, median household income, median age and total population.
    """
    import requests
    import pandas as pd

    url = 'https://acs2021.ctdata.org/data/data.geojson'
    res = requests.get(url).json()
    features = res['features']

    ct_data_dict = dict()
    for i in range(len(features)):
        for key, val in features[i]['properties'].items():
            if key not in ct_data_dict:
                ct_data_dict[key] = [val]
            else:
                ct_data_dict[key].append(val)

    longitude = [features[i]['geometry']['coordinates'][0][0][0] for i in range(len(features))]
    ct_data_dict['longitude'] = longitude
    latitude = [features[i]['geometry']['coordinates'][0][0][1] for i in range(len(features))]
    ct_data_dict['latitude'] = latitude

    ct_dem_df = pd.DataFrame.from_dict(ct_data_dict).sort_values(by='name', ignore_index=True)

    for i in ct_dem_df.columns:
        if 'moe' in i:
            ct_dem_df.drop(columns=i, inplace=True)
        elif 'change' in i:
            ct_dem_df.drop(columns=i, inplace=True)

    rch = ['name', 'b19013', 'b01003', 'b25077', 'b01002',
           'longitude', 'latitude']
    rel_cols = list()
    for i in ct_dem_df.columns:
        for j in rch:
            if j in i:
                rel_cols.append(i)

    ct_dem_df = ct_dem_df[rel_cols]

    def cols_clean(ct):
        new_cols = list()
        for ind, val in enumerate(ct):
            if 'b25077' in val:
                val = val.replace('b25077', 'median_home_value')
                new_cols.append(val)
            elif 'b01003' in val:
                val = val.replace('b01003', 'total_population')
                new_cols.append(val)
            elif 'b19013' in val:
                val = val.replace('b19013', 'median_household_income')
                new_cols.append(val)
            elif 'b01002' in val:
                val = val.replace('b01002', 'median_age')
                new_cols.append(val)
            elif 'name' in val:
                val = val.replace('name', 'Locality')
                new_cols.append(val)
            elif 'longitude' in val:
                new_cols.append(val)
            elif 'latitude' in val:
                new_cols.append(val)

        return new_cols

    ct_dem_df.columns = cols_clean(list(ct_dem_df.columns))

    return ct_dem_df


if __name__ == '__main__':
    print(demographic_data())
