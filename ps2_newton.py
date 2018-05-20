#Problem Set 2
#Name: Trevor Tomlin
#Collaborators: N/A
#Time 5:00

def compute_root(poly, x_0, epsilon):
    i = 0
    evaluate = evaluate_poly(poly, x_0)
    while abs(evaluate) > epsilon:
        evaluate = evaluate_poly(poly, x_0)
        deriv = compute_deriv(poly)
        evaluateDeriv = evaluate_poly(deriv, x_0)
        x_0  = x_0 - (evaluate/evaluateDeriv)
        i = i + 1
    root = (x_0, i)
    return (root)

def compute_deriv(poly):
    result = 0
    newPoly = [None] * len(poly)
    for i in range(1,len(poly)):
        currentExponent = i
        if currentExponent == 0:
            term = 0.0
        else:
            term = poly[i] * currentExponent
        currentExponent = currentExponent - 1
        newPoly[currentExponent + 1] = term
    newPoly = [i for i in newPoly if i is not None]
    newPolyTup = tuple(newPoly)
    return(newPolyTup)

def evaluate_poly(poly, x):
    result = 0
    for i in range(0,len(poly)):
        currentExponent = i
        result  = result + (float(poly[i]) * (x ** currentExponent))
    return (result)

def main():
    print ("1. Evaluate Polynomial")
    print ("2. Compute Derivitive of a Polynomial")
    print ("3. Compute Root")

    choice = float(input("Enter the number of the function you would like to go to: "))
    #choice = 3

    if choice == 1:
        values = input("Enter the coefficients of the polynomial function seperated by a comma:")
        x = float(input("Enter x: "))
        delimited = values.split(",")
        poly = tuple(delimited)
        evaluate = evaluate_poly(poly, x)
        print ("Evaluation:",evaluate)
    elif choice == 2:
        values = input("Enter the coefficients of the polynomial function seperated by a comma:")
        delimited = values.split(",")
        poly = tuple(delimited)
        #poly = (-13.39,0.0,17.5,3.0,1.0)
        derivitive = compute_deriv(poly)
        print("Derivitive:",derivitive)
    elif choice == 3:
        values = input("Enter the coefficients of the polynomial function seperated by a comma:")
        delimited = values.split(",")
        poly = tuple(delimited)
        #poly = (-13.39,0.0,17.5,3.0,1.0)
        x_0 = float(input("Enter initial guess: "))
        #x_0 = 0.1
        epsilon = float(input("Enter epsilon: "))
        #epsilon = 0.0001
        root = compute_root(poly, x_0, epsilon)
        print("Root:",root[0],"Iterations:",root[1])
    else:
        print ("Invalid input. Try again")

if __name__ == '__main__':
    main()
