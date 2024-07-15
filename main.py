class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._status = "user"
        self.users = []

    def info(self):
        print(f"Список пользователей {self.users}")

    def user_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._status = "admin"

    def add_user(self, id, name):
        self.name = name
        self.users.append({"id": id, "name": name, "Статаус": "Пользователь"})
        print(f"Пользователь {self.name} добавлен")

    def remove_user(self, name):
        for u in self.users:
            if u["name"] == name:
                self.users.remove(u)
                print(f"Пользователь {name} удален")
            else:
                print("Пользователь не найден")

adm = Admin(1, "Виктор")

adm.add_user(2, "Максим")
adm.add_user(3, "Алексей")
adm.add_user(4, "Игорь")
adm.add_user(5, "Иван")
adm.add_user(6, "Антон")
adm.info()

adm.remove_user("Антон")
adm.info()


