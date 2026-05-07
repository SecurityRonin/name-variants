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

RUSSIAN_SURNAME_VARIANTS: dict[str, list[str]] = {
    # ── Common Russian surnames ──────────────────────────────────────────────
    "Иванов": ["ivanov", "ivanoff", "ivanow"],
    "Смирнов": ["smirnov", "smirnoff", "smyrnov"],
    "Кузнецов": ["kuznetsov", "kouznetsov", "kuznetzov"],
    "Попов": ["popov", "popoff", "popow"],
    "Васильев": ["vasilyev", "vasiliev", "vassiliev", "vasilev"],
    "Петров": ["petrov", "petroff", "petrow"],
    "Соколов": ["sokolov", "sokoloff", "sokolof"],
    "Михайлов": ["mikhailov", "michailov", "mikhayloff"],
    "Новиков": ["novikov", "novikoff"],
    "Фёдоров": ["fyodorov", "fedorov", "feodorov", "fédorov"],
    "Морозов": ["morozov", "morozoff"],
    "Волков": ["volkov", "volkoff"],
    "Алексеев": ["alekseyev", "alexeyev", "alexeev"],
    "Лебедев": ["lebedev", "lebedef"],
    "Семёнов": ["semenov", "semyonov", "semenoff"],
    "Егоров": ["yegorov", "egorov"],
    "Павлов": ["pavlov", "pavloff"],
    "Козлов": ["kozlov", "kozloff"],
    "Степанов": ["stepanov", "stepanoff"],
    "Николаев": ["nikolayev", "nikolaev", "nikolaïev"],
    "Орлов": ["orlov", "orloff"],
    "Андреев": ["andreyev", "andreev", "andreeff"],
    "Макаров": ["makarov", "makaroff"],
    "Никитин": ["nikitin", "nikitine"],
    "Захаров": ["zakharov", "zacharov", "zaharoff"],
    "Зайцев": ["zaitsev", "zaytsev", "zaitzev"],
    "Соловьёв": ["solovyov", "soloviev"],
    "Борисов": ["borisov", "borissov"],
    "Яковлев": ["yakovlev", "yakovleff"],
    "Григорьев": ["grigoryev", "grigoriev"],
    "Романов": ["romanov", "romanoff"],
    "Воробьёв": ["vorobyov", "vorobiev"],
    "Сергеев": ["sergeyev", "sergeev"],
    "Кузьмин": ["kuzmin", "kouzmine"],
    "Фролов": ["frolov", "froloff"],
    "Александров": ["alexandrov", "alexandroff"],
    "Дмитриев": ["dmitriev", "dmitrieff"],
    "Королёв": ["korolyov", "korolev"],
    "Гусев": ["gusev", "goussev"],
    "Тихонов": ["tikhonov", "tichonov"],
    "Медведев": ["medvedev", "medvedeff"],
    "Пушкин": ["pushkin", "pouschkin"],
    "Достоевский": ["dostoevsky", "dostoyevsky", "dostoevski", "dostoevskiy"],
    "Толстой": ["tolstoy", "tolstoi"],
    "Чехов": ["chekhov", "chekov", "tchekhov", "tschechow"],
    "Горбачёв": ["gorbachev", "gorbachov", "gorbatschow"],
    "Ельцин": ["yeltsin", "yeltsyn", "eltsine"],
    "Путин": ["putin", "poutin"],
    "Жириновский": ["zhirinovsky", "zhirinovskiy"],
    "Лужков": ["luzhkov", "luzhkoff"],
    # ── Ukrainian surnames (different romanization from Russian) ─────────────
    "Шевченко": ["shevchenko", "shevtchenko"],
    "Кравчук": ["kravchuk", "kravtchuk"],
    "Янукович": ["yanukovych", "yanukovich"],
    "Тимошенко": ["tymoshenko", "timoshenko"],
    "Зеленський": ["zelensky", "zelenskyy", "zelenskiy"],
    "Порошенко": ["poroshenko", "porochenko"],
    "Кличко": ["klitschko", "klychko", "klitchko"],
    "Бандера": ["bandera"],
    "Грушевський": ["hrushevsky", "grushevsky"],
    # ── Common Russian given names ────────────────────────────────────────────
    "Александр": ["alexander", "aleksandr", "alexandre"],
    "Дмитрий": ["dmitry", "dmitri", "dmitriy"],
    "Сергей": ["sergei", "sergey", "serguei"],
    "Андрей": ["andrei", "andrey", "andrew"],
    "Алексей": ["alexei", "alexey", "aleksey"],
    "Михаил": ["mikhail", "michael", "michail"],
    "Николай": ["nikolai", "nikolay", "nicolas"],
    "Владимир": ["vladimir", "vladimyr"],
    "Иван": ["ivan", "iwan"],
    "Павел": ["pavel", "paul"],
    "Наталья": ["natalia", "natasha", "natalya"],
    "Елена": ["elena", "yelena", "helen"],
    "Ольга": ["olga", "olha"],
    "Татьяна": ["tatiana", "tatyana", "tatiyana"],
    "Ирина": ["irina", "irena"],
    "Светлана": ["svetlana", "svyetlana"],
    "Анна": ["anna", "ana"],
    "Екатерина": ["ekaterina", "katerina", "catherine"],
    "Мария": ["maria", "mariya", "mary"],
    "Людмила": ["lyudmila", "ludmila"],
}
