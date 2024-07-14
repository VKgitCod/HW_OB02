class User():
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = "user"
        self.users = []

    def info(self):
        print(f"Список пользователей {self.users}")

class Admin(User):
    def __init__(self, id, name, status):
        super().__init__(id, name, status)
        self._status = "admin"

    def _add_user(self, id, name):
        self.users.append({"id": id, "name": name, "Статаус": "Пользователь"})
        print(f"Пользователь {self.name} добавлен")

    def _remove_user(self, name):
        for u in self.users:
            if u["name"] == name:
                self.users.remove(name)
            else:
                print("Пользователь не найден")

adm = Admin(1, "Виктор", "")

adm._add_user(2, "Максим")
adm.info()

adm._remove_user("Максим")
adm.info()

