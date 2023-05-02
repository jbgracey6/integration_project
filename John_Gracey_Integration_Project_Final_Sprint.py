"""
Name: John Gracey
Project Name: Vector Detector
Description: a program to complete mathematical problems related to
Calculus III.
"""

# /* introduction of user to the program, asks what problem program will be
# solving */
print('Hello! ' + 'Welcome to Vector Detector. ' +
      'What can we help you with today?')
print('>>>Please enter one of the following numbers to continue: ',
      '(1) dot product', '(2) cross product', sep='\n')
print('>>>Or, press x to exit.')
# stores the input to action question under variable action
action = input('')

# make sure that action is a valid input

while (action != '1' and action != '2' and action != 'x'):
    print('Please check that you have entered a valid input.')
    action = input('Enter 1, 2, or x (to exit): ')

# /* used this Stack Overflow page to find a library to import so I could
# insert an exit option
# https://stackoverflow.com/questions/543309/programmatically-stop-execution-of-python-script */

import sys

if action == 'x':
    print('Not in the math mood? Have a good day!')
    sys.exit()
# so that revised, robust code works with my if/else statements
if action == '1':
    problem_type = 'dot product'
if action == '2':
    problem_type = 'cross product'

# if/else statements to gather the vectors that program needs to work with
if problem_type == str('cross product') or problem_type == str('dot product'):
    print('>>>Enter your force vector in the component form below. '
          'x, y, and z should all be real numbers.')
else:
    print("Sorry, that's not an option.")

# /* used this Stack Overflow page for reference with my try/except lines
# https://stackoverflow.com/questions/15232465/how-to-repeat-try-except-block */

if problem_type == str('cross product') or problem_type == str('dot product'):
    x_comp_1 = (input('x: '))
    while True:
        try:
            x_comp_1 == float(x_comp_1)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            x_comp_1 = input('x: ')
    y_comp_1 = (input('y: '))
    while True:
        try:
            y_comp_1 == float(y_comp_1)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            y_comp_1 = input('y: ')
    z_comp_1 = (input('z: '))
    while True:
        try:
            z_comp_1 == float(z_comp_1)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            z_comp_1 = input('z: ')

    print('So, your force vector is <', x_comp_1, ',', y_comp_1, ',', z_comp_1,
          '>.')

    print('>>>Now, enter your direction vector in the component form below. '
          'x, y, and z should all be real numbers')

    x_comp_2 = (input('x: '))
    while True:
        try:
            x_comp_2 == float(x_comp_2)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            x_comp_2 = input('x: ')
    y_comp_2 = (input('y: '))
    while True:
        try:
            y_comp_2 == float(y_comp_2)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            y_comp_2 = input('y: ')
    z_comp_2 = (input('z: '))
    while True:
        try:
            z_comp_2 == float(z_comp_2)
            break
        except:
            print('Your component can only contain numerical values. '
                  'Please try again.')
            z_comp_2 = float('z: ')

    print('So, your direction vector is <', x_comp_2, ',', y_comp_2, ',', z_comp_2, '>.')

    # /* Calculuations - to find dot product, each vector component must be
    # multiplied by the respective component in the second vector. */
    x1_x2 = float(x_comp_1) * float(x_comp_2)
    y1_y2 = float(y_comp_1) * float(y_comp_2)
    z1_z2 = float(z_comp_1) * float(z_comp_2)
    dot_product = x1_x2 + y1_y2 + z1_z2

    # Output dot product
    print('The dot product of your two vectors is', format(dot_product, '0.4f'), end='.\n')

# /* more calculations. If the perfect amount/direction of force is used,
# then the magnitude of force should be the same as the dot product of force
# and direction. */

force_magnitude = ((float(x_comp_1)) ** 2) + ((float(y_comp_1)) ** 2) + \
                  ((float(z_comp_1)) ** 2) ** 0.5
direction_vector_magnitude = ((float(x_comp_2)) ** 2) + \
                             ((float(y_comp_2)) ** 2) + ((float(z_comp_2))
                                                         ** 2) ** 0.5
force_waste = force_magnitude - direction_vector_magnitude
force_waste_percent = (float(force_waste) / float(force_magnitude)) * 100

vector_comparison = force_magnitude // direction_vector_magnitude

if int(dot_product) % 2 != 0:
    print("That's odd!")

# a dot product of zero indicates that two vectors are perpendicular.
elif dot_product == 0:
    print('Your force and direction vectors are perpendicular.')

print('Your force magnitude is', force_magnitude, end='. ')
print('This means that ', format(force_waste_percent, '0.4f'),
      '% of your force is going to waste.', sep='')
print('In other words, your direction vector could fit inside the force '
      'vector', vector_comparison, 'times.')

if force_waste_percent > 50:
    print('What a waste!')

# added if/else here to prevent huge lines of hyphens/tildas
if force_magnitude < 79 and direction_vector_magnitude < 79:
    print('Force vector:     ' + '-' * int(force_magnitude))
    print('Direction vector: ' + '~' * int(direction_vector_magnitude))
else:
    print('Sorry, your magnitudes were too large for our visual '
          'representation.')

# cross product calculations, using determinant equations for both vectors

x_comp_cp = float(y_comp_1) * float(z_comp_2) - float(y_comp_2) * \
            float(z_comp_1)
y_comp_cp = (float(x_comp_1) * float(z_comp_2) - float(x_comp_2) *
             float(z_comp_1)) * (-1)
z_comp_cp = float(x_comp_2) * float(y_comp_1) - float(x_comp_1) * \
            float(y_comp_2)

print('Your cross product is <', str(x_comp_cp) + ',', str(y_comp_cp) + ',',
      str(z_comp_cp) + ',', '>', end='. ')
print('This vector is perpendicular to both force and direction.')

print("Now, let's differentiate a vector-valued function. Your components must"
      " be pieces of a polynomial\n(e.g. 5t^3, 2t^7) and must use t as the "
      "variable.")

# Prompt the user to enter three polynomials
poly1 = input('>>>Enter the first polynomial: ')
poly2 = input('>>>Enter the second polynomial: ')
poly3 = input('>>>Enter the third polynomial: ')

# verifies that the input uses the correct variable
while ('t' not in poly1 or 't' not in poly2 or 't' not in poly3):
    # /* I used this W3 schools page for reference
    # https://www.w3schools.com/python/gloss_python_check_string.asp */
    print('Oops! Check that you used the right variable.')
    poly1 = input('>>>Enter the first polynomial: ')
    poly2 = input('>>>Enter the second polynomial: ')
    poly3 = input('>>>Enter the third polynomial: ')


# Define a function to find the derivative of a polynomial
def derivative(poly):
    terms = poly.split('+')
    # /* Used this W3 Schools page for reference with .split
    # https://www.w3schools.com/python/ref_string_split.asp */
    result = ''
    for term in terms:
        coef, exp = term.split('t^')
        coef = int(coef)
        exp = int(exp)
        if exp > 0:
            new_coef = coef * exp
            new_exp = exp - 1
            result += str(new_coef) + 't^' + str(new_exp)
        elif exp == 0:
            result += '0t^0'
            # If power is 0, then the polynomial is actually a constant
        elif not exp >= 0:
            result += 'n/a'
            # Polynomials can't have negative powers

    return result


# Find the derivative of each polynomial and print the results
print("The derivative of", poly1, "is", derivative(poly1))
print("The derivative of", poly2, "is", derivative(poly2))
print("The derivative of", poly3, "is", derivative(poly3))

print('So, the velocity vector to your vector-valued function is: <',
      derivative(poly1), ',', derivative(poly2), ',',
      derivative(poly3), '>.')

# only calculates the second derivative if possible, to prevent errors
if derivative(poly1) != 'n/a':
    second_deriv1 = derivative(derivative(poly1))
else:
    second_deriv1 = 'n/a'
if derivative(poly2) != 'n/a':
    second_deriv2 = derivative(derivative(poly2))
else:
    second_deriv2 = 'n/a'
if derivative(poly3) != 'n/a':
    second_deriv3 = derivative(derivative(poly3))
else:
    second_deriv3 = 'n/a'

print("The second derivative of", poly1, "is", second_deriv1)
print("The second derivative of", poly2, "is", second_deriv2)
print("The second derivative of", poly3, "is", second_deriv3)

print('So, the acceleration vector to your vector-valued function is: <',
      second_deriv1, ',', second_deriv2, ',',
      second_deriv3, '>.')

if second_deriv1 == '0t^0' and second_deriv2 == '0t^0' and second_deriv3 == \
        '0t^0':
    print('Your acceleration is zero, meaning the object is moving at a '
          'constant velocity.')

print('Wanna know a higher derivative of a monomial?')
mono = input('>>>Enter a monomial of the form at^n, where t is the variable, '
             'a is a constant, and n is a positive exponent: ')
loop_count = (input('>>>How many times would you like to differentiate the '
                    'monomial? '))
while True:
    try:
        loop_count == int(loop_count)
        break
    except:
        print('Make sure your input is a positive, whole number.')
        loop_count = (input('>>>How many times would you like to differentiate'
                            ' the monomial? '))

#for loop to use my differentiation function multiple times

x = 0
for x in range(int(loop_count)):
    mono = derivative(mono)
    x = x + 1
print('Differentiated ', loop_count, ' times, your monomial becomes ', mono,
      '.', sep='')

print('Thanks for using Vector Detector, have a good day!')