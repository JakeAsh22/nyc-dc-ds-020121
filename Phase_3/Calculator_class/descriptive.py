#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator():
    def __init__(self, data):
        self.data = data
        self.length = self.__get_length()
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_stand_dev()

    def __get_length(self):
        return len(self.data)

    def __calc_mean(self):
        # # print(type(self.data))
        # # print(type(self.length))
        # d = self.data
        # print(d)
        # sum_d = sum(d)
        mean = sum(self.data)/self.length
        return mean

    def __calc_median(self):
        sorted_data = self.data
        sort_data = sorted(sorted_data)
        if len(self.data) % 2 == 0:
            median1 = sort_data[self.length//2]
            median2 = sort_data[self.length//2 - 1]
            median = (median1 + median2)/2
        else:
            median = sort_data[self.length//2]
        return median

    def __calc_variance(self):
        m = self.mean
        n = self.length
        deviations = [(x - m) ** 2 for x in self.data]
        print(deviations)
        variance = sum(deviations) / (len(self.data)-1)
        print(variance ** 0.5)
        return variance

        # avg = sum(lst) / len(lst)
        # var = sum((x-avg)**2 for x in lst) / len(lst)

    def __calc_stand_dev(self):
        return self.variance ** 0.5

    def add_data(self, data):
        self.data.extend(data)
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_stand_dev()

    def remove_data(self, data):
        self.data = [x for x in self.data if x not in data]
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_stand_dev()
    pass
