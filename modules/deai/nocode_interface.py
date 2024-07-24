# nocode_interface.py
from flask import Flask, request, jsonify
from ai_design_generator import AIDesignGenerator

app = Flask(__name__)
generator = AIDesignGenerator()

@app.route('/generate_design', methods=['POST'])
def generate_design():
    params = request.json
    design = generator.generate_design(params)
    return jsonify({'design': design.tolist()})

@app.route('/components', methods=['GET'])
def get_components():
    # 这里应该返回可用组件的列表
    return jsonify({
        'components': [
            {'id': 'button', 'name': 'Button'},
            {'id': 'input', 'name': 'Input Field'},
            {'id': 'dropdown', 'name': 'Dropdown Menu'}
        ]
    })

@app.route('/create_app', methods=['POST'])
def create_app():
    app_design = request.json
    # 这里应该实现应用创建逻辑
    # 现在只是返回一个模拟的响应
    return jsonify({'app_id': 'app_123', 'status': 'created'})

if __name__ == '__main__':
    app.run(debug=True)
