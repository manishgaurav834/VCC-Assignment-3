# Cloud Bursting: Local-to-GCP Auto-Scaling 🚀

This repository contains a Python-based implementation of a **Cloud Bursting** architecture. The system monitors local CPU utilization and automatically provisions an Ubuntu instance on **Google Cloud Platform (GCP)** when local resources exceed a defined threshold.

## 📌 Project Overview
The goal of this project is to handle "bursty" workloads by dynamically offloading tasks to the cloud. When the local machine hits a high-load state (simulated via `stress`), a script triggers the GCP SDK to create a pre-configured VM running an Nginx web server.

## 🛠️ Tech Stack
* **Local Environment:** Ubuntu VM (VirtualBox)
* **Cloud Provider:** Google Cloud Platform (GCP)
* **Language:** Python 3.x
* **Libraries:** `psutil`, `subprocess`
* **Tools:** `gcloud` CLI, `stress`, `tmux`

## 🚀 How It Works
1.  **Monitor:** The `autoscale.py` script uses `psutil` to check CPU usage every 2 seconds.
2.  **Trigger:** If CPU usage > **75%**, the scaling function is called.
3.  **Burst:** The script executes a `gcloud compute instances create` command.
4.  **Provision:** A new `e2-micro` instance is deployed with an Nginx startup script.

## 📂 File Structure
* `autoscale.py`: The core monitoring and scaling logic.
* `vcc3_arc.png`: Architecture diagram.
* `report.pdf`: Detailed project implementation report.

## ⚙️ Setup & Usage
1.  **Authenticate GCP:**
    ```bash
    gcloud auth activate-service-account --key-file=your-service-account.json
    gcloud config set project your-project-id
    ```
2.  **Install Dependencies:**
    ```bash
    pip install psutil
    ```
3.  **Run the Monitor:**
    ```bash
    python3 autoscale.py
    ```
4.  **Simulate Load:**
    ```bash
    sudo apt install stress
    stress --cpu 4 --timeout 30s
    ```
---
**Author:** Gaurav Manish (B22CS079)
