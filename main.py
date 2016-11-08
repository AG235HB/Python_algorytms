def mode_selector():
    if len(sys.argv) >= 2:
        #SORT: bubble, selection, insertion, merge, quick
        #SEARCH: binary, linear
        #STACK
        #QUEUE
        #if len(sys.argv) == 2:
        #    random = True
        if sys.argv[1]=='-h':
            print("Help:")
        elif sys.argv[1]=='-sort':
            if len(sys.argv)>=3:
                if sys.argv[2]=='bubble':
                    from sort import bubble
                    #bubble.awake()
                    if len(sys.argv)==3:
                        print(len(sys.argv)==3)
                        print('random')
                        print(bubble.random_sort())
                    elif len(sys.argv[3])<=2 or sys.argv[3]=='-r':
                        print(len(sys.argv[3])<=2)
                        print('random')
                        print(bubble.random_sort())
                    else:
                        st = sys.argv[3:]
                        print('MAIN')
                        print(st)
                        print(bubble.sort(sys.argv[3:]))
                elif sys.argv[2]=='insertion':
                    from sort import insertion
                    insertion.awake()
                elif sys.argv[2]=='merge':
                    from sort import merge
                    merge.awake()
                elif sys.argv[2]=='quick':
                    from sort import quick
                    quick.awake()
                elif sys.argv[2]=='selection':
                    from sort import selection
                    selection.awake()
                else:
                    print('ERROR in sort')
            else:
                    print('ERROR with '+sys.argv[1])
        elif sys.argv[1]=='-search':
            print('Search')
        elif sys.argv[1]=='-joke':
            import os
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("The classic mistake inventors absolutely reliable systems - this underestimation of the ingenuity of clinical idiots.\n\nDouglas Adams")
        else:
            print('ERROR')
        
    else:
        print("Usage:...")

    #print(random)

def find_separator(collection):
    #print(collection)
    for index, item in enumerate(collection):
        #print(item)
        if item == ',':
            return ','
        if item == ' ':
            return ' '
    return None

if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        input_func = raw_input
    else:
        input_func = input

    mode_selector()

    #print("\nPOW!\n")

    #user_input = input_func('enter numbers\n')
    #print(find_separator(user_input))
    #unsorted = [int(item) for item in user_input.split(find_separator(user_input))]