# nasaApod Codex Instructions

## Project

`nasaApod` is a Python web application for NASA Astronomy Picture of the Day.

The project normally lives at:

    /home/kevwal/appLearning/nasaApod

Before modifying it, inspect:

- `app.py`
- `requirements.txt`
- `Dockerfile`
- `templates/`
- `k8s/`
- current Git state

This repository currently lacks a README. Do not infer undocumented operational
details when they can be verified from the code or deployment files.

## Runtime

The Kubernetes/container application listens on:

    8081

The Kubernetes deployment and service currently use port:

    8081

Do not change this port casually.

## Kubernetes

This application is intended to run on the home Kubernetes cluster.

Deployment manifests live under:

    k8s/

The application is exposed through appServer nginx at:

    /apod/

Do not assume the Kubernetes node address or externally exposed NodePort is
permanent. Inspect:

    /home/kevwal/appLearning/appserver-config/nginx/sites-available/app-portal

before changing external routing.

Before applying Kubernetes changes:

1. Inspect the active kubectl context.
2. Review the manifests.
3. Prefer `kubectl diff`.
4. Do not expose Kubernetes secrets in Git.

## Shared UI

Where appropriate, use:

    /shared-style/portal-theme.css

Source:

    /home/kevwal/appLearning/app-style

## API Credentials

NASA/API credentials must be provided through runtime configuration or secrets.

Never hard-code or commit API credentials.

## Git

Preserve the existing `main` branch convention.

Before committing, inspect status/diff and verify container and Kubernetes
configuration if changed.

Do not push or merge unless explicitly requested.
