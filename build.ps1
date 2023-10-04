# venvをアクティベート
. .\venv\Scripts\Activate

# requirements.txtを生成
pip freeze | Out-File -Encoding utf8 requirements.txt

# venvをディアクティベート
deactivate

# Dockerイメージをビルド
docker build -t mr-middleware-ws .

Write-Output "Docker build complete!"
