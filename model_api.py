import http.server
import socketserver
import subprocess
import os
import json

# 端口号
PORT = 8000

# 环境变量设置
os.environ['ADSP_LIBRARY_PATH'] = "./libs/arm64-v8a:./obj/local/arm64-v8a"
os.environ['LD_LIBRARY_PATH'] = "./libs/arm64-v8a:" + os.environ.get('LD_LIBRARY_PATH', '') + ":./obj/local/arm64-v8a"

# 配置文件路径和其他参数
CONFIG_FILE = "config_minicpm_2b.yaml"
PREFORMATTER = "MinicpmNoInput"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # 获取请求内容长度
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # 解析收到的JSON数据
        data = json.loads(post_data)
        messages = data.get('messages', [])
        MAX_RESPONSE = str(data['max_out_len'])
        responses = []

        for message in messages:
            content = message['content']
            
            # 将每个 content 写入 prompt 文件
            with open("prompt0.txt", "w") as f:
                f.write(content)
            
            print(MAX_RESPONSE)
            # 运行模型脚本
            result = subprocess.run([
                "./libs/arm64-v8a/main", CONFIG_FILE,
                "-i", "prompt0.txt",
                "-m", MAX_RESPONSE,
                "--preformatter", PREFORMATTER
            ], capture_output=True, text=True)
            # print(result)
            # 收集结果
            
            output = result.stdout
            print(output)
            print("处理结束")
            if output.endswith('</s>'):
                output = output.rsplit('</s>', 1)[0]
            if output.startswith("Reading prompt from file:"):
                output = output.split('\n', 1)[-1]
            output = output.lstrip()
            print(output)
            responses.append({"content": output})
        
        # 返回结果
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        
        # 将结果转化为JSON格式并发送回客户端
        self.wfile.write(json.dumps({"messages": responses}, ensure_ascii=False).encode('utf-8'))

# 启动服务器
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
