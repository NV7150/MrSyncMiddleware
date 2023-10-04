# venvをアクティベート
. .\Middleware\venv\Scripts\Activate

# requirements.txtを生成
pip freeze | Out-File -Encoding utf8 .\Middleware\requirements.txt

# Dockerイメージをビルド
dokcer-compose build -f docker-compose-dev

Write-Output "Docker build complete!"
