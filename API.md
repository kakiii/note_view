# API接口描述

## User部分

#### 用户的Login

使用`/auth/login`，使用**POST**操作，发送的JSON文件包含：

```json
{
    "username":...,  //用户名
    "password":...   //密码
}
```

返回的json以status进行标记，分别有：
1. status:200 用户存在，且密码匹配，允许登陆
2. status:201 用户存在，但密码不匹配，不允许登陆
3. status:202 用户不存在，推荐用户前往Register页面

#### 用户的Register

使用`/auth/register`，使用**POST**操作，发送的JSON文件包含了：

```json
{
    "username":...,  //用户名
    "password":...   //密码
}
```
后端会对收到的用户名进行验证，确认用户名是否已被注册过。

返回的json以status进行标记，分别有：
1. status:200 用户名尚未被注册过，注册成功，建议用户前往登陆界面。
2. status:201 用户名已经被注册过，注册失败。

#### 对用户数量的统计

使用`/auth/check`，使用**GET**操作，无需发送body内容。

返回的json内容为：

```json
{
    "user_number":...,//用户的总数
}
```

#### 获取所有用户的名称

使用`/auth/getAllUser`，使用**GET**操作，无需发送body内容。

返回的json内容为：

```json
["user1", "user2", "user3", ...] //包含了所有用户名的数组
```

#### 依据正则，利用部分用户名寻找用户

使用`/auth/findUser`,使用**POST**操作，发送已知的用户名片段。

> 等待加入对多个匹配对象同时返回的功能支持

返回的json内容为：

```json
{
    "username":... //完整的用户名
}
```

#### 管理员BAN掉指定的用户（需指定完整的用户名）

使用`/auth/banUser`，使用**PUT**操作。
如果该用户之前没有被BAN，则在用户的数据库中加入`ban:100`的条目。

返回的内容有两种：
1. `"delete":"done"`  用户被BAN的操作已成功
2. `"delete":"undone"`  用户已经被BAN，操作失败


#### 管理员获取所有被BAN用户的清单

使用`/auth/banUserList`，使用**GET**操作。

返回的json内容为：

```json
["user1", "user2", ...] //一被BAN用户的用户名组成的数组
```

## Disucssion部分

#### 获取当前discussion总数

使用`/content/discussion/`接口，使用**GET**操作，没有BODY参数。

返回的内容为：
```json
{
    "discussion_size":... //讨论总数
}
```

#### 用户添加自己的discussion

使用`/content/discussion/`接口，使用**POST**操作。

**该操作和上面的获取总数使用同一个URL的接口，只有HTTP的操作不同**

需要发送BODY内容，类似：

```json
{
    "author":..., //discussion的作者
    "content":... //discussion的具体内容
}
```

**该API目前暂时不返回有意义的内容**

#### 依据特定的ID获取Discussion的内容

使用`/content/discussion/<id>`接口，使用**GET**操作。

`<id>`内的内容即讨论的序号。

如果找到了对应的discussion内容，返回：

```json
{
    "id":...,//discussion的id
    "content":...,//discussion的具体内容
    "author":...//discussion的作者
}
```

如果**没有找到**对应的discussion内容，则返回：
```json
{
    "id":...,
    "content":"NOT FOUND"
}
```