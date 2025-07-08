from utils.math_ops import multiply
from utils.beautify_ops import beautify
from utils.basic import greet_user

def main():
    name = input("Enter your name: ")
    print(greet_user(name))  
    demo()

def demo():
    print("2 x 5 =", multiply(2, 5))

if __name__ == "__main__":
    main()

json_data = {}
beautify(json_data)
demo()
