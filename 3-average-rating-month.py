import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc  # Needed to support dtype=datetime64[ns, UTC] from Pandas and datetime.datetime comparison
from justpy import chartcomponents

# Load the Pandas DataFrame
data = pd.read_csv('assets/csv/reviews.csv', parse_dates=['Timestamp'])  # Timestamp column is parsed as text otherwise
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()

# Highcharts Spline Chart JS Code 
# https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/spline-inverted
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Date Range: 01.01.2018 to 29.03.2021'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Ave. Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Ave. Rating',
        data: []
    }]
}
"""

def app():
    """
    Function to create a Quasar Page using the Vue.js framework from the supported components within the JustPy package.
    Highcharts SVG Charting Library is used to create the data visualisation.
    """
    webpage = jp.QuasarPage()
    jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h5 text-center q-pa-md")

    # JustPy converts string to Python Dictionary before displaying the content
    hc = jp.HighCharts(a=webpage, options=chart_def)

    """
    Access the hc dictionary keys using dot notation.
    Pass the Pandas DataFrame index and column data as chart x & y values
    """
    hc.options.title.text = 'Average Rating by Month'
    hc.options.subtitle.text = 'Interactive chart using JustPy with HighCharts'
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])

    return webpage

# Call the app function using justpy
jp.justpy(app)