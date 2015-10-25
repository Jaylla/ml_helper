# Machine Learning Helper

Some help functions for machine learning preprocessing

For dealing with categorical features:
* replace_string_with_enumerated_cols
* replace_string_with_hash_cols
* binarize_string_cols

### Examples
```Python
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
    
```