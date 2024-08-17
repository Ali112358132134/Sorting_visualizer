def merge_sort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        return array
    else:
        k = len(array) // 2
        i, j = 0, 0
        tmp_arr = []
        r = merge_sort([x for i, x in enumerate(array) if i >= k])
        l = merge_sort([x for i, x in enumerate(array) if i < k])
        while i < k and j < len(r):
            if l[i] > r[j]:
                tmp_arr.append(r[j])
                j += 1
            elif l[i] < r[j]:
                tmp_arr.append(l[i])
                i += 1
            else:
                tmp_arr.append(l[i])
                tmp_arr.append(r[j])
                i, j= i + 1, j + 1           
        while j < len(r):
            tmp_arr.append(r[j])
            j += 1
        while i < k:
            tmp_arr.append(l[i])
            i += 1
        return tmp_arr