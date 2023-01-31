if __name__ == '__main__':
   score_lst=[]
   marksheet=[]
   
   for _ in range(int(input())):
    name = input()
    score=float(input())
    marksheet.append([name,score])
    score_lst.append(score)

   second_lowest =sorted(set(score_lst))[1]
   for student in sorted(marksheet):
        if student[1]==second_lowest:
            print(student[0]) 
