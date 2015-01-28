# -*- coding: utf-8 -*-
from collections import Counter
import matplotlib.pyplot as plt
from parse import parse, MY_FILE


def visualize_days():
    """Visualize data by day of week"""

    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Same logic witout the iterator
    # lista = []
    # for item in data_file:
    #    lista.append(item["DayOfWeek"])
    # counter = Counter(lista)

    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
            counter["Monday"],
            counter["Tuesday"],
            counter["Wednesday"],
            counter["Thursday"],
            counter["Friday"],
            counter["Saturday"],
            counter["Sunday"],
        ]
    # day_tuple is necessary to use in matplorlib.xticks()
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save the plot!
    plt.savefig("Days.png")

    # close plot file
    plt.clf()


def main():
    visualize_days()

if __name__ == "__main__":
    main()