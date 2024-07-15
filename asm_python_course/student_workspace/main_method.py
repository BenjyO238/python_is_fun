import random



# get the area of a rectangle
def get_area(length, width):
    return length * width



if __name__ == '__main__':
    length_string = input('Enter the length of a rectangle: ')
    width_string = input('Enter the width of a rectangle: ')

    length = int(length_string)
    width = int(width_string)

    print('The area of the rectangle is', get_area(length, width))

