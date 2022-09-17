

#数据集 iris
from sklearn.datasets import load_iris
#划分数据
from sklearn.model_selection import train_test_split
#特征值标准化
from sklearn.preprocessing import StandardScaler
#预估期
from sklearn.tree import DecisionTreeClassifier

def decision_iris():
    """
    用决策树算法对鸢尾花进行分类
    """
    #1获取数据
    iris = load_iris()
    #2划分数据集
    # 训练集的特征值x_train 测试集的特征值x_test 训练集的目标值y_train 测试集的目标值y_test
    x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,random_state=6)
    #3特征工程 标准化
    scaler = StandardScaler()
    # 训练集标准化
    x_train=scaler.fit_transform(x_train)
    #测试集标准化 需要用训练集的标准差 平均值等
    x_test=scaler.transform(x_test)
    #4KNN算法预估器
    classifier = DecisionTreeClassifier(criterion="entropy")
    classifier.fit(x_train,y_train)
    #5模型评估
    #方法1 直接比对真实值和预测值
    predict = classifier.predict(x_test)
    print("预测的结果\n",predict)
    print("比对正确结果和预测值\n",y_test == predict)
    #方法2 计算准确率
    score = classifier.score(x_test, y_test)
    print("准确率:\n",score)

if __name__ == "__main__":
    decision_iris()
