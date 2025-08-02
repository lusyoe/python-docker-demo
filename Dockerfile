# 使用官方镜像作为基础镜像
# FROM python:3.11-slim
FROM registry.cn-hangzhou.aliyuncs.com/lusyoe/python:3.11-slim

# 设置工作目录
WORKDIR /app

# 拷贝当前目录内容到容器中
COPY . .

# 暴露端口
EXPOSE 8000

# 设置容器启动命令
CMD ["python", "main.py"]