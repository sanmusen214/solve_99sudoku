import copy


# 生成全为0的九宫格并返回
def new99():
    newlist = [[0 for i in range(9)] for j in range(9)]
    return newlist

#自定义输入九宫格
def make99():
    listnew=new99()
    for i in range(9):
        strm=input("请按行输入（空的则为0）: ");
        if(len(strm)!=9):
            print("输入错误重新输入第{}行".format(i+1))
            i-=2
            continue
        for j in range(9):
            listnew[i][j]=int(str[j])
    return listnew


# 打印99九宫格
def print99(list99):
    for rowx in range(9):
        if rowx!=0 and rowx%3==0:
            print("- - - - - - - - - - -")
        for eachy in range(9):
            if eachy!=0 and eachy%3==0:
                print("|",end=' ')
            print(list99[rowx][eachy],end=' ')
        print(" ")
        
# 修改九宫格第x行，y列为z
def changexyz(x,y,z,list99):
    list99[x][y]=z
    return list99

# 检查99宫格第col列数字wantnum出现次数，返回int
def show_times_in_col(alist,col,wantnum):
    showtime=0
    for times in range(9):
        if(alist[times][col]==wantnum):
            showtime+=1
    return showtime

# 检查99宫格第row行数字wantnum出现次数，返回int
def show_times_in_row(alist,row,wantnum):
    showtime=0
    for times in range(9):
        if(alist[row][times]==wantnum):
            showtime+=1
    return showtime

# 检查99宫格第squarenum块数字wantnum出现次数,x(1,2,3),y(1,2,3)
def show_times_in_square(alist,squarenumy,squarenumx,wantnum):
    showtime=0
    for i in range(squarenumy*3-3,squarenumy*3):
        for j in range(squarenumx*3-3,squarenumx*3):
            if(alist[i][j]==wantnum):
                showtime+=1
    return showtime
    
# 检查99宫格第col列的wantnum的出现位置，返回位置的二维列表
def show_post_in_col(alist,col,wantnum):
    showpost=[]
    for times in range(9):
        if(alist[times][col]==wantnum):
            showpost.append([times,col])
    return showpost
# 检查99宫格第row列的wantnum的出现位置，返回位置的二维列表
def show_post_in_row(alist,row,wantnum):
    showpost=[]
    for times in range(9):
        if(alist[row][times]==wantnum):
            showpost.append([row,times])
    return showpost
# 检查99宫格第yx块的wantnum的出现位置，返回位置的二维列表
def show_post_in_square(alist,squarenumy,squarenumx,wantnum):
    showpost=[]
    for i in range(squarenumy*3-3,squarenumy*3):
        for j in range(squarenumx*3-3,squarenumx*3):
            if(alist[i][j]==wantnum):
                showpost.append([i,j])
    return showpost
    
#判断是否已全部解完，返回boolean
def whetherdone(list99):
    for i in range(9):
        for j in range(9):
            if(list99[i][j]==0):
                return False
    return True

#以是否有最少方法的数字完成解来判断是否往下有解
def whether_have_solution(list99):
    num,num_pro,num_post=show_mostpro_exa_num(list99)
    if(num==0 and not whetherdone(list99)):
        return False
    return True


#查看数字X(temp)在九宫格（list99）里可能出现的地方，返回可能性九宫格
def wherex(temp,list99):
    list00=new99()
    #行列查重
    for i in range(9):
        for j in range(9):
            if(show_times_in_col(list99,j,temp)!=0 or show_times_in_row(list99,i,temp)!=0 or list99[i][j]!=0):
                list00[i][j]=1
    # 区块查重
    for i in range(1,4):
        for j in range(1,4):
            if(show_times_in_square(list99,i,j,temp)!=0):
                for ii in range(i*3-3,i*3):
                    for jj in range(j*3-3,j*3):
                        list00[ii][jj]=1
    return list00

        
# 显示可确定放置的数字,返回该数字
def show_exa_num(list99):
    for nums in range(1,10):
        listpro=wherex(nums,list99)
        # 唯一确定
        for y in range(9):
            if(show_times_in_col(listpro,y,0)==1 or show_times_in_row(listpro,y,0)==1):#只有一个空可填入
                return nums
        for i in range(1,4):
            for j in range(1,4):
                if(show_times_in_square(listpro,i,j,0)==1):
                    return nums
    return 0

#寻找可放置块的所有方法最少的数字，返回该数字和最少方法的方法数和地方
#type 1按列 2按行 3按块 post 绝对坐标的列表的列表
def show_mostpro_exa_num(list99):
    mostpro_exa_num=0
    mostpro_exa_num_pro=9
    mostpro_exa_num_post=[]
    for anum in range(1,10):
        prolist=wherex(anum,list99)
        for i in range(9):
            if(show_times_in_col(prolist,i,0)!=0 and show_times_in_col(prolist,i,0)<mostpro_exa_num_pro):
                mostpro_exa_num_pro=show_times_in_col(prolist,i,0)
                mostpro_exa_num=anum
                mostpro_exa_num_post=show_post_in_col(prolist,i,0)
            if(show_times_in_row(prolist,i,0)!=0 and show_times_in_row(prolist,i,0)<mostpro_exa_num_pro):
                mostpro_exa_num_pro=show_times_in_row(prolist,i,0)
                mostpro_exa_num=anum
                mostpro_exa_num_post=show_post_in_row(prolist,i,0)
        for sy in range(1,4):
            for sx in range(1,4):
                if(show_times_in_square(prolist,sy,sx,0)!=0 and show_times_in_square(prolist,sy,sx,0)<mostpro_exa_num_pro):
                    mostpro_exa_num_pro=show_times_in_square(prolist,sy,sx,anum)
                    mostpro_exa_num=anum
                    mostpro_exa_num_post=show_post_in_square(prolist,sy,sx,0)
    return mostpro_exa_num,mostpro_exa_num_pro,mostpro_exa_num_post
                    
        
        

#确切放置数字直到无确切数字,返回新99
def solve99in_oneway(list99):
    while(1):
        num,pro,post=show_mostpro_exa_num(list99)
        if(len(post)!=1):
            return list99
        else:
            list99[post[0][0]][post[0][1]]=num

            
# 根据已知最小可能的数字及其位置来递归讨论并更改多种可能的情况,mode为0只求一解，mode为1求所有解
# 保证传入的数独已按照一种解法的解完！！！savelist非常重要，保证尝试失败后能够原样恢复尝试前的数独
def solve99in_mulway(listtemp,mode):  #!!求多解在横列上会重复
    savelist=copy.deepcopy(listtemp)  #拷贝一份更改前的数独
    newlisttemp=solve99in_oneway(copy.deepcopy(listtemp))#将尝试的数独进行单一解（对递归后的尝试有实际作用）
    if(not whether_have_solution(newlisttemp)):#解不通无法继续求解就直接返回false
        return False
    if(whetherdone(newlisttemp)):#数独塞满了就返回true，并更改全局list99
        global list99
        list99=copy.deepcopy(newlisttemp)
        print("求出一种解法")
        global num_of_solution
        num_of_solution+=1
        print99(list99)
        return True
    #列出当前最优数字的相关参数,递归部分
    selnum,selnum_pro,selnum_post=show_mostpro_exa_num(newlisttemp)
    if(selnum==0):
        return False
    for each_post in selnum_post:
        newlisttemp2=changexyz(each_post[0],each_post[1],selnum,copy.deepcopy(newlisttemp))
        #print(selnum_post)#debug
        #print("changing {},{}为{}".format(each_post[0]+1,each_post[1]+1,selnum))#debug
        if(solve99in_mulway(newlisttemp2,mode)):#根据尝试的填入数字如果能解通就返回true
            if(mode==0):
                return True
            else:
                newlisttemp=copy.deepcopy(savelist)#求多解，还原这次猜测，再次猜
                continue
        else:
            newlisttemp=copy.deepcopy(savelist)#如果根据尝试填入的解不通就还原数独
            #print("复原{}，{}为0".format(each_post[0]+1,each_post[1]+1))#debug
            #print99(newlisttemp)#debug
    return False
    
    
    
    
    
        
    




# -----------------------------------------------
if __name__=='__main__':
    waitstep=input("按回车下一步")
    list99=[[0,0,9,7,4,8,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [0,2,0,1,0,9,0,0,0],
            [0,0,7,0,0,0,2,4,0],
            [0,6,4,0,1,0,5,9,0],
            [0,9,8,0,0,0,3,0,0],
            [0,0,0,8,0,3,0,2,0],
            [0,0,0,0,0,0,0,0,6],
            [0,0,0,2,7,5,9,0,0]]
    # list99=make99()
    # print99(list99) 
    rootlist=copy.deepcopy(list99)
    print("数独已保存")
    tru1=1
    while(tru1==1):
        print("操作列表: ")
        print("0. 打印当前数独")
        print("1. 显示数字x可能放置的图")
        print("2. 显示可确定放置的数字")
        print("3. 修改某一个格子内容")
        print("4. 尝试解题")
        print("5. 尝试以解多种解法开始解题")
        print("6. 显示最可能解的数")
        print("7. 保存当前数独")
        print("8. 还原保存的数独")
        print("9. 重新输入数独")
        tempkey=input("请选择: ")
        if (tempkey=="1"):
            while(tru1==1):
                wantnumtext=input("请选择想查看的数X的可能图(0为可放置): ")
                if(len(wantnumtext)!=1):
                    print("请输入一位数!")
                    continue
                wantnum=int(wantnumtext)
                listx=wherex(wantnum,list99)
                print99(listx)
                waitstep=input("按回车下一步")
                break
            
        elif tempkey=="2":
            mostpronum=show_exa_num(list99)
            if(mostpronum==0):
                print("目前无可确定数字")
                waitstep=input("按回车下一步")
                continue
            print("确定放置的数字是{}".format(mostpronum))
            waitstep=input("按回车下一步")
                
        elif tempkey=="3":
            editstr=input("修改x行y列的值为z(xyz): ");
            if(not editstr.isdigit() or len(editstr)!=3):
                print("输入错误")
            else:
                pstx=int(editstr[0])-1
                psty=int(editstr[1])-1
                valuez=int(editstr[2])
                list99=changexyz(pstx,psty,valuez,list99)
                print("修改完成~")
                print99(list99)

        
        elif tempkey=="4":
            print("以唯一解法开始解题")
            list99=solve99in_oneway(list99)
            print99(list99)
            if(not whetherdone(list99)):
                print("可能有多种解法，可以用5. 以多种解法开解")
            print("解题结束")
            waitstep=input("按回车下一步")
            
        elif tempkey=="5":
            choosemode=input("请选择：\n0. 求一个解\n1. 求所有解\n")
            if(choosemode!="0" and choosemode!="1"):
                print("选择错误")
                continue
            num_of_solution=0
            mode=int(choosemode)
            solve99in_mulway(list99,mode)
            print("输出{}种解法数独".format(num_of_solution))
            waitstep=input("按回车下一步")
        elif tempkey=="6":
            a,b,c=show_mostpro_exa_num(list99)
            print("下一个可能解的数为{}，可能有{}种方法，可能摆放的位置如下".format(a,b))
            print99(wherex(a,list99))
            
            
        elif tempkey=="7":
            rootlist=copy.deepcopy(list99)
            print("当前数独已被保存")
        elif tempkey=="8": 
            list99=copy.deepcopy(rootlist)
            print("已还原上一个保存的数独")
        elif tempkey=="9":
            list99=make99()
            print99(list99)
            rootlist=copy.deepcopy(list99)
        elif tempkey=="0":
            print99(list99)
        else:
            print("输入歪了")
            waitstep=input("按回车下一步")

        
