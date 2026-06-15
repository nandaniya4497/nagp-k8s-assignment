# NAGP 2026 Technology

# Kubernetes, DevOps & FinOps Assignment

## Author Information

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
https://github.com/nandaniya4497/nagp-k8s-assignment.git
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

<img width="1024" height="1536" alt="ChatGPT Image Jun 12, 2026, 06_11_20 PM" src="https://github.com/user-attachments/assets/d684e067-5484-4f85-83c7-6424a273bf3f" />

---

## Comprehensive Documentation

Assignment documentation is available at:

[Assignment Documentation](docs/assignment-documentation.md)

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
('Sanjay', 'IT'),
('Minaxi', 'HR'),
('Sagar', 'Finance'),
('Simaran', 'Operations'),
('Mitul', 'Marketing'),
('Meera', 'Sales'),
('Monika', 'Support'),
('Priyanka', 'Engineering'),
('Nirav', 'Production'),
('Hetvi', 'Safety');
```

---

# Development Setup

## Clone Repository

```bash
git clone https://github.com/nandaniya4497/nagp-k8s-assignment.git

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

```powershell
pip install -r app/requirements.txt
```

Dependencies:

```text
fastapi
uvicorn
psycopg2-binary
```

## Run Locally

```powershell
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
docker build -t sanjaynagarro/nagp-api:v1 -f docker/Dockerfile .
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

# Complete Deployment and Testing Steps

This section contains the full sequence from GKE cluster creation to application testing and assignment demonstrations.

## 1. Set GCP Project

```powershell
gcloud config set project PROJECT_ID
```

Verify the active project:

```powershell
gcloud config get-value project
```

## 2. Create GKE Cluster

```powershell
gcloud container clusters create nagp-cluster-2026 --num-nodes=3 --disk-size=30GB --zone=us-central1-a
```

## 3. Connect kubectl to Cluster

```powershell
gcloud container clusters get-credentials nagp-cluster-2026 --zone us-central1-a
```

Verify nodes:

```powershell
kubectl get nodes
```

## 4. Install NGINX Ingress Controller

```powershell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

Verify controller pods:

```powershell
kubectl get pods -n ingress-nginx
```

Verify external load balancer IP:

```powershell
kubectl get svc -n ingress-nginx ingress-nginx-controller
```

Wait until the `EXTERNAL-IP` value is assigned.

## 5. Build and Push Docker Image

Build the API image:

```bash
docker build -t sanjaynagarro/nagp-api:v1 -f docker/Dockerfile .
```

Push the image:

```bash
docker push sanjaynagarro/nagp-api:v1
```

## 6. Deploy Kubernetes Objects

Create namespace first:

```powershell
kubectl apply -f k8s/namespace.yaml
```

Create configuration, secret, database init script, and storage:

```powershell
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/postgres-init-configmap.yaml
kubectl apply -f k8s/postgres-pvc.yaml
```

Deploy PostgreSQL and internal database service:

```powershell
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
```

Deploy API tier and internal API service:

```powershell
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/api-service.yaml
```

Deploy Ingress and HPA:

```powershell
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml
```

## 7. Verify Kubernetes Objects

Verify all namespace objects:

```powershell
kubectl get all -n nagp-assignment
```

Verify API pods:

```powershell
kubectl get pods -n nagp-assignment -l app=api
```

Expected:

```text
4 API pods in Running state
```

Verify PostgreSQL pod:

```powershell
kubectl get pods -n nagp-assignment -l app=postgres
```

Expected:

```text
1 PostgreSQL pod in Running state
```

Verify services:

```powershell
kubectl get svc -n nagp-assignment
```

Expected:

```text
api-service        ClusterIP
postgres-service   ClusterIP
```

Verify PVC:

```powershell
kubectl get pvc -n nagp-assignment
```

Expected:

```text
postgres-pvc   Bound
```

Verify Ingress:

```powershell
kubectl get ingress -n nagp-assignment
```

Verify HPA:

```powershell
kubectl get hpa -n nagp-assignment
```

## 8. Verify Database Initialization

The table and sample records are initialized automatically from `k8s/postgres-init-configmap.yaml` when PostgreSQL starts with an empty persistent volume.

Connect to PostgreSQL:

```powershell
kubectl exec -it -n nagp-assignment deployment/postgres -- psql -U postgres -d nagpdb
```

Verify records:

```sql
SELECT * FROM employees;
```

Exit PostgreSQL:

```sql
\q
```

## 9. Get Application URL

Get the Ingress IP:

```powershell
kubectl get ingress -n nagp-assignment
```

Use the `ADDRESS` value as `<INGRESS-IP>`.

## 10. Test Application

Test home endpoint:

```powershell
curl http://<INGRESS-IP>/
```

Expected:

```json
{
  "message": "NAGP Assignment"
}
```

Test employee endpoint:

```powershell
curl http://<INGRESS-IP>/employees
```

Expected:

```json
[
  {
    "id": 1,
    "name": "Sanjay",
    "department": "IT"
  }
]
```

The actual response contains all seeded employee records from PostgreSQL.

## 11. Demonstrate API Self-Healing

List API pods:

```powershell
kubectl get podspowershell -n nagp-assignment -l app=api
```

Delete one API pod:

```
kubectl delete pod -n nagp-assignment <api-pod-name>
```

Watch pod recreation:

```powershell
kubectl get pods -n nagp-assignment -l app=api -w
```

Expected result: Kubernetes recreates the deleted API pod and restores 4 API replicas.

## 12. Demonstrate Database Self-Healing and Persistence

Check data before deleting the PostgreSQL pod:

```powershell
curl http://<INGRESS-IP>/employees
```

List PostgreSQL pod:

```powershell
kubectl get pods -n nagp-assignment -l app=postgres
```

Delete PostgreSQL pod:

```powershell
kubectl delete pod -n nagp-assignment <postgres-pod-name>
```

Watch pod recreation:

```powershell
kubectl get pods -n nagp-assignment -l app=postgres -w
```

After the pod is running again, verify data still exists:

```powershell
curl http://<INGRESS-IP>/employees
```

Expected result: employee records are still available because PostgreSQL uses `postgres-pvc`.

## 13. Demonstrate Rolling Update

Build a new image version:

```bash
docker build -t sanjaynagarro/nagp-api:v2 -f docker/Dockerfile .
```

Push the new image:

```bash
docker push sanjaynagarro/nagp-api:v2
```

Update the deployment image:

```powershell
kubectl set image -n nagp-assignment deployment/api api=sanjaynagarro/nagp-api:v2
```

Watch rollout:

```powershell
kubectl rollout status -n nagp-assignment deployment/api
```

Verify updated pods:

```powershell
kubectl get pods -n nagp-assignment -l app=api
```

Expected result: API pods are updated gradually using the rolling update strategy.

## 14. Demonstrate HPA

Verify HPA configuration:

```powershell
kubectl get hpa -n nagp-assignment
```

Verify observed CPU and memory usage:

```powershell
kubectl top pods -n nagp-assignment
kubectl top deployment api -n nagp-assignment
```

Generate load:

```powershell
kubectl run load-generator -n nagp-assignment --image=busybox:1.36 --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://api-service/employees; done"
```

Watch HPA:

```powershell
kubectl get hpa -n nagp-assignment -w
```

Watch API pods:

```powershell
kubectl get pods -n nagp-assignment -l app=api -w
```

Expected result: API replicas can scale from 4 up to 10 when CPU utilization crosses the target threshold.

Delete load generator after demonstration:

```powershell
kubectl delete pod -n nagp-assignment load-generator
```

---

# FinOps Considerations

The Service/API tier defines explicit CPU and memory requests and limits in `k8s/api-deployment.yaml`. These values reserve predictable capacity for the API pods and prevent a single pod from consuming excessive node resources.

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

## Observed Metrics Based Optimization

Metrics are observed using Kubernetes Metrics Server through `kubectl top`. On GKE, Metrics Server is available by default in most standard clusters.

Commands used:

```powershell
kubectl top pods -n nagp-assignment
kubectl top deployment api -n nagp-assignment
kubectl get hpa -n nagp-assignment
```

Optimization applied:

| Observation | Optimization |
| ----------- | ------------ |
| API pods need guaranteed baseline compute | Set API requests to `100m` CPU and `128Mi` memory |
| API pods should not overuse node resources | Set API limits to `500m` CPU and `512Mi` memory |
| Traffic can increase temporarily | Added HPA with min `4` and max `10` replicas |
| CPU utilization can indicate high request processing load | HPA scales on `70%` CPU utilization |
| Memory pressure can indicate inefficient resource use | HPA also watches `75%` memory utilization |

After observing real usage, requests can be adjusted. For example, if `kubectl top pods` shows API pods consistently using only `40Mi` memory, the memory request can be reduced from `128Mi` to a lower safe value such as `96Mi`. If CPU usage is consistently near the request during normal traffic, the CPU request can be increased to avoid throttling and unstable autoscaling.

## Cost Optimization Opportunities

### 1. Horizontal Pod Autoscaling

Scale API pods only when CPU or memory utilization requires more capacity.

### 2. Cluster Autoscaler

Automatically remove unused nodes.

### 3. Right-Sizing

Monitor:

```powershell
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

## Source Code Repository

Repository URL:

```text
https://github.com/<your-github-username>/nagp-k8s-assignment
```

Repository contents:

* FastAPI application source code in `app/`
* Dockerfile in `docker/Dockerfile`
* Kubernetes manifests in `k8s/`
* Comprehensive documentation in `docs/assignment-documentation.md`
* README with deployment and testing steps

## Docker Hub

Docker Hub repository:

```text
https://hub.docker.com/r/sanjaynagarro/nagp-api
```

Docker image:

```text
sanjaynagarro/nagp-api:v1
```

## Application URL

Service API endpoint:

```text
http://<INGRESS-IP>/employees
```

Replace `<INGRESS-IP>` with the address shown by:

```powershell
kubectl get ingress -n nagp-assignment
```

## Screen Recording

Screen recording URL:

```text
<Video URL>
```

The recording demonstrates:

* All Kubernetes objects deployed and running.
* API call retrieving records from PostgreSQL.
* API microservice pod deletion and automatic regeneration.
* Database pod deletion and automatic regeneration.
* Database persistence after PostgreSQL pod recreation.
* Rolling update deployment strategy.
* HPA configuration for the Service/API tier.
* FinOps considerations including requests, limits, HPA, right-sizing, and cleanup.

It includes:

* Requirement Understanding
* Assumptions
* Solution Overview
* Justification for the Resources Utilized

## Final Submission Values To Replace

Before submitting, replace these placeholders with actual values:

| Placeholder | Replace With |
| ----------- | ------------ |
| `https://github.com/nandaniya4497/nagp-k8s-assignment` | Final GitHub or GitLab repository URL |
| `http://<INGRESS-IP>/employees` | Final API URL from Kubernetes Ingress |
| `<Video URL>` | Screen recording link |

---

# Cleanup

Delete Application:

```powershell
kubectl delete -f k8s/
```

Delete NGINX Ingress Controller:

```powershell
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

Delete Cluster:

```powershell
gcloud container clusters delete nagp-cluster-2026 --zone us-central1-a
```

This prevents unnecessary GCP charges.
