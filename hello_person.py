def hello(name, lang):
    greetings = {
        "Tamil":"வணக்கம் ",
        "English": "Hello",
        "Spanish": "Hola",
        "Hindi": "Namastae" 
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-m", "--my_name", metavar="my_name",required=True,
        help="The name of the person to greet" # -n means flag val
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",required=True, choices=["Tamil","English","Spanish","Hindi"], help="The language of the greeting"
    )

    args = parser.parse_args()

    hello(args.my_name, args.lang)

    # msg =f"Hello! {args.my_name}"
    # print(msg)


    