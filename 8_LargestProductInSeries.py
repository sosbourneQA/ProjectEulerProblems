# The four adjacent digits in the 1000-digit number
# that have the greatest product are 9 × 9 × 8 × 9 = 5832.

# 73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586
# 15607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648
# 95044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962
# 90491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336
# 78812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064
# 95514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998900088
# 95243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568
# 28489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987
# 87992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022569831552
# 0005593572972571636269561882670428252483600823257530420752963450

# Find the thirteen adjacent digits in the 1000-digit number that
# have the greatest product. What is the value of this product?

def compute():

    num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    max = 0

    # ans =int(num[0]) * int(num[1])
    #
    # print(ans)
    for x in range(0, len(num) - 12):
        product = int(num[x]) * int(num[x+1]) * int(num[x+2]) * int(num[x+3]) * int(num[x+4]) * int(num[x+5]) * int(num[x+6]) * int(num[x+7]) * int(num[x+8]) * int(num[x+9]) * int(num[x+10]) * int(num[x+11]) * int(num[x+12])
        if product > max:
            max = product
            print(max)



compute()