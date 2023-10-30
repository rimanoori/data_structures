"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-15"
-------------------------------------------------------
"""
from Food import Food
from pickle import TRUE
from _ast import Break


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        Food - a completed Food object (Food).
    -------------------------------------------------------
    """
    Name=input("Name:")
    Origin=int(input(
        """Origin
        0 Canadian
        1 Chinese
        2 Indian
        3 Ethiopian
        4 Mexican
        5 Greek
        6 Japanese
        7 Italian
        8 American
        9 Scottish
        10 New Zealand
        11 English"""))
    Veg=input("Vegetarian (Y/N):")
    if Veg=="Y":
        Veg=True
    else:
        Veg=False
    Calories=float(input("Calories:"))
    food = Food(Name,Origin,Veg,Calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of Food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        Food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    striii=line.split("|")
    if (striii[2]=="False"):
        vegetarian = False
    else:
        vegetarian = True
    food = Food(striii[0],int(striii[1]),vegetarian,float(striii[3]))

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of Food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of Food data (file)
    Returns:
        foods - a list of Food objects (list of Food)
    -------------------------------------------------------
    """
    foods=[]
    line= file_variable.readline()

    while(line!=""):
        foods.append(read_food(line))
    
        line= file_variable.readline()
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of Food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in foods:
        print(f"{i.name}|{i.origin}|{i.is_vegetarian}|{i.calories}",file=file_variable)
        


    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies=[]
    for i in foods:
        if(i.is_vegetarian==True):
            veggies.append(i)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a Food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins=[]
    for food in foods:
        if food.origin==origin:
            origins.append(food)
    return origins


    # Your code here

  #  return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    n=0
    total=0
    for i in foods:
        total+=i.calories
        n+=1
    avg=total/n
    return avg

    # Your code here

#    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    total=0
    n=0
    for i in foods:
        if i.origin==origin:
            total+=i.calories
            n+=1
    avg_cal=total/n
    return avg_cal
    # Your code here

 #   return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    res=f"""Food                                Origin       Vegetarian Calories
    \n----------------------------------- ------------ ---------- --------\n"""
    for i in foods:
        res+=f"""{i.name:<35s} {Food.ORIGIN[i.origin]:<12s} {str(i.is_vegetarian):>11s} {i.calories:9.1f}\n"""
    
    
    print(res)
    

    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food; if -1, accept any origin (int)
        max_cals - the maximum calories for the Food; if 0, accept any calories value (int)
        is_veg - whether the Food is vegetarian or not; if False accept any Food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result=[]
    for i in foods:
        if i.origin==origin or origin==-1:
            if i.calories<=max_cals or max_cals==0:
            
                if is_veg==i.is_vegetarian or is_veg==False:
                    result.append(i)


                                    
    
    return result
    # Your code here

    #return result
