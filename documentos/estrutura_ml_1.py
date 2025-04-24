# prompt: consegue listar a estrutura de modelos de machine learning?
# Dentro de 3 estruturas que me interessam, são elas:
# supervised_learning
# unsupervised_learning
# reinforcement_learning

def listar_modelos_machine_learning():
  """Lista a estrutura de modelos de Machine Learning em 3 categorias."""

  print("Estruturas de Modelos de Machine Learning:")
  print("\n1. Aprendizado Supervisionado (Supervised Learning):")
  print("   - Regressão Linear:")
  print("     - Previsão de valores contínuos (e.g., preço de uma casa).")
  print("   - Regressão Logística:")
  print("     - Classificação binária (e.g., spam ou não spam).")
  print("   - Máquinas de Vetores de Suporte (SVM):")
  print("     - Classificação e regressão, busca por hiperplano que separa classes.")
  print("   - Árvores de Decisão:")
  print("     - Classificação e regressão, regras de decisão baseadas em atributos.")
  print("   - Florestas Aleatórias:")
  print("     - Combinação de várias árvores de decisão para melhorar a precisão.")
  print("   - Redes Neurais Artificiais (RNAs):")
  print("     - Modelos inspirados em cérebros biológicos, capazes de aprender padrões complexos.")
  print("   - K-Nearest Neighbors (KNN):")
  print("     - Classificação e regressão, classificação com base nos vizinhos mais próximos.")
  print("   - Naive Bayes:")
  print("     - Classificação probabilística baseada no teorema de Bayes.")

  print("\n2. Aprendizado Não Supervisionado (Unsupervised Learning):")
  print("   - Agrupamento (Clustering):")
  print("     - K-Means:")
  print("       - Agrupa dados em clusters com base na distância entre os pontos.")
  print("     - DBSCAN:")
  print("       - Agrupa dados com base em densidade, identificando clusters com alta densidade.")
  print("     - Hierarchical Clustering:")
  print("       - Cria uma hierarquia de clusters, formando uma árvore de clusters.")
  print("   - Redução de Dimensionalidade:")
  print("     - PCA (Principal Component Analysis):")
  print("       - Reduz a dimensionalidade dos dados, mantendo a maior parte da variância.")
  print("     - t-SNE (t-distributed Stochastic Neighbor Embedding):")
  print("       - Reduz a dimensionalidade e preserva a estrutura local dos dados.")
  print("   - Associação:")
  print("     - Apriori:")
  print("       - Descobre regras de associação entre itens (e.g., pessoas que compram X também compram Y).")

  print("\n3. Aprendizado por Reforço (Reinforcement Learning):")
  print("   - Q-learning:")
  print("     - Agente aprende uma política para maximizar a recompensa em um ambiente.")
  print("   - Deep Q-Networks (DQN):")
  print("     - Combina Q-learning com redes neurais profundas para aprender políticas complexas.")
  print("   - SARSA:")
  print("     - Algoritmo de aprendizado por reforço on-policy.")
  print("   - Actor-Critic:")
  print("     - Algoritmo que utiliza duas redes neurais, uma para a política (actor) e outra para a função de valor (critic).")

listar_modelos_machine_learning()
