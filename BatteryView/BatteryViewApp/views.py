from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader   
# Create your views here.
import plotly.graph_objs as go
from django.shortcuts import render
import modules.entsoe_api as entsoe
from datetime import datetime


def graph_view(request):
    # Define x and y values
    if request.method == 'POST':
        slope = float(request.POST.get('slope'))
        intercept = float(request.POST.get('intercept'))
    else:
        slope = 1
        intercept = 0

    # Use the slope and intercept to create x and y values for the line
    x = [0, 1, 2, 3, 4, 5]
    y = [slope * xi + intercept for xi in x]
    trace = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='My Line'
    )

    # Create a layout with a title
    layout = go.Layout(
        title='My Plotly Chart'
    )

    # Create a figure with the trace and layout
    fig = go.Figure(data=[trace], layout=layout)

    # Print the HTML for the chart
    plot_html = fig.to_html(full_html=False)
    # Pass the x and y values as context variables to the template
    context = {
        'plot': plot_html,
        'x': slope,
        'y': intercept,
    }

    return render(request, 'plot.html', context)

def avg_price_graph_view(request):
    if request.method == 'POST':
        startDate = datetime.strptime(request.POST.get('startDate'), '%Y-%m-%d')
        endDate = datetime.strptime(request.POST.get('endDate'), '%Y-%m-%d')
    else:
        return None
    df = entsoe.getRangeData(startDate, endDate)
    avg = list(entsoe.getColStats(df))
    x = range(0, len(avg))
    y = avg
    trace = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='My Line'
    )

    # Create a layout with a title
    layout = go.Layout(
        title=f'Avg Hourly'
    )
    fig = go.Figure(data=[trace], layout=layout)
    plot_html = fig.to_html(full_html=False)
    return HttpResponse(plot_html)