# recommendation_engine.py
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

app = Flask(__name__)

# 假设我们有一个包含项目数据的 CSV 文件
df = pd.read_csv('items.csv')

# 创建 TF-IDF 向量
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.json['preferences']
    user_vector = tfidf.transform([user_preferences])
    
    # 计算余弦相似度
    cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # 获取前5个推荐
    related_product_indices = cosine_similarities.argsort()[-5:][::-1]
    recommendations = df.iloc[related_product_indices]
    
    return jsonify(recommendations.to_dict('records'))

if __name__ == '__main__':
    app.run(port=5000)
