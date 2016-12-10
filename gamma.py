import argparse
import numpy as np

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('gamma_constant', type=float, help='Gamma power constant')
	parser.add_argument('steps', type=int, help='Quantization steps')
	args = parser.parse_args()
	return args.gamma_constant, args.steps

def gamma(values, power):
	return np.power(values, power)

def main():
	gamma_constant, steps = arguments()
	values = np.linspace(0.0, 1.0, steps)
	gamma_values = gamma(values, gamma_constant)
	gamma_values = np.around(gamma_values * (steps - 1)).astype(int)
	print(','.join(map(str,gamma_values)))

if __name__ == '__main__':
	main()