import pprint

message = 'It was a bright cold day in April, ad the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count)

# pretty print
pprint.pprint(count)

print(pprint.pformat(count))