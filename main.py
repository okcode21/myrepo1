def main():
    name = input("Enter your name: ")
    print(greet_user(name))
    demo()

from utils.math_ops import multiply

def demo():
    print("2 x 5 =", multiply(2, 5))

    
if __name__ == "__main__":
    main()

from utils import beautify_ops
json_data = {}
beautify(json_data)
demo()
