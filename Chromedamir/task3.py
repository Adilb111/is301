try:
    # ���� ������
    a = float(input("a: "))
    b = float(input("b: "))
    
    # �������� � ����������
    if a > 0 and b > 0:
        S = a * b
        P = 2 * (a + b)
        print(f"S = {S}")
        print(f"P = {P}")
    else:
        print("������: ������� ������ ���� ��������������.")
except ValueError:
    print("������: ������� �����.")