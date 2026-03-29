import psutil
import subprocess
import time
import os

Threshold = 75.0
Project_Id = "vcc3-491712"
Zone = "us-central1-a"
Instance_Name = "gcp-cloud-burst-vm"

def scale_tp_go():
      print(f"\n Warning : Resource usage exceeded {Threshold}%!")
      print("Scaling to Google Cloud Platform...")

      cmd = [
          "gcloud" , "compute", "instances", "create", Instance_Name,
          f"--project={Project_Id}",
          f"--zone={Zone}",
          "--machine-type=e2-micro",
          "--image-family=ubuntu-2204-lts",
          "--image-project=ubuntu-os-cloud",
          "--metadata=startup-script=sudo apt-get update && sudo apt-get install -y nginx"
         ]

      result = subprocess.run(cmd, capture_output=True, text=True)

      if result.returncode == 0:
          print("SUCCESS: Cloud VM is live and running Nginx.")
      else:
          print("ERROR:",result.stderr)

print(f"Monitoring Local VM (Threshold: {Threshold}%)...")
print("Press Ctrl+C to stop.")

try:
     while True:
            cpu_usage = psutil.cpu_percent(interval=2)
            print(f"Current Local CPU Usage: {cpu_usage}%", end="\r")

            if cpu_usage> Threshold:
                scale_tp_go()
                break
            time.sleep(1)
except KeyboardInterrupt:
       print("\nMonitoring stopped.")
