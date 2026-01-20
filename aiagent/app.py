"""
AI 对话系统后端
使用 FastAPI 和 Claude API 实现
"""
# 修复 anthropic 0.18.1 与 httpx 0.28.1 版本兼容性问题
# 需要在导入 anthropic 之前修补
import os
# 临时移除代理相关的环境变量，避免 httpx 尝试初始化代理
_proxy_env_backup = {}
for key in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    if key in os.environ:
        _proxy_env_backup[key] = os.environ.pop(key)

import anthropic._base_client
import httpx

# 保存原始方法
_original_sync_init = anthropic._base_client.SyncHttpxClientWrapper.__init__
_original_httpx_init = httpx.Client.__init__

def _patched_sync_init(self, *args, **kwargs):
    # 移除所有代理相关参数
    kwargs.pop('proxies', None)
    kwargs.pop('proxy', None)
    # 确保 trust_env=False 以避免从环境变量读取代理
    if 'trust_env' not in kwargs:
        kwargs['trust_env'] = False
    return _original_sync_init(self, *args, **kwargs)

def _patched_httpx_init(self, *args, **kwargs):
    # 移除代理相关参数
    kwargs.pop('proxies', None)
    kwargs.pop('proxy', None)
    # 确保 trust_env=False 以避免从环境变量读取代理
    if 'trust_env' not in kwargs:
        kwargs['trust_env'] = False
    return _original_httpx_init(self, *args, **kwargs)

# 应用补丁
anthropic._base_client.SyncHttpxClientWrapper.__init__ = _patched_sync_init
httpx.Client.__init__ = _patched_httpx_init

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from anthropic import Anthropic

# 初始化 FastAPI 应用
app = FastAPI(title="AI 对话系统")

# 配置 CORS，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议设置为具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Claude API 密钥
ANTHROPIC_API_KEY = "sk-hggwRFoKBysZEWRIqNWloiLvqJPmdKext7iFMHKYm5Ii6Way"

# 初始化 Claude 客户端（补丁已处理版本兼容性问题）
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# 请求模型
class ChatRequest(BaseModel):
    message: str
    conversation_history: list = []  # 对话历史记录


# 响应模型
class ChatResponse(BaseModel):
    response: str
    success: bool


# API 路由必须在静态文件挂载之前定义
@app.get("/")
async def root():
    """重定向到前端页面"""
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    处理对话请求
    """
    try:
        # 构建消息历史
        messages = []
        
        # 添加历史对话
        for item in request.conversation_history:
            if item.get("role") == "user":
                messages.append({"role": "user", "content": item.get("content", "")})
            elif item.get("role") == "assistant":
                messages.append({"role": "assistant", "content": item.get("content", "")})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": request.message})
        
        # 调用 Claude API
        response = client.messages.create(
            model="claude-opus-4-5-20251101",  # 使用最新的 Claude 3.5 Sonnet 模型
            max_tokens=1024,
            messages=messages
        )
        
        # 提取回复内容
        assistant_message = response.content[0].text
        
        return ChatResponse(
            response=assistant_message,
            success=True
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI 服务错误: {str(e)}"
        )


@app.options("/api/chat")
async def chat_options():
    """处理 CORS 预检请求"""
    return {"status": "ok"}


@app.get("/api/health")
async def health():
    """健康检查接口"""
    return {"status": "ok", "message": "服务运行正常"}


# 挂载静态文件目录（必须在 API 路由之后）
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
