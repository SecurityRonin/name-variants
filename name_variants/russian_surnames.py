"""
Russian/Slavic surname lookup: Cyrillic → romanization variants.

Key problem: Multiple transliteration standards in active use:
  - BGN/PCGN 1947 (US/UK official)
  - ISO 9:1995
  - Informal British (-off/-eff endings for -ov/-ev)
  - Pre-revolutionary spellings (Tchaikovsky vs. Chaikovsky)

  Ельцин → Yeltsin (BGN) / Yeltsyn / Eltsine (French)
  Чехов → Chekhov (common) / Chekov (simplified) / Tchekhov (old French)
  Горбачёв → Gorbachev (BGN) / Gorbachov / Gorbatschow (German)

Also covers Ukrainian and Belarusian names which have distinct
romanization patterns from Russian.

Sources:
  - BGN/PCGN 1947 Russian romanization
  - ISO 9:1995
  - British Standard BS 2979:1958
  - Common diaspora (UK/US/HK) variant spellings
"""

RUSSIAN_SURNAME_VARIANTS: dict[str, dict] = {
    'Иванов': {
        "forms": ['ivanov', 'ivanoff', 'ivanow'],
        "frequency": 1_500_000,
    },
    'Смирнов': {
        "forms": ['smirnov', 'smirnoff', 'smyrnov'],
        "frequency": 1_100_000,
    },
    'Кузнецов': {
        "forms": ['kuznetsov', 'kouznetsov', 'kuznetzov'],
        "frequency": 900_000,
    },
    'Попов': {
        "forms": ['popov', 'popoff', 'popow'],
        "frequency": 650_000,
    },
    'Васильев': {
        "forms": ['vasilyev', 'vasiliev', 'vassiliev', 'vasilev'],
        "frequency": 620_000,
    },
    'Петров': {
        "forms": ['petrov', 'petroff', 'petrow'],
        "frequency": 600_000,
    },
    'Соколов': {
        "forms": ['sokolov', 'sokoloff', 'sokolof'],
        "frequency": 580_000,
    },
    'Михайлов': {
        "forms": ['mikhailov', 'michailov', 'mikhayloff'],
        "frequency": 570_000,
    },
    'Новиков': {
        "forms": ['novikov', 'novikoff'],
        "frequency": 510_000,
    },
    'Фёдоров': {
        "forms": ['fyodorov', 'fedorov', 'feodorov', 'fédorov'],
    },
    'Морозов': {
        "forms": ['morozov', 'morozoff'],
    },
    'Волков': {
        "forms": ['volkov', 'volkoff'],
    },
    'Алексеев': {
        "forms": ['alekseyev', 'alexeyev', 'alexeev'],
    },
    'Лебедев': {
        "forms": ['lebedev', 'lebedef'],
    },
    'Семёнов': {
        "forms": ['semenov', 'semyonov', 'semenoff'],
    },
    'Егоров': {
        "forms": ['yegorov', 'egorov'],
    },
    'Павлов': {
        "forms": ['pavlov', 'pavloff'],
    },
    'Козлов': {
        "forms": ['kozlov', 'kozloff'],
    },
    'Степанов': {
        "forms": ['stepanov', 'stepanoff'],
    },
    'Николаев': {
        "forms": ['nikolayev', 'nikolaev', 'nikolaïev'],
    },
    'Орлов': {
        "forms": ['orlov', 'orloff'],
    },
    'Андреев': {
        "forms": ['andreyev', 'andreev', 'andreeff'],
    },
    'Макаров': {
        "forms": ['makarov', 'makaroff'],
    },
    'Никитин': {
        "forms": ['nikitin', 'nikitine'],
    },
    'Захаров': {
        "forms": ['zakharov', 'zacharov', 'zaharoff'],
    },
    'Зайцев': {
        "forms": ['zaitsev', 'zaytsev', 'zaitzev'],
    },
    'Соловьёв': {
        "forms": ['solovyov', 'soloviev'],
    },
    'Борисов': {
        "forms": ['borisov', 'borissov'],
    },
    'Яковлев': {
        "forms": ['yakovlev', 'yakovleff'],
    },
    'Григорьев': {
        "forms": ['grigoryev', 'grigoriev'],
    },
    'Романов': {
        "forms": ['romanov', 'romanoff'],
    },
    'Воробьёв': {
        "forms": ['vorobyov', 'vorobiev'],
    },
    'Сергеев': {
        "forms": ['sergeyev', 'sergeev'],
    },
    'Кузьмин': {
        "forms": ['kuzmin', 'kouzmine'],
    },
    'Фролов': {
        "forms": ['frolov', 'froloff'],
    },
    'Александров': {
        "forms": ['alexandrov', 'alexandroff'],
    },
    'Дмитриев': {
        "forms": ['dmitriev', 'dmitrieff'],
    },
    'Королёв': {
        "forms": ['korolyov', 'korolev'],
    },
    'Гусев': {
        "forms": ['gusev', 'goussev'],
    },
    'Тихонов': {
        "forms": ['tikhonov', 'tichonov'],
    },
    'Медведев': {
        "forms": ['medvedev', 'medvedeff'],
    },
    'Пушкин': {
        "forms": ['pushkin', 'pouschkin'],
    },
    'Достоевский': {
        "forms": ['dostoevsky', 'dostoyevsky', 'dostoevski', 'dostoevskiy'],
    },
    'Толстой': {
        "forms": ['tolstoy', 'tolstoi'],
    },
    'Чехов': {
        "forms": ['chekhov', 'chekov', 'tchekhov', 'tschechow'],
    },
    'Горбачёв': {
        "forms": ['gorbachev', 'gorbachov', 'gorbatschow'],
    },
    'Ельцин': {
        "forms": ['yeltsin', 'yeltsyn', 'eltsine'],
    },
    'Путин': {
        "forms": ['putin', 'poutin'],
    },
    'Жириновский': {
        "forms": ['zhirinovsky', 'zhirinovskiy'],
    },
    'Лужков': {
        "forms": ['luzhkov', 'luzhkoff'],
    },
    'Шевченко': {
        "forms": ['shevchenko', 'shevtchenko'],
    },
    'Кравчук': {
        "forms": ['kravchuk', 'kravtchuk'],
    },
    'Янукович': {
        "forms": ['yanukovych', 'yanukovich'],
    },
    'Тимошенко': {
        "forms": ['tymoshenko', 'timoshenko'],
    },
    'Зеленський': {
        "forms": ['zelensky', 'zelenskyy', 'zelenskiy'],
    },
    'Порошенко': {
        "forms": ['poroshenko', 'porochenko'],
    },
    'Кличко': {
        "forms": ['klitschko', 'klychko', 'klitchko'],
    },
    'Бандера': {
        "forms": ['bandera'],
    },
    'Грушевський': {
        "forms": ['hrushevsky', 'grushevsky'],
    },
    'Александр': {
        "forms": ['alexander', 'aleksandr', 'alexandre'],
    },
    'Дмитрий': {
        "forms": ['dmitry', 'dmitri', 'dmitriy'],
    },
    'Сергей': {
        "forms": ['sergei', 'sergey', 'serguei'],
    },
    'Андрей': {
        "forms": ['andrei', 'andrey', 'andrew'],
    },
    'Алексей': {
        "forms": ['alexei', 'alexey', 'aleksey'],
    },
    'Михаил': {
        "forms": ['mikhail', 'michael', 'michail'],
    },
    'Николай': {
        "forms": ['nikolai', 'nikolay', 'nicolas'],
    },
    'Владимир': {
        "forms": ['vladimir', 'vladimyr'],
    },
    'Иван': {
        "forms": ['ivan', 'iwan'],
    },
    'Павел': {
        "forms": ['pavel', 'paul'],
    },
    'Наталья': {
        "forms": ['natalia', 'natasha', 'natalya'],
    },
    'Елена': {
        "forms": ['elena', 'yelena', 'helen'],
    },
    'Ольга': {
        "forms": ['olga', 'olha'],
    },
    'Татьяна': {
        "forms": ['tatiana', 'tatyana', 'tatiyana'],
    },
    'Ирина': {
        "forms": ['irina', 'irena'],
    },
    'Светлана': {
        "forms": ['svetlana', 'svyetlana'],
    },
    'Анна': {
        "forms": ['anna', 'ana'],
    },
    'Екатерина': {
        "forms": ['ekaterina', 'katerina', 'catherine'],
    },
    'Мария': {
        "forms": ['maria', 'mariya', 'mary'],
    },
    'Людмила': {
        "forms": ['lyudmila', 'ludmila'],
    },
}
