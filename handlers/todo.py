import json
import numpy as np

def main(event, context):
    a = np.arange(15).reshape(3, 5)
    return {
        'statusCode': 200,
        'body': json.dumps({'data': a.tolist()})
    }
