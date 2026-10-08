# devops-cicd-terraform-aws

![CI](https://github.com/hadjarkamelia/devops-cicd-terraform-aws/actions/workflows/ci.yml/badge.svg)

Projet DevOps : une petite API Python (FastAPI) avec un pipeline CI/CD automatisé qui teste le code, construit une image Docker, la scanne pour détecter les failles de sécurité, puis la publie sur GitHub Container Registry.

## Stack

- **Python / FastAPI** : API avec une route `/health`
- **Pytest et Flake8** : tests automatiques et vérification du style
- **Docker** : conteneurisation de l'application
- **GitHub Actions** : pipeline CI/CD
- **Trivy** : scan de sécurité de l'image
- **GitHub Container Registry** : stockage de l'image

## Pipeline

À chaque push sur `main`, le pipeline :

1. Installe les dépendances
2. Vérifie le style du code (flake8)
3. Lance les tests (pytest)
4. Construit l'image Docker
5. Scanne l'image avec Trivy
6. Publie l'image sur GHCR

![Pipeline](pipeline.png)

## Lancer l'API en local

```bash
docker run -p 8000:8000 ghcr.io/hadjarkamelia/health-api:latest
```

Puis ouvrir http://localhost:8000/health

## Prochaines étapes

- Infrastructure as Code avec Terraform
- Déploiement sur AWS
- Monitoring avec Prometheus et Grafana (voir mon repo `monitoring-infrastructure`)
