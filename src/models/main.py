import sys
sys.path.append('../../')


if __name__ == '__main__':
    print('### Model Main ###')

    model_exec_plan = {
        model: [{
            'name': 'AIC',
            'criteria': {}
        }, {
            'name': 'SimpleLm',
            'criteria': {}
        }, {
            'name': 'StepWise',
            'criteria': {
                'name': 'p_value',
                'threshold': [0.01, 0.05, 0.1]
            }
        }]
    }