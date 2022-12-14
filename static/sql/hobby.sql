CREATE DATABASE IF NOT EXISTS ikigai;
USE ikigai;
GRANT ALL ON ikigai.* to mysql;  /* docker-compose を使わない場合この行を消す */
DROP TABLE IF EXISTS hobbies;
CREATE TABLE hobbies(
    hobby varchar(30) not null,
    outdoor integer default 0,
    skill integer default 0,
    `group` integer default 0,  /* group は予約語であるためバッククォートで囲む */
    cost integer default 0
);
INSERT INTO hobbies VALUES
('テニス', 1, 1, 1, 1), /*
('草野球', 1, 1, 1, 1),
('サバイバルゲーム', 1, 1, 1, 1),
*/

('バンド活動', 0, 1, 1, 1), /*
('ユーチューブ活動', 0, 1, 1, 1), */

('キャンプ', 1, 0, 1, 1), /*
('グランピング', 1, 0, 1, 1),
('ラフティング', 1, 0, 1, 1),

('乗馬', 1, 1, 0, 1),
('ゴルフ', 1, 1, 0, 1), */
('カメラ', 1, 1, 0, 1),

('バスケットボール', 1, 1, 1, 0), /*
('バドミントン', 1, 1, 1, 0),
('バレーボール', 1, 1, 1, 0),
('フットサル', 1, 1, 1, 0), */

('該当なし＊', 0, 0, 1, 1),

('ピアノ', 0, 1, 0, 1),

('該当なし＊＊', 0, 1, 1, 0),

('劇団四季鑑賞', 1, 0, 0, 1),

('カフェ巡り', 1, 0, 1, 0),

('スケートボード', 1, 1, 0, 0), /*
('水泳', 1, 1, 0, 0),

('猫飼育', 0, 0, 0, 1), */
('競馬', 0, 0, 0, 1),

('オンラインゲーム', 0, 0, 1, 0),

('筋トレ', 0, 1, 0, 0), /*
('プログラミング', 0, 1, 0, 0),
('料理', 0, 1, 0, 0),

('ランニング', 1, 0, 0, 0),
('ジョギング', 1, 0, 0, 0),
('散歩', 1, 0, 0, 0),
('サイクリング', 1, 0, 0, 0),
('縄跳び', 1, 0, 0, 0), */
('昆虫採集', 1, 0, 0, 0), /*

('映画鑑賞', 0, 0, 0, 0),
('お香', 0, 0, 0, 0),
('パズル', 0, 0, 0, 0),
('ユーチューブ鑑賞', 0, 0, 0, 0), */
('読書', 0, 0, 0, 0);

