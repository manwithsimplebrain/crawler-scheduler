from celery import Celery
from datetime import datetime
import subprocess

app = Celery(
    'crawler_scheduler',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1'
)

@app.task
def run_spider():
    """
    Gọi Scrapy spider qua subprocess
    """
    try:
        print("Starting Scrapy spider...")
        subprocess.run(
            ["scrapy", "crawl", "example", "-o", "/tmp/output.json", "-t", "json"],
            cwd="scrapy_app",
            check=True
        )
        print("Scrapy spider finished.")
    except subprocess.CalledProcessError as e:
        print(f"Error running spider: {e}")
