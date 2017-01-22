import panflute as pf

input_fn = 'benchmark.json'
output_fn = 'panflute.json'


def empty_test(element, doc):
    return


def test_filter(element, doc):
    if type(element) == pf.Header:
        return []
    if type(element) == pf.Str:
        element.text = element.text + '!!'
        return element


print('\nLoading JSON...')

with open(input_fn, encoding='utf-8') as f:
    doc = pf.load(f)

print('Dumping JSON...')
with open(output_fn, mode='w', encoding='utf-8') as f:
    pf.dump(doc, f)
    f.write('\n')

print(' - Done!')


print('\nComparing...')

with open(input_fn, encoding='utf-8') as f:
    input_data = f.read()

with open(output_fn, encoding='utf-8') as f:
    output_data = f.read()

print('Are both files the same?')
print(' - Length:', len(input_data) == len(output_data),
      len(input_data), len(output_data))
print(' - Content:', input_data == output_data)

print('\nApplying trivial filter...')
doc = doc.walk(action=empty_test, doc=doc)
print(' - Done!')

print(' - Dumping JSON...')
with open(output_fn, mode='w', encoding='utf-8') as f:
    pf.dump(doc, f)
    f.write('\n')
print(' - Done!')
print(' - Comparing...')
with open(input_fn, encoding='utf-8') as f:
    input_data = f.read()
with open(output_fn, encoding='utf-8') as f:
    output_data = f.read()
print(' - Are both files the same?')
print('   - Length:', len(input_data) ==
      len(output_data), len(input_data), len(output_data))
print('   - Content:', input_data == output_data)


assert input_data == output_data
