import pyautogui as auto
import pyperclip
import time

auto.FAILSAFE = True

pokemonEncontrado = False
tentativa = 0


def clickBotaoSobrePokemon():
    auto.click(x=1255, y=507)  # as coordenadas dependem da resolução do monitor/navegador


def clickBotaoNomePokemon():
    auto.click(x=750, y=259)  # as coordenadas dependem da resolução do monitor/navegador


def clickBotaoClose():
    auto.click(x=1249, y=251)  # as coordenadas dependem da resolução do monitor/navegador


def clickBotaoTipoPokemon():
    auto.click(x=1284, y=346)  # as coordenadas dependem da resolução do monitor/navegador


pergunta = input("Você quer achar qualquer raro? s/n: ").lower().strip()


def autoProcuraRaro():
    global tentativa, pokemonEncontrado

    sequencia = ['w', 'd', 's', 'a']
    for tecla in sequencia:
        auto.press(tecla)
        auto.click(x=1284, y=346, clicks=3, interval=0.12)  # as coordenadas dependem da resolução do monitor/navegador. Este é o autoclick do TipoPokemon
        time.sleep(0.35)
        auto.hotkey('ctrl', 'c')
        time.sleep(0.05)
        poketype = pyperclip.paste().lower().strip()

        tentativa += 1

        if poketype != "":
            print(f'Você encontrou um Pokémon raro do tipo {poketype} na {tentativa}a tentativa!!.')
            pokemonEncontrado = True
            break
        else:
            print(f"Pokémon raro não encontrado. Tentativa número {tentativa}")
            time.sleep(1)


if pergunta == "s":
    while not pokemonEncontrado:
        autoProcuraRaro()

def autoProcuraPokeEspecifico():
    global tentativa, pokemonEncontrado

    sequencia = ['w', 'd', 's', 'a']
    for tecla in sequencia:
        auto.press(tecla)
        time.sleep(0.8)
        clickBotaoSobrePokemon()
        time.sleep(0.6)
        clickBotaoNomePokemon()
        clickBotaoNomePokemon()
        time.sleep(0.2)
        auto.hotkey('ctrl', 'c')
        nomePokemon = pyperclip.paste().lower().strip()

        tentativa += 1

        if nomePokemon == pokemonProcurado:
            print(f'O Pokémon {pokemonProcurado} foi encontrado na {tentativa}a tentativa!!')
            clickBotaoClose()
            pokemonEncontrado = True
            break
        elif nomePokemon == "":
            print(f'Nada encontrado. Tentativa número {tentativa}')
            clickBotaoClose()
            time.sleep(0.5)
        else:
            print(f'Outro pokémon encontrado: {nomePokemon}. Tentativa número {tentativa}')
            clickBotaoClose()
            time.sleep(0.5)


if pergunta == "n":
    pokemonProcurado = input('Digite o nome do Pokémon que deseja encontrar: ').lower().strip()
    while not pokemonEncontrado:
        autoProcuraPokeEspecifico()
