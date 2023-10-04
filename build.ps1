# venvをアクティベート
. .\Middleware\venv\Scripts\Activate

# requirements.txtを生成
pip freeze | Out-File -Encoding utf8 .\Middleware\requirements.txt

# venvをディアクティベート
deactivate

# Dockerイメージをビルド
docker build -t mr-middleware-ws .\Middleware\

Write-Output "Docker build complete!"
