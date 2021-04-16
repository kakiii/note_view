# COMP 208 作业仓库

## UPDATE

进行开发时，需要同时开启两个服务器。
一个用于`app.py`文件，端口 5000；
一个用于`npm run serve`，端口不限。

*本地开发验证成功的组件，需要添加特定的`if-else`语句对开发环境和部署环境进行区分*

具体实现请看`components`文件夹下的Login和Register。

## 部署方法

### 方法一

1. 使用`npm install`安装所有的依赖
2. 使用`npm run serve`运行开发服务器
3. 使用`npm run build`运行打包服务

## 方法二

需要先安装 yarn，以`npm install --global yarn`

1. 使用`yarn install`安装依赖
2. 使用`yarn serve`运行开发服务器
3. 使用`yarn build`运行打包服务

### Progress

**NEW: 实现用户的个人界面**
- [ ] Register System 0.2
- [ ] Login System 0.2
- [ ] Gravataar 0.2
- [ ] Note Editing 0.1
- [ ] Note Exportation 0.0.1
- [ ] Discussion Board 0.
- [ ] Code Editor 0.0.1
- [ ] Admin Page 0.1
- [ ] Home Page UI Design 0.0.2
- [ ] Search Engine 0.0.2


### Note

要实现开发时和部署时不同的配置，需要使用if-else语句指定`process.env.NODE_ENV`为"development"或"production"。