import re


def get_policy(policy):
    match = re.match(r"(\d+)-(\d+) ([a-z])", policy)
    return (match.group(1), match.group(2), match.group(3))


def is_password_ok(policy, password):
    policy = get_policy(policy)
    regex = re.escape(
        policy[2]) + r"{" + re.escape(policy[0]) + r"," + re.escape(policy[1]) + r"}"
    return bool(re.search(regex, password))


def iter_passwords(policy, passwords):
    return list(filter(lambda password: is_password_ok(policy, password), passwords))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        passwords = dict()
        for line in f:
            policy, password = line.split(":")
            if(policy in passwords):
                passwords[policy] += [password.strip()]
            else:
                passwords[policy] = [password.strip()]
    results = [iter_passwords(key, passwords[key]) for key in passwords]
    print(len([res for res in results if res]))

