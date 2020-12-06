import sys
from typing import List, Dict, Tuple
import re

valid_years: Dict[str, Tuple[int, int]] = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030)
}

valid_eye_colors: List[str] = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]


def get_attributes(passport: str) -> Dict[str, str]:
    attributes_str = passport.split()
    attributes = {}
    for attribute_str in attributes_str:
        pair = attribute_str.split(":")
        attributes[pair[0]] = pair[1]
    return attributes


def check_year(year_str: str, low: int, high: int) -> bool:
    if len(year_str) != 4:
        return False
    year = int(year_str)
    if year < low or year > high:
        return False
    return True


def check_height(hgt: str):
    matches = re.match(r"(\d{2,3})(in|cm)", hgt)
    if matches is None:
        return False
    groups = matches.groups()
    height_number = int(groups[0])
    height_unit = groups[1]
    if height_unit == "cm" and (height_number < 150 or height_number > 193):
        return False
    if height_unit == "in" and (height_number < 59 or height_number > 76):
        return False
    return True


def check_passport_1(passport: str) -> bool:
    attributes = get_attributes(passport)
    if len(attributes) < 7:
        return False

    if len(attributes) == 7 and "cid" in attributes:
        return False

    return True


def check_passport_2(passport: str) -> bool:
    if not check_passport_1(passport):
        return False

    attributes = get_attributes(passport)

    # Check years (byr, iyr and eyr)
    for year_key, year in valid_years.items():
        if not check_year(attributes[year_key], *year):
            return False

    # Check height (hgt)
    if not check_height(attributes["hgt"]):
        return False

    # Check hair color (hcl)
    hcl = attributes["hcl"]
    hcl_match = re.match(r"#(?:\d|[a-f]){6}", hcl)
    if hcl_match is None:
        return False

    # Check eye color (ecl)
    if attributes["ecl"] not in valid_eye_colors:
        return False

    # Check passport ID (pid)
    pid = attributes["pid"]
    pid_match = re.match(r"\d{9}", pid)
    if pid_match is None:
        return False

    return True


with open(sys.argv[1], "r") as f:
    content = f.read()
    passports = content.split("\n\n")
    num_valid_1 = 0
    num_valid_2 = 0
    for passport in passports:
        num_valid_1 += check_passport_1(passport)
        num_valid_2 += check_passport_2(passport)
    print(f"Part 1: {num_valid_1}")
    print(f"Part 2: {num_valid_2}")
