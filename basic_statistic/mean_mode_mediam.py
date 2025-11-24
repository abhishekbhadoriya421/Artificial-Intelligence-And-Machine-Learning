# Dataset 1 — Student Marks (Easy)

def find_mean(data,length):
    return sum(data)/length

def find_median(data,length):
    data = sorted(data)  
    mid = (length//2)-1
    if(length%2 ==0):
        return (data[mid]+data[mid+1])/2
    else:
        return data[mid]

def find_mode(data,length):
    mode = data[0]
    modes = []
    max_count = 1
    for i in range(0,length):
        count = 0
        temp_mode = data[i]
        for j in range(0,length):
            if data[i] == data[j]:
                count+=1

        if max_count < count:
            max_count = count
            mode = temp_mode
            modes = []
        elif max_count == count:
            if temp_mode not in modes:
                modes.append(temp_mode)
    return int(mode) if len(modes) == 0 else modes

student_marks = [55, 60, 65, 70, 70, 75, 80, 85, 85, 90]
length = len(student_marks)
mean = find_mean(student_marks,length)
median = find_median(student_marks,length)
mode = find_mode(student_marks,length)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")