"""
CP1404 Practical
hex colours in a dictionary
"""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
               "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
               "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
               "aquamarine4": "#458b74", "azure1": "#f0ffff",
               "azure2": "#e0eeee", "azure3": "#c1cdcd",
               "azure4": "#838b8b", "beige": "#f5f5dc",
               "bisque1": "#ffe4c4", "bisque2": "#eed5b7",
               "bisque3": "#cdb79e", "bisque4": "#8b7d6b"}

def main():
    colour_name = input("What colour would you like the hex value of: ").lower()

    while colour_name != "":

            print("{} is {}".format(colour_name, HEX_COLOURS.get(colour_name)))

            colour_name = input("What colour would you like the hex value of: ").lower()

    print('Goodbye')

main()