def cube(num):
    return num ** 3


if __name__ == "__main__":
    # Default value to avoid input() in Jenkins
    num = 3
    print("Cube is:", cube(num))
