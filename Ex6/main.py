"""
Module with main game loop
"""
import game


it_space = game.Location("ІТ Простір")
it_space.set_description("""Пристанище всіх заблудших душ айтішників.
Сонячного світла і свіжого повітря вони не бачили з часу побудови""")

trapezna = game.Location("Трапезна")
trapezna.set_description(
    """Насправді всі вступають в УКУ лише для 50% знижки тут""")

biblioteka = game.Location("Бібліотека ЦЩ")
biblioteka.set_description("Найкраще місце для...")

kolegium = game.Location("Колегіум")
kolegium.set_description("Бережи вас Бог, якщо ви назвете це гуртожитком")

kolegium.link_location(biblioteka, 'схід')
biblioteka.link_location(kolegium, 'захід')
biblioteka.link_location(trapezna, 'північ')
trapezna.link_location(biblioteka, 'південь')
kolegium.link_location(it_space, 'північ')
it_space.link_location(kolegium, 'південь')
it_space.link_location(trapezna, 'схід')
trapezna.link_location(it_space, 'захід')


susid_glib = game.Friend("сусід Гліб", "Хоч і ЕПЕшник, але всеодно кентите")
susid_glib.set_conversation(
    "Тримай ти забув тут ключі від кімнати під час останньої тривоги")
it_space.set_character(susid_glib)

ohoronets = game.Enemy(
    "Охоронець", "Сумлінно виконує свою роботу і не пускає нікого без ключа")
ohoronets.set_conversation("Е! Куда без ключа?")
ohoronets.set_weakness("ключі")
kolegium.set_character(ohoronets)

key = game.Item("ключі")
key.set_description("Ключі від кімнати в колегіумі")
it_space.set_item(key)

dz = game.Item("есе")
dz.set_description(
    "Кров'ю і потом дісталось це есе з філософії, не без допомоги ЕПЕшника Гліба")
biblioteka.set_item(dz)

vuklachad = game.Enemy("Викладач", "Бачиш його в трапезній частіше ніж на парах")
vuklachad.set_conversation("*Кидає злий погляд ніби ти забрав перед ним останні деруни*")
vuklachad.set_weakness("ece")
trapezna.set_character(vuklachad)

curr_location = it_space
backpack = []

dead = False

print("""Твоє завдання пройти всі локації і повернутись назад""")
list_loc = []

while dead == False:

    print("\n")
    curr_location.get_details()

    inhabitant = curr_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = curr_location.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        curr_location = curr_location.move(command)
        list_loc.append(curr_location)
    elif command == "говорити":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "бити":
        if inhabitant is not None:
            print("Чим хочеш бити?")
            fight_with = input()


            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print("Єєєй, ти виграв битву!")
                    curr_location.character = None
                else:
                    print("Йойки, ти програв битву")
                    print("Це кінець гри :(")
                    dead = True
            else:
                print("В тебе нема " + fight_with)
        else:
            print("Успокійся, тут нема з ким битись")
    elif command == "взяти":
        if item is not None:
            print("Ти поклав " + item.get_name() + " в рюкзак")
            backpack.append(item.get_name())
            curr_location.set_item(None)
        else:
            print("Нема шо тут брати")
    else:
        print("Не знаю я оце ваше " + command)

    if set(list_loc) == {trapezna, it_space, biblioteka, kolegium}\
        and list_loc[-1] == it_space:
        print("Єєєєєй, ти виграв! І як справжній айтішник знову прийшов кодити")
        dead = True