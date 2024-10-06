constants = {
    1:" ",
    2:" ",
    3:" ",
    4:" ",
    5:" ",
    6:" ",
    7:" ",
    8:" ",
    9:" "
}

winning_combinations = [
    [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
]
 

def check_combinations(constants,winning_combinations):
    count = 0 
    comparison_list = []
    for combination in winning_combinations: #goes through every combinationb
        for number in combination: #goes through every number in the combination
            comparison_list.append(constants[number])
        if comparison_list[0] == comparison_list[1] and comparison_list[1] == comparison_list[2] and comparison_list[2] != " ":
            return True
            break
        else:
            comparison_list = []
            
            
turn = "x"     

while True:
    print(" "+constants[1]+" | "+constants[2]+" | "+constants[3]+" \n------------\n "+constants[4]+" | "+constants[5]+" | "+constants[6]+"  \n------------\n "+constants[7]+" | "+constants[8]+" | "+constants[9]+"  \n ")
    if turn == "x":
        while True:
            location = int(input("Where would you like to go? Input an integer as your answer: "))
            if constants[location] != " ":
                print("Cannot go there")
            else:
                break
        constants[location] = "x" 
    else:
        while True:
            location = int(input("Where would you like to go? Input an integer as your answer: "))
            if constants[location] != " ":
                print("Cannot go there")
            else: 
                break
        constants[location] = "o"
        
        
    result = check_combinations(constants,winning_combinations)

    if result == True: #if theres a win
        break

    if turn == "x":
        turn = "o"
    else:
        turn = "x"
