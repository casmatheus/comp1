def questao4(nome):
  try:
    arquivo = open(nome, 'r')
  except FileNotFoundError:
    print("Arquivo nao encontrado")
    return -1

  maquinas = {'M1': [0, 0.0], 'M2': [0, 0.0], 'M3': [0, 0.0] }  
  n_linha = 0
  for linha in arquivo:
    horarios = linha.split(',')
    n_maquina = 0
    for maquina in maquinas:
      try:
        horas = float(horarios[n_maquina])
      except ValueError:
        print(f"Linha {n_linha + 1}: tempo indisponivel para a maquina {n_maquina + 1}.")
        n_maquina += 1
        continue
      maquinas[maquina][0] += 1
      maquinas[maquina][1] += horas
      n_maquina += 1
    n_linha += 1
  arquivo.close()

  for maquina in maquinas:
    maquinas[maquina][1] /= (maquinas[maquina][0] * 24) / 100
    maquinas[maquina] = tuple(maquinas[maquina])

  return maquinas

