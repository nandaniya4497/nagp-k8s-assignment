# NAGP Kubernetes, DevOps and FinOps Assignment Documentation

## Requirement Understanding

The assignment requires a Kubernetes-based multi-tier application with one service/API tier and one database tier.

The service tier must expose an endpoint externally and fetch records from the database tier when the API is invoked. The application must be containerized, pushed to Docker Hub, and deployed on Kubernetes using manifests included in the repository.

The database tier must contain one table with 5 to 10 records, must persist data across pod recreation, and must remain accessible only inside the Kubernetes cluster.

The Kubernetes deployment must demonstrate ConfigMaps, Secrets, Ingress, rolling updates, self-healing, HPA, persistent storage, and FinOps resource optimization.

## Assumptions

* Google Kubernetes Engine is used as the Kubernetes platform.
* NGINX Ingress Controller is installed in the cluster.
* Docker Hub is used as the container registry.
* The API image is published as `sanjaynagarro/nagp-api:v1`.
* The API tier uses Python FastAPI.
* The database tier uses PostgreSQL.
* PostgreSQL data is persisted using a Kubernetes PersistentVolumeClaim.
* Kubernetes Metrics Server is available for HPA and `kubectl top` metrics.
* The final Ingress IP and screen recording URL are added after deployment and demo recording.

## Solution Overview

The solution contains two tiers:

* Service/API tier: Python FastAPI application.
* Database tier: PostgreSQL database.

The FastAPI service exposes:

* `/` for a basic health/home response.
* `/employees` for fetching employee records from PostgreSQL.

The API tier receives database host, port, database name, and user from a Kubernetes ConfigMap. The database password is injected from a Kubernetes Secret. The application uses a PostgreSQL connection pool to avoid opening a new database connection for every request.

The API tier is deployed as a Kubernetes Deployment with 4 replicas. It is exposed internally through a ClusterIP Service and externally through an Ingress resource handled by NGINX Ingress Controller. Rolling updates are enabled for the API deployment.

The database tier is deployed as a single PostgreSQL pod managed by a Kubernetes Deployment. It is exposed only inside the cluster using a ClusterIP Service. PostgreSQL uses a PersistentVolumeClaim so data remains available after pod deletion or recreation.

The initial database table and records are created using `k8s/postgres-init-configmap.yaml`, which mounts an initialization SQL script into the PostgreSQL container.

The HorizontalPodAutoscaler scales the API deployment based on observed CPU and memory utilization.

## Justification for the Resources Utilized

### API Deployment

The API tier runs 4 replicas to satisfy the assignment requirement and provide availability during pod deletion or rolling updates.

Resource requests:

```yaml
requests:
  cpu: 100m
  memory: 128Mi
```

These requests reserve a small baseline amount of CPU and memory for each API pod. FastAPI is lightweight, so this is suitable for the assignment workload.

Resource limits:

```yaml
limits:
  cpu: 500m
  memory: 512Mi
```

These limits prevent API pods from consuming excessive node resources during traffic spikes or unexpected behavior.

### API HPA

The API tier uses an HPA with:

* Minimum replicas: 4
* Maximum replicas: 10
* CPU target utilization: 70%
* Memory target utilization: 75%

This allows the API tier to scale based on observed metrics instead of permanently running maximum capacity.

### Database Deployment

The database tier runs 1 PostgreSQL replica because the assignment requires one database pod. PostgreSQL uses persistent storage through `postgres-pvc` so data is not lost when the pod is recreated.

The database is not externally exposed because external users should access data only through the API tier.

### Services and Ingress

Both API and PostgreSQL Services use ClusterIP. The API is exposed externally only through Ingress, while PostgreSQL remains internal to the cluster.

This avoids direct database exposure and keeps tier-to-tier communication stable by using Kubernetes service DNS names instead of pod IPs.

### FinOps Optimization

The solution applies FinOps practices through:

* CPU and memory requests/limits for API pods.
* HPA based on observed CPU and memory utilization.
* Right-sizing guidance using `kubectl top`.
* Cluster Autoscaler recommendation to remove unused node capacity.
* Spot/preemptible node recommendation for non-production workloads.
* Cleanup steps to remove load balancers and the GKE cluster after assignment validation.

Observed metrics can be collected using:

```bash
kubectl top pods -n nagp-assignment
kubectl get hpa -n nagp-assignment
```

The resource requests and limits can be adjusted after observing real CPU and memory usage during testing.

## Assignment Demo Checklist

Record the following during the screen recording:

* Show all Kubernetes objects running in `nagp-assignment`.
* Show NGINX Ingress Controller running in `ingress-nginx`.
* Show the API endpoint returning records from PostgreSQL.
* Delete one API pod and show Kubernetes recreating it.
* Delete the PostgreSQL pod and show Kubernetes recreating it.
* Call `/employees` again after database pod recreation to prove persistence.
* Show the API rolling update command and rollout status.
* Show HPA configuration and metrics.
* Explain FinOps choices: requests, limits, HPA, right-sizing, and cleanup.
