#!/bin/bash
# AI 对话系统启动脚本 - 使用 Python 3.9

cd "$(dirname "$0")"

# 检查 .env 文件
if [ ! -f ".env" ]; then
    echo "❌ 错误: 未找到 .env 文件"
    echo "请创建 .env 文件并添加以下内容:"
    echo "ANTHROPIC_API_KEY=你的_claude_api_密钥"
    exit 1
fi

# 启动应用
echo "🚀 启动 AI 对话系统..."
echo "📝 使用 Python 3.9"
echo "🌐 访问地址: http://localhost:8000"
echo "按 Ctrl+C 停止服务"
echo ""

python3.9 app.py
