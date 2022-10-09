# IKIGAI
ハッカソン用 by team B ロウリュ

# Environment
## docker-compose
- `docker-compose build` でコンテナを作成.
- `docker-compose up -d db` でデータベース側のコンテナを立ち上げる.
- `docker-compose up` でweb側のコンテナも立ち上げる. ターミナル上に`http://0.0.0.0:8000/`が出力されるのでそれをブラウザのアドレスバーに貼っつける.

## MySQL
- `docker-compose up -d db` でデータベース側のコンテナを立ち上げる.
- `docker cp my.cnf ikigai_db_1:/etc/my.cnf ` で文字コードを`utf8mb4`に書き換える. 詳細は[こちら](https://qiita.com/decoch/items/bfa125ae45c16811536a). (本当はdocker-compose.ymlで解決したかった)
- `docker cp static/sql/hobby.sql $(docker-compose ps -q db):/tmp/hobby.sql` でローカルにあるsqlファイルをコンテナ側にコピーする.
- `docker-compose exec db bash` でデータベース側のコンテナに入る.
- `mysql < /tmp/hobby.sql` でコピーしたsqlファイルをmysqlに登録する.

