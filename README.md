# Python Docker 演示项目

这是一个简单的Python HTTP服务器演示项目，展示了如何使用Docker容器化Python应用程序。

博客文章介绍：https://blog.lusyoe.com/article/docker-getting-started-first-container

## 项目描述

该项目包含一个基础的HTTP服务器，运行在8000端口上，当访问时会返回"Hello, World"消息。项目使用Docker进行容器化部署，便于在不同环境中运行。

## 项目结构

```
python-docker-demo/
├── Dockerfile      # Docker容器配置文件
├── main.py         # Python HTTP服务器主程序
└── README.md       # 项目说明文档
```

## 功能特性

- 基于Python内置的HTTP服务器
- 监听8000端口
- 返回简单的"Hello, World"响应
- 使用Docker容器化部署
- 支持跨平台运行

## 环境要求

- Docker Desktop 或 Docker Engine
- 网络连接（用于拉取Docker镜像）

## 快速开始

### 1. 构建Docker镜像

```bash
docker build -t python-docker-demo .
```

### 2. 运行容器

```bash
docker run -p 8000:8000 python-docker-demo
```

### 3. 访问应用

打开浏览器或使用curl命令访问：

```bash
curl http://localhost:8000
```

或者在浏览器中访问：`http://localhost:8000`

你应该看到输出：`Hello, World`

## 详细说明

### Dockerfile 分析

- 使用阿里云镜像源的Python 3.11 slim版本作为基础镜像
- 设置工作目录为 `/app`
- 将当前目录的所有文件复制到容器中
- 暴露8000端口
- 设置容器启动命令为运行 `main.py`

### main.py 分析

- 使用Python内置的 `http.server` 模块
- 创建自定义的 `HelloHandler` 类处理HTTP请求
- 监听所有网络接口的8000端口
- 对所有GET请求返回"Hello, World"文本

## 开发说明

### 本地开发

如果你想在本地运行而不使用Docker：

```bash
python main.py
```

### 修改代码

1. 修改 `main.py` 文件
2. 重新构建Docker镜像：`docker build -t python-docker-demo .`
3. 重新运行容器：`docker run -p 8000:8000 python-docker-demo`

### 自定义端口

如果你想使用不同的端口，可以修改Dockerfile中的EXPOSE指令和main.py中的端口号，然后重新构建镜像。

## 故障排除

### 端口被占用

如果8000端口被占用，可以使用其他端口：

```bash
docker run -p 8080:8000 python-docker-demo
```

然后访问 `http://localhost:8080`

### 容器无法启动

检查Docker是否正在运行：

```bash
docker --version
docker ps
```

### 镜像构建失败

确保在项目根目录下运行构建命令，并且Dockerfile存在。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

本项目采用MIT许可证。 