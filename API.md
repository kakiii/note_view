# API接口描述

## User部分

#### 用户的Login

使用`/auth/login`，使用**POST**操作，发送的JSON文件包含：

```json
{
    "username":...,
    "password":...
}
```