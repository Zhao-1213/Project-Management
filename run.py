# run.py
from app import create_app
# B3修改了这里
app = create_app()
# 修改主函数入口
if __name__ == '__main__':
    app.run(debug=True)

# 这是C4自己的部分
# C44444444444444