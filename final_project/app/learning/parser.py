def with_names(data):
    result = data.copy()
    result.drop(['1', '2', '3', '4', '5', '6', '7', 'cor', 'date'], axis=1, inplace=True)
    return result


def build_for_cascade(data):
    result = data.copy()
    result.drop(['name', 'label', 'bad', 'snow'], axis=1, inplace=True)
    return result


def build_for_single(data):
    result = data.copy()
    result.drop(['name', 'label'], axis=1, inplace=True)
    return result


def label(data, column='label'):
    return data[[column]]


def add_labels(data):
    c = data.copy()
    bad = []
    snow = []
    for x in c['label']:
        if x == 5:
            bad.append(1)
            snow.append(x)
        elif x == 4 or x == 2:
            bad.append(0)
            snow.append(1)
        else:
            bad.append(0)
            snow.append(0)
    c['bad'] = bad
    c['snow'] = snow
    return c


def remove_bad(data):
    mask = data['snow'].isin([5])
    return data[~mask]


def only_green(data):
    mask = data['label'].isin([5, 4, 2])
    return data[~mask]


def only_snow(data):
    mask = data['label'].isin([5, 1, 0])
    return data[~mask]

