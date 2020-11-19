def banner_text(text: str = " ", custom_width: int = 80) -> None:
    """
    This function is intended to display a banner text in a formatted way.
    :param text: Text that will be printed
    :param custom_width: Width that user can provide to calculate the currently window size.
    :raises ValueError: If the length of the text is greater than the width.
    :return: Return the text formatted with the custom width provided
    """
    if len(text) > custom_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, custom_width))

    if text == "*":
        print("*" * custom_width)
    else:
        output_string = "**{0}**".format(text.center(custom_width - 4))
        print(output_string)


user_custom_width = int(input("Please provide a custom witdh: "))
banner_text("*", user_custom_width)
banner_text("Always look on the bright side of life...", user_custom_width)
banner_text("If life seems jolly rotten,", user_custom_width)
banner_text("There's something you've forgotten!", user_custom_width)
banner_text("And that's to laugh and smile and dance and sing,", user_custom_width)
banner_text(custom_width=60)
banner_text("When you're feeling in the dumps,", user_custom_width)
banner_text("Don't be silly chumps,", user_custom_width)
banner_text("Just purse your lips and whistle - that's the thing!", user_custom_width)
banner_text("And... always look on the bright side of life...", user_custom_width)
banner_text("*", user_custom_width)

