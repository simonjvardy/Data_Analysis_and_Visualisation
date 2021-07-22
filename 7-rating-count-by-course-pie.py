import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc  # Needed to support dtype=datetime64[ns, UTC] from Pandas and datetime.datetime comparison
from justpy import chartcomponents

# Load the Pandas DataFrame   
data = pd.read_csv('assets/csv/reviews.csv', parse_dates=['Timestamp'])  # Timestamp column is parsed as text otherwise
share = data.groupby(['Course Name'])['Rating'].count()

# Highcharts Spline Chart JS Code
# https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/pie-basic
chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: [{
            name: '',
            y: null,
            sliced: true,
            selected: true
        }]
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
    hc.options.title.text = 'Aggregated Average Ratings by Day of the Week'
    hc.options.subtitle.text = 'Interactive chart using JustPy with HighCharts'

    # construct a list comprehension of DataFrame columns and column data
    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(share.index, share)]

    hc.options.series[0].data = hc_data
    
    return webpage
    
jp.justpy(app)