import argparse, os, sys
import numpy as np
from flask import Flask, render_template


def matrix_calc(size):
    matrix_a = np.random.rand(size, size)
    matrix_b = np.random.rand(size, size)
    result = np.matmul(matrix_a, matrix_b)
    return result.sum()

matrices_env = os.environ.get("MATRICES")
if matrices_env:
    try:
        matrices = int(matrices_env)
    except ValueError:
        print("Error: MATRICES is not a valid integer")
        sys.exit(1)
else:
    matrices = 1000

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the index page."""
    result = matrix_calc(matrices)
    return render_template('index.html', matrices=matrices, result=result)


if __name__ == '__main__':
    pass
