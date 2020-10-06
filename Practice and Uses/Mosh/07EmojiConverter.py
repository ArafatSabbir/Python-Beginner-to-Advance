emoji_Dictionary = {
    ":)" : "😊",
    ":D" : "😁",
    ":p" : "😋",
    ":(" : "😒",
    ":v:" : "✌",
    ":cat:" : "😻",
    "<3" : "❤"
}


massage = input("..>")
words = massage.split(' ')
final_massage = ""
for word in words:
    final_massage += emoji_Dictionary.get(word, word) + " "

print(final_massage)