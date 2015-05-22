import sys

def getJModels():
  data = {}
  with open('./data/jmodeltest2_output/aP6.fas.jmodeltest.console') as f:
    lines = f.readlines()
    models = []
    for i, line in enumerate(lines):
      tokens = line.split(' ');
      tokens = filter(lambda x: x.strip() != '', tokens)
      if (len(tokens) > 0 and tokens[0] == 'Model' and tokens[1] == '-lnL'):
        data['columns'] = tokens;
        modelStrArr = lines[i+2 : i+26];
        for modelStr in modelStrArr:
          model = {}
          modelTokens = filter(lambda x: x.strip() != '', modelStr.split(' '))
          model['name'] = modelTokens[0]
          model['lnl'] = modelTokens[1]
          models.append(model);
  return models


def getMegaModels():
  with open('./data/mega_output/aP6.model_selection_data') as f:
    lines = f.readlines()
    models = []
    for i, line in enumerate(lines):
      if i == 0:
        # data['columns'] = line.split('\n')
        blah = False
      key = line.split(',')[0]
      key = key[0:4]
      if key == 'From':
        model = {}
        tokens = lines[i - 1].split(',')
        model['name'] = tokens[0]
        model['lnl'] = tokens[4]
        models.append(model)
  return models

def printModels(name, models):
  print
  print name
  for model in models:
    for key in model:
      text = key + ': ' + model[key]
      print(text)
  print


jModels = getJModels()

megaModels = getMegaModels()

printModels('JModels', jModels)
printModels('megaModels', megaModels)