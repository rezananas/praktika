# Дополнительное практическое задание по модулю: "Классы и объекты."

from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname # имя пользователя, строка
        self.password = hash(password) # пароль, число
        self.age = age # возраст, число


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = 0 # секунда остановки (изначально 0)
        # adult_mode - ограничение по возрасту, bool (False по умолчанию)

class UrTube:
    def __init__(self):
        self.users = {} # список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None # текущий пользователь, User

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) not in self.users.values():
                self.current_user = nickname

    def register(self, nickname, password, age):
        self.age = age
        if nickname not in self.users:
            self.users[nickname] = password
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        return self.current_user == None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
        return self.videos

    def get_videos(self, text):
        list_videos = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self, movie):
        if self.current_user:
            if self.age > 18:
                for video in self.videos:
                    if movie in video.title:
                        for i in range(video.duration):
                            count = ''
                            video.time_now += 1
                            count += str(video.time_now)
                            print(count, end=' ')
                            sleep(1)
                        print('\nКонец видео')
                        video.time_now -= video.duration
            else:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы посмотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
