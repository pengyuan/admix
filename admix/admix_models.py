# population names for all models
def populations(model):
    if model == 'K7b':
        return ['South Asian',
                'West Asian',
                'Siberian',
                'African',
                'Southern',
                'Atlantic Baltic',
                'East Asian']
    elif model == 'K12b':
        return ['Gedrosia',
                'Siberian',
                'Northwest African',
                'Southeast Asian',
                'Atlantic Med',
                'North European',
                'South Asian',
                'East African',
                'Southwest Asian',
                'East Asian',
                'Caucasus',
                'Sub Saharan']
    elif model == 'E11':
        return ['African',
                'European',
                'India',
                'Malay',
                'South Chinese Dai',
                'Southwest Chinese Yi',
                'East Chinese',
                'Japanese',
                'North Chinese Oroqen',
                'Yakut',
                'American']
    elif model == 'globe13':
        return ['Siberian',
                'Amerindian',
                'West African',
                'Palaeo African',
                'Southwest Asian',
                'East Asian',
                'Mediterranean',
                'Australasian',
                'Artic',
                'West Asian',
                'North European',
                'South Asian',
                'East African']
    elif model == 'globe10':
        return ['Ameriandian',
                'West Asian',
                'Australasian',
                'Palaeo African',
                'Neo African',
                'Siberian',
                'Southern',
                'East Asian',
                'Atlantic Baltic',
                'South Asian']
    else:
        print('Model does not exist!')
        return None

# number of populations in all models
def n_populations(model):
    return len(populations(model))

# model alleles file names
def snp_file_name(model):
    return model + '.alleles'

# model frequency matrix file names
def frequency_file_name(model):
    return model + '.' + str(n_populations(model)) + '.F'
