pip install airbyte
pip show airbyte
cd Airbyte
docker compose down -v
docker compose up -d

Best: Use the official abctl install (recommended)
Airbyte’s docs suggest installing and running Airbyte locally using their CLI tooling (abctl). This is the supported modern approach and replaces Docker Compose.
winget install Airbyte.abctl ## did not work
abctl local install
Airbyte — Local Dev (compose)

- **What this folder does:** spins up Airbyte server, webapp, and a Postgres DB for local testing.

Quick start (compose)

```powershell
cd Airbyte
docker compose down -v
docker compose up -d
```

- Web UI: http://localhost:8001 (webapp) or API: http://localhost:8000
- Local files volume: `../kaggle/data/row` is mounted into the server at `/local-files`.

Notes & troubleshooting

- The repo includes docker-compose configuration; make sure you run compose from the `Airbyte/` folder or pass `-f Airbyte/docker-compose.yml` from repo root.
- If the server exits with Micronaut placeholder errors (e.g. `${WORKSPACE_ROOT}` or `${DATABASE_URL}`), the compose file needs the matching environment variables and volumes — that is already handled in the repo but may have been edited.
- If you prefer the official CLI workflow, `abctl` is recommended by Airbyte upstream (`abctl local install`), but Docker Compose works for development.

Want me to start the Airbyte services and confirm ports are reachable? I can do that now.
pip install airbyte
pip show airbyte
cd Airbyte
docker compose down -v
docker compose up -d

Best: Use the official abctl install (recommended)

Airbyte’s docs suggest installing and running Airbyte locally using their CLI tooling (abctl). This is the supported modern approach and replaces Docker Compose.
winget install Airbyte.abctl ## did not work
abctl local install

