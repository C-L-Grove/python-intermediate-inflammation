"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

# Initial analyse_data
# def analyse_data(data_dir):
#     """Calculate the standard deviation by day between datasets

#     Gets all the inflammation csvs within a directory, works out the mean
#     inflammation value for each day across all datasets, then graphs the
#     standard deviation of these means."""
#     data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
#     if len(data_file_paths) == 0:
#         raise ValueError(f"No inflammation csv's found in path {data_dir}")
#     data = map(models.load_csv, data_file_paths)

#     means_by_day = map(models.daily_mean, data)
#     means_by_day_matrix = np.stack(list(means_by_day))

#     daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

#     graph_data = {
#         'standard deviation by day': daily_standard_deviation,
#     }
#     # views.visualize(graph_data)
#     return daily_standard_deviation

# Refactoring out daily_standard_deviation calculation
# def analyse_data(data_dir):
#     """Calculate the standard deviation by day between datasets
#     Gets all the inflammation csvs within a directory, works out the mean
#     inflammation value for each day across all datasets, then graphs the
#     standard deviation of these means."""
#     data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
#     if len(data_file_paths) == 0:
#         raise ValueError(f"No inflammation csv's found in path {data_dir}")
#     data = map(models.load_csv, data_file_paths)
#     daily_standard_deviation = compute_standard_deviation_by_day(data)

#     graph_data = {
#         'standard deviation by day': daily_standard_deviation,
#     }
#     # views.visualize(graph_data)
#     return daily_standard_deviation

# Pre Class load data
# def load_inflammation_data(dir_path):
#     data_file_paths = glob.glob(os.path.join(dir_path, 'inflammation*.csv'))
#     if len(data_file_paths) == 0:
#         raise ValueError(f"No inflammation csv's found in path {dir_path}")
#     data = map(models.load_csv, data_file_paths)
#     return list(data)

class CSVDataSource:
    """
    Loads all the inflamation CSVs within a specified folder
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation CSVs found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)


class JSONDataSource:
    """
    Loads all the inflammation JSONs within a specified folder.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation JSONs found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)


def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation


# Refactoring out loading the data
# def analyse_data(data_dir): # Pre data load class
def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets
    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    # data = load_inflammation_data(data_dir)
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    # graph_data = {
    #     'standard deviation by day': daily_standard_deviation,
    # }
    # views.visualize(graph_data)
    return daily_standard_deviation
