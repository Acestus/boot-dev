kubectl delete deployment <deployment-name>
kubectl delete service <service-name>
kubectl delete configmap <configmap-name>
newgrp docker
minikube addons enable metrics-server
kubectl -n kube-system get pod
kubectl top pod
k proxy

cd kubernetes
kubectl get pods
kubectl top pods
kubectl apply -f testram-configmap.yaml
kubectl apply -f testram-deployment.yaml
kubectl delete -f testram-deployment.yaml
kubectl describe pod synergychat-testram-5f4bb756d-srsth
kubectl apply -f testcpu-hpa.yaml
kubectl apply -f testcpu-deployment.yaml
kubectl get hpa
kubectl get deployments
kubectl apply -f web-hpa.yaml
kubectl delete -f web-deployment.yaml
kubectl apply -f web-deployment.yaml