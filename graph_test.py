"""Test file."""
import json
import pdb
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.offline as offline


def json_to_list(filename):
    """Turn a json file into a python list."""
    data = json.load(open(filename))
    return data


def wordcount(data, search_word):
    """Return the number of times a word has been used."""
    count = 0
    for result in data:  # do something which each result from scrape
        for key in result:
            text_list = result[key].split()
            for word in text_list:
                if word.lower() == search_word.lower():
                    count += 1
    return count


def generate_chart_on_keyword(words, filename, count_function):
    """Make a bar chart based on given words."""
    yvalues = []
    data = json_to_list(filename)
    for word in words:
        yvalues.append(count_function(data, word))
    chart_data = [go.Bar(
        x=words,
        y=yvalues)]
    div = offline.plot(chart_data, auto_open=False, output_type='div')
    return div


def get_job_locations(filename):
    """Get the number of jobs by country as a dictionary."""
    raw_data = json_to_list('python_jobs.json')
    countries = {}
    for job in raw_data:
        location = job['loc']
        country = location.split()[-1].lower()
        if country == 'usa' or country == 'states' or country == 'us':
            countries.setdefault('usa', 0)
            countries['usa'] += 1
        elif country == 'uk' or country == 'kingdom' or country == 'england':
            countries.setdefault('uk', 0)
            countries['uk'] += 1
        else:
            countries.setdefault(country, 0)
            countries[country] += 1
    return countries


def get_job_types(filename):
    """Get the number of jobs by country as a dictionary."""
    raw_data = json_to_list('python_jobs.json')
    job_types = {}
    for job in raw_data:
        types = job['job_type']
        for item in types:
            job_types.setdefault(item, 0)
            job_types[item] += 1
    return job_types


def dict_to_pie_chart_url(dict):
    """Turn dictionary into chart based on kvp."""
    labels = []
    values = []
    for key in dict:
        labels.append(key)
        values.append(dict[key])
    trace = go.Pie(labels=labels, values=values)
    url = py.plot([trace], auto_open=False)
    # pdb.set_trace()
    return url


def dict_to_pie_chart_tag(dict):
    """Turn dictionary into chart based on kvp."""
    labels = []
    values = []
    for key in dict:
        labels.append(key)
        values.append(dict[key])
    trace = go.Pie(labels=labels, values=values)
    url = offline.plot([trace], auto_open=False, output_type='div')
    return url


languages = ['python', 'c', 'java', 'c++', 'c#', 'r', 'javascript', 'Go', 'swift', 'kotlin', 'php']


def wordcount_for_reddit(data, search_word):
    """Return the number of times a word has been used."""
    count = 0
    for result in data:  # do something which each result from scrape
        for key in result:
            stringed_list = str(result[key])
            text_list = stringed_list.split()
            for word in text_list:
                if search_word == 'Go':
                    if word == search_word:
                        count += 1
                elif word.lower() == search_word.lower():
                    count += 1
    return count


if __name__ == '__main__':
    data = json_to_list('example.json')
    count1 = wordcount(data, 'and')
    print(count1)
