class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: Неверный объект пользователя.")

    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: Пользователь не найден.")

    def get_users(self):
        return self._users_list

    def __str__(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}, Количество пользователей: {len(self._users_list)}"


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Алиса")

    # Вывод информации об администраторе
    print(admin)

    # Создаем пользователей
    user1 = User(2, "Боб")
    user2 = User(3, "Чарли")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)
# Вывод информации о всех пользователях
    for user in admin.get_users():
        print(user)

    # Администратор удаляет пользователя
    admin.remove_user(2)

    # Вывод информации о всех пользователях после удаления
    for user in admin.get_users():
        print(user)
