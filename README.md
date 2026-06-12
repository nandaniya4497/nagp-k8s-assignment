# NAGP 2026 Technology Band III Workshop

# Kubernetes, DevOps & FinOps Home Assignment

## Candidate Information

**Name:** Sanjay Nandaniya

**Technology Stack**

* Python FastAPI
* PostgreSQL
* Docker
* Kubernetes (GKE)
* NGINX Ingress Controller
* Docker Hub
* Google Cloud Platform (GCP)

---

# Repository Information

## GitHub Repository

```text
https://github.com/<your-github-username>/nagp-k8s-assignment
```

## Docker Hub Repository

```text
https://hub.docker.com/r/sanjaynagarro/nagp-api
```

## Docker Image

```bash
docker pull sanjaynagarro/nagp-api:v1
```

---

# Application URL

## Home Endpoint

```text
http://<INGRESS-IP>/
```

Example:

```text
http://34.27.163.214/
```

## Employee Endpoint

```text
http://<INGRESS-IP>/employees
```

Example:

```text
http://34.27.163.214/employees
```

---

# Project Overview

This project demonstrates deployment of a multi-tier application on Google Kubernetes Engine (GKE).

The solution consists of:

1. FastAPI Microservice Tier
2. PostgreSQL Database Tier
3. Kubernetes Ingress
4. Persistent Storage
5. Horizontal Pod Autoscaler
6. ConfigMaps
7. Secrets
8. Rolling Updates
9. Self-Healing

---

# Requirement Understanding

The assignment requires:

* One API/Microservice Tier
* One Database Tier
* Database Persistence
* Kubernetes Deployment
* Rolling Updates
* Self-Healing
* Horizontal Pod Autoscaling
* Ingress-based External Access
* ConfigMaps
* Secrets
* FinOps Optimization

---

# Assumptions

* Google Cloud Platform is used.
* Kubernetes cluster is hosted on GKE.
* PostgreSQL is used as database.
* FastAPI is used as microservice framework.
* NGINX Ingress Controller is installed.
* Docker images are stored on Docker Hub.

---

# Solution Architecture

```text
                        INTERNET
                            │
                            ▼
                 +-------------------+
                 |  NGINX INGRESS    |
                 |  Load Balancer    |
                 +---------+---------+
                           │
                           ▼
                +--------------------+
                |    api-service     |
                |    ClusterIP       |
                +---------+----------+
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 +-------------+   +-------------+   +-------------+
 | FastAPI Pod |   | FastAPI Pod |   | FastAPI Pod |
 +-------------+   +-------------+   +-------------+
                          │
                          ▼
                +--------------------+
                | postgres-service   |
                |    ClusterIP       |
                +---------+----------+
                          │
                          ▼
                +--------------------+
                |  PostgreSQL Pod    |
                +---------+----------+
                          │
                          ▼
                +--------------------+
                | Persistent Volume  |
                |        Claim       |
                +---------+----------+
                          │
                          ▼
                +--------------------+
                | Persistent Disk    |
                +--------------------+
```

---

# Requirement Mapping

| Requirement        | Implementation            |
| ------------------ | ------------------------- |
| API Tier           | FastAPI                   |
| Database Tier      | PostgreSQL                |
| External Access    | Ingress                   |
| Internal DB Access | ClusterIP Service         |
| 4 API Pods         | Deployment Replicas = 4   |
| ConfigMap          | Database Configuration    |
| Secret             | Database Password         |
| Persistence        | PVC                       |
| Rolling Updates    | Deployment Strategy       |
| Self-Healing       | Deployment Controller     |
| HPA                | Horizontal Pod Autoscaler |
| FinOps             | Requests, Limits, HPA     |

---

# Project Structure

```text
nagp-k8s-assignment/

├── app
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
│
├── k8s
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── api-deployment.yaml
│   ├── api-service.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
│
├── Dockerfile
├── README.md
└── docs
```

---

# API Design

## Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "NAGP Assignment"
}
```

## Employee Endpoint

```http
GET /employees
```

Returns employee records stored in PostgreSQL.

---

# Database Schema

Database:

```text
nagpdb
```

Table:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```

Sample Data:

```sql
INSERT INTO employees (name, department) VALUES
('John Doe', 'IT'),
('Jane Smith', 'HR'),
('Mike Johnson', 'Finance'),
('Sarah Wilson', 'Operations'),
('David Brown', 'Marketing'),
('Emily Davis', 'Sales'),
('Chris Taylor', 'Support'),
('Lisa Anderson', 'Engineering');
```

---

# Development Setup

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/nagp-k8s-assignment.git

cd nagp-k8s-assignment
```

## Create Python Virtual Environment

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r app/requirements.txt
```

Dependencies:

```text
fastapi
uvicorn
psycopg2-binary
```

## Run Locally

```bash
cd app

uvicorn main:app --reload
```

Access:

```text
http://localhost:8000
```

---

# Docker Build & Push

## Build Image

```bash
docker build -t sanjaynagarro/nagp-api:v1 .
```

## Verify Image

```bash
docker images
```

## Push Image

```bash
docker login

docker push sanjaynagarro/nagp-api:v1
```

---

# Google Kubernetes Engine Setup

## Set Project

```bash
gcloud config set project PROJECT_ID
```

## Create Cluster

```bash
gcloud container clusters create nagp-cluster-2026 \
--num-nodes=3 \
--zone=us-central1-a
```

## Connect Cluster

```bash
gcloud container clusters get-credentials \
nagp-cluster-2026 \
--zone us-central1-a
```

## Verify

```bash
kubectl get nodes
```

---

# Kubernetes Deployment

## Create Namespace

```bash
kubectl apply -f k8s/namespace.yaml
```

## Create ConfigMap

```bash
kubectl apply -f k8s/configmap.yaml
```

## Create Secret

```bash
kubectl apply -f k8s/secret.yaml
```

## Create PVC

```bash
kubectl apply -f k8s/postgres-pvc.yaml
```

Verify:

```bash
kubectl get pvc
```

Expected:

```text
STATUS = Bound
```

## Deploy PostgreSQL

```bash
kubectl apply -f k8s/postgres-deployment.yaml
```

## Create PostgreSQL Service

```bash
kubectl apply -f k8s/postgres-service.yaml
```

Verify:

```bash
kubectl get pods
```

Expected:

```text
postgres-xxxxx 1/1 Running
```

---

# Database Initialization

Connect PostgreSQL:

```bash
kubectl exec -it deployment/postgres -- \
psql -U postgres -d nagpdb
```

Create Table:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```

Insert Data:

```sql
INSERT INTO employees (name, department) VALUES
('John Doe', 'IT'),
('Jane Smith', 'HR'),
('Mike Johnson', 'Finance'),
('Sarah Wilson', 'Operations'),
('David Brown', 'Marketing'),
('Emily Davis', 'Sales'),
('Chris Taylor', 'Support'),
('Lisa Anderson', 'Engineering');
```

Verify:

```sql
SELECT * FROM employees;
```

Exit:

```sql
\q
```

---

# Deploy API

```bash
kubectl apply -f k8s/api-deployment.yaml
```

Verify:

```bash
kubectl get pods
```

Expected:

```text
4 API Pods Running
```

## Create API Service

```bash
kubectl apply -f k8s/api-service.yaml
```

---

# Install NGINX Ingress Controller

```bash
kubectl apply -f \
https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

Verify:

```bash
kubectl get pods -n ingress-nginx
```

Expected:

```text
ingress-nginx-controller 1/1 Running
```

---

# Deploy Ingress

```bash
kubectl apply -f k8s/ingress.yaml
```

Verify:

```bash
kubectl get ingress
```

---

# Deploy HPA

```bash
kubectl apply -f k8s/hpa.yaml
```

Verify:

```bash
kubectl get hpa
```

---

# Validation

## Verify Pods

```bash
kubectl get pods
```

Expected:

```text
4 FastAPI Pods
1 PostgreSQL Pod
```

## Verify Services

```bash
kubectl get svc
```

## Verify PVC

```bash
kubectl get pvc
```

## Verify Ingress

```bash
kubectl get ingress
```

---

# Application Testing

## Home Endpoint

```bash
curl http://<INGRESS-IP>/
```

Expected:

```json
{
  "message":"NAGP Assignment"
}
```

## Employees Endpoint

```bash
curl http://<INGRESS-IP>/employees
```

Expected:

Employee records from PostgreSQL.

---

# Self-Healing Demonstration

Delete API Pod:

```bash
kubectl delete pod <api-pod-name>
```

Observe:

```bash
kubectl get pods -w
```

New pod is automatically created.

---

Delete PostgreSQL Pod:

```bash
kubectl delete pod <postgres-pod-name>
```

Observe:

```bash
kubectl get pods -w
```

Pod is recreated automatically.

---

# Persistence Demonstration

After PostgreSQL pod recreation:

```bash
curl http://<INGRESS-IP>/employees
```

Data remains available.

This proves persistent storage functionality.

---

# Rolling Update Demonstration

Build New Image:

```bash
docker build -t sanjaynagarro/nagp-api:v2 .
```

Push:

```bash
docker push sanjaynagarro/nagp-api:v2
```

Update Deployment:

```bash
kubectl set image deployment/api \
api=sanjaynagarro/nagp-api:v2
```

Verify:

```bash
kubectl rollout status deployment/api
```

No downtime occurs.

---

# Horizontal Pod Autoscaler

Configuration:

* Minimum Replicas: 4
* Maximum Replicas: 10
* Target CPU Utilization: 70%

Verify:

```bash
kubectl get hpa
```

---

# FinOps Considerations

## Resource Requests

```yaml
requests:
  cpu: 100m
  memory: 128Mi
```

## Resource Limits

```yaml
limits:
  cpu: 500m
  memory: 512Mi
```

## Cost Optimization Opportunities

### 1. Horizontal Pod Autoscaling

Scale only when required.

### 2. Cluster Autoscaler

Automatically remove unused nodes.

### 3. Right-Sizing

Monitor:

```bash
kubectl top pods
```

Adjust resources based on actual utilization.

### 4. Spot/Preemptible Nodes

Reduce compute costs for non-production workloads.

### 5. Remove Unused Load Balancers

Delete infrastructure after testing.

---

# Validation Checklist

✅ API Accessible Through Ingress

✅ Database Accessible Only Inside Cluster

✅ 4 API Pods Running

✅ ConfigMap Implemented

✅ Secret Implemented

✅ Persistent Storage Implemented

✅ Rolling Updates Working

✅ Self-Healing Demonstrated

✅ HPA Configured

✅ FinOps Requirements Addressed

---

# Deliverables

## GitHub Repository

<Repository URL>

## Docker Hub

<Docker Hub URL>

## Application URL

<Ingress URL>

## Screen Recording

<Video URL>

The recording demonstrates:

* Kubernetes Objects
* API Access
* Database Access
* Rolling Updates
* Self-Healing
* Persistence
* HPA
* FinOps Considerations

---

# Cleanup

Delete Application:

```bash
kubectl delete -f k8s/
```

Delete Cluster:

```bash
gcloud container clusters delete \
nagp-cluster-2026 \
--zone us-central1-a
```

This prevents unnecessary GCP charges.
