import pickle


class CountryState:
    def __init__(self):
        self.capitals = {}

    def add_country(self, country, capital):
        if self.find_capital(country) is None:
            self.capitals[country] = capital
            return f"Страна: {country}, Столица: {capital}"
        else:
            return "Страна уже добавлена"

    def del_country(self, country):
        if self.find_capital(country) is not None:
            removed = self.capitals.pop(country)
            return f"Убрано - {country}:{removed}"
        else:
            return "Страны нет в словаре"

    def find_country(self, capital):
        for key, value in self.capitals.items():
            if value == capital:
                return key
        else:
            return None

    def find_capital(self, country):
        if country in self.capitals.keys():
            return self.capitals[country]
        else:
            return None

    def change_capital(self, country, capital):
        if self.find_capital(country) is not None:
            self.capitals[country] = capital
        else:
            return "Страны нет в словаре"

    def save_pkl(self):
        with open('saved_data.pkl', 'wb') as file:
            pickle.dump(self.capitals, file)
        return "Файл создан"

    def read_pkl(self):
        with open('saved_data.pkl', 'rb') as file:
            loaded_data = pickle.load(file)
            self.capitals.update(loaded_data)
        return f"Данные из файла записаны: {loaded_data}"


country_state = CountryState()
print(country_state.add_country("Россия", "Москва"))
print(country_state.find_capital("Россия"))
print(country_state.save_pkl())
print(country_state.del_country("Россия"))
print(country_state.find_capital("Россия"))
print(country_state.read_pkl())
print(country_state.find_capital("Россия"))