from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
# sklearn 数据集获取
def datasets_demo():
    iris=load_iris()
    print("鸢尾花数据集:\n",iris)
    print("查看数据集描述:\n",iris["DESCR"])
    print("查看特征值名字:\n", iris.feature_names)

     # 数据集划分
    x_train,x_text,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)

    return None


#字典特征抽取
def dict_demo():

    data=[
        {'city':'北京','temperature':100},
        {'city': '上海', 'temperature': 60},
        {'city': '深圳', 'temperature': 30}
    ]
    #实例化转换器类
    vectorizer = DictVectorizer(sparse=False)
    #调用转换
    transform = vectorizer.fit_transform(data)
    print(transform)
    #特征名称
    print(vectorizer.feature_names_)

# 文本特征提取
# def

if __name__ == "__main__":
    # 数据集使用
    # datasets_demo()
    #字典特征抽取
    dict_demo()