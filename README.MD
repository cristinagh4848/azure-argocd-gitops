# Hackathon ArgoCD Python FastApi Example

## Requirements

You will need the following installed to follow this example:
- Helm
- Kubectl
- Docker
- Python 3.9
- Azure CLI
- Minikube



## Python Fast Api

### Build Docker Image
```bash
docker build -t argocd-python-fastapi:latest .

# Push to docker hub
docker login
docker images
docker tag argocd-python-fastapi jhawthorn22/argocd-python-fastapi:1.0.0
docker push jhawthorn22/argocd-python-fastapi:1.0.0
```


## Development

### Run Container Locally
```bash
docker run -d --name argocd-python-fastapi -p 80:80 argocd-python-fastapi:latest
```

### Minikube Config and Helm Deployment
```bash
minikube start --driver=docker
kubectl config get-contexts
kubectl config set-context minikube

# Enable nginx for minikube
minikube addons enable ingress

# Helm install app
kubectl create namespace apps
helm upgrade --install argocd-python-fastapi charts/apps \
    --namespace apps \
    --values apps/fastapi/helm-config/minikube.yaml
```

### Test App Deployment
```bash
minikube ip
# Change ip to your minikube ip
echo "192.168.49.2 argocd-python-fastapi.local argocd-python-fastapi" >> /etc/hosts

# NOTE: I had to do this on WSL but 
sudo -- sh -c "echo \"192.168.49.2 argocd-python-fastapi.local argocd-python-fastapi\" >> /etc/hosts"


```

### Deploy ArgoCD
```bash
helm...
```


### Api Docs
- [docs](<localhost/docs>)
- [redocs](<localhost/redocs>)