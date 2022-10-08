import sys
import onnx
import argparse

def main(args):
    help_menu = """
    Main function to check model using onnx.
    """

    if args.model_name.split('.')[-1] != 'onnx':
        raise ValueError("Model file name should have onnx extention .onnx, given", args.model_name)

    model = onnx.load(args.model_name)
    onnx.checker.check_model(model)
    print(onnx.helper.printable_graph(model.graph))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line tool to quickly verify ONNX models using onnx.check_model')
    parser.add_argument('--model-name', type=str, required=True, help='model file name .onnx')
    args = parser.parse_args()
    main(args)
