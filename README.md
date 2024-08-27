
 カレンダーアプリ

このプロジェクトは、Djangoを使用して作成されたToDoリストとカレンダー機能を統合したアプリケーションです。ユーザーはタスクを追加し、カレンダーに表示して管理することができます。

## 目次

- [機能](#機能)
- [使い方](#使い方)
- [必要要件](#必要要件)
- [インストール手順](#インストール手順)
<!-- - [ライセンス](#ライセンス) -->

## 機能

- [ ] タスクの追加、編集、削除
- [ ] カレンダー表示
- [ ] タスクのカレンダー表示
- [ ] タスクの完了状態管理

## 使い方

### 必要要件

- Python 3.8+
- 開発環境はWindows11
- その他の依存関係は `requirements.txt` に記載

### インストール手順

1. リポジトリをクローンします。

   ```bash
   git clone https://github.com/Shota-Kizaki/ToDo_Calendar.git
   ```

2. 仮想環境を整えます。

   ```bash
   cd ToDo_Calendar
   python -m venv .venv
   .venv\Scripts\activate 
   pip install -r requirements.txt
   ```

3. Djangoの準備と開始

   ```bash
   python manage.py makemigrations top
   python manage.py migrate
   python manage.py runserver
   ```

