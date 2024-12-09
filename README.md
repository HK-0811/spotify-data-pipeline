# Spotify Data Pipeline with Real-Time Automation
![image](https://github.com/HK-0811/spotify-data-pipeline/blob/master/assets/SpotifyDataPipeline.png)

- Fetches real-time data on songs, albums, and artists using the Spotify API.
- Stores raw data in AWS S3 for scalable and secure storage.
- Transforms raw data into an optimized format using AWS Glue ETL jobs.
- Automates the process with AWS Lambda, triggering Glue jobs whenever new data is added to S3.
- Orchestrates and monitors workflows efficiently with Apache Airflow.
- Provides actionable insights by analyzing and visualizing the processed data in Power BI.

# Steps to run the project

1. Clone the repository
   ```bash
     git clone https://github.com/HK-0811/spotify-data-pipeline

3. Create a virtual environment
   ```bash
    python -m venv venv

5. Activate the virtual environment
      ```bash
     venv\Scripts\activate

7. Install the dependencies
      ```bash
      pip install -r requirements.txt

9. Rename the configuration file and add required credentials to it
    ```bash
     mv config/config.conf.example config/config.conf
     
11. Build and Start the container
       ```bash
      docker-compose up -d --build
    

## Learn more:
Check out my detailed blog post on this project [here](https://medium.com/@himanshukotkar007/building-a-spotify-data-pipeline-from-api-to-insights-7b02198bb1d4).
