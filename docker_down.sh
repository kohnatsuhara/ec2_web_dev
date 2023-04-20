WORKDIR=$(cd "$(dirname "$0")" && pwd)
cd "$WORKDIR"

docker compose down
cd lightgbm
docker compose down