from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    new_dict = {}
    for i in s:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict



