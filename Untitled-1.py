def my_func(subj):
 for x in subj:
     print(x)
subjects = ["python","java","c"]
my_func(subjects)
#2
def my_func(*id):
   print("The thirdbid is " +id[2])
my_func("alpha","beta","gaming")

#3
def my_func(ch1,ch2):
   print("the oldest child is " + ch1)
my_func(ch2="mukesh", ch1="ramen")
#4 dictionart-muttable and not duplicate valve allowed
my_dict={
   "ram":15,
   "shyam":17,
   "akshay":16
}
print(my_dict)
print(my_dict['akshay'])
my_dict['sal']=[15,17,15]
     

# files
f=open(' )#f is file handle or file oject
r=f.read()#reads the whole file
print(r)
f.close()# should always close at the end

#
f=open('myfile')
line=f.readline() # reads one line
print(line)
f.close() # should always close at the end