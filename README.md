# Spotify Data Pipeline with Real-Time Automation
![image](https://github.com/HK-0811/spotify-data-pipeline/blob/master/assets/SpotifyDataPipeline.png)

This project demonstrates the creation of an automated data pipeline using Spotify API, AWS services, and Apache Airflow. It fetches real-time data on songs, albums, and artists, processes it using AWS Glue, and stores it in an optimized format in AWS S3. A Lambda function ensures event-driven automation by triggering the Glue ETL job upon data insertion into S3. The pipeline is orchestrated using Apache Airflow for seamless workflows, and the processed data is analyzed and visualized in Power BI. This project showcases ETL processes, cloud services, and data visualization expertise.

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
    

Learn more:
Check out my detailed blog post on this project [here](https://medium.com/@himanshukotkar007/building-a-spotify-data-pipeline-from-api-to-insights-7b02198bb1d4).
