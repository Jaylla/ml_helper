import pandas as pd
from sklearn import preprocessing


def replace_string_with_enumerated_cols(data_frame, cols_to_replace):
    """replace values of particular columns with integer numbers"""

    for col in cols_to_replace:
        data_frame[col] = pd.factorize(data_frame[col])[0]
    return data_frame


def replace_string_with_hash_cols(data_frame, cols_to_replace):
    """replace values of particular columns with its hash values"""

    for col in cols_to_replace:
        data_frame[col] = data_frame[col].apply(hash)
    return data_frame


def binarize_string_cols(data_frame, cols_to_replace):
    """replace each of cols_to_replace with set of binary columns"""

    for col in cols_to_replace:
        lb = preprocessing.LabelBinarizer()
        col_values = lb.fit_transform(data_frame[col])
        classes = [col + '_' + x for x in lb.classes_]
        binarized_column = pd.DataFrame(col_values, columns=classes)

        # add new columns and remove the old one
        data_frame = pd.concat([data_frame, binarized_column], axis=1)
        data_frame = data_frame.drop([col], axis=1)
    return data_frame


if __name__ == '__main__':
    data = pd.DataFrame({'pet':      ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat'],
                         'children': [4, 0, 3, 1, 2, 3, 0],
                         'job': ['engineer', 'developer', 'manager', 'developer', 'manager', 'manager', 'developer'],
                         'salary':   [90, 24, 44, 27, 32, 59, 36]})
    print(data)

    b = binarize_string_cols(data, ['pet', 'job'])
    print(b)
    h = replace_string_with_hash_cols(data, ['pet', 'job'])
    print(h)
    e = replace_string_with_enumerated_cols(data, ['pet', 'job'])
    print(e)
