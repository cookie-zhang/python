# AI 对话系统

一个基于 FastAPI 和 Claude API 的现代化 AI 对话系统。

## 功能特点

- 🚀 使用 FastAPI 作为后端框架，性能优异
- 💬 支持多轮对话，保持上下文
- 🎨 现代化的 UI 设计，响应式布局
- 🔒 支持环境变量配置 API 密钥
- 📱 移动端友好

## 快速开始

### 1. 安装依赖

```bash
cd aiagent
python3.9 -m pip install -r requirements.txt
```

### 2. 配置 API 密钥

复制 `.env.example` 文件并重命名为 `.env`：

```bash
cp .env.example .env
```

然后编辑 `.env` 文件，填入你的 Claude API 密钥：

```
ANTHROPIC_API_KEY=your_claude_api_key_here
```

### 3. 启动服务

```bash
python3.9 app.py
```

或者使用 uvicorn 直接启动：

```bash
python3.9 -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 4. 访问应用

打开浏览器访问：http://localhost:8000

## 项目结构

```
aiagent/
├── app.py              # FastAPI 后端应用
├── requirements.txt    # Python 依赖包
├── .env.example       # 环境变量示例文件
├── .env               # 环境变量文件（需要自己创建）
├── static/            # 静态文件目录
│   └── index.html     # 前端页面
└── README.md          # 项目说明文档
```

## API 接口

### POST /api/chat

发送消息给 AI 并获取回复。

**请求体：**

```json
{
  "message": "你好",
  "conversation_history": [
    {
      "role": "user",
      "content": "之前的消息"
    },
    {
      "role": "assistant",
      "content": "之前的回复"
    }
  ]
}
```

**响应：**

```json
{
  "response": "你好！有什么可以帮助你的吗？",
  "success": true
}
```

### GET /api/health

健康检查接口，用于检查服务是否正常运行。

## 技术栈

- **后端**: FastAPI
- **前端**: HTML + CSS + JavaScript
- **AI 模型**: Claude 3.5 Sonnet (Anthropic)
- **服务器**: Uvicorn

## 注意事项

1. 请妥善保管你的 API 密钥，不要将 `.env` 文件提交到版本控制系统
2. 生产环境建议修改 CORS 配置，限制允许的域名
3. 可以根据需要调整 Claude 模型版本和参数

## 许可证

MIT License
