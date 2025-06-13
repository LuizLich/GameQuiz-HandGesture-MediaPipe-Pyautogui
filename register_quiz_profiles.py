import pyautogui
import os

quiz_profiles_path = "quiz_profiles.py"

def get_click_position(label):
    print(f"\n➡️ Posicione o mouse sobre o botão da alternativa '{label}' e pressione Enter...")
    input("Pressione Enter para capturar.")
    pos = pyautogui.position()
    print(f"✔️ Capturado: {label} → {pos}")
    return pos

def salvar_perfil(nome_perfil, alternativas, cooldown, gesture_map):
    if not os.path.exists(quiz_profiles_path):
        with open(quiz_profiles_path, "w") as f:
            f.write("profiles = {}\n")

    with open(quiz_profiles_path, "r") as f:
        content = f.read()

    if "profiles =" not in content:
        content = "profiles = {}\n" + content

    novo_perfil = f"""
profiles["{nome_perfil}"] = {{
    "alternatives": {{
        {", ".join([f'"{k}": ({v[0]}, {v[1]})' for k, v in alternativas.items()])}
    }},
    "cooldown": {cooldown},
    "gesture_map": {{
        {", ".join([f'"{k}": "{v}"' for k, v in gesture_map.items()])}
    }}
}}
"""

    with open(quiz_profiles_path, "a") as f:
        f.write(novo_perfil)

    print(f"\n✅ Perfil '{nome_perfil}' salvo com sucesso em '{quiz_profiles_path}'!")

print("=== REGISTRADOR DE PERFIL DE QUIZ ===")
nome = input("📝 Nome do novo perfil (ex: quiz_geral): ")

num_opcoes = int(input("🔢 Quantas alternativas o quiz tem? (2 a 6): "))
if num_opcoes < 2 or num_opcoes > 6:
    print("❌ Número de alternativas inválido. Encerrando.")
    exit()

alternativas = {}
for i in range(num_opcoes):
    letra = chr(ord('A') + i)
    pos = get_click_position(letra)
    alternativas[letra.lower()] = (pos.x, pos.y)

cooldown = float(input("⏱️ Tempo de cooldown entre cliques (em segundos): "))

# Mapping of gestures recognized by the model (0 to 5) to letters A-F
print("\n🖐️ Informe o mapeamento dos gestos para alternativas.")
print("O modelo retorna valores de 0 a 5 → A a F")

gesture_map = {}
for i in range(num_opcoes):
    gesture = str(i)  # model returns 0 to 5
    alt = input(f"Gesto '{gesture}' ativa qual alternativa? (a/b/c/d/e/f): ").strip().lower()
    if alt in alternativas:
        gesture_map[gesture] = alt
    else:
        print(f"⚠️ Alternativa '{alt}' inválida ou não definida. Ignorando gesto '{gesture}'.")

# Save in the file
salvar_perfil(nome, alternativas, cooldown, gesture_map)