---
title: Kubernetes and Virtual Kubelet in a nutshell 
author: "Adi Polak"
description: "Step by step tutorial on how to scale web app using the right infrastructure such as Kubernetes and virtual kubelet"
tags: ["beginners", "devops", "tutorial", "Kubernetes"]
date: "2021-01-10"
draft: false
---

<img class="responsive" src="https://images.unsplash.com/photo-1550587381-a9ec95bbe09e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80;" alt="drawing">

Today, you will learn how to take a web app (it can be any programming language,\
we used Java & Kotlin) and distribute it using Kubernetes (K8s) and Virtual Kubelet (VK).

Well, if you don't know yet why you should consider distributing your web app - read my post [here](https://dev.to/azure/why-should-i-distribute-my-web-app-1kk8).

<span style="background-color: #FFFF00">**So, you are probably asking yourself**</span>\
<span style="background-color: #FFFF00">**"what is Kubernetes and what can I use it for?"**</span>\
<span style="background-color: #FFFF00">**Just keep reading**</span>


Kubernetes is an open-source container-orchestration system for automating application deployment, scaling, and management.
It is used to build distributed, scalable microservices.

It brings many new concepts and terminology we need to familiarize ourselves with, these are the very basics:

## Basic Glossary:
<span style="background-color: #FFFF00">**Node**</span> - Hardware component. Often a VM hosted on a cloud and provide CPU and RAM resources to be used by the Kubernetes cluster.\
<span style="background-color: #FFFF00">**Kubernetes Master**</span> - A node or nodes that are in charge of managing the Kubernetes cluster state.\
<span style="background-color: #FFFF00">**Kubelet**</span> - Primary "node agents" that runs on each node. It manages the containers that were created by Kubernetes and runs on the node it manages.\ 
It communicates with the K8S master.\
<span style="background-color: #FFFF00">**Pod**</span> - hold one or more containers. Containers that share the same pod also share resources and network.\
Pod can be in charge of containers on different nodes- different physical machines or virtual machine(VM).\
It serves as unit of deployment, horizontal scaling, and replication.\
<span style="background-color: #FFFF00">**PodSpec** </span> - Yaml or JSON file that describes the pod spec. It is used by kubelet to make sure that the containers are healthy and running according to expectations.\
<span style="background-color: #FFFF00">**Cluster** </span> - Series of nodes connected together.\
There are many more concepts and terminology but this is the basic that we need to understand virtual kubelet and to start using K8S.\
<span style="background-color: #FFFF00">**Kubernetes API**</span> - Server (REST) that runs on the master node and speaks directly with the kubelets running on the nodes.\

------------------------
In the chart from [Kubernetes.io](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/) we can see the nodes and master:




**Hey, where are the pods?**
Well, the pods can be part of the Deployment or the ReplicaSet.\
The ReplicaSet/Deployment defines the replicas that are distributed among multiple nodes.\
\
Here is another chart that shows the pods work from [the new stack](https://thenewstack.io/kubernetes-deployments-work/) website:

<img class="responsive"  src="https://storage.googleapis.com/cdn.thenewstack.io/media/2017/11/07751442-deployment.png" alt="drawing">

Another diagram shows how ReplicaSet work with Deployment,\
where Deployment can be view as a template for ReplicaSet with replicas default of 3.\
Diagram from Nir Mata [site](https://www.nirmata.com/2018/03/03/kubernetes-for-developers-part-2-replica-sets-and-deployments/):


<img class="responsive"  src="https://www.nirmata.com/wp-content/uploads/2018/03/Deployment.png" alt="drawing">


### How Kubernetes works? 
Kubernetes manages N number of nodes and within those nodes, there are these kubelets.\
Kubelets manage everything related to the node and the pods running on it. Pods are just a collection of containers.

When we take an app put it in a container, upload it to container [registry](https://azure.microsoft.com/en-in/services/container-registry/?WT.mc_id=devto-blog-adpolak) and deploy it into Kubernetes.\
It then deployed onto a VM somewhere that is managed by Kubernetes cluster in our case [Azure Kubernetes Service (AKS)](
https://docs.microsoft.com/en-us/azure/aks?WT.mc_id=devto-blog-adpolak).\
We can see that VM and track it from the CLI and the UI - at that point,\
there is no per-second or pay-as-you-go billing since it is the classic scenario of\
managed K8S service where we pay for the machines in use even if we end up not using them.


## What about Virtual Kubelet (VK)? 
With Virtual Kubelet we don't see the actual node only one virtual node for each service used.\
It acts as an abstraction for us and can spin as many pods as needed.\
Behind the scene, we can have multiple VMs but we will see only one for the specific service that we are using.\
We are not exposed to the VMs running in the managed service that \
we are using from the Virtual Kubelet.\
**Virtual Kubelet acts as a stand-in that help us proxy to other managed services** with higher abstraction.

Virtual Kubelet is an open-source implementation of Kubernetes kubelet\
with the purpose of connecting Kubernetes to other APIs.\
It registers itself as a node and allows us to deploy unlimited amounts of pods and containers.\
It gives us the ability to connect with serverless containers platforms as well.\
Meaning we can take any stateless app, containerize it and provision it through\
the pods and the Virtual Kubelet will manage it for us and will shift it to the\
managed service. We don't need to manage the infrastructure.\
It can scales up or down - all managed by the service.\
According to the managed service in use, we can benefit from [Pay-as-you-Go accounts](https://azure.microsoft.com/en-in/offers/ms-azr-0003p?WT.mc_id=devto-blog-adpolak), flexible auto-scaling and many more.

-------------------------------------------------

 When combining AKS with Azure Container Instances(ACI) you benefit from a fast orchestration of containers.\
 We combine the two using _virtual nodes_. Results in the automation of containers scheduling.\
 Scheduling in container context refers to the ability of the administrator to load a\
 service onto a host system that defined how to run a specific container.\
 Using ACI with _virtual nodes_ results in faster provisioning of pods.

 [Virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-cli?WT.mc_id=devto-blog-adpolak) can be used with AKS and are powered by the open-source Virtual Kubelet.


<img class="responsive"  src="https://github.com/virtual-kubelet/virtual-kubelet/raw/master/website/static/img/diagram.svg?sanitize=true" alt="drawing">


### **Pros:**
**✅ Fully managed solution of top of Kubernetes**
Allow us to connect to many managed solutions from various cloud providers in various regions.

**✅ Pay exactly for what you use**
Managed solutions like [ACI](https://azure.microsoft.com/en-us/services/container-instances?WT.mc_id=devto-blog-adpolak) or [AWS Fargate](https://aws.amazon.com/fargate/) help us\
scale up or down according to our needs without intervention from our side.

**✅Portability**
Everywhere K8S runs, you can run your Virtual Kubelet and connect it with your managed service.

**✅ Regions and other clusters**
From Virtual Kubelet you can leverage services that run on other regions and even other cloud providers.

### **Cons:**
**❗️ Security**
In general, you should always think about security.\
Remember, Security is everyone job!
The overall security aspect of using Kubernetes is pretty complex to begin with.\
When adding Virtual Kubelet, one should be aware of security issues that can\
arise from communicating with other services outside of the Kubernetes cluster and outside of the region/cloud provider.\
If we decide to work with ACI or other internal services, we can establish an internal virtual\
network from K8s cluster to ACI. This way we can eliminate this security concern.

------------------------------------ 

## Let's get practical with a tutorial
In JVM world there are many frameworks that can help us create a web app fast. One that includes the server and UI.\
Our app uses Spring boot. Spring Boot has many embedded features like server and more.\
For the server options, we can pick from Tomcat, Jetty or Undertow.

So you are probably asking yourself, how to get started with Spring Boot?\
go to Spring initializer [site](https://start.spring.io/) and download a template or download the demo app from this [github repository](https://github.com/adipola/virtual-kubelet-kotlin-spring-demo).

In this tutorial, we will deploy a kotlin-spring app to a Virtual Node on K8s cluster.
We will use the next services: AKS, ACR and ACI.

<img class="responsive" src="/images/k8s.png" alt="drawing">



\
__For the tutorial you will need:__
1. Demo [app](https://github.com/adipola/virtual-kubelet-kotlin-spring-demo)
2. Azure [free](https://azure.microsoft.com/en-us/free?WT.mc_id=devto-blog-adpolak) subscription
3. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?WT.mc_id=devto-blog-adpolak&view=azure-cli-latest)
4. [AKS cluster](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough?WT.mc_id=devto-blog-adpolak)


<span style="background-color: #FFFF00">**At this point we have an AKS cluster**</span>
, an app to deploy to our cluster and CLI tools installed.\
For the second phase, we will need an ACI account, Docker registry to store our app image (we will use Azure container registry - [ACR]([https://azure.microsoft.com/en-in/services/container-registry?WT.mc_id=devto-blog-adpolak])


Our demo app comes with a docker file that defines the app already, so we can push it to ACR.\
Navigate in the terminal or CMD into your app directory and run:

```bash
set ACR_NAME={acr name}
az login
az acr login --name $ACR_NAME
docker build --no-cache -t demo .
docker tag demo $ACR_NAME.azurecr.io/samples/demo
docker push $ACR_NAME.azurecr.io/samples/demo
```
This is the push process:

<img class="responsive" src="/images/01-02-push_docker.png" alt="drawing"> \

To test yourself - run your local docker with remote image
```bash
docker run -it --rm -p 8080:80 $ACR_NAME.azurecr.io/samples/demo
```

The docker container will start running locally and you will see something like this:
![](https://github.com/adipola/my-posts/blob/master/pictures/01-01-spring.png?raw=true)
you can stop it with _ctrl+C_.

Now let's connect to our AKS cluster, for that we will need our resource group name and our AKS cluster name:
```bash
set RES_GROUP={resource group name}
set AKS_NAME={AKS name}
az aks get-credentials --resource-group $RES_GROUP --name $AKS_NAME
```
*Verify the connection to the cluster*
```bash
kubectl get nodes
```
we will get the list of our nodes, version, status and more.

Next we will create the authentication between the container registry (ACR) and AKS,\
this is an important step, without it, AKS cluster will not be able to pull the image from the registry.
We will do it using secret - follow [this](https://docs.microsoft.com/bs-latn-ba/azure/container-registry/container-registry-auth-aks#access-with-kubernetes-secret?WT.mc_id=devto-blog-adpolak)


in the tutorial you are running this - remember to **take a note** of them both!
```bash
# Output used when creating Kubernetes secret.
echo "Service principal ID: $CLIENT_ID"
echo "Service principal password: $SP_PASSWD"
```

Validate your connection and secret with logging into docker - 
```bash
docker login $ACR_LOGIN_SERVER --username $CLIENT_ID --password $SP_PASSWD
```
If this is failing, AKS will not be able to pull the image, and later in the tutorial you will get this error `got HTTP response status code 400 error code “InaccessibleImage”`.
Make sure to follow the tutorial in the [link](https://docs.microsoft.com/bs-latn-ba/azure/container-registry/container-registry-auth-aks#access-with-kubernetes-secret?WT.mc_id=devto-blog-adpolak) step by step.


### Install connector:
For installing the connector and the ability to use virtual nodes, we will create a subnet in our network and will install an AKS cluster there with add-ons for virtual node.
This is a more secure way since we create an internal network that is isolated from our bigger K8s cluster.\
Follow the step-by-step [here](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-cli?WT.mc_id=devto-blog-adpolak) but don't deploy the app - we will deploy our app instead.

For deploying the app run:
```bash
kubectl apply -f kotlin-spring-virtual-kublet-linux.yaml
```
This YAML file describes to K8s, pods and kubelet how we want our app to run,\
what is the deployments and the services in use. Each deploy component in our file\
starts with `apiVersion` followed by `kind`, `metadata` and `spec` In our file we have one service named- `azure-spring-kotlin-front-virtual-service`
and one deployment named: `azure-spring-kotlin-front-virtual`.
Under `deployment` and under `spec -> template -> spec` we have the configuration\
for the node selector, we might have many nodes in our cluster, and we would like this app\
to be deployed to our virtual node one and not to the rest.\
For achieving this, under `nodeSelector` we describe the `type` by giving it the value of `virtual-kubelet`.\
This specifies the pods and kubelet that we will deploy this app only on this specific type of node and no other.

Our second component is of `kind` `service` , it's spec type is `loadBalancer` and\
it will have an `External API` for the app so we can load it in our browser.\
For doing it, we need to expose it first - notice that we are exposing the app and not the LoadBalancer itself since we can expose a deployment:

```bash
kubectl expose deployment azure-spring-kotlin-front-virtual --type=LoadBalancer --port 80 --target-port 8080
```

To find the `External API` run:
```bash
kubectl get services
```
And search for `External API` at **azure-spring-kotlin-front-virtual** entry.


### How to debug:

Use the next commands to debug and get a hold of what is happening in the cluster:
```bash
kubectl get services
kubectl get pods
kubectl get deployment
```

From the commands above we will get the data and first statuses of the various component, after figuring out what failed we can run:
```bash
kubectl describe {pod/service/node} {name of pod/service/node}
```
This will give us a JSON back with information like events, under event we will see what failed, it can be - `FailedSynch` app status `Terminated` - which usually reflects that the app crashed and we should check the node logs using
```bash
kubectl logs {name of node}
```

There are many more commands to debug K8s cluster and this was just the tip of the iceberg. Feel free to play and investigate the API.


Have something to add that I forgot to mention? want to discuss more options? write in comments or send a DM on [twitter](https://twitter.com/AdiPolak).


# Learn more 💡
 👉🏼  Watch this [video](https://azure.microsoft.com/en-us/resources/videos/azure-friday-virtual-kubelet-introduction?WT.mc_id=devto-blog-adpolak
) on Virtual Kubelet by Ria Bhatia and Scott Hanselman

 👉🏼 [Quickstart:](https://docs.microsoft.com/en-us/azure/dev-spaces/quickstart-java?toc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Faks%2FTOC.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fbread%2Ftoc.json&WT.mc_id=devto-blog-adpolak) Develop with Java on Kubernetes using Azure Dev Spaces

👉🏼 Java and [Azure](https://azure.microsoft.com/en-us/develop/java/?WT.mc_id=devto-blog-adpolak)

 👉🏼 Kubernetes and Apache Spark on Azure [tutorial](https://docs.microsoft.com/en-us/azure/aks/spark-job?WT.mc_id=devto-blog-adpolak)

<br></br>



*This article originally appeared in Adi Polak's Dev.to blog https://dev.to/adipolak/kubernetes-and-virtual-kubelet-in-a-nutshell-gn4.*