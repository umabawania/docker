# **Understanding Docker: A Beginner-Friendly Guide 🚀**

## What is **Docker** 🐳

Docker is a containerization tool that packages an application along with everything it needs to run — such as its dependencies, libraries, configuration, and runtime — into a unit called a container.

A **container** is a small, isolated environment where our application can run consistently.

## **Why Docker?**

**Suppose** I have an application that requires:

- Python 3.11
- PostgreSQL client
- Some Python libraries
- Specific environment variables
- Application code

Instead of installing all of these things manually on a server, I can define them in a Docker image. Anyone who runs that image gets the same environment.

The important thing to understand is that a Docker **image** is like a blueprint, while a Docker **container** is a running instance of that image.

## Docker Architecture —

![Docker Architecture](https://miro.medium.com/v2/resize:fit:630/1*OrUs0r66hmeTkdzKnWENwQ.png)

**Docker Architecture**

So, users send requests to the Docker Engine via the CLI, GUI, or API. The request goes to the REST API, which forwards it to the Docker Daemon, which is the main brain of Docker.

The Docker Daemon handles the requests and manages containers and images using containerd. Containerd is a container runtime manager that uses runc to run the container.

The above picture clearly indicates that the Docker Daemon is the brain of Docker. If the Docker Daemon is killed or stops working for some reason, Docker is brain-dead.

## Containers vs Virtual Machines

![Containers vs Virtual Machines](https://miro.medium.com/v2/resize:fit:630/0*RTi9IK2AcSswyQ7e.png)

Containers and virtual machines are both technologies used to isolate applications and their dependencies, but they have some key differences:

1. **Resource Utilization:**

   Containers share the host operating system kernel, making them lighter and faster than VMs. VMs have a full-fledged OS and hypervisor, making them more resource-intensive.

2. **Portability:**

   Containers are portable and can run on any system, while VMs are less portable as they need a compatible hypervisor to run.

3. **Security:**

   VMs provide more security as each VM has its own OS and is isolated from the host and other VMs. Containers provide less isolation as they share the host operating system kernel.

4. **Management:**

   Containers are fast-moving and very lightweight in nature, so containers are easier to manage compared to VMs.

## Why are containers lightweight?

Containers are very lightweight in nature because they don’t have a full-fledged operating system. They share the host OS, kernel, and libraries to run an isolated application.

Docker containers are designed to be minimal, only including what is necessary for the application to run, further reducing their size.

## Docker Lifecycle

There are three important things:

1. `docker build` → builds Docker images from a Dockerfile
2. `docker run` → runs a container from a Docker image
3. `docker push` → pushes the container image to public/private registries to share the Docker image

![Docker Lifecycle](https://miro.medium.com/v2/resize:fit:630/0*HHMHork6hVFabTB2.png)

## Dockerfile

A Dockerfile is a file where you define the steps to build your Docker image.

### Docker Registries

A Docker registry is a centralized location where you can store, share, and manage your Docker images.

We can push our application images to the registry and pull them whenever we need to deploy the application in different environments.