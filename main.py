import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
#CHAT_ID = os.getenv("CHAT_ID")
GROUP_ID = os.getenv("GROUP_ID")



if BOT_TOKEN is None:
    print("❌ Error: BOT_TOKEN is not set in the environment.")
else:
    print(f"✅ Success! Token starts with: {BOT_TOKEN[:5]}...")

def send_telegram_message(chat_id, text):
    print("Call Send Telegram Message")
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    print(response.text)
    print("End of Telegram Message")

def get_bible_quote(line):
    # Wir suchen Johannes 3, Vers 16
    # Nutze "John" statt "Johannes", um Fehler zu vermeiden
    stelle = line
    #url = f"https://bible-api.com/{stelle}"
    url = f"https://bible-api.com/{stelle}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Wir ziehen uns einfach nur den Text-Teil aus der Antwort
        text = data["text"]
        print(f"Bibelvers gefunden:\n{text}")
    else:
        print(f"Fehler: {response.status_code}")
    return text



def get_bible_verse(book, chapter, translation='rst'):
    # Пример использования API justbible.ru
    url = f"https://justbible.ru/api/bible?translation={translation}&book={book}&chapter={chapter}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return "Ошибка получения данных"


# Получить главу 1 из книги Бытие (Genesis)

if __name__ == "__main__":
        for counter in range(2,8):
            quote = "John 2:"+str(counter)
            text = get_bible_quote(quote)
            send_telegram_message(GROUP_ID, text)

            # russian
            verse = get_bible_verse('1', str(counter))
            send_telegram_message(GROUP_ID, verse["1"])
            print(verse["1"])
