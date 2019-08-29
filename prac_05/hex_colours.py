"""
CP1404 Practical
hex colours in a dictionary
"""

HEX_COLOURS = {"alice blue": "#f0f8ff", "antique white": "#faebd7", "antique white1": "#ffefdb", "antique white2": "#eedfcc", "antique white3": "#cdc0b0", "antique white4": "#8b8378", "aqua marine1": "#7fffd4", "aqua marine2": "#76eec6", "aqua marine4": "#458b74", "azure1": "#f0ffff"}

def main():
    colour_name = input("What colour would you like the hex value of: ")

    while colour_name != " ":
        try:
            print(HEX_COLOURS[colour_name])
        except KeyError:
            print("Hex value not defined")

        colour_name = input("What colour would you like the hex value of: ")

    print('Goodbye')

main()