## Project Source

This project is based on [google-A2A](https://github.com/google/A2A).

License: This project is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0) - see the [LICENSE](https://github.com/google/A2A/blob/main/LICENSE) file for details.

### Development instructions
1. You must complete static/agent.json according to models/types.py:AgentCard
2. You must complete your agent function in service/custom_task_manager.py
3. If your api requires auth verification, you can complete the logic in utils/jwt_util.py:verify_jwt
4. You can also customize the api in the router

### Running instructions
1. pip3 install -r requirements.txt
2. python3 app.py
