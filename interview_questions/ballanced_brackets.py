def is_ballanced(input):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    stack = []
    for char in input:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            pos = close_list.index(char)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "is not"
    if len(stack) == 0:
        return "is"


def main():
    sample_imput = "{[]{()}}"
    print("the string " + sample_imput + " " + is_ballanced(sample_imput) + " ballanced")


if __name__ == "__main__": main()
