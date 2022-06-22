from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# 主页


@app.route('/')
def index():
    return render_template('index.html')

# api


@app.route('/api', methods=['POST'])
def api():
    length = request.form['length']
    width = request.form['width']
    height = request.form['height']
    # 处理逻辑
    # 这里可以对接模型进行计算，然后返回给前端，前端接收到结果可以进行展示
    # 处理逻辑
    msg = f'长:{length} 宽:{width} 高:{height}'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run(debug=False)
