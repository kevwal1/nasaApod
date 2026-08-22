# NASA Astronomy Picture of the Day

Flask application that displays NASA's Astronomy Picture of the Day at the
canonical appServer URL `/apod/`.

## Configuration

- `PORT` defaults to `8080`.
- `NASA_API_KEY` optionally supplies a NASA API key. If unset, the application
  uses NASA's rate-limited public `DEMO_KEY`; no credential is required.
- `NASA_APOD_API_URL` optionally overrides the APOD endpoint for testing.

Do not commit API credentials or `.env` files.

## Development and tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 app.py
```

The development routes are `/` and `/apod/`. Health checks are available at
`/healthz` and `/apod/healthz`.

## Container

```bash
docker build -t nasa-apod:dev .
docker run --rm -p 8080:8080 nasa-apod:dev
```

The production container runs Gunicorn as numeric UID `10001` on port `8080`.

## Kubernetes

Manifests under `k8s/` define an `apps`-namespace Deployment with two replicas,
a ClusterIP Service, and a standard Kubernetes Ingress for `/apod/` using the
`traefik` IngressClass. Private GHCR images use the existing `ghcr-pull` Secret.

Production image references must use an immutable Git SHA tag and registry
digest. The Ingress preserves the `/apod/` prefix; no strip middleware is used.
