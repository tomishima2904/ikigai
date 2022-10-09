# IKIGAI
ハッカソン用 by team B ロウリュ

# Environment
## docker-compose
- `docker-compose build` でコンテナを作成.
- `docker-compose up -d db` でデータベース側のコンテナを立ち上げる.
- `docker-compose up` でweb側のコンテナも立ち上げる. ターミナル上に`http://0.0.0.0:8000/`が出力されるのでそれをブラウザのアドレスバーに貼っつける.

## MySQL
- `docker-compose up -d db` でデータベース側のコンテナを立ち上げる.
- /etc/my.cnf の文字コードを`utf8mb4`に書き換える.
- `docker cp static/sql/hobby.sql $(docker-compose ps -q db):/tmp/hobby.sql` でローカルにあるsqlファイルをコンテナ側にコピーする.
- `docker-compose exec db bash` でデータベース側のコンテナに入る.
- `mysql < /tmp/hobby.sql` でコピーしたsqlファイルをmysqlに登録する.

