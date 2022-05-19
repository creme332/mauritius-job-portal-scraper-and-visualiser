# -*- coding: utf-8 -*-
"""
Created on Fri May 6 2022
Python Version : 3.9.7
Panda version : 1.3.3
Summary : Create charts to visualise job data from data.csv.
@author: me
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

data_source_filename = 'TESTING.csv'
jobs_df = pd.read_csv(data_source_filename)
jobs_df.drop_duplicates(
    subset=None, keep='first', inplace=False)  # drop duplicates

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)


def HorizontalLollipopChart(source_filename, destination_filename):
    # using data from csv file
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns

    # my_labels = df[column_headings[0]].tolist()
    # my_data = df[column_headings[1]].tolist()

    # when using data from dictionary
    # df = pd.DataFrame(list(dictionary.items()), columns=['Name', 'Value'])

    # Reorder it based on the values:
    ordered_df = df.sort_values(by=column_headings[1])  # VARIABLE
    my_range = range(1, len(df.index)+1)
    plt.style.use('default')

    # Horizontal version
    plt.hlines(y=my_range, xmin=0,
               xmax=ordered_df[column_headings[1]], color='skyblue')
    plt.plot(ordered_df[column_headings[1]], my_range, "D")
    plt.yticks(my_range, ordered_df[column_headings[0]])

    # plt.savefig(destination_filename, bbox_inches='tight')
    plt.show()
    plt.close()


def HorizontalBarChart(source_filename, destination_filename):
    # =============================================================================
    #     for key in list(dictionary):
    #         if dictionary[key] == 0:
    #             dictionary.pop(key, None)
    # =============================================================================
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns

    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()

# =============================================================================
#     # when reading from dictionary
#     my_labels = list(dictionary.keys())
#     my_data = list(dictionary.values())
# =============================================================================

    #colours = ['red', 'yellow', 'green', 'blue', 'orange', 'black']
    cmap = plt.cm.tab10
    colors = cmap(np.arange(len(my_labels)) % cmap.N)
    # plt.style.use('ggplot')

    plt.barh(my_labels, my_data, color=colors)
    # plt.title('Programming languages')
    plt.ylabel('Language')  # VARIABLE
    plt.xlabel('Frequency')

    plt.show()
    # plt.savefig(destination_filename, bbox_inches='tight')
    plt.close()


def VerticalBarChart(dictionary, filename):
    # filter out data which have a count of 0
    for key in list(dictionary):
        if dictionary[key] == 0:
            dictionary.pop(key, None)

    plt.bar(range(len(dictionary)), dictionary.values(),
            align='center', width=0.3)
    plt.xticks(range(len(dictionary)), dictionary.keys())

    plt.savefig(filename, bbox_inches='tight')
    plt.close()


def PieChart(languages):
    # filter out languages which have not been used at all
    for lang in list(languages):
        if languages[lang] == 0:
            languages.pop(lang, None)

    languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    x, y = zip(*languages)  # unpack a list of pairs into two tuples

    # create a figure and set different background
    fig = plt.figure()
    fig.patch.set_facecolor('black')

    # Change color of text
    plt.rcParams['text.color'] = 'white'

    # Create a circle at the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='black')

    # Pieplot + circle on it
    plt.pie(y, labels=x, shadow=True, autopct='%1.1f%%')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('filename.pdf')
    plt.close()

    # =============================================================================
    #     # words which must be analysed separately :
    #         node.js, react.js, Oracle Cloud, vue.js
    # =============================================================================
    languages = {
        "C++": 0, "Java": 0, "Python": 0, "Javascript": 0, "PHP": 0,
        "HTML": 0, "CSS": 0, "Node.js": 0, "Clojure": 0,
        "C#": 0, "Bash/Shell": 0, "PowerShell": 0, "Kotlin": 0,
        "Rust": 0, "Typescript": 0, "SQL": 0, "Ruby": 0, "Dart": 0
    }
    # java is a substring of javascript
    # ruby is  a subting of ruby on rails

    databases = {
        "MySQL": 0, "PostgreSQL": 0, "SQLite": 0, "MongoDB": 0,
        "Microsoft SQL Server": 0, "Redis": 0, "MariaDB": 0, "Firebase": 0,
        "Elasticsearch": 0, "Oracle": 0, "DynamoDB": 0, "Cassandra": 0,
        "IBM DB2": 0, "Couchbase": 0
    }  # Will misflag Oracle Cloud as Oracle database

    cloud_platforms = {"AWS": 0,
                       "Google Cloud Platform": 0,
                       "Microsoft Azure": 0,
                       "React.js": 0,
                       "Heroku": 0,
                       "DigitalOcean": 0,
                       "Watson": 0,
                       "Oracle Cloud Infrastructure": 0
                       }

    web_frameworks = {"Svelte": 0,
                      "ASP.NET Core": 0,
                      "FastAPI": 0,
                      "React.js": 0,
                      "Vue.js": 0,
                      "Express": 0,
                      "Spring": 0,
                      "Ruby on Rails": 0,
                      "Angular": 0,
                      "Django": 0,
                      "Laravel": 0,
                      "Flask": 0,
                      "Gatsby": 0,
                      "Symfony": 0,
                      "ASP.NET": 0,
                      "jQuery": 0,
                      "Drupal": 0,
                      "Angular.js": 0
                      }

    libraries = {".NET Framework": 0,
                 "NumPy": 0,
                 ".NET Core": 0,
                 "Pandas": 0,
                 "TensorFlow": 0,
                 "React Native": 0,
                 "Flutter": 0,
                 "Keras": 0,
                 "PyTorch": 0,
                 "Cordova": 0,
                 "Apache Spark": 0,
                 "Hadoop": 0,
                 "Tableau": 0,
                 "Power BI": 0,
                 "Power Query": 0,
                 }

    other_tools = {
        "Git": 0,
        "Terraform": 0,
        "Kubernetes": 0,
        "Docker": 0,
        "Ansible": 0,
        "Yarn": 0,
        "Unreal Engine": 0,
        "Unity 3D": 0,
    }  # Git is a substring of GitHub

    # word frequency of Linux, GitHub

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"]
        words = re.findall(r'\w+', jobs_details)

        # search languages
        for lang in languages:
            if lang.lower() in words.lower():
                languages[lang] += 1

        # search databases
        for db in databases:
            if db.lower() in words.lower():
                databases[db] += 1

        # search cloud platforms
        for cp in cloud_platforms:
            if cp.lower() in words.lower():
                cloud_platforms[cp] += 1

        # search web frameworkds
        for wb in web_frameworks:
            if wb.lower() in words.lower():
                web_frameworks[wb] += 1

        # search other
        for lb in libraries:
            if lb.lower() in words.lower():
                libraries[lb] += 1

        for tool in other_tools:
            if tool.lower() in words.lower():
                other_tools[tool] += 1

    HorizontalBarChart(languages, "TEST.pdf")

HorizontalBarChart("LanguageCountData.csv", "")


# To-Do
# - Search each language/framework on site to see if spelling matches expected spelling
# - Create a separate file to store frequencies
# - Alternate spelling of React.js = ReactJS, React
# - Black background, change colors of bars
# - add xlabel, ylabel to parameters
#    https://towardsdatascience.com/donut-plot-with-matplotlib-python-be3451f22704
#   create donut plot with percentage
#   create donut plot with percentage
