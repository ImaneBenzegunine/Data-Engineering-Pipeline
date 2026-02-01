pip install airbyte
pip show airbyte
cd Airbyte
docker compose down -v
docker compose up -d

Best: Use the official abctl install (recommended)

Airbyte’s docs suggest installing and running Airbyte locally using their CLI tooling (abctl). This is the supported modern approach and replaces Docker Compose.
winget install Airbyte.abctl ## did not work
abctl local install

