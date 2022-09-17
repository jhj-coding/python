# 我不知道我在哪 我知道5个人分别在哪个区 我看我和谁最近 我就在哪个区
# 根据邻居推断我的类别


#数据集 iris
from sklearn.datasets import load_iris
#划分数据
from sklearn.model_selection import train_test_split
#特征值标准化
from sklearn.preprocessing import StandardScaler
#预估期
from sklearn.neighbors import KNeighborsClassifier
#交叉验证与网格搜索
from sklearn.model_selection import GridSearchCV

def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类 添加网格搜索和交叉验证
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
    classifier = KNeighborsClassifier()
    #加入网格搜索与交叉验证
    #参数准备
    param_dict={"n_neighbors":[1,3,5,7,9,11]}

    #cv代表几折交叉验证
    classifier=GridSearchCV(classifier,param_grid=param_dict,cv=10)

    classifier.fit(x_train,y_train)
    #5模型评估
    #方法1 直接比对真实值和预测值
    predict = classifier.predict(x_test)
    print("预测的结果\n",predict)
    print("比对正确结果和预测值\n",y_test == predict)
    #方法2 计算准确率
    score = classifier.score(x_test, y_test)
    print("准确率:\n",score)

    print("最佳参数：\n",classifier.best_params_)
    print("最佳结果：\n",classifier.best_score_)
    print("最佳估计器：\n",classifier.best_estimator_)
    print("交叉验证结果：\n",classifier.cv_results_)


if __name__ == "__main__":
    knn_iris_gscv()
