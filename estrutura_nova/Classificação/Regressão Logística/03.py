#import pandas
import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("diabetes.csv", header=None, names=col_names)

print(pima.head())
'''
Seleção de recurso
Aqui, você precisa dividir as colunas fornecidas em dois tipos de variáveis: 
dependente (ou variável-alvo) e independente (ou variáveis de recursos).
'''
#split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] # Features
y = pima.label # Target variable

'''
Divisão de dados
Para entender o desempenho do modelo, dividir o conjunto de dados em um conjunto de treinamento 
e um conjunto de teste é uma boa estratégia.
Vamos dividir o conjunto de dados usando a função train_test_split(). 
Você precisa passar 3 parâmetros: recursos, alvo e tamanho do conjunto de teste. 
Além disso, é possível usar random_state para selecionar registros aleatoriamente.
'''
# split X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

'''
Desenvolvimento e previsão de modelos
Primeiro, importe o módulo Logistic Regression e crie um objeto classificador de Logistic Regression 
usando a função LogisticRegression() com random_state para reprodutibilidade.
Em seguida, ajuste seu modelo no conjunto de treinamento usando fit() e 
faça a previsão no conjunto de teste usando predict(). 
'''
# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16)

# fit the model with data
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

'''
Avaliação do modelo usando a matriz de confusão
Uma matriz de confusão é uma tabela usada para avaliar o desempenho de um modelo de classificação. 
Você também pode visualizar o desempenho de um algoritmo. 
O fundamental de uma matriz de confusão é o número de previsões corretas e incorretas somadas por classe.
'''