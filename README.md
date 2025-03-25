# Dynamic-process-dashboard
Team Members

1.M.Rathnesh

2.Yuvraj singh

3.Akanksha

**Project Description**
      
The Dynamic Process Monitoring Dashboard is a real-time system monitoring tool designed to track CPU usage, memory consumption, disk activity, network speed, and running processes. This dashboard helps users analyze system performance, identify high resource consumption, and optimize overall efficiency.

Built using Python, Dash, and Plotly, this interactive tool provides graphical insights into system performance, helping users make informed decisions for system optimization.

**Features**

1.Monitors CPU, Memory, Disk, and Network usage in real-time
2.Displays running processes with CPU and memory consumption
3.Graphical representation of system performance using Plotly
4.Auto-refreshing dashboard with updates every second
5.Logging and reporting for historical analysis
6.Lightweight and optimized for performance

**Technologies Used**

Python 3.x – The core language used for backend processing, system monitoring, and visualization.

 **Libraries and Tools:**
1. Dash- Builds the interactive web-based dashboard.
2. Plotly- Creates real-time graphs and visualizations.
3. Psutil- Retrieves real-time system statistics (CPU, Memory, Disk, Network).
4. collections.deque-Efficiently stores real-time system metrics for fast updates.
5. pandas- Logs and reports system data for later analysis.
6. Flask (built into Dash)- Provides the backend for serving the dashboard.

    **Miscellaneous Tools:**
1. GitHub- Version control and project collaboration.
2. VS Code- Development environment for writing and testing Python code.

**Usage**

1.The system collects CPU, Memory, Disk, and Network usage using psutil.
2. The running processes are sorted by CPU usage and displayed in a table.
3️. Data updates every second to provide real-time monitoring.
4️. Users can analyze performance trends and optimize resource usage.

**Example Output**

Timestamp: 2024-03-24 12:30:45
CPU Usage: 45.2%
Memory Usage: 68.3%
Disk Usage: 52.7%
Network Speed: 1.2 MB/s
Top Processes:
- Process: Chrome.exe, PID: 10234, CPU: 10.5%, Memory: 512 MB
- Process: Python.exe, PID: 4536, CPU: 8.7%, Memory: 256 MB




