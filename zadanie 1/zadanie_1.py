import math
def one():
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        result = num1 + num2
        print("���������:", result)
def vtoroi():
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        result = num1 - num2
def treti():
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        result = num1 * num2
while True:
    print("�������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ����� 1 ������� �� �����")
    print("8. ����� ��������� �����")
    print("9. ����� �� ���������")
    print("10. �����")
    print("11. �������")
    print("12. �������")

    choice = int(input("������� ����� ��������: "))

    if choice == 1:
       one()
    elif choice == 2:
        vtoroi()
        
        print("���������:", result)
    elif choice == 3:
        treti()
        
        print("���������:", result)
    elif choice == 4:

        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        result = num1 / num2
        print("���������:", result)
    elif choice == 5:
        num1 = float(input("������� �����: "))
        power = int(input("������� �������: "))
        result = num1 ** power
        print("���������:", result)
    elif choice == 6:
        num = float(input("������� �����: "))
        result = math.sqrt(num)
        print("���������:", result)
    elif choice == 7:
        num = float(input("������� �����: "))
        result = num * 0.01
        print("���������:", result)
    elif choice == 8:
        num = int(input("������� �����: "))
        result = 1
        for i in range(1, num + 1):
            result *= i
        print("���������:", result)
    elif choice == 9:
        break
    elif choice == 10:
        num = float(input("������� �����: "))
        result = math.sin(num)
        print("���������:", result)
    elif choice == 11:
        num = float(input("������� �����: "))
        result = math.cos(num)
        print("���������:", result)
    elif choice == 12:
        num = float(input("������� �����: "))
        result = math.tan(num)
        print("���������:", result)
    else:
        print("������������ ����� ��������. ���������� �����.")











def rectangle_area(width, height):
    area = width * height
    return area

width = int(input())
height = int(input())
area = rectangle_area(width, height)
print(area)










number=int(input())
def is_even(number):
    return number % 2 == 0

print(is_even(number))
















def sum_digits(number):
    return sum(map(int, list(number)))
 
print(sum_digits(input()))