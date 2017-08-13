

# build data with names and labels
def with_names(data):
    result = data.copy()
    result.drop(['1', '2', '3', '4', '5', '6', '7', 'cor', 'date'], axis=1, inplace=True)
    return result


# build data without names and labels
def build_for_single(data):
    result = data.copy()
    result.drop(['name', 'label'], axis=1, inplace=True)
    return result


# build data only with labels
def label(data, column='label'):
    return data[[column]]










