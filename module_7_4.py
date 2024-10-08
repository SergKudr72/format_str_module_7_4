class Team:
    def __init__(self, name: str, _num: int, score_: int, _time: float):
        self.name = name
        self._num = _num
        self.score_ = score_
        self._time = _time

    def team_nums(self):
        print('В команде %s участников: %s!' % (self.name, self._num))

    def team_nums_sum(self, nums):
        print('Итого сегодня в командах участников: %s и %d!' % (self._num, nums))

    def score_rezult(self):
        print('Команда {} решила задач: {}!'.format(self.name, self.score_))

    def time_score(self):
        print('{} решили задачи за {} с!'.format(self.name, self._time))

    def scores_sum(self, scores):
        print(f'Команды решили {self.score_} и {scores} задач.')

    def challenge_result(self, names, scores, times):
        if self.score_ > scores or self.score_ == scores and self._time > times:
            result = f'победа команды {self.name}!'
        elif self.score_ < scores or self.score_ == scores and self._time < times:
            result = f'победа команды {names}!'
        else:
            result = 'ничья!'
        print(f'Результат битвы: {result}')

    def tasks_total(self, other_team_score):
        return self.score_ + other_team_score

    def time_avg(self, other_team_time):
        return self._time + other_team_time

    def all_rezults(self):
        print(f'Сегодня было решено {team1.tasks_total(team2.score_)} задач, в среднем по '
              f'{round(team1.time_avg(team2._time) / team1.tasks_total(team2.score_), 2)} секунды на задачу!.')




team1 = Team('Мастера кода', 5, 40, 1552.512, )
team2 = Team('Волшебники данных', 6, 42, 2153.31451)

# Пример входных данных
# team1_num = 5
# team2_num = 6
# score_1 = 40
# score_2 = 42
# team1_time = 1552.512
# team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

team1.team_nums()
team1.team_nums_sum(team2._num)
team2.score_rezult()
team2.time_score()
team1.scores_sum(team2.score_)
team1.challenge_result(team2.name, team2.score_, team2._time)
team1.all_rezults()


