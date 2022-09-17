

#数据集 iris
from sklearn.datasets import fetch_20newsgroups
#划分数据
from sklearn.model_selection import train_test_split
#文本特征抽取
from sklearn.feature_extraction.text import TfidfVectorizer
#预估期
from sklearn.naive_bayes import MultinomialNB


def nb_news():
    """
    用朴素贝叶斯算法对新闻进行分类
    """
    #1获取数据
    news = fetch_20newsgroups(subset="all")
    #2划分数据集
    # 训练集的特征值x_train 测试集的特征值x_test 训练集的目标值y_train 测试集的目标值y_test
    x_train,x_test,y_train,y_test=train_test_split(news.data,news.target)
    #3特征工程 标准化  文本特征抽取 tfidf
    tfidf_vectorizer = TfidfVectorizer()

    # 训练集标准化
    x_train=tfidf_vectorizer.fit_transform(x_train)
    #测试集标准化 需要用训练集的标准差 平均值等
    x_test=tfidf_vectorizer.transform(x_test)
    #4朴素贝叶斯算法预估器
    nb = MultinomialNB()
    nb.fit(x_train,y_train)
    #5模型评估
    #方法1 直接比对真实值和预测值
    predict = nb.predict(x_test)
    print("预测的结果\n",predict)
    print("比对正确结果和预测值\n",y_test == predict)
    #方法2 计算准确率
    score = nb.score(x_test, y_test)
    print("准确率:\n",score)


if __name__ == "__main__":
    nb_news()
