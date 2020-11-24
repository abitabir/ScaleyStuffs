# CONSTANTS
CHESSBOARD_SQUARES = 8*8
AVERAGE_MASS_OF_SINGLE_RICE_GRAIN_IN_MG = 30

# function defining
def calculating_mass_of_grains_of_rice_per_chessboard_square(current_chessboard_square_number, approximate_single_rice_grain_mass_in_mg):
    grains_of_rice = pow(2, (current_chessboard_square_number - 1))
    mass_of_grains_of_rice = grains_of_rice * approximate_single_rice_grain_mass_in_mg
    return(grains_of_rice, mass_of_grains_of_rice)

# function call and output
for chessboard_square_number in range(1, (CHESSBOARD_SQUARES + 1)):
    grains_of_rice, mass_of_grains_of_rice = calculating_mass_of_grains_of_rice_per_chessboard_square(chessboard_square_number, AVERAGE_MASS_OF_SINGLE_RICE_GRAIN_IN_MG)
    print("For the", str(chessboard_square_number) + "st/nd/rd/th chessboard square", grains_of_rice, "grains of rice were to be given to the wise man by the king as his self-chosen prize for inventing the chessboard, which amounted to the whopping mass of", mass_of_grains_of_rice, "miligrams.")
