🚀Automated Crypto Data Pipeline (ETL)

This is my hands-on data engineering project. I built an automated data pipeline (ETL) that collects live cryptocurrency exchange rates, saves a backup file, and stores the structured results into a relational database. The entire infrastructure runs inside isolated **Docker** containers.

## 📊 Pipeline Graph (Architecture)
The workflow follows a clean 3-step operational path managed by Apache Airflow:

[1. Create Table] (PostgresOperator)Creates SQL Schema ──>
[2. Fetch API to S3](Requests API) Saves Raw JSON to Lake  ──> 
[3. Load S3 to Postgres](Pandas & SQLAlchemy)  Loads Database Tables
   

## 🏗️ Technologies I Mastered in this Project:
- **Orchestration (Apache Airflow):** Scheduled the workflow to run automatically and mastered task state tracking inside the web UI.
- **Data Lake Storage (AWS S3 / LocalStack):** Implemented a decoupled Data Lake tier. Used LocalStack to practice saving raw JSON payloads just like in a real Amazon Web Services cloud environment.
- **Data Transformation (Python & Pandas):** Wrote scripts to clean, filter, and restructure nested API data fields into flat dataframes.
- **Analytical Warehousing (PostgreSQL):** Established a secure database connection layer using SQLAlchemy to append clean metrics into final relational tables.
- **Container Deployment (Docker & Docker-Compose):** Orchestrated a multi-container network running 5 different infrastructure services together seamlessly on my machine.

## 🎯 Practical Problems I Solved:
- **API Rate-Limit Protection:** Designed a resilient Python handler. If the external API blocks frequent requests (HTTP 429 errors), my script automatically switches to a fallback cache layer to keep the pipeline stable and green.
- **Decoupled Architecture:** Separated storage from processing. If the PostgreSQL database goes offline, the raw files remain perfectly safe in the S3 Data Lake.
- **Environment Management:** Learned how to natively inject software dependencies (`pandas`, `sqlalchemy`, `boto3`) into isolated Linux containers using a structured `requirements.txt` manifest.
