### 项目来源说明

本项目基于 [google-A2A](https://github.com/google/A2A) 开发。

许可证：本项目采用 [Apache 许可证 2.0](https://opensource.org/licenses/Apache-2.0) - 详细内容请查看 [LICENSE](https://github.com/google/A2A/blob/main/LICENSE) 文件。

### 开发说明
1. 必须根据 models/types.py:AgentCard 完善 static/agent.json
2. 必须在 service/custom_task_manager.py 中完善你的 agent 功能
3. 如果你的 api 需要 auth 验证，可以在 utils/jwt_util.py:verify_jwt 中完善逻辑
4. 另外你还可以在 router 中自定义 api

### 运行说明
1. pip3 install -r requirements.txt
2. python3 app.py
