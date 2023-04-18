import re
with open("regex_test.txt") as text:
    names = text.readlines()
    print(f"File contents: {names}")

print('\n')
for name in names:
    find_last_n = re.compile('([A-Z][a-z]+)( [A-Z])? ([A-Z][a-z]+)\n$')
    search_last_n =find_last_n.findall(name)
    result = ' '.join(' '.join(match) for match in search_last_n) if search_last_n else None
    print(result)
