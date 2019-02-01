from treetable import treetable
import random
import string


def _gen_line(groups):
    if isinstance(groups, dict):
        return {
            name.rstrip('<>='): _gen_line(group)
            for name, group in groups.items()
        }
    else:
        format_ = groups
        if 'd' in format_:
            return random.randrange(50)
        elif '%' in format_:
            return random.random()
        elif 's' in format_:
            size = int(format_.rstrip('s'))
            return ''.join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(1, size)))
        else:
            raise ValueError(f"Don't know how to handle format {format_}")


def print_groups(groups, num_lines=4):
    lines = []
    for _ in range(num_lines):
        lines.append(_gen_line(groups))
    print(treetable(lines, groups, shorten=False))
    print()
    print(treetable(lines, groups, shorten=True))
    print()


groups = {
    'name': '10s',
    'info': {
        'index': 'd',
        'status': '1s',
    },
    'metrics>': {
        'train': {
            'precision': '.1%',
            'recall': '.1%',
        },
        'test': {
            'auc': '.1%',
            'accuracy': '.1%',
        }
    },
}
print_groups(groups, 0)
print_groups(groups)

groups['plop'] = {}
print_groups(groups)

groups = {
    'info': {
        'index': 'd',
        'status': '1s',
    },
    'metrics>': {
        'precision': '.1%',
        'recall': '.1%',
    }
}
print_groups(groups)
