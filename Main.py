import random

def get_computer_choice():
    return random.choice(["taş", "kağıt", "makas"])

def determine_winner(user, computer):
    if user == computer:
        return "Berabere!"
    elif (user == "taş" and computer == "makas") or \
         (user == "kağıt" and computer == "taş") or \
         (user == "makas" and computer == "kağıt"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def main():
    while True:
        user_choice = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q' tuşuna basın): ").lower()
        if user_choice == 'q':
            print("Oyun sonlandırıldı. Güle güle!")
            break
        elif user_choice not in ["taş", "kağıt", "makas"]:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Bilgisayarın seçimi: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
