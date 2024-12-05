from cgi import print_environ_usage

from aocd import get_data
from aocd import submit

data = get_data(day=5, year=2024) #1854
#data="47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"

rules, updates = data.split("\n\n")
rules_lines = rules.split("\n")
updates_lines = updates.split("\n")
rules_array = []
lookup_list = {}
updates_array = []

for line in updates_lines:
    updates_array.append(list(map(int, line.split(","))))

for line in rules_lines:
    rules_array.append(list(map(int, line.split("|"))))


def compute_lookup_array(rules_array):
    for rule in rules_array:
        if rule[0] not in lookup_list:
            lookup_list[rule[0]] = []
        lookup_list[rule[0]].append(rule[1])

compute_lookup_array(rules_array)

print(lookup_list)
print(updates_array)

total = 0

for update in updates_array:
    rule_valid=False

    for i in range(len(update)):
        if update[i] in lookup_list:
            print(f"Found {update[i]} in lookup list on line {update}")
            prior_list = update[:i]
            # is the rule broken by any prior numbers?\
            for prior in prior_list:
                if prior in lookup_list[update[i]]:
                    rule_valid = True
                    print(f"Rule invalid {prior} in lookup list for {update[i]}")
                    # move the prior number to above the current number
                    update.remove(prior)
                    update.insert(i, prior)
                    print(f"Updated line {update}")

    print(f"Update {update} Rule valid: {rule_valid}")
    if rule_valid:
        total += update[int((len(update) -1) / 2)]

print(total)
submit(total, part="b", day=5, year=2024)