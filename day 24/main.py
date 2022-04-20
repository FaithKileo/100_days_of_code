PLACEHOLDER = "[name]"

with open("day 24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # readlines arranges the number of many objects in a list with spaces

with open("day 24\Input\Letters\starting_letter.docx") as letter_file:
    letter_contents = letter_file.read() 
    
    for name in names:
        
        stripped_name = name.strip()
        # strip removes all unneccessarry spaces and arrange the work clearly.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # replace places the new content in the place of the old one and changes it.
        
    # creating a file for each letter. 
        with open(f"day 24\Output\ReadyToSend\letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)