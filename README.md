# Vue.js と Django Rest Framework によるSPAのテスト

本のタイトルと値段を登録、更新するホームページを作成。

Vue.jsはCDN版を使用する。
SPAは、Cookie認証によるSPAとする。

```javascript
cd ~/PycharmProjects/
git clone https://github.com/Washington-Ksea/book-register-Vue-DRF.git

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

./manage.py runserver
```


djangoに関しては、以下のバージョンを使用する。

```javascript
Django==2.2
djangorestframework==3.9.2
```

## 参考

　akiyoki : 現場で使えるDRFの薄い本