def main():
    height, width = input().split()

    weights = input().split()
    weights = list(map(lambda x: int(x), weights))

    print(height, width)
    print(weights)

if __name__ == "__main__":
    main()
