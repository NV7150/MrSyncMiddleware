# venvをアクティベート
. .\Middleware\venv\Scripts\Activate

# requirements.txtを生成
pip freeze | Out-File -Encoding utf8 .\Middleware\requirements.txt

# Dockerイメージをビルド
docker-compose -f docker-compose-dev.yaml build

Write-Output "Docker build complete!"
