import requests
from datetime import datetime, timedelta
from sgp4.api import Satrec


def get_tle_data(url):
    response = requests.get(url)
    return response.text


def tle_lines_to_list(tle):
    split_data = tle.strip().split("\n")
    stripped_data = [line.strip() for line in split_data]
    return stripped_data


def tle_notation_to_float(s):
    s = s.strip()
    if not s or s == "00000+0":
        return 0.0
    base, exp = s[:-2], s[-2:]
    base = "0" + "." + base
    return float(f"{base}e{exp}")


def epoch_to_datetime(epoch):
    year = int(epoch[0:2])
    day_of_year = float(epoch[2:])
    year += 2000 if year < 57 else 1900

    epoch_base = datetime(year, 1, 1)

    epoch_datetime = epoch_base + timedelta(days=day_of_year - 1)

    return epoch_datetime


def datetime_to_jd(dt):
    jd = dt.toordinal() + 1721424.5 + (dt.hour + dt.minute / 60
                                       + dt.second / 3600
                                       + dt.microsecond / 3.6e9) / 24.0
    jd_int = int(jd)
    jd_frac = jd - jd_int
    return jd_int, jd_frac


def tle_to_dict(tle_data):
    """
    Parses a tle satellite dataset into a python dictionary.
    :param: tle_data
    :return: dictionary of tle key:value pairs
    """
    tle_data_split = tle_data.strip().split("\n")
    tle_data_stripped = [line.strip() for line in tle_data_split]

    tle_list = []
    line_list = []


    for line in tle_data_stripped:
        line_list.append(line)
        if len(line_list) == 3:
            tle_list.append(line_list)
            line_list = []

    tle_dict = {}

    for sat in tle_list:
        name = sat[0]
        line_1 = sat[1]
        line_2 = sat[2]
        line_dict = {}

        #Line 1 values
        sat_number = int(line_1[2:7].strip())
        classification = line_1[7]
        Int_designation = line_1[9:17]
        epoch = datetime_to_jd(epoch_to_datetime(line_1[18:32]))
        first_derivative_of_mean_motion = float(line_1[33:43])
        second_derivative_of_mean_motion = tle_notation_to_float(line_1[44:52])
        bstar_drag_term = tle_notation_to_float(line_1[53:61])
        ephemeris_type = int(line_1[62])
        element_set_number = int(line_1[64:68])
        checksum_1 = int(line_1[68])

        #Line 2 values
        sat_number_2 = int(line_2[2:7].strip())
        inclination = float(line_2[8:16])
        raan = float(line_2[17:25])
        eccentricity = float("." + line_2[26:33].strip())
        perigee = float(line_2[34:42])
        mean_anomaly = float(line_2[43:51])
        mean_motion = float(line_2[52:63])
        revolution_number = int(line_2[63:68])
        checksum_2 = int(line_2[68])

        line_dict["Line1"] = {"satellite number": sat_number, "classification": classification, "international designator": Int_designation, "epoch": epoch,
                              "first derivative of mean motion": first_derivative_of_mean_motion, "second derivative of mean motion": second_derivative_of_mean_motion,
                              "BSTAR drag term": bstar_drag_term, "ephemeris type": ephemeris_type, "element set number": element_set_number, "checksum 1": checksum_1}

        line_dict["Line2"] = {"satellite number": sat_number_2, "inclination": inclination, "RAAN": raan, "eccentricity": eccentricity, "perigee": perigee,
                              "mean anomaly": mean_anomaly, "mean motion": mean_motion, "revolution number": revolution_number, "checksum 2": checksum_2}

        tle_dict[name] = line_dict

    return tle_dict


def propagate(lines, time):
    ISS = Satrec.twoline2rv(lines[1], lines[2])
    jd_int, jd_frac = time
    error_code, position, velocity = ISS.sgp4(jd_int, jd_frac)
    return position, velocity