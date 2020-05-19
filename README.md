# 这是一个给爱人搭的表白+生日祝福网站


其实大部分素材也是网上找的，我把它们集成到了`Django`，并添加了自己的模块：


1. `hpBirthDApp`：包含入口登录(login)页面、生日祝福(cake)页面、记忆(memory)页面；

2. `index`：爱心树表白墙页面；

3. `player`：视频播放页面，可添加你自己录制的视频。


## 使用方法：
修改`static/birth/js/login.js`里的登录密码
修改`templates/Memories.html`里的你自己想表达的话
修改`media/img与video`里的照片、视频换成你自己的


配置Nginx与wsgi后可以部署上线
后台运行：
```python
python manage.py runserver 
```
