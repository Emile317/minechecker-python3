# Imports:
import requests, time, sys

# View MojangAPI related stuff here: https://wiki.vg/Mojang_API
# Please note the API has a rate limit of 600 requests in a 10 minute interval.
# Also note that names written to the output file might have a block, this can only be checked manually.

try:
    starting_index = int(sys.argv[1])
except Exception as e:
    print("incorrect or missing starting index input")
    exit()

success = True

try:
    # Open unclaimed words dump file for appending:
    unclaimed_file = open("unclaimed.txt", "a")

    # Open words dump file for reading:
    word_file = open("words.txt", "r")
    word_array = word_file.readlines()

    # Print some useful info:
    print("[INFO] {0} words were read from the provided file.".format(len(word_array)))
    print("[INFO] Starting checks. You will be notified when an account is added to the unclaimed file.")

    # Loop over each line in word array:
    count = 1
    for x in range(len(word_array)):
        if count < starting_index:
            count += 1
            continue

        word = word_array[x].strip()
        response = requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(word))
        if response.status_code == 404:
            print("[INFO] {0} is not taken.".format(word))
            unclaimed_file.write(f'{word}\n')

        print(f"account number {count} has been checked.")
        count += 1

        # Sleep for one second (Only lower if your list is short):
        time.sleep(1)

    # Finish up:
    print("[INFO] All names have been checked.")
    unclaimed_file.close()

except Exception as e:
    print(f'[INFO] An unexpected error occured while checking account {count}. Words file might be corrupt. Error msg:\n{e}')
    success = False

# if all accounts were successfully checked, writes 'success' to output.txt
# otherwise writes the account where an error occured.
# this is for the bash script to let it run this python script again starting where it left off
with open('output.txt', 'w') as output_file:
    if success:
        output_file.write("success")
    else:
        output_file.write(str(count))