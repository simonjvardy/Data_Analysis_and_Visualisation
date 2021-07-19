import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc  # Needed to support dtype=datetime64[ns, UTC] from Pandas and datetime.datetime comparison
from justpy import chartcomponents

# Load the Pandas DataFrame
data = pd.read_csv('assets/csv/reviews.csv', parse_dates=['Timestamp'])  # Timestamp column is parsed as text otherwise
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).count().unstack()

# Highcharts Spline Chart JS Code 
# https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/streamgraph
chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'center',
        text: ''
    },

    subtitle: {
        floating: true,
        align: 'center',
        y: 30,
        text: ''
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Course Launched'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Python got popular'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    series: [{
        name: "",
        data: []
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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
    hc.options.title.text = 'Average Rating by Month by Course'
    hc.options.subtitle.text = 'Interactive chart using JustPy with HighCharts'
    hc.options.xAxis.categories = list(month_average_crs.index)

    # Create a nested list comprehension of DataFrame columns and column data
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    return webpage

# Call the app function using justpy
jp.justpy(app)