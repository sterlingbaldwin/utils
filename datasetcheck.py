import json
import os
import argparse

def check_for_data(start, end, path, filetype):
    """
    Parameters
    ----------
        start (int), the first year of data
        end (int), the last year of data
        path (str), path to where to look for data
        filetype (str), a string in the format 'somefiletype-{y}-{m}.someextension'
    Returns
    -------
        missing (list), a list of strings of the missing data
    """
    contents = os.listdir(path)
    missing = list()

    for year in range(start, end + 1):
        for month in range(1, 13):
            name = filetype.format(y=year, m=month)
            if name not in contents:
                missing.append(name)
    return missing

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', help="Start year", type=int)
    parser.add_argument('-e', '--end', help="end year", type=int)
    parser.add_argument('-t', '--filetype', help="name of the files, with {y} for the year and {m} for the month")
    parser.add_argument('-p', '--path', help="path to directory to search")
    parser.add_argument('-o', '--output', help="path of where to place output file")
    ARGS = parser.parse_args()

    MISSING = check_for_data(
        start=ARGS.start,
        end=ARGS.end,
        path=ARGS.path,
        filetype=ARGS.filetype)

    if MISSING:
        print('found {} missing files'.format(len(MISSING)))

        with open(ARGS.output, 'w') as fp:
            json.dump(fp=fp, obj=MISSING)
    else:
        print('No files missing')
    