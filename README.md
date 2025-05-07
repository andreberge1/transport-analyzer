# transport-analyzer
Analyzing public transport in the Oslo area of Norway

## Phase 1: Plan & design
1. Define the Problem
* What value are you delivering? (e.g., visualize bus delay patterns)
* What will users see? (Map, time series chart, table of arrivals)

2. Identify the Data Source
* Choose a real-time transit API (e.g., TransportAPI, OpenMobilityData, city-specific APIs)
* Review API docs, test endpoints using curl or Postman

3. Sketch the System Architecture
* API → Python ETL → SQL Database → Streamlit Dashboard → Azure (optional)
* Tools: VS Code + Git + Docker

## Phase 2: Setup Your Environment
1. Create a GitHub Repo
* Setup README.md, .gitignore, requirements.txt

2. Create a Virtual Environment

3. Install Required Libraries

4. Setup Azure SQL (or use SQLite locally for now)
* Create a database and table schema

Test DB connection from Python

## Phase 3: Build the ETL Pipeline
1. Extract
* Write a Python script to pull live data from the API
* Save JSON responses locally for debugging

2. Transform
* Use pandas to normalize data:
  * Filter for useful columns (e.g., bus ID, location, timestamp)
* Clean formats (e.g., timestamps, nulls)

3. Load
* Store data in your SQL database using sqlalchemy or raw SQL

4. Schedule (Optional)
* Add a cron job or use schedule library to run every X minutes

Log output to a .log file

## Phase 4: Build the dashboard
1. Use Streamlit or Dash
* Set up a basic app: streamlit run app.py

Add:
* Map of vehicle positions (use folium, pydeck, or Plotly)
* Charts (e.g., number of buses over time, average delay)
* Filters (e.g., route, time)

2. Read from the SQL DB
* Query the data based on user inputs
* Cache data to improve performance

## Phase 5: Containerize & Test
1. Create a Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]

2. Build and Run
docker build -t transit-dashboard .
docker run -p 8501:8501 transit-dashboard

## Phase 6: Deploy and automate
1. Deploy to Azure (optional)
* Use Azure App Service or Azure Container Instances
* Add deployment credentials/secrets

2. Set Up CI/CD (GitHub Actions)
* Auto-build Docker image and deploy on push to main
* Test Python code or validate JSON schema before build

## Document & share
* Update your README.md with:
* Project overview
* How to run it locally (Docker + Streamlit)
* Screenshots or video demo
* Architecture diagram
* Create a short demo video or live link (if deployed)
* Write a LinkedIn post or blog about your process