import sys
sys.path.append('../../../')
import pandas as pd
from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager



if __name__ == '__main__':
 print("Hello")


# get source
loader = SourceFactory('csv').generate()
data = SourceManager(loader).exec('../../../data/preprocessed')[0]

# initialize split object
ratio_splitter = SplitFactory('ratio').generate()
training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
# print(training)
# print(testing)

importer_object = ImporterFactory('csv').generate()
importer_manager = ImporterManager(importer_object)
files = [{
    'dir': '../../../data/preprocessed/',
    'files': ['covid_19.csv']
}]
data = importer_manager.exec(files)[0]
# print(data)

training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
print(training.columns)
# print(testing)
#
X = training[["Health.expenditures....of.GDP.","Literacy...."]] # here we have 2 variables for the multiple linear regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example
Y = training['Physicians.density..physicians.1.000.population.']
#
# X = sm.add_constant(X) # adding a constant
#
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X)
#
# print_model = model.summary()
# print(print_model)