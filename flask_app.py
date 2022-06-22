from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# 主页


@app.route('/')
def index():
    return render_template('index.html')


# api
@app.route('/api', methods=['POST'])
def api():
    name = request.form['name']
    length = request.form['length']
    width = request.form['width']
    height = request.form['height']
    # 处理逻辑
    # 这里可以对接模型进行计算，然后返回给前端，前端接收到结果可以进行展示
    # 处理逻辑
    msg = f'Name:{name} Length:{length} WIdth:{width} Height:{height}'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run(debug=False)
