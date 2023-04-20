WORKDIR=$(cd "$(dirname "$0")" && pwd)
cd "$WORKDIR"

docker compose up -d
cd lightgbm
docker compose up -d