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
    'dir': '../../../data/source/',
    'files': ['he_li_pd.csv', 'death_recovery_gdp_unemp_withnan.csv']
}, {
    'dir': '../../../data/preprocessed/',
    'files': ['covid_19.csv']
}]
list_from_importer = importer_manager.exec(files)
# print(list_from_importer)


df_from_importer = pd.DataFrame(list_from_importer[0])
training, testing = SplitManager(ratio_splitter).exec(df_from_importer, 0.8)
print(training.columns)
# print(testing)

X = training[['Interest_Rate','Unemployment_Rate']] # here we have 2 variables for the multiple linear regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example
Y = training['Stock_Index_Price']
#
# X = sm.add_constant(X) # adding a constant
#
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X)
#
# print_model = model.summary()
# print(print_model)