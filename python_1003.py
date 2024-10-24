hensu1 :int = 10
hensu2 :str = "lesson"

lst :list[int] = [1, 2, 3, 4, 5]
tpl :tuple = ("abc", "def", "ghi")
st :set = {10, 20, 30}
dic :dict = {"suzuki":1, "tanaka":2}
dic2 :dict[str,int] = {"suzuki":1, "tanaka":2}

hensu3 :int = 20
print(hensu1 + hensu3)

hensu4 :str = "python"
print(hensu2 + "の" + hensu4)
print(f"{hensu2}の{hensu4}")
print(f"計算結果は{hensu1 + hensu3}")
print(f"計算結果は{hensu2}の{hensu4}")

lst.append(6)
lst + [5]

if hensu1 % 2 == 0 and hensu1 % 3 == 0:
    print("偶数")

hensu5 = 1 if hensu1 % 2 == 0 else 0
print(f"{1 if hensu1 % 2 == 0 else 0}")

if (hensu6 := 5) > 4:
    print(f"{hensu6}は4より大きい")

for i in range(len(lst)):
    if i % 2 != 0:
        lst[i] = lst[i] * 2

i = 0
for n in lst:
    if i % 2 != 0:
        lst[i] = n * 2
    i += 1

def calc(args1 :int, args2 :int) -> float:
    try:
        result = args1 / args2
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
    except ValueError:
        return 
    except Exception:
        return

    return result


class Human:
    gender = "men"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._address = "tokyo"

    def nameprint(self):
        self._namecheck(self.name)
        return f"名前は{self.name}です"

    @classmethod
    def set_gender(cls, gender):
        cls.gender = gender

    def _namecheck(self, name):
        if isinstance(name, str):
            print("文字列です")
        print("文字列ではないです")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

Human.gender = "women"
Human.set_gender("women")
human1 = Human("Taro", 18)
human1.address = "osaka"


class Student(Human):
    def __init__(self, school):
        super().__init__()
        self.school = school

    def schoolprint(self):
        print(self.school)

Student("terakoya")