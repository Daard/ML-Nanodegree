import seaborn as sns

def explore(data):
    n_images = len(data)
    n_features = len(data.columns[:-1])
    n_good = len(data.loc[data['label'] == 0])
    n_not_bad = len(data.loc[data['label'] == 1])
    n_with_snow = len(data.loc[data['label'] == 2])
    n_snow_and_clouds = len(data.loc[data['label'] == 4])
    n_bad = len(data.loc[data['label'] == 5])

    # Print the results
    print("Total number of images: {}".format(n_images))
    print("Number of features: {}".format(n_features))
    print("Number of good images: {}".format(n_good))
    print("Number of not bad images: {}".format(n_not_bad))
    print("Number of images with snow: {}".format(n_with_snow))
    print("Number of images with snow and clouds: {}".format(n_snow_and_clouds))
    print("Number of bad images: {}".format(n_bad))

    sns.factorplot(x='1', data=data, hue='label', kind='count')