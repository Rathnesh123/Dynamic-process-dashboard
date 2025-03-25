import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import psutil
import plotly.graph_objs as go
import pandas as pd
from collections import deque

# Initialize Dash app
app = dash.Dash(__name__)

# Store real-time data using deque (keeps last 50 values)
max_len = 50
cpu_usage = deque(maxlen=max_len)
memory_usage = deque(maxlen=max_len)
disk_usage = deque(maxlen=max_len)
network_speed = deque(maxlen=max_len)

# Layout of the Dashboard
app.layout = html.Div(children=[
    html.H1("🔹 Real-Time System Monitoring Dashboard", style={'textAlign': 'center'}),

    # CPU, Memory, Disk, and Network Graphs
    dcc.Graph(id='cpu-graph'),
    dcc.Graph(id='memory-graph'),
    dcc.Graph(id='disk-graph'),
    dcc.Graph(id='network-graph'),

    # Process Table
    html.H3("Running Processes", style={'textAlign': 'center'}),
    dash_table.DataTable(
        id='process-table',
        columns=[
            {"name": "PID", "id": "pid"},
            {"name": "Name", "id": "name"},
            {"name": "CPU (%)", "id": "cpu"},
            {"name": "Memory (MB)", "id": "memory"}
        ],
        style_table={'overflowX': 'auto'},
        style_header={'backgroundColor': 'black', 'color': 'white'},
        style_cell={'textAlign': 'center'}
    ),

    # Interval for Live Updates
    dcc.Interval(id='interval-update', interval=1000, n_intervals=0)
])

# Callback to update graphs and process table
@app.callback(
    [Output('cpu-graph', 'figure'),
     Output('memory-graph', 'figure'),
     Output('disk-graph', 'figure'),
     Output('network-graph', 'figure'),
     Output('process-table', 'data')],
    Input('interval-update', 'n_intervals')
)
def update_dashboard(n):
    # Get system metrics
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    net_speed = (net_io.bytes_sent + net_io.bytes_recv) / (1024 * 1024)  # Convert to MB

    # Append data
    cpu_usage.append(cpu)
    memory_usage.append(memory)
    disk_usage.append(disk)
    network_speed.append(net_speed)

    # Get running processes
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        process_list.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cpu': proc.info['cpu_percent'],
            'memory': round(proc.info['memory_info'].rss / (1024 * 1024), 2)  # Convert to MB
        })

    # Sort processes by CPU usage
    process_list = sorted(process_list, key=lambda x: x['cpu'], reverse=True)[:10]

    # Create graphs
    cpu_fig = go.Figure([go.Scatter(y=list(cpu_usage), mode='lines', name='CPU Usage (%)')])
    memory_fig = go.Figure([go.Scatter(y=list(memory_usage), mode='lines', name='Memory Usage (%)')])
    disk_fig = go.Figure([go.Scatter(y=list(disk_usage), mode='lines', name='Disk Usage (%)')])
    network_fig = go.Figure([go.Scatter(y=list(network_speed), mode='lines', name='Network Speed (MB/s)')])

    # Set graph styles
    for fig in [cpu_fig, memory_fig, disk_fig, network_fig]:
        fig.update_layout(title=fig.data[0].name, xaxis_title="Time", yaxis_title="Usage", template="plotly_dark")

    return cpu_fig, memory_fig, disk_fig, network_fig, process_list

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
