import os


def correct_num(start, end):
    txt = input()
    while (
        not (txt.isdigit())
        or txt.startswith("0")
        or int(txt) not in range(start, end + 1)
    ):
        txt = input("\nНеккоректный ввод. Попробуйте снова\n\n>> ")
    return int(txt)


os.system("cls")
print(
    "Ave Caesar!",
    "Программа шифрования\\дешифрования сообщений по методу Цезаря.",
    sep="\n",
)

rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng = "abcdefghijklmnopqrstuvwxyz"

print("\nВыберите язык алфавита\n1 - Русский\n2 - Английский\n\n>> ", end="")
lang = [rus, eng][correct_num(1, 2) - 1]

print("\nВыберите операцию\n1 - Шифрование\n2 - Дешифрование\n\n>> ", end="")
oper = [1, -1][correct_num(1, 2) - 1]

print(
    "\nВведите шаг сдвига вправо (от 1 до ", len(lang) - 1, ")\n\n>> ", sep="", end=""
)
rot = correct_num(1, len(lang) - 1) * oper

txt = input("\nВведите текст\n\n>> ")

print("\nРезультат работы программы:")
for c in txt:
    if c.lower() in lang:
        new_c = lang[(lang.find(c.lower()) + rot) % len(lang)]
        print(new_c if c.islower() else new_c.upper(), end="")
    else:
        print(c, end="")
