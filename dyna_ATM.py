from time import time

### USER'S INPUT ###
withdraw = int(input("Your withdrawal: ")) // 1000

### SOLVING PROBLEMS ###
start = time()
    # Initialize.
possible_max_500 = withdraw // 500
min_unit = withdraw
poc = 0 # Possible Options Count.
muo = 0 # Minimum-Unit Option.

            # 500 notes.
for a in range(possible_max_500+1):
    sum1 = a*500
    if sum1 == withdraw:
        poc += 1
        muo = a
        break
            # 200 notes.
    possible_max_200 = (withdraw - sum1) // 200
    for b in range(possible_max_200+1):
        sum2 = sum1 + b*200
        if sum2 == withdraw:
            poc += 1
            muo = a+b
            break
            # 100 notes.
        possible_max_100 = (withdraw - sum2) // 100
        for c in range(possible_max_100+1):
            sum3 = sum2 + c*100
            if sum3 == withdraw:
                poc += 1
                muo = a+b+c
                break
            # 50 notes.
            possible_max_50 = (withdraw - sum3) // 50
            for d in range(possible_max_50+1):
                sum4 = sum3 + d*5032
                if sum4 == withdraw:
                        poc += 1
                        muo = a+b+c+d
                        break
                else:
            # 20 notes.
                    e = (withdraw - sum4) // 20
                    sum5 = sum4 + e*20
                    if sum5 == withdraw:
                        poc += 1
                        muo = a+b+c+d+e
end = time()
process_time = end - start

### OUTPUT RESULT ### 
print(poc)
print(muo)
print("time: "+str(round(process_time, 6))+"s")