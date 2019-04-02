#input format: ["name1 status loc1 loc2...", "name2 status loc1 loc2...", ...]
#cutoff at 365 days
#name is unique

def days_till_healthy_palantir(string_list):
    info = [] #list of strings to return
    num_days = 0
    team = {}
    
    #organizing team info into format:
    #team[name] = [status, curr_office_index, offices_lst]
    
    
def main():
    #1. string format test
    string_list1 = ["Adam HEALTHY PaloAlto"]
    #2. simple case test
    string_list2 = ["Adam HEALTHY DC NY PaloAlto",
                  "Bob SICK DC NY PaloAlto"]
    #3. less simple case test
    string_list3 = ["Adam RECOVERING NY DC DC PaloAlto NY NY PaloAlto",
                   "Bob HEALTHY NY DC PaloAlto",
                   "Claire HEALTHY DC PaloAlto NY",
                   "Dan SICK NY NY PaloAlto DC NY"]
    
    #1
    test = days_till_healthy_palantir(string_list1)
    print(*test, sep="\n")
    
    #2
    '''test = days_till_healthy_palantir(string_list2)
    print(*test, sep="\n")
    
    #3
    test = days_till_healthy_palantir(string_list3)
    print(*test, sep="\n")'''

main()