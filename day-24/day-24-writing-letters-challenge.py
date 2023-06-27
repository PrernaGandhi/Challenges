PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as letter_template, \
        open("./Input/Names/inviting_names.txt") as invitee_names:
    template_contents = letter_template.read()
    names = invitee_names.readlines()
    # names = invitee_names.read().split("\n")
    for name in names:
        # strip function strips new lines and spaces too
        name = name.strip()
        file_content = template_contents.replace("%s" % PLACEHOLDER, f"{name}")
        with open(f"./Output/ReadyToSend/letter_to_invite_{name}.txt", "w") as output_file:
            output_file.write(file_content)


