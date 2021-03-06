import itertools
from operator import attrgetter

from dataactcore.models.lookups import FILE_TYPE


def get_report_path(job, report_type):
    """
    Return the filename for the error report.
    Does not include the folder to avoid conflicting with the S3 getSignedUrl method.
    """
    path = 'submission_{}_{}_{}_report.csv'.format(job.submission_id, job.file_type.name, report_type)
    return path


def get_cross_report_name(submissionId, source_file, target_file):
    """Return filename for a cross file error report."""
    return "submission_{}_cross_{}_{}.csv".format(submissionId, source_file, target_file)


def get_cross_warning_report_name(submissionId, source_file, target_file):
    """Return filename for a cross file warning report."""
    return "submission_{}_cross_warning_{}_{}.csv".format(submissionId, source_file, target_file)

def get_cross_file_pairs():
    """
    Create a list that represents each possible combination of files used
    in cross file validations.

    Returns:
        a list of tuples, where the first tuple represents file #1 in a pair
        and the second tuple represent file #2 in a pair
    """
    # make sure the list is sorted by files' order attributes to ensure that files
    # in pairs are always listed in the same order
    crossfile_sorted = sorted([f for f in FILE_TYPE if f.crossfile], key=attrgetter('order'))
    # create unique combinations of all files eligible for cross-file validation
    crossfile_combos = itertools.combinations(crossfile_sorted, 2)
    return list(map(list, crossfile_combos))
