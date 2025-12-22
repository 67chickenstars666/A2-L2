print("Enter marks obtained in 5 subjects:")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())
totalmarks=markone+marktwo+markthree+markfour+markfive
avg= totalmarks/5
if avg>=90 and avg<=100:
    print("Grade A")
elif avg>=80 and avg<90:
    print("Grade B")
elif avg>=70 and avg<80:
    print("Grade C")
elif avg>=60 and avg<70:
    print("Grade D")
else:
    print("Grade F")